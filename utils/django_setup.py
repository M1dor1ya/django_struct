# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 17:26
# @Author  : Zcs
# @File    : django_setup.py
"""
在脚本里使用Django环境的方法，使用setup方法建立Django环境
"""
import os, sys, django

def start_django():
    DjangoModulePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(DjangoModulePath)
    os.chdir(DjangoModulePath)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cso_alpha.settings")
    django.setup()

def main():
    start_django()
    #  from phaser1.api.fmg.nginx_txt.utils import test
    #  test()
    from server_ctr.handler.capital_handler import CapitalHandler
    obj = CapitalHandler()
    data = obj.get_capital()
    print(data)
if __name__ == '__main__':
    main()
