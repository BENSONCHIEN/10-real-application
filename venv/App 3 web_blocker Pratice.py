import time
from datetime import datetime as dt
# dt.now()
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1" #会连到这个地址
website_list = ["www.facebook.com","facebook.com"]
# 两种方法
# 一、打开文件，编辑host文件，
# 二、第三方工具

''' without using 'with' statement 
file = open('file_path','w')
file.write('hello world !')
file.close()
'''

while True:
    if dt(dt.now().year, dt.now().month,dt.now().day,8) <dt.now()< dt(dt.now().year,dt.now().month,dt.now().day,17):
        print("working hours")
        # with statement can handle file simply (do not need to write file.close())
        # with open('path','mode') as file:
        #     file.write
        with open(hosts_path,'r+') as file: #'r' read mode
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write("\n" + redirect +'  ' + website+"\n")
    else:
#难点: 去除block的网址,保留原有的内容
#读取全部内容 > 把光标放到最开头 > 把读取的再写入一遍,直到in website list的 > 截断,把后面的都删除
# a + b (储存 a+b)> 0 + a + b > a + a + b > (把后面的删除) a, 去除了b
        with open(hosts_path,'r+') as file:
            content = file.readlines() #all line
            file.seek(0) #replave the pointer, go to the first character of the file content
            for line in content:  #each line
                if not any(website in line for website in website_list):
                    file. write(line)
            # 等价于下面
            # for line in content:
            #     for website in website_list:
            #         if website not in line:
            #             file.write(line)

            file.truncate() #截断，从当前位置起截断，未指定则从这截断，之后的所有字符被删除
        print("fun hours")
    time.sleep(5) # run per 5 second

# read():
# 1、读取整个文件，返回的是一个字符串，字符串包括文件中的所有内容。
# 2、若想要将每一行数据分离，即需要对每一行数据进行操作，此方法无效。
# 3、若内存不足无法使用此方法。
# readline():
# 1、每次读取下一行文件。
# 2、可将每一行数据分离。
# 3、主要使用场景是当内存不足时，使用readline()可以每次读取一行数据，只需要很少的内存。
# readlines():
# 1、一次性读取所有行文件。
# 2、可将每一行数据分离，从代码中可以看出，若需要对每一行数据进行处理，可以对readlines()求得的结果进行遍历。
# 3、若内存不足无法使用此方法。
