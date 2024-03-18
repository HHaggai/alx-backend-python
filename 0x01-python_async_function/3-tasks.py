#!/usr/bin/env python3
""" Import wait_random from 0-basic_async_syntax.
    Write a funct (do not create an async funct, use the regular funct
    syntax to do this) task_wait_random that takes an integ max_delay and
    returns a asyncio.Task. """
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ Tasks """
    task = asyncio.create_task(wait_random(max_delay))
    return task
