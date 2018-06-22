#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests

bot = requests.get('https://slack.com/api/users.list?token=xoxp-7164360422-222327958535-306884292960-2a8f4820fc5bbd07f29d54e91193a849&pretty=1').json()

for user in bot['members']:
    if user['name'] == 'bottest':
        print user['id'], user['name']                                    
