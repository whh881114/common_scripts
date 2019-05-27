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
            j = re.sub(r'(#.*)|(\n)', "", i)
            if j == '':
                pass    # 当匹配到以#开头或\n的内容时，直接跳过。
            else:
                k = re.sub(r'(\ +)|(\t+)', " ", j)  # 将行内容的多个空格或tab内容统一换成一个空格
                l = re.sub(r'\ +', " ", k)  # 将行内容的多个空格统一换成一个空格，这个防止\t和\ 相互交叉填写。
                host_list.append(l)

    # 去掉重复内容，并删除空内容''。
    host_list=list(set(host_list))
    # print("Debug " * 20)
    # print(host_list)
    # print("Debug " * 20)

    # 对文件中的每行进行强制性检查格式，只允许有四列，其他情况全记录在日志中。
    for i in host_list:
        if len(i.split(' ')) != 4:
            logger.warn("%s，此行内容不符标准格式：主机名/IP地址 ssh端口 用户名 密码，支持多个空格或TAB分隔，但是只允许存在四列。" % i)
        else:
            (host, port, username, password) = i.split(' ')
            logger.info("开始为%s配置ssh信任。" % host)

            # 设置ps1值，因为建立信息时，不一定是root，所以配置ps1值为root和普通用户提示符。
            ps1 = '#|$'
            try:
                port = int(port)
                cmd = 'ssh-copy-id -f -p %d %s@%s' % (port, username, host)
            except:
                logger.critical("主机记录异常%s %s %s %s，不能转换成正确的ssh-copy-id命令，跳过此主机记录。" % (host, port, username, password))
                continue

            child = pexpect.spawn(cmd)
            index = child.expect([ps1, pexpect.EOF, pexpect.TIMEOUT, 'assword:', '(yes/no)?'])

            # 当主机名故意写错时，index == 0也是成功的，无法用child.before或child.after来匹配内容。所以先使用一个nc命令来测试端口或主机名对不对的情况。
            cmd = "nc -zv %s %d" % (host, port)
            retcode = subprocess.call(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            if retcode == 0:
                pass
            else:
                logger.critical("主机记录异常%s %d %s %s，测试主机所对应的端口不通，跳过此主机记录，请检查主机名或端口名。" % (host, port, username, password))
                continue

            if index == 0:
                # 匹配到ps1，那说明已经配置过了信任。
                child.sendline('exit')
                logger.info("主机记录正常%s %d %s %s，此主机已经配置过了信任，忽略此记录。" % (host, port, username, password))

            elif index == 1:
                # 没有匹配除ps1，'assword:', '(yes/no)?'以外的匹配项。
                logging.error("主机记录异常%s %d %s %s，建立信任时，没有匹配到所期望的匹配符。" % (host, port, username, password))

            elif index == 2:
                logging.error("主机记录异常%s %d %s %s，建立信任时，连接超时。" % (host, port, username, password))

            elif index == 3:
                child.sendline("%s" % password)
                sub_index = child.expect(['assword:', ps1])
                if sub_index == 0:
                    logger.error("主机记录异常%s %d %s %s，建立信任时，用户所对应的密码错误。" % (host, port, username, password))
                elif sub_index == 1:
                    child.sendline('exit')
                    logger.info("主机记录正常%s %d %s %s，此主机已成功配置信任。" % (host, port, username, password))

            elif index == 4:
                pexpect.spawn('yes')

                # 第一个内容，如果匹配时，还有可能再出现一个'(yes/no)?'，这表示目标主机换过IP地址。所以这些还需一个index再做分支判断。
                sub_index = child.expect(['(yes/no)?', 'assword:'])

                if sub_index == 0:
                    child.sendline('yes')
                    child.expect('assword:')
                    child.sendline("%s" % password)
                elif index == 1:
                    child.sendline("%s" % password)

                # 此时再检查密码是否输入错误。
                sub_index = child.expect(['assword:', ps1])
                if sub_index == 0:
                    logger.error("主机记录异常%s %d %s %s，建立信任时，用户所对应的密码错误。" % (host, port, username, password))
                elif sub_index == 1:
                    child.sendline('exit')
                    logger.info("主机记录正常%s %d %s %s，此主机已成功配置信任。" % (host, port, username, password))



if __name__ == "__main__":
    main()