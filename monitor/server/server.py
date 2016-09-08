#!/usr/bin/env python
# -*- coding: <utf-8> -*-

from core.main_server import MonitorServer


if __name__ == '__main__':
    s = MonitorServer('0.0.0.0', '8000')
    s.run()
