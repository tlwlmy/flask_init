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
# 关系等级
USER_STAT_RANK_ONE    = 1    # 徒弟
USER_STAT_RANK_TWO    = 2    # 徒孙
USER_STAT_RANK_TRE    = 3    # 曾徒孙

# 用户汇总数据
USER_BILL_PAY_TYPE_SUMMARY     = 0    # 汇总

USER_DEFAULT_HEAD_IMG_URL = 'http://{0}/static/headimg/headimg.png'    # 微信用户默认头像

# 查询用户关系的信息
USER_RELATIONSHIP_QUERY_FATHER      = 1    # 查询用户师傅们的信息
USER_RELATIONSHIP_QUERY_GRANDFATHER = 2    # 查询用户师祖们的信息
USER_RELATIONSHIP_QUERY_ANCERSTORS  = 3    # 查询用户师公们的信息

# 兑换操作
USER_EXCHANGE_APPLY_FOR_GIFT = 1    # 申请兑换
USER_EXCHANGE_CANCEL_GIFT    = 2    # 取消兑换

# 兑换情况
USER_EXCHANGE_NEVER_APPLY_FOR  = 0    # 用户未申请过兑换
USER_EXCHANGE_HAVE_APPLIED_FOR = 1    # 用户兑换过

# 新手红包状态
USER_NOVICE_HONGBAO_NOT_RECEIVE        = 0    # 新手红包未领取
USER_NOVICE_HONGBAO_RECEIVE_NOT_REMIND = 1    # 新手红包已领取未提示
USER_NOVICE_HONGBAO_RECEIVE_AND_REMIND = 2    # 新手红包已领取且提示

# 邀请活动
WECHAT_INVITE_ACTIVITY_END         = 0    # 邀请活动结束标志
WECHAT_INVITE_ACTIVITY_SOLD_OUT    = 0    # 活动下架
WECHAT_USER_SUBSCRIBE_APP_COUNT    = 10    # 完成关注公众号个数
WECHAT_FATHER_INVITE_INTERVAL      = 3     # 邀请徒弟间隔
WECHAT_FATHER_OBTAIN_WELFARE_LIMIT = 20     # 邀请福利次数

# 微信用户加密密钥
WECHAT_USER_ENCRYPT_SECRET = 'a0d56f733398f1d7186a3119624f07ba'


# 公众号
# 公众号分成方式
APP_SHARE_TYPE_REGULAR_PRICE = 0   # 固定价格的分成
APP_SHARE_TYPE_DYMANIC_RATIO = 1   # 动态的分成比例

APP_BILL_SUMMARY     = 0    # 公众号汇总

APP_WECHAT_JUMP_AID = 3    # 活动中间跳转公众号id
APP_WECHAT_PAY_AID  = 2    # 微信有支付功能的公众号aid
APP_WECHAT_RELATE_AIDS = range(11, 31)    # 微信关联公众号列表


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

# 公众号应用类型
APP_WECHAT_APPLY_TYPE_NORMAL = 0    # 正常
APP_WECHAT_APPLY_TYPE_UNION  = 1    # 联合
APP_WECHAT_APPLY_TYPE_SIGNIN = 2    # 签到

# 应用类型列表
APP_WECHAT_APPLY_TYPE_LISTS = [
    APP_WECHAT_APPLY_TYPE_NORMAL,
    APP_WECHAT_APPLY_TYPE_UNION,
    APP_WECHAT_APPLY_TYPE_SIGNIN,
]


# 兑换礼物选项
APP_TARGETING_GIFT_ENTIRE   = 0    # 选择全部礼物
APP_TARGETING_GIFT_SPECIFIC = 1    # 特定礼物

PRICE_EXCHANGE_RATE = 1000    # 积分兑换比例 1元等于1000积分


# 手机平台
MOBILE_PLATFORM_IOS    = 1
MOBILE_PLATFORM_ANDROID = 2

# 后台登录账号
BACKGROUND_LOGIN_USER_NAME = 'xiaopao'    # 后台登录用户名
BACKGROUND_LOGIN_PASSWORD  = 'xp42#$*('   # 后台登录用户密码

# 领取福利安全域名链接
RECEIVE_WELFARE_SEC_URL = 'http://sec.18city.net/?id=3&mt=2'

# celery队列
CELERY_BROKER_URL = 'redis://localhost:6379/11'

APP_BACKUP_URL = 'http://www.weixinyunduan.com/gzzh/artview-1.html?wid=323593&rid=365372'    # 公众号备用链接

# 微信用户授权跳转链接
USER_WECHAT_AUTH_URL = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid={appid}&redirect_uri={redirect_uri}&response_type=code&scope={scope}&state={state}#wechat_redirect'

# 领取福利链接
RECEIVE_WELFARE_URL = 'http://xpzhuan.duapp.com/app.php'

# 用户邀请图片
USER_SIGNIN_INVITE_URL = 'http://xpweb.b0.upaiyun.com/pic/invite_s.jpg'

# 静态文件url
USER_STATIC_URL = 'http://img.coosport.cn/static/'

# 跳转网页
USER_WECHAT_AUTH_JUMP_WEB_ONE  = 1    # 跳转前端页面一 邦卡
USER_WECHAT_AUTH_JUMP_WEB_TWO  = 2    # 跳转前端页面二 首页
USER_WECHAT_AUTH_JUMP_WEB_TRE  = 3    # 跳转前端页面三 赚钱攻略
USER_WECHAT_AUTH_JUMP_WEB_FOUR = 4    # 跳转前端页面四 兑换页面
USER_WECHAT_AUTH_JUMP_WEB_FIVE = 5    # 跳转前端页面五 获取验证码
USER_WECHAT_AUTH_JUMP_WEB_SIX  = 6    # 跳转前端页面六 激活提现

# 跳转外部安全链接
JUMP_SECURITY_EXTERNAL_URL = 'http://{access_domain}/jp_dm?jt={jump_type}&s={s}'

# 跳转外部安全链接
WECHAT_JUMP_EXTERNAL_URL = 'http://{access_domain}/wechat/{uid}/jump?jump_type={jump_type}'

# 微信中间跳转链接
WECHAT_MIDDLE_WEB_URL = 'http://{access_domain}/wechat/jump?jump_type={jump_type}&s={s}'

# 网赚获取付费openid链接
WECHAT_MZ_PAY_URL = 'http://{access_domain}/app/gp_jump?uid={uid}'

# 用户跳转外部链接
USER_EXTERNAL_WEB_URL = {
    '1': 'http://{access_domain}/user/bind',
    '2': 'http://{access_domain}/user/info',
    '3': 'http://{access_domain}/user/how',
    '4': 'http://{access_domain}/user/exchange',
    '5': 'http://{access_domain}/user/code',
    '6': 'http://{access_domain}/user/pay',
}

# 广告平台密钥
AD_PLATFORM_APP_SECRET = {
    'wanpu': {
        'ios': '025333735039097cf5bf845a48a657c9',
    },
}


# 用户授权跳转链接
USER_AUTH_URL = {
    '1': 'https://open.weixin.qq.com/connect/oauth2/authorize?appid={appid}&redirect_uri=http%3A//{jump_domain}/wechat/auth_jump%3Fappid%3D{appid}%26jump_type%3D1&response_type=code&scope=snsapi_base&state=123#wechat_redirect',
    '2': 'https://open.weixin.qq.com/connect/oauth2/authorize?appid={appid}&redirect_uri=http%3A//{jump_domain}/wechat/auth_jump%3Fappid%3D{appid}%26jump_type%3D2&response_type=code&scope=snsapi_base&state=123#wechat_redirect',
    '3': 'https://open.weixin.qq.com/connect/oauth2/authorize?appid={appid}&redirect_uri=http%3A//{jump_domain}/wechat/auth_jump%3Fappid%3D{appid}%26jump_type%3D3&response_type=code&scope=snsapi_base&state=123#wechat_redirect',
    '4': 'https://open.weixin.qq.com/connect/oauth2/authorize?appid={appid}&redirect_uri=http%3A//{jump_domain}/wechat/auth_jump%3Fappid%3D{appid}%26jump_type%3D4&response_type=code&scope=snsapi_base&state=123#wechat_redirect',
}

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

