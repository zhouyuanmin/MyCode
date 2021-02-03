"""
JWT请求
需要在headers里面构建一个字段Authorization
内容是 JWT + 空格 + jwt内容
"""
import requests

headers = {
    "Authorization": "JWT " + "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6IjE3ODU5NzE3NTIyIiwiZXhwIjoxNjEyNDAyMDU1LCJlbWFpbCI6IiJ9.1ILI1-AdAb8InFVwwVovLu7mH1W2qM9FYGDJplDPwhI",
}  # 注意JTW后面跟了一个空格
a = requests.get(url='http://127.0.0.1:8000/user/', headers=headers)
print(a.json())
