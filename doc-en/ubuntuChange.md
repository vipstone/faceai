# Ubuntu apt-get和pip源更换 #

更新数据源为国内，是为了加速安装包的增加速度。


# 更换apt-get数据源 #

1. 输入：sudo -s切换为root超级管理员；
2. 执行命令：vim /etc/apt/sources.list；
1. 使用命令：%d 清空所有内容；
1. 清华数据源地址：https://mirrors.tuna.tsinghua.edu.cn/help/ubuntu/ 选择相应的版本复制内容，点击“i”键进入编辑文本模式，粘贴内容到vim编辑窗体，点击“ESC”键进入编辑模式，输入“:wq”保存离开；
2. 更新源：sudo apt-get update；
3. 更新软件：sudo apt-get upgrade；


# pip3的安装与升级 #
安装pip3：sudo apt-get install python3-pip

升级pip3：sudo pip install --upgrade pip

查看pip版本：pip -V


# pip源更换 #

1. 根目录创建.pip文件：mkdir ~/.pip；
1. 创建文件pip.conf：vim .pip/pip.conf；
1. 点击“i”键，进入编辑模式，复制信息：
 ```
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
trusted-host = pypi.tuna.tsinghua.edu.cn
```
这个更换的是清华的源，清华的源5分钟同步官网一次，建议使用。
清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/
阿里云 http://mirrors.aliyun.com/pypi/simple/
中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
豆瓣(douban) http://pypi.douban.com/simple/
中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/

1. 点击：“ESC”切换到命令行模式，输入“:wq”保存离开。



# 修改默认python版本号 #

我们也可以把Ubuntu的默认python版本号进行修改，步骤如下：

1、删除原有Python连接文件

>sudo rm /usr/bin/python

2、切换成root账户，建立指向Python3的连接

切换root账户：sudo -s

建立执行Python3的连接

>ln -s /usr/bin/python3.6 /usr/bin/python

以上操作就是完成默认Python版本号设置，使用：python -V查看默认版本号.
