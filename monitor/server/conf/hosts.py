#!/usr/bin/env python
# -*- coding: <utf-8> -*-

from conf import templates


g1 = templates.LinuxTemplate()
g1.group_name = 'Test groups'
g1.hosts = ['192.168.1.11', '192.168.1.101']


g2 = templates.LinuxTemplate()
g2.group_name = 'puppet server groups'
g2.hosts = ['192.168.1.11', '192.168.1.130', '192.168.1.145']


monitored_groups = [g1, g2]
