from urllib import request
import shutil
import platform
from tkinter import *

hosts_path = ''
my_system = platform.platform().split('-')[0]


def system():
    global my_system
    global hosts_path
    print(my_system)
    if my_system == 'Linux':
        hosts_path = '/etc/hosts'
    else:
        hosts_path = 'C:\Windows\System32\drivers\etc\hosts'


# 备份
def backup():
    shutil.copy(hosts_path, sys.path[0] + '/bf_hosts')


# 下载
def get_hosts():
    with request.urlopen("https://github.com/TianhaoZhu/hosts/archive/master.zip") as web:
        # 为保险起见使用二进制写文件模式，防止编码错误
        with open(sys.path[0] + '/hosts', 'wb') as outfile:
            outfile.write(web.read())
    shutil.unpack_archive(sys.path[0] + '/hosts', sys.path[0], 'zip')


# 替换
def replace():
    shutil.copy(sys.path[0] + '/hosts-master/hosts', hosts_path)


# 恢复
def over():
    shutil.copy(sys.path[0] + '/bf_hosts', hosts_path)


system()
root = Tk()
bf_button = Button(root, text='备份', command=backup)
bf_button.pack()
get_button = Button(root, text='获取', command=get_hosts)
get_button.pack()
apply_button = Button(root, text='应用', command=replace)
apply_button.pack()
over_button = Button(root, text='恢复', command=over)
over_button.pack()
status = Label(root,text='test',bd=1,relief=SUNKEN)
status.pack(side= BOTTOM,fill=X)

root.mainloop()
