#! /usr/bin/env python
# -*- coding:utf-8 -×-

import sys
import tornado
from tornado.concurrent import TracebackFuture, return_future
from tornado import httputil, stack_context
import gen
import tornado.ioloop
from inspect import getargspec
from tornado.util import raise_exc_info, ArgReplacer
from tornado.stack_context import ExceptionStackContext, wrap
import types
from types import GeneratorType
import ipdb
from gen import Return

def handler_call(res):
    print 'in handler_call', res
    return res

def sync_t(a, b, callback=None):
#    future = TracebackFuture()

    if callback is not None:
        callback = stack_context.wrap(callback)

#        def handle_future(future):
#            exc = future.exception()
#            result = future.result()
#            tornado.ioloop.IOLoop.current().add_callback(callback, result)
#        future.add_done_callback(handle_future)

    res = a + b
#    callback(res)


#t = gen.Task(sync_t)

_NO_RESULT = object()

def m_return_future(f):
    replacer = ArgReplacer(f, 'callback')

    def wrapper(*args, **kwargs):
        future = TracebackFuture()
#        ipdb.set_trace()
        print args, kwargs
#        callback, args, kwargs = replacer.replace(lambda value=_NO_RESULT: future.set_result(value),args, kwargs)
        callback = None
        kwargs['callback'] = lambda value = _NO_RESULT: future.set_result(value)
        print callback, args, kwargs
        def handle_error(typ, value, tb):
            future.set_exc_info((typ, value, tb))
            return True

        exc_info = None
        with ExceptionStackContext(handle_error):
            try:
                result = f(*args, **kwargs)
                if result is not None:
                    raise ReturnValueIgnoredError('@return_future should not be used with function that return values')
            except:
                exc_info = sys.exc_info()
                raise

        if exc_info is not None:
            future.result()

        if callback is not None:
            def run_callback(future):
                result = future.result()
                if result is _NO_RESULT:
                    callback('result is NULL')
                else:
                    callback(future.result())
            future.add_done_callback(wrap(run_callback))
#        print future.result(), 'in the wapper'
        return future

    return wrapper

def m_engine(func):
    func = m_make_coroutine_wrapper(func, replace_callback=False)
    def wrapper(*args, **kwargs):
        future = func(*args, **kwargs)
        def final_callback(future):
            if future.result() is not None:
                raise ReturnValueIgnoredError("@gen.engine functions cannot return values: %r" % (future.result(),))
        future.add_done_callback(stack_context.wrap(final_callback))
        return wrapper

def m_coroutine(func, replace_callback=True):
    return m_make_coroutine_wrapper(func, replace_callback)


def m_make_coroutine_wrapper(func, replace_callback=True):
    if hasattr(types, 'm_coroutine'):
        func = types.coroutine(func)

#    ipdb.set_trace()
    def wrapper(*args, **kwargs):
        ipdb.set_trace()
        future = TracebackFuture()
        if replace_callback and 'callback' in kwargs:
            callback = kwargs.pop('callback')
            IOLoop.current().add_future(future, lambda future: callback(future.result()))

        try:
            result = func(*args, **kwargs)
        except (Return, StopIteration) as e:
#            ipdb.set_trace()
            result = gen._value_from_stopiteration(e)
        except Exception:
#            ipdb.set_trace()
            future.set_exc_info(sys.exc_info())
            return future
        else:
#            ipdb.set_trace()
            if isinstance(result, GeneratorType):
                try:
                    orig_stack_contexts = stack_context._state.contexts
                    yielded = next(result)
                    if stack_context._state.contexts is not orig_stack_contexts:
                        yielded = TracebackFuture()
                        yielded.set_exception(stack_context.StackContextInconsistentError('stack_context inconsistency (probably caused'))
                except (StopIteration, Return) as e:
                    future.set_result(gen._value_from_stopiteration(e))
                except Exception:
                    future.set_exc_info(sys.exc_info())
                else:
                    try:
                        result.send(yielded.result()) 
                    except (StopIteration, Return) as e:
                        ipdb.set_trace()
                        future.set_result(gen._value_from_stopiteration(e))
                        
#                    gen.Runner(result, future, yielded)
                try:
                    return future
                finally:
                    future = None

        future.set_result(result)
        return future
    return wrapper
            

            
@m_coroutine
def future_func(arg1, arg2):
    result = arg1 + arg2
    # Do stuff (possibly asynchronous)
    print 'callback begin'
#    callback(result)
    raise gen.Return(result)
    print 'callback end'

#@m_engine
@m_corocallere
def caller():
#    ipdb.set_trace()
#    res = yield future_func(1, 2, handler_call)

    print 'run in caller'
    res = yield future_func(9, 2)
    print 'result', res
#    ipdb.set_trace() 
#    print res
#    callback()
    pass

@m_coroutine
def main():
    caller()

if __name__ == '__main__':
    tornado.ioloop.IOLoop.current().run_sync(caller)


