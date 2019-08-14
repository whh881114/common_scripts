# -*- coding: UTF-8 -*-


servers = """
jsse 10.104.133.231 eshop-buy-app-ha
jsse 10.104.134.14 eshop-buy-app-ha
jsse 10.104.135.230 eshop-sale-app-ha
jsse 10.8.34.16 gdm-buy-app-ha

general 10.8.8.113 eshop-content-ms-ha
general 10.8.19.20 eshop-csmp-api-ha
general 10.8.8.49 eshop-customer-api-ha
general 10.8.8.180 eshop-customer-ms-ha
general 10.8.26.5 eshop-goods-ms-ha
general 10.8.19.24 eshop-omp-api-ha
general 10.8.8.132 eshop-order-ms-ha
general 10.8.8.37 eshop-pay-ms-ha
general 10.8.8.96 eshop-presale-ms-ha
general 10.8.26.10 eshop-sale-api-ha
general 10.8.8.229 eshop-store-ms-ha
general 10.8.19.10 eshop-wx-mini-api-ha
general 10.8.28.179 ems-customer-api-ha
general 10.8.28.164 ems-pay-api-ha
general 10.8.28.203 ems-wxmini-api-ha
general 10.8.34.28 gdm-content-ms-ha
general 10.8.34.44 gdm-customer-ms-ha
general 10.8.34.8 gdm-ems-wxmini-api-ha
general 10.8.34.11 gdm-resproxy-api-ha
general 10.8.34.4 gdm-wx-mini-api-ha
"""

for server in servers.splitlines():
    if server == '':
        pass
    else:
        tmp_list = server.split(' ')
        app_type = tmp_list[0]
        app_ipaddr = tmp_list[1]
        app_name = tmp_list[2]
        if app_type == 'jsse':
            print("- service_name: '%s'" % app_name)
            print("  ip_list: ['%s']" % app_ipaddr)
            print("  uri: 'jsse/testManager/test'")
            print("  port: 10014")
            print("  pattern : 'errrorMsg\":\"ok'")
            print("")
            """
              - service_name : 'eshop-common-server'
                ip_list : ['10.104.150.232']
                uri : 'jsse/testManager/test'
                port : 10014
                pattern : 'errrorMsg":"ok'
            """
        elif app_type == 'general':
            print("- service_name: '%s'" % app_name)
            print("  ip_list: ['%s']" % app_ipaddr)
            print("  uri: 'check'")
            print("  port: 80")
            print("  pattern: 'errorCode\":0'")
            print("")
            """
              - service_name : 'eshop-content-ms-proxy'
                uri : 'check'
                port : 80
                pattern : 'errorCode":0'
            """