import time
from datetime import datetime as dt
host_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.0"
website_list = ["facebook.com","www.facebook.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() <dt(dt.now().year,dt.now().month,dt.now().day,17):
        print("working time")
        with open(host_path,'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write("\n" + website + "  " + redirect)
    else:

        print("fun hour")
        with open(host_path,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any( website in line for website in website_list):
                    file.write(line)
            file.truncate()

    time.sleep(10)
