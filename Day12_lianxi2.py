#Day12_lianxi2.py

# 写一个程序，以电子时钟格式打印时间：
# 格式为：
#     HH:MM:SS
'''
import time
s = time.time()
s1 = time.localtime(s)
print(s1[3],":",s1[4],":",s1[5])
'''
'''

def show_time():
    import time
    while True:
        t = time.localtime()
        print("%02d:%02d:%02d"%(t[3],t[4],t[5]),
        end='\r')
        time.sleep(0.1)


show_time()
'''

def show_time():
    import time
    while True:
        t = time.localtime()
        # print("%02d:%02d:%02d"%(t[3],t[4],t[5]),
        # #有两个百分号的时候，后面必须是元组
        # end='\r')
        print("%02d:%02d:%02d"%t[3:6],end='\r')
        time.sleep(0.1)


show_time()