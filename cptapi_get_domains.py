#!/usr/bin/python3
# -*- coding: utf-8 -*-
import OpenSSL
from cptapi import Cptapi
from my_config import *
#domain_name='Global'
domain_name=''
domain=Cptapi(user,password,url,domain_name,api_wait_time=api_wait_time,read_only=False,page_size=page_size,publish_wait_time=publish_wait_time)
try:
    domains=domain.show_domains()
    domain.logout()
    for domain in domains:
        print(domain['name'])
except OpenSSL.SSL.SysCallError as e:
    logging.error(e)
    logging.error("SSL connection error.")
    logout()
except requests.exceptions.SSLError as e:
    logging.error(e)
    logout()
except requests.exceptions.ConnectionError as e:
    logging.error(e)
    logging.error("Connection error.")
except ValueError as err:
    print(err.args)
