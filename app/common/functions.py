#!/usr/bin/env python
#-*- coding: utf-8 -*-
# vim:fenc=utf-8
# @author tlwlmy
# @version 2016-09-11


import json, random, string, hashlib, urlparse
from decimal import Decimal
from flask import jsonify, make_response, request
from datetime import date, datetime
from functools import wraps
from app.common.constant import PRICE_EXCHANGE_RATE, CM_STATIC_URL

def api_response(contents, code=200):
    """返回API的响应
    :param contents: dict, JSON内容
    :param code: int, HTTP CODE
    :return: response
    """
    response = jsonify(contents)
    response.status_code = code
    return response

def replace_content(content, params):
    # 替换参数
    for key, value in params.items():
        content = content.replace('{' + key + '}', str(value))
    return content

def cover_none(key):
    # 转换None为字符串
    return '' if key is None else key

def random_lower_str(randomlength=5):
    # 随机长度字符串
    return ''.join(random.sample(string.lowercase, randomlength))

def random_int_str(randomlength=6):
    # 随机长度数字字符串
    return ''.join(map(str, [random.randint(0, 9) for i in range(0, randomlength)]))

def parse_url_params(url_conf, params):
    effect = True
    final = {}

    for key, conf in url_conf.items():
        if conf['need'] == 1:
            value = params.get(key, None)
            if value is None:
                effect = False
                continue
            final[key] = value
        else:
            final[key] = params.get(key, conf['default'])

        if final[key] is not None:
            if conf['type'] == 'i':
                final[key] = int(final[key])
            elif conf['type'] == 't':
                final[key] = datetime.fromtimestamp(int(final[key]))
            elif conf['type'] == 'd':
                final[key] = Decimal(final[key])

    return effect, final

def generate_str(final):
    # 字典按照'&'分割转字符串
    combine_str = ''
    for key, value in final.items():
        if type(value) == int:
            combine_str += "%s=%d&" % (key, value)
        else:
            combine_str += "%s=%s&" % (key, value)

    if final.keys():
        combine_str = combine_str[0:-1]

    return combine_str

def parse_str(combine_str):
    # 解析参数
    final = {}
    if combine_str.find('&') >= 0:
        for item in combine_str.split('&'):
            item = item.split('=')
            final[item[0]] = item[1]

    return final

class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, Decimal):
            return str(obj)
        else:
            return json.JSONEncoder.default(self, obj)

def md5(raw_str):
    # md5加密
    return hashlib.new('md5', str(raw_str)).hexdigest()

def parse_dict(final):
    # 拼接字典参数
    return '&'.join(['{0}={1}'.format(key, val) for key, val in final.items()])

def get_signature(params, secret):
    # 参数排序签名加secret拼接MD5签名
    keys = params.keys()
    keys.sort()

    sign_str = ''
    for key in keys:
        sign_str += "%s=%s&" % (key, params[key])

    #拼接上密钥
    sign_str += "%s=%s" % ("key", secret)
    return md5(sign_str).upper()

def url_dict_params(need, ktype, default='None', alias=None):
    """
    need: 参数是否必须 0表示不需要 1表示需要
    ktype: 参数类型 i表示整形 t表示时间戳 D表示Decimal
    default: 当need为不必要时默认值
    alias: 别名,使用参数名
    """

    final = {
        'need': need,
        'type': ktype,
    }

    # 默认值
    if default != 'None':
        final['default'] = default

    # 别名
    if alias is not None:
        final['alias'] = alias

    return final

def get_remote_ip():
    # 获取ip地址
    if 'X-Real-Ip' in request.headers.keys():
        return request.headers['X-Real-Ip']
    elif 'X-Forwarded-For' in request.headers.keys():
        return request.headers.getlist('X-Forwarded-For')[0]
    return request.remote_addr

def filter_fields(white_fields, modify_info):
    # 过滤参数

    final = {field: modify_info[field] for field in white_fields if field in modify_info.keys()}

    return final

def compare_fields(white_fields, record, modify_info):
    # 比较参数

    final = {field: modify_info[field] for field in white_fields if field in modify_info.keys() and modify_info[field] != record[field]}

    return final

def cover_point_to_price(point):
    # 积分兑换为钱

    return 1.0 * point / PRICE_EXCHANGE_RATE

def cover_price_to_point(price):
    # 钱兑换为积分

    return int(price * PRICE_EXCHANGE_RATE)

def filter_static_url(url):
    # 处理静态文件url

    url_split = urlparse.urlparse(url)

    # 路径
    path = url_split.path[8:] if url_split.path.find('/static/') == 0 else url_split.path

    # 静态文件名
    filename = '{0}{1}'.format(path, '' if url_split.query == '' else '?{0}'.format(url_split.query))

    return filename

def format_static_url(filename):
    # 格式化静态文件url

    return CM_STATIC_URL + filename
