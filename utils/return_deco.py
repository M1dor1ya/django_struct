# -*- coding: utf-8 -*-
# @Time    : 2018/6/25 16:18
# @Author  : Zcs
# @File    : return_deco.py
import json
from django.http import JsonResponse


def return_deco(func):
    def wrapper(*args, **kw):

        #  status, data = func(*args, **kw)
        result = func(*args, **kw)
        if type(result) is tuple:
            status = result[0]
            data = result[1]
            if status == 0:
                if data != '':
                    return_dict = {'status': '0', 'results': data}
                else:
                    return_dict = {'status': '0'}
            elif status == 1:
                if data != '':
                    return_dict = {'status': '1', 'msg': data}
                else:
                    return_dict = {'status': '1'}

            json_data = json.dumps(return_dict)
            return JsonResponse(json_data, safe=False)
        else:
            return result
    return wrapper
