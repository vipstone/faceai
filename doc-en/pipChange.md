# pip/pip3更换国内源——Windows版 #

用途：pip更换为国内源，可以大大的提高安装成功率和速度。


# Windows更换pip/pip3源 #

1. 打开目录：%appdata%
1. 新增pip文件夹，新建pip.ini文件
1. 给pip.ini添加内容
```
[global]
timeout = 6000
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
trusted-host = pypi.tuna.tsinghua.edu.cn
```

这个更换的是清华的源，清华的源5分钟同步官网一次，建议使用。

注意：不管你用的是pip3还是pip，方法都是一样的，都是创建pip文件夹。


# 国内源列表 #

清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/

阿里云 http://mirrors.aliyun.com/pypi/simple/

中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/ 

豆瓣(douban) http://pypi.douban.com/simple/ 

中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/

