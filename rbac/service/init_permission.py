# -*- coding: utf-8 -*-
# @Time    : 2019/9/29 3:59 PM
# @Author  : all is well
# @File    : init_permission.py
# @Software: PyCharm


from ..models import Menu
from django.conf import settings


def init_permission(request, user_obj):
    """
    初始化用户权限, 写入session
    :param request:
    :param user_obj:
    :return:
    """
    # 获取用户权限QuerySet
    user_permission_obj = user_obj.roles.values('permissions__name',
                                                'permissions__path',
                                                'permissions__icon',
                                                'permissions__component',
                                                'permissions__menu__id').distinct()
    permission_path_list = []  # 获取用户权限信息
    permission_menu_list = []  # 获取用户菜单信息

    for perm in user_permission_obj:
        permission_path_list.append(perm['permissions__path'])
        if perm['permissions__menu__id']:
            temp_data = {
                "mid": perm['permissions__menu__id'],
                "name": perm['permissions__name'],
                "path": perm['permissions__path'],
                "component": perm['permissions__component'],
                "meta": {
                    "title": perm['permissions__name'],
                    "icon": perm['permissions__icon']
                }
            }
            permission_menu_list.append(temp_data)

    # menu_list = list(Menu.objects.values('id', 'name', 'path', 'icon', 'hidden', 'component'))
    menu_list = []
    menu_obj = Menu.objects.values('id', 'name', 'path', 'icon', 'hidden', 'component')
    for menu in menu_obj:
        menu["meta"] = {
            "title": menu['name'],
            "icon": menu['icon']
        }
        menu_list.append(menu)
    # 注：session在存储时，会先对数据进行序列化，因此对于Queryset对象写入session， 加list()转为可序列化对象

    # 保存权限URL
    request.session[settings.PERMISSION_URL_KEY] = permission_path_list

    # 保存 权限菜单 和 所有菜单
    request.session[settings.MENU_KEY] = {
        settings.ALL_MENU_KEY: menu_list,
        settings.PERMISSION_MENU_KEY: permission_menu_list,
    }

