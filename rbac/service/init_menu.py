# -*- coding: utf-8 -*-
# @Time    : 2019/9/28 9:34 PM
# @Author  : all is well
# @File    : init_menu.py
# @Software: PyCharm

from django.conf import settings
import re


def get_structure_data(request):
    """处理菜单结构"""
    menu = request.session[settings.MENU_KEY]
    all_menu = menu[settings.ALL_MENU_KEY]
    permission_menu = menu[settings.PERMISSION_MENU_KEY]


    menu_list = []
    for menu in all_menu:
        del menu['id']
        del menu['is_show']
        menu['meta'] = { 'title': '表格', 'icon': 'example' }
        menu_list.append(menu)


    print("所有菜单： %s" %menu_list)
    print("权限菜单： %s" %permission_menu)



    return menu_list

    # {'name': '用户管理', 'path': '/user', 'icon': 'tb', 'component': Layout, meta: {title: '表格', icon: 'example'}, },

    # {
    #     path: '/',
    #     component: Layout,
    #     redirect: '/dashboard',
    #     children: [{
    #         path: 'dashboard',
    #         name: 'Dashboard',
    #         component: () = > import
    # ('@/views/dashboard/index'),
    # meta: {title: '首页', icon: 'dashboard', noCache: true}
    # }]
    # },
    # # 定制数据结构
    # all_menu_dict = {}
    # for item in all_menu:
    #     item['status'] = False 是否显示
    #     item['open'] = False #展开
    #     item['children'] = []
    #     all_menu_dict[item['id']] = item
    #
    # request_rul = request.path_info
    #
    # for path in permission_path:
    #     # 添加两个状态：显示 和 展开
    #     path['status'] = True
    #     pattern = path['path']
    #     if re.match(pattern, request_rul):
    #         path['open'] = True
    #     else:
    #         path['open'] = False
    #
    #     # 将path添加到菜单下
    #     all_menu_dict[path['menu_id']]["children"].append(path)
    #
    #     # 显示菜单：path 的菜单及上层菜单 status: true
    #     pid = path['menu_id']
    #     while pid:
    #         all_menu_dict[pid]['status'] = True
    #         pid = all_menu_dict[pid]['parent_id']
    #
    #     # 展开path上层菜单：path['open'] = True, 其菜单及其父菜单open = True
    #     if path['open']:
    #         ppid = path['menu_id']
    #         while ppid:
    #             all_menu_dict[ppid]['open'] = True
    #             ppid = all_menu_dict[ppid]['parent_id']
    #
    # # 整理菜单层级结构：没有parent_id 的为根菜单， 并将有parent_id 的菜单项加入其父项的chidren内
    # menu_data = []
    # for i in all_menu_dict:
    #     if all_menu_dict[i]['parent_id']:
    #         pid = all_menu_dict[i]['parent_id']
    #         parent_menu = all_menu_dict[pid]
    #         parent_menu['children'].append(all_menu_dict[i])
    #     else:
    #         menu_data.append(all_menu_dict[i])
    # return menu_data

