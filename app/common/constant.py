#!/usr/bin/env python
#-*- coding: utf-8 -*-
# vim:fenc=utf-8
# @author tlwlmy
# @version 2016-09-11

import os

MZ_ROOT_PATH = os.getcwd()    # 根目录
MZ_CM_SATIC_PATH = os.path.join(MZ_ROOT_PATH, 'app/static')    # 静态文件目录


WEIXIN_TOKEN = 'weixin'


WX_EVENT_CLICK_SINGIN     = 1    # 微信点击事假
WX_EVENT_CLICK_EXPAND     = 2    # 微信点击推广
WX_EVENT_CLICK_USER_INFO  = 3    # 微信点击用户信息
WX_EVENT_CLICK_PROFIT     = 4    # 微信点击赚钱攻略
WX_EVENT_CLICK_BIND_MZ    = 5    # 微信点击绑定应用账号
WX_EVENT_CLICK_ACTIVE_PAY = 6    # 微信点击激活提现
WX_EVENT_CLICK_INVITE     = 7

# pay_type分类
MZ_PAY_TYPE_MODE_SIGNIN   = 1    # 签到
MZ_PAY_TYPE_MODE_SON      = 2    # 收徒
MZ_PAY_TYPE_MODE_EXCHANGE = 3    # 兑换
MZ_PAY_TYPE_MODE_SIGNIN   = 4    # 联盟


# pay_type
# 徒弟们
WX_PAY_TYPE_BILL_SUMMARY     = 0    # 汇总

WX_PAY_TYPE_SIGNIN_RANK_ONE  = 1    # 自己签到
WX_PAY_TYPE_SIGNIN_RANK_TWO  = 2    # 徒弟签到
WX_PAY_TYPE_SIGNIN_RANK_TRE  = 3    # 徒孙签到
WX_PAY_TYPE_SIGNIN_RANK_FOUR = 4    # 曾徒孙签到

# 师傅们
WX_PAY_TYPE_ART_FATHER      = 11    # 师傅收徒
WX_PAY_TYPE_ART_GRANDFATHER = 12    # 祖师收徒
WX_PAY_TYPE_ART_ANCERSTORS  = 13    # 师公收徒

# 支付
MZ_PAY_TYPE_EXCHANGE_ONE     = 21    # 1元直充
MZ_PAY_TYPE_EXCHANGE_TWO     = 22    # 2元直充
MZ_PAY_TYPE_EXCHANGE_TRE     = 23    # 3元直充
MZ_PAY_TYPE_EXCHANGE_FIVE    = 24    # 5元直充
MZ_PAY_TYPE_EXCHANGE_TEN     = 25    # 10元直充
MZ_PAY_TYPE_EXCHANGE_TWENTY  = 26    # 20元直充
MZ_PAY_TYPE_EXCHANGE_FIFTY   = 27    # 50元直充
MZ_PAY_TYPE_EXCHANGE_HUNDRED = 28    # 100元直充
MZ_PAY_TYPE_EXCHANGE_FVHDR   = 29    # 500元直充


WX_PAY_TYPE_GIVE_PRESENT  = 30    # 赠送收入

MZ_PAY_TYPE_PERFECT_USER_INFO = 50    # 完善个人资料
MZ_PAY_TYPE_BIND_MOBILE       = 51    # 绑定手机
MZ_PAY_TYPE_APP_EXP           = 52    # 体验试玩
MZ_PAY_TYPE_CREATE_SHORTCUT   = 53    # 创建快捷方式
MZ_PAY_TYPE_NOVICE_HONGBAO    = 54    # 新手红包

MZ_PAY_TYPE_FULFIL_ALN_TASK           = 60    # 完成联盟任务
MZ_PAY_TYPE_SON_FULFIL_ALN_TASK       = 61    # 徒弟完成联盟任务
MZ_PAY_TYPE_GRANDSON_FULFIL_ALN_TASK  = 62    # 徒孙完成联盟任务
MZ_PAY_TYPE_OFFSPRING_FULFIL_ALN_TASK = 63    # 曾徒孙完成联盟任务


MZ_PAY_TYPE_SUBSCRIBE_HONGBAO = 70    # 关注红包
MZ_PAY_TYPE_SON_SUBSCRIBE     = 71    # 徒弟关注


# 美赚用户任务分类
MZ_TASK_MODE_ENTIRE     = 0    # 全部任务
MZ_TASK_MODE_SELF       = 1    # 自己任务
MZ_TASK_MODE_SON        = 2    # 徒弟任务
MZ_TASK_MODE_EXCHANGE   = 3    # 自己兑换任务

MZ_TASK_MODE = {
    MZ_TASK_MODE_ENTIRE: [],
    MZ_TASK_MODE_SELF: [
        MZ_PAY_TYPE_PERFECT_USER_INFO,
        MZ_PAY_TYPE_CREATE_SHORTCUT,
        MZ_PAY_TYPE_BIND_MOBILE,
        MZ_PAY_TYPE_FULFIL_ALN_TASK,
    ],
    MZ_TASK_MODE_SON: [
        MZ_PAY_TYPE_SON_FULFIL_ALN_TASK,
        MZ_PAY_TYPE_GRANDSON_FULFIL_ALN_TASK,
        MZ_PAY_TYPE_OFFSPRING_FULFIL_ALN_TASK,
    ],
    MZ_TASK_MODE_EXCHANGE: [
        MZ_PAY_TYPE_EXCHANGE_ONE,
        MZ_PAY_TYPE_EXCHANGE_TWO,
        MZ_PAY_TYPE_EXCHANGE_TRE,
        MZ_PAY_TYPE_EXCHANGE_FIVE,
        MZ_PAY_TYPE_EXCHANGE_TEN,
        MZ_PAY_TYPE_EXCHANGE_TWENTY,
        MZ_PAY_TYPE_EXCHANGE_FIFTY,
        MZ_PAY_TYPE_EXCHANGE_HUNDRED,
        MZ_PAY_TYPE_EXCHANGE_FVHDR,
    ],
}

# 徒弟收益付费类型
MZ_DISCIPLE_PAY_TYPE = {
    'son': [
        WX_PAY_TYPE_ART_FATHER,
        MZ_PAY_TYPE_SON_FULFIL_ALN_TASK,
    ],
    'grandson':[
        WX_PAY_TYPE_ART_GRANDFATHER,
        MZ_PAY_TYPE_GRANDSON_FULFIL_ALN_TASK,
    ]
}


# 兑换方式
EXCHANGE_GIFT_WAY_WECHAT         = 1    # 微信支付
EXCHANGE_GIFT_WAY_ALIPAY         = 2    # 支付宝支付
EXCHANGE_GIFT_WAY_MOBILE         = 3    # 手机直充
EXCHANGE_GIFT_WAY_QQ_COIN        = 4    # Q币
EXCHANGE_GIFT_WAY_MOBILE_TRAFFIC = 5    # 流量充值


# 用户
USER_DEFAULT_HEAD_IMG_URL = 'http://{0}/static/headimg/headimg.png'    # 微信用户默认头像

# 查询用户关系的信息
USER_RELATIONSHIP_QUERY_FATHER      = 1    # 查询用户师傅们的信息
USER_RELATIONSHIP_QUERY_GRANDFATHER = 2    # 查询用户师祖们的信息
USER_RELATIONSHIP_QUERY_ANCERSTORS  = 3    # 查询用户师公们的信息

# 微信用户加密密钥
WECHAT_USER_ENCRYPT_SECRET = 'a0d56f733398f1d7186a3119624f07ba'

# 公众号
# 公众号分成方式
APP_SHARE_TYPE_REGULAR_PRICE = 0   # 固定价格的分成
APP_SHARE_TYPE_DYMANIC_RATIO = 1   # 动态的分成比例

# 兑换列表状态
STAT_EXCHANGE_STATUS_WAITING_CHECK = 0    # 等待审核
STAT_EXCHANGE_STATUS_CHECK_SUCCESS = 1    # 审核通过
STAT_EXCHANGE_STATUS_REJECT        = 2    # 拒绝兑换
STAT_EXCHANGE_STATUS_SUCCESS       = 3    # 兑换成功
STAT_EXCHANGE_STATUS_FAIL          = 4    # 兑换失败
STAT_EXCHANGE_STATUS_CANCEL        = 5    # 取消兑换

# 公众号类型
APP_WECHAT_TYPE_AUTH_SERVER      = 0    # 认证服务号
APP_WECHAT_TYPE_UNAUTH_SERVER    = 1    # 未认证服务号
APP_WECHAT_TYPE_UNAUTH_SUBSCRIBE = 2    # 未认证订阅号


PRICE_EXCHANGE_RATE = 1000    # 积分兑换比例 1元等于1000积分

# 手机平台
MOBILE_PLATFORM_IOS     = 1
MOBILE_PLATFORM_ANDROID = 2

# 后台登录账号
BACKGROUND_LOGIN_USER_NAME = 'xiaopao'    # 后台登录用户名
BACKGROUND_LOGIN_PASSWORD  = 'jitui123'   # 后台登录用户密码

# 微信用户授权跳转链接
USER_WECHAT_AUTH_URL = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid={appid}&redirect_uri={redirect_uri}&response_type=code&scope={scope}&state={state}#wechat_redirect'

# 缓存的有效时间
class Duration:
    HalfMin   = 30;
    OneMin    = 60;
    TwoMin    = 120;
    ThrMin    = 180;
    FiveMin   = 300;
    TenMin    = 600;
    FifMin    = 900;
    TwentyMin = 1200;
    HalfHour  = 1800;
    OneHour   = 3600;
    TwoHour   = 7200;
    FiveHour  = 18000;
    HalfDay   = 43200;
    OneDay    = 86400;
    TenDay    = 864000;
