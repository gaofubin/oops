# -*- coding: utf-8 -*-
# @Time    : 2019/9/28 9:34 PM
# @Author  : all is well
# @File    : init_menu.py
# @Software: PyCharm

from django.conf import settings
import re


def init_menu(request):
    """处理菜单结构"""
    menu = request.session[settings.MENU_KEY]
    all_menu = menu[settings.ALL_MENU_KEY]
    permission_menu = menu[settings.PERMISSION_MENU_KEY]

    all_menu_dict = {}
    permission_menu_dict = {}
    menu_list = []
    for menu in all_menu:
        menu['children'] = []
        menu['alwaysShow'] = 'true'
        all_menu_dict[menu['id']] = menu

    request_url = request.path_info

    for perm_menu in permission_menu:
        all_menu_dict[perm_menu['mid']]['children'].append(perm_menu)

    for menu in all_menu_dict.values():
        menu_list.append(menu)

    # print(menu_list)
    # print("所有菜单： %s" %all_menu)
    # print("权限菜单： %s" %permission_menu)

    return menu_list

