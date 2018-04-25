#coding=utf-8
#练习类
import datetime
import time

#开始计时
startTime = datetime.datetime.now()

time.sleep(1)

#结束计时
endTime = datetime.datetime.now()
print(endTime - startTime)
#输出：0:00:01.000791