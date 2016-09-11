#!/usr/bin/env python
#-*- coding: utf-8 -*-
# vim:fenc=utf-8
# @author tlwlmy
# @version 2016-09-11

from app import redis_store
import pickle
from functools import wraps
from app.common.constant import Duration

def format_record(record, rtype, dict_keys):
    """
    格式化记录
    @params rtype str: 返回类型 list表示列表 dict表示字典
    @params dict_keys list: 字典类型key列表
    """

    if isinstance(record, list) and rtype == 'dict':
        # 生产多重key数据
        final = {}
        dict_keys_len = len(dict_keys)
        for row in record:
            # 利用字典可变性质，一层层生产字典
            r = final
            for index in range(0, dict_keys_len):
                key = row[dict_keys[index]]
                if key not in r.keys():
                    r[key] = {}
                if index == dict_keys_len - 1:
                    r[key] = row
                r = r[key]
        return final

    return record

def generate_cache_key(func_name, prefix, prefix_keys):
    # 生产缓存key
    cache_key = prefix if prefix is not None else func_name
    # cache_key = '{0}:{1}'.format(cache_key, ':'.join(map(str, prefix_keys)))
    for index in range(len(prefix_keys)):
        cache_key = '{0}:{1}'.format(cache_key, prefix_keys[index] if prefix_keys[index] is not None else '')
    return cache_key

def cached(prefix=None, rtype='list', dict_keys=[], timeout=Duration.HalfHour, func_type='class'):
    # 查询缓存数据
    def wrapper_fun(func):
        @wraps(func)
        def _wrapper_fun(*args, **kwargs):
            # 生产缓存key
            start_index = 1 if func_type == 'class' else 0
            cache_key = generate_cache_key(func.func_name, prefix, args[start_index:])

            # 外部修改缓存时长
            expire_time = kwargs['timeout'] if 'timeout' in kwargs.keys() else timeout

            # 删除timeout参数
            if 'timeout' in kwargs.keys():
                del kwargs['timeout']

            # 查询redis缓存数据
            final = redis_store.get(cache_key) if expire_time else None
            if final is None:
                record = func(*args, **kwargs)
                final = format_record(record, rtype, dict_keys)


                # 序列化参数，写缓存，设置缓存有效时间
                final = pickle.dumps(final)
                if expire_time:
                    redis_store.set(cache_key, final, expire_time)

            # 格式化参数
            final = pickle.loads(final)

            return final
        return _wrapper_fun
    return wrapper_fun
