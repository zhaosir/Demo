#! /usr/bin/env python
# -*- coding:utf-8 -*-


obj = {
    '$and': [
        {'name': 'jim'},
        '$or': [
            {
                'state': 1
            },
            {
                'age': {
                    '$gt': 10
                }
            }
        ]
    ]
}

sql = ""

def json2where(jsonobj):
    def _like():
        pass

    def _between():
        pass

    def _or():
        pass

    def _and(k, v):
        return '%s=%s' % (k, v)
    
    _where_str = ''
    _where = []
#    _like_obj = jsonobj.get('$like') 
#    _between_obj = jsonobj.get('$between') 
#    _or_obj = jsonobj.get('$or')
    _temp = []
    for key, val in jsonobj.iteritems():
        if key == '$like':
            a = json2where(val)
            _where_str += a
        elif key == '$between':
            a = json2where(val)
            _where_str += a
        elif key == '$or':
            a = json2where(val)
            _where_str += a
        else:
            _where_str += '%s=%s and ' % (key, val)
    return _where_str



if __name__ == '__main__':
    print json2where(obj)
