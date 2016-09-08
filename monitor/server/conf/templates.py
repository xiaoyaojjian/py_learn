#!/usr/bin/env python
# -*- coding: <utf-8> -*-


from conf.services import linux


class BaseTemplate(object):
    def __init__(self):
        self.name = 'YourTemplateName'
        self.group_name = 'YourGroupName'
        self.hosts = []
        self.services = []


class LinuxTemplate(BaseTemplate):
    def __init__(self):
        super(LinuxTemplate, self).__init__()
        self.name = 'LinuxTemplate'
        self.services = [
                linux.cpu,
                linux.memory,
                        ]