#! /usr/bin/env python
# -*- coding:utf-8 -*-


import sys
import threading
import ipdb


class _State(threading.local):
    def __init__(self):
        self.contexts = (tuple(), None)
_state = _State()

class ExceptionStackContext(object):
    """Specialization of StackContext for exception handling.

    The supplied ``exception_handler`` function will be called in the
    event of an uncaught exception in this context.  The semantics are
    similar to a try/finally clause, and intended use cases are to log
    an error, close a socket, or similar cleanup actions.  The
    ``exc_info`` triple ``(type, value, traceback)`` will be passed to the
    exception_handler function.

    If the exception handler returns true, the exception will be
    consumed and will not be propagated to other exception handlers.
    """
    def __init__(self, exception_handler):
        self.exception_handler = exception_handler
        self.active = True

    def _deactivate(self):
        self.active = False

    def exit(self, type, value, traceback):
        if type is not None:
            return self.exception_handler(type, value, traceback)

    def __enter__(self):
        self.old_contexts = _state.contexts
        self.new_contexts = (self.old_contexts[0], self)
        _state.contexts = self.new_contexts

        return self._deactivate

    def __exit__(self, type, value, traceback):
        try:
            if type is not None:
                return self.exception_handler(type, value, traceback)
        finally:
            final_contexts = _state.contexts
            _state.contexts = self.old_contexts

            if final_contexts is not self.new_contexts:
                pass
            # Break up a reference to itself to allow for faster GC on CPython.
            self.new_contexts = None


class Test:
    def do(self):
        def err_handler(type, value, trackback):
            pass
        exc_info = None
        with ExceptionStackContext(err_handler):
            try:
                raise Exception('hello') 
            except:
                exc_info = sys.exc_info()
                ipdb.set_trace()
                raise
        print 'do end'

if __name__ == '__main__':
    Test().do()

