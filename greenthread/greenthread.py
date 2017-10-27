# -*- coding: utf-8 -*-
__author__ = 'cain'

from eventlet.twistedutil import callInGreenThread
from eventlet.twistedutil import deferToGreenThread
from core.database import in_transaction
import logging


def monkey_patch_block_on():
    from eventlet import twistedutil
    _block_on = twistedutil.block_on

    def block_on(d):
        if in_transaction():
            msg = 'cannot switch to hub in DB transaction!'
            logging.info(msg)
            raise RuntimeError(msg)
        return _block_on(d)
    setattr(twistedutil, 'block_on', block_on)


def green_thread(func):
    def _wrap_func(*args, **kwargs):
        return callInGreenThread(func, *args, **kwargs)
    return _wrap_func

def defer_to_green_thread(func):
    def _wrap_func(*args, **kwargs):
        return deferToGreenThread(func, *args, **kwargs)
    return _wrap_func
