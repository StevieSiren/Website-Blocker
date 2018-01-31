import time
from datetime import datetime as dt

hosts_path = r'C:\Windows\System32\drivers\etc\hosts'
redirect = '127.0.0.1'
website_list = ['www.facebook.com', 'www.twitter.com', 'www.youtube.com']
final_list = [redirect + ' ' + i for i in website_list]
final_list_block = '\n'.join(final_list)

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        print('Within working hours - websites are blocked.')
        with open(hosts_path, "r+") as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + ' ' + website + '\n')
    else:
        with open(hosts_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print('It is time to have fun!')
    time.sleep(5)
