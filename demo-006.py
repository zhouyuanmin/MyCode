"""
git做对象资源服务器
让git用来存储图片、视频、文件等

需要将文件移动到local_repo_path目录里面，再执行git命令即可

链接前缀为 https://gitee.com/zhouyuanmin/images/raw/master/
后面接路径即可
如: https://gitee.com/zhouyuanmin/images/raw/master/imgs/20210508101552.png

上传文件需要使用ssh，并且配置好git相关的ssh
"""
local_repo_path = '/Users/myard/Desktop/images'
git_cmd = f'git -C {local_repo_path}'
total_git_cmd = f'{git_cmd} pull && {git_cmd} add . && {git_cmd} commit -m "sync" && {git_cmd} push origin master'
print(total_git_cmd)
