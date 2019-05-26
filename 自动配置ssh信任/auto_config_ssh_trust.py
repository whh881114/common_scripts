# -*- coding: UTF-8 -*-

"""
@File  : auto_config_ssh_trust.py
@Author: Roy Wong (whh881114@gmail.com)
@Date  : 2019/05/26
@Desc  : 使用pexpect模块完成ssh-copy-id操作，以达到创建ssh信任操作。
"""

import re
import sys
import pexpect
import subprocess
import logging
import logging.config


def usage():
    print("Usage: %s <configured_ssh_hosts.list>" % sys.argv[0])
    print("Description: Configure the ssh trust between localhost and the hosts in the list automatically.")
    sys.exit(255)


def main():
    # 读取日志配置文件内容
    logging.config.fileConfig('logging.conf')

    # 创建一个日志器logger
    logger = logging.getLogger('root')


    if len(sys.argv) != 2:
        usage()
    else:
        host_file = sys.argv[1]
        # 将windows换行转换成linux换行，\r\n -> \n。
        cmd = 'dos2unix %s' % host_file
        retcode = subprocess.call(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        if retcode == 0:
            logger.info("强制将%s文件换行格式转为linux格式成功。" % host_file)
        else:
            logger.critical("强制将%s文件换行格式转为linux格式失败。" % host_file)
            sys.exit(254)


    # 日志输出测试命令
    # logger.debug('debug message')
    # logger.info('info message')
    # logger.warn('warn message')
    # logger.error('error message')
    # logger.critical('critical message')

    # 读出主机列表文件
    with open(host_file, 'r') as f:
        host_list = []
        for i in f.readlines():
            # 去掉注释内容
            host_list.append(re.sub(r'(#.*)|(\n)', "", i))

    # 去掉重复内容，并删除空内容''。
    host_list=list(set(host_list))
    host_list.remove('')
    # print(host_list)

    # 对文件中的每行进行强制性检查格式，只允许有四列，其他情况全记录在日志中。
    for i in host_list:
        if len(i.split(' ')) != 4:
            logger.warn("%s，此行内容不符标准格式：主机名/IP地址 ssh端口 用户名 密码，只能以一个空格隔开。" % i)
        else:
            (host, port, username, password) = a.split(' ')
            logger.info("开始为%s配置ssh信任。" % host)

            # 设置ps1值，因为建立信息时，不一定是root，所以配置ps1值为root和普通用户提示符。
            ps1 = '\#|\$'
            try:
                cmd = 'ssh-copy-id -p %d %s@$' % (int(port), host, username)
            except:
                logger.critical("主机记录异常%s %d %s %s，不能转换成正确的ssh-copy-id命令，跳过此主机记录。" % (host, port, username, password))
                break

            child = pexpect.spawn(cmd)
            index = child.expect(['(yes/no)?', 'assword:', ps1, pexpect.EOF, pexpect.TIMEOUT])

            # 第一个内容，如果匹配时，还有可能再出现一个'(yes/no)?'，这表示目标主机换过IP地址。
            # 所以这些还需一个index再做分支判断。

            # 承接上面一个，输入错误的密码后，会再次提示'assword:'，所以这时就需要做提示了。


if __name__ == "__main__":
    main()