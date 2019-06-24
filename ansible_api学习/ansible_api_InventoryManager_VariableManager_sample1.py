# -*- coding: UTF-8 -*-

"""
使用ansible api运行一个playbook
"""


from __future__ import print_function


# 用于读取yaml和json格式文件
from ansible.parsing.dataloader import DataLoader

# 用于管理变量的类，包含主机，组和扩展等变量
from ansible.vars.manager import VariableManager

# 用于创建和管理 inventory，导入inventory文件
from ansible.inventory.manager import InventoryManager

# ad-hoc存储着角色列表，任务，处理代码块
from ansible.playbook.play import Play

# ad-hoc ansible底层用到的任务队列
from ansible.executor.task_queue_manager import TaskQueueManager

# 回调基类， 用来定义回调事件，比如返回失败成功等信息
from ansible.plugins.callback import CallbackBase

# 执行playbook
from ansible.executor.playbook_executor import PlaybookExecutor

# 操作单个主机
from ansible.inventory import host

# 操作单个主机组
from ansible.inventory import group


"""
InventoryManager

实例化需要两个参数：
    1. 参数一为读取yml文件的信息，需要实例化Dataloader。
    2. 参数二为读取从哪个位置读取资产配置文件，多个可逗号分割。
"""
ansible_host_sources = [
    '/etc/ansible/hosts'
]
inventory = InventoryManager(loader='', sources=ansible_host_sources)

# 以字典的方式打印出主机和主机组相关信息
# print(inventory.get_groups_dict())

# 获取所有的主机
# print(inventory.get_hosts())


"""
添加主机到指定主机组：
    1. 参数一指定主机地址。
    2. 参数二指定主机端口。
    3. 参数三指定主机群组，必须存在的群组。
"""

inventory.add_group('foreman')
print(inventory.get_groups_dict())
print(inventory.get_hosts())
print('- ' * 80)

inventory.add_host(host='foreman.example.com', port=22, group='foreman')
print(inventory.get_groups_dict())
print(inventory.get_hosts(pattern='*'))
print('- ' * 80, end='\n\n')

"""
VariableManager

实例化需要两个参数：
    1. 参数一为读取yml文件的信息，需要实例化DataLoader。
    2. 参数二为资产管理配置变量。
"""
loader = DataLoader()
inventory = InventoryManager(loader='', sources=ansible_host_sources)
variable = VariableManager(loader=loader, inventory=inventory)

# 获取变量
print(variable.get_vars())

host = inventory.get_host(hostname='django2.example.com')
host_vars = variable.get_vars(host=host)
print(host_vars)
print('- ' * 80)

# 设置主机变量方法，传入的host是inventory.get_host获得的主机对象
host = inventory.get_host(hostname='django2.example.com')
variable.set_host_variable(host=host, varname='ansible_ssh_pass', value='12345')
host_vars = variable.get_vars(host=host)
print(host_vars)

variable.set_host_variable(host=host, varname='ansible_ssh_pass', value='12345_again')
host_vars = variable.get_vars(host=host)
print(host_vars)