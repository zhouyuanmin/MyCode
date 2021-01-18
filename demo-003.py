"""
QQ登陆
需要安装第三方包: pip install QQLoginTool
"""
from QQLoginTool.QQtool import OAuthQQ

# QQ登录参数
QQ_CLIENT_ID = '101474184'
QQ_CLIENT_SECRET = 'c6ce949e04e12ecc909ae6a8b09b637c'
QQ_REDIRECT_URI = 'http://www.meiduo.site:8080/oauth_callback.html'

# "https://graph.qq.com/oauth2.0/show?which=Login&display=pc&response_type=code&client_id=101474184&redirect_uri=http%3A%2F%2Fwww.meiduo.site%3A8080%2Foauth_callback.html&state=%2F&scope=get_user_info

# 获取QQ登录页面网址
oauth = OAuthQQ(client_id=QQ_CLIENT_ID, client_secret=QQ_CLIENT_SECRET,
                redirect_uri=QQ_REDIRECT_URI, state="yard.html")
login_url = oauth.get_qq_url()
print(login_url)  # 将链接粘贴到浏览器请求，登陆成功之后，返回的链接就包含了code的值

code = ''  # AF6298841730C2A00F0675BDF8E90040
if code:
    access_token = oauth.get_access_token(code)
    print(access_token)
    openid = oauth.get_open_id(access_token)
    print(openid)
    # 8D2F1BAE028ECA45A903C5ABA4483A2D
    # 7515974396649D3E850422595209B350
