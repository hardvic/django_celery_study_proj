# !/usr/bin/env python
# -*- coding: utf-8 -*-

from demoapp.tasks import add

if __name__ == '__main__':
    re = add.delay(1, 2)
    print(re)
