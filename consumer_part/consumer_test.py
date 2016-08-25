# !/usr/bin/env python
# -*- coding: utf-8 -*-

from demoapp.tasks import add, mul, xsum
from celery import chain, group, chord
from celery.result import ResultBase
from datetime import datetime, timedelta
import time
from pytz import timezone


class Consumer(object):
    """
    该类是消费类
    """

    def add_consumer(self, x=None, y=None):
        return add.delay(x, y)

    def add_bind_consumer(self):
        return add_bind.delay(x, y)

    def chain_consumer(self):
        return chain(add.s(3, 4), mul.s(6), mul.s(10)).apply_async()

    def group_consumer(self):
        return group(add.s(i, i) for i in range(10))().get()

    def chord_consumer(self):
        return chord((add.s(i, i) for i in range(10)), xsum.s())().get()

    def map_consumer(self):
        pass

    def starmap_consumer(self):
        pass

    def chunk_consumer(self):
        pass

    # periodic 目前只支持 apply_async 中的 eta 和 countdown 两种方式
    def periodic_consumer(self):
        pass

    def periodic_eta_consumer(self):
        # 时区问题
        #  方法一:
        local_to_use = timezone('Asia/Shanghai')
        target_time = datetime.now(tz=local_to_use) + timedelta(seconds=2)

        #  方法二:
        local_to_use = timezone('Asia/Shanghai')
        local_time = local_to_use.localize(datetime.now())
        target_time = local_time + timedelta(seconds=5)
        return pr_test.apply_async((10, 10), eta=target_time)

    def a_consumer(self, x):
        result = A.delay(x)
        # return list(result.collect())
        return [v for v in result.collect()
                if not isinstance(v, (ResultBase, tuple))]


if __name__ == '__main__':
    # print(datetime.now() + timedelta(seconds=5))

    # exit(0)

    test = Consumer()
    print(test.add_consumer(), )
    # print(test.chord_consumer(), )
    exit()

    re = test.periodic_eta_consumer()
    print('start')
    time.sleep(20)
    print('hi')
    print(re)
    print(re.status)
    print(re.id)
    #
    print(re.get())

    exit()
    # chain 的实验
    # re = test.chain_consumer()
    # time.sleep(2)
    # print(re.ready(), )
    # print(re.successful(), )
    # print(re.get(), )


    # re_list = []
    # for i in xrange(10):
    #     re_list.append(test.add_consumer(i, i + 1))
    # for each_re in re_list:
    #     print(each_re.id, each_re.state, each_re.get())
    #
    from celery.result import AsyncResult
    from combine_example.celery_app import app
    #
    # # 根据对应的id 返回对应的结果.
    # for each_re in re_list:
    #     res = AsyncResult(each_re, app=app)
    #     print(res.state, res.get(), )

    res = AsyncResult(u'8cf32079-b320-49f1-a3f0-59836ba1b6bc', app=app)
    print(res.state)
    print(res.get())
