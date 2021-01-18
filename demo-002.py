"""
使用容联云通讯平台来实现发短信功能
需要安装sdk库: pip install ronglian-sms-sdk
"""
from ronglian_sms_sdk import SmsSDK

accId = '8a216da8762cb4570176ef87f32243ba'
accToken = '97f09583668147a8ad064c9d139f408a'
appId = '8a216da8762cb4570176ef87f42243c1'


def send_message():
    sdk = SmsSDK(accId, accToken, appId)
    tid = '1'
    mobile = '17859717522'
    data = (1234, 5)
    resp = sdk.sendMessage(tid, mobile, data)
    print(resp)


if __name__ == '__main__':
    send_message()
