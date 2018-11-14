#!/usr/bin/python

# -*- encoding: utf-8 -*-

"""
@Author  :   {Cassiellb}

@License :   (C) Copyright 2013-2017, {Nanjing University of posts and Telecommunications}

@Contact :   {695290718@qq.com}

@Software:   PyCharm

@File    :   app.py

@Time    :   2018/11/14 10:48

@Desc    :

"""

import logging

import aiomysql as aiomysql

import asyncio
import os
import json
import time
from datetime import datetime

logging.basicConfig(level=logging.INFO)
from aiohttp import web


def index(request):
    return web.Response(body=b'<h1>Awesome</h1>')


async def init(event_loop):
    app = web.Application(loop=event_loop)
    app.router.add_route('GET', '/', index)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
