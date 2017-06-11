#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
This is a tool for ADB command
author:maxinyu
'''

import os
import tkFileDialog 
import subprocess
#import PyQt4.QtCore,PyQt4.QtGui 
from Tkinter import *

'''
连接设备
'''
def menu_device_click():
    deviceinfo = subprocess.check_output('adb devices').split('\r\n')
    device = deviceinfo[1].split('\t')
    deviceid = device[0]
    if deviceid:
        print('device connect succeed!')
    else:
        print('please connect your device!!!')
    '''
    text = os.popen('adb devices')
    print text.read()
    
    if text:  
        print os.popen('adb devices').read()
    else:
        print('请打开USB调试！！！')
    '''
'''
root
'''
def menu_root_click():
    text = os.popen('adb root')
    if text:
        print text.read()
        print("ROOT finished!")

'''
shell
'''
def menu_shell_click():
    #subprocess.call(shell=True)
    text = os.popen('adb shell')
    print text.read()


'''
安装应用
'''
def menu_install_click():
    filename=choose_file()
    text = os.popen("adb install " + filename)  
    print text.read() 

'''
卸载应用
'''
def menu_uninstall_click():
    text = os.popen("adb uninstall com.baidu.duersdkdemo")  
    print text.read()

    
'''
导出系统日志
'''
def menu_log_output_click():
    filename=save_file()
    text = os.popen('adb logcat -v time > ' + filename)  
    print text.read()

'''
清空系统日志
'''
def menu_log_clear_click():
    if os.popen('adb logcat -c'):  
        print('clear finished!')

'''
重置电量
'''
def menu_battery_reset_click():
    subprocess.call('adb shell dumpsys batterystats --enable full-wake-history', shell=True)
    print('-----------------------')
    subprocess.call('adb shell dumpsys batterystats --reset', shell=True)

'''
导出电量
'''
def menu_battery_output_click():
    filepath=choose_path()
    os.popen('adb shell dumpsys batterystats > ' + des)  
 

'''
发送文件到手机
'''
def menu_push_click():
    src=choose_file()
    if src:
        print("source file:" + src)
        print("please choose destination:")
        des = choose_path()
        if des:
            print(des)
            text = os.popen('adb push ' + src + des)  
            print text.read()

'''
文件导出到PC
'''
def menu_pull_click():
    src=choose_file()
    if src:
        print("source file:" + src)
        print("please choose destination:")
        des = save_file()
        if des:
            print(des)
            text = os.popen('adb pull ' + src + des)
            print text.read()  


'''
sdkLogAll导出到PC
'''
def menu_pull_default_click():
    des=choose_path()
    text = os.popen('adb pull sdcard/baidu/duersdk/sdkLogAll.txt '+ des)
    print text.read()


'''
删除文件
'''
def menu_rm_click():
    pass


'''
列出所有应用
'''
def menu_listall_click():
    text = os.popen('adb shell pm list packages -f')  
    print text.read()

'''
列出第三方应用
'''
def menu_3rd_click():
    text = os.popen('adb shell pm list packages -3')  
    print text.read()


'''
选择文件
'''
def choose_file():
    filename = tkFileDialog.askopenfilename()
    #str = unicode(filename.toUtf8(), 'utf-8', 'ignore') 
    return filename

'''
选择路径
'''
def choose_path():
    path = tkFileDialog.askdirectory() 
    return path

'''
保存文件
'''
def save_file():
    filepath = tkFileDialog.asksaveasfilename()
    return filepath



def main():
    win = Tk()
    win.geometry('400x250+500+300') 
    win.title('ADBTool v1.0.0')

    #菜单项
    menubar = Menu(win)
    
    adb_debug = Menu(menubar, tearoff=0)
    adb_debug.add_command(label="设备连接",command=menu_device_click)
    adb_debug.add_command(label="adb root", command=menu_root_click)
#    adb_debug.add_command(label="进入shell", command=menu_shell_click)
    menubar.add_cascade(label="DEBUG",menu=adb_debug)


    adb_install = Menu(menubar, tearoff=0)
    adb_install.add_command(label="安装应用", command=menu_install_click)
    adb_install.add_command(label="卸载应用（默认卸载duersdkdemo）", command=menu_uninstall_click)
    menubar.add_cascade(label="安装卸载", menu=adb_install)

    adb_log = Menu(menubar, tearoff=0)
    adb_log.add_command(label="导出系统日志（-v time）", command=menu_log_output_click)
    adb_log.add_command(label="清空日志缓存", command=menu_log_clear_click)
    menubar.add_cascade(label="日志", menu=adb_log)

    adb_battery = Menu(menubar, tearoff=0)
    adb_battery.add_command(label="重置电量文件", command=menu_battery_reset_click)
    adb_battery.add_command(label="导出电量文件", command=menu_battery_output_click)
    menubar.add_cascade(label="电量统计", menu=adb_battery)

    adb_file = Menu(menubar, tearoff=0)
    adb_file.add_command(label="发送文件到手机", command=menu_push_click)
    adb_file.add_command(label="导出文件到PC", command=menu_pull_click)
    adb_file.add_command(label="导出文件到PC(sdkLogAll.txt)", command=menu_pull_default_click)
    adb_file.add_command(label="删除文件", command=menu_rm_click)
    menubar.add_cascade(label="文件", menu=adb_file)

    adb_app = Menu(menubar, tearoff=0)
    adb_app.add_command(label="所有应用（-f）", command=menu_listall_click)
    adb_app.add_command(label="第三方应用", command=menu_3rd_click)
    menubar.add_cascade(label="列举应用", menu=adb_app)


    win.config(menu=menubar)
    win.mainloop()

if __name__ == '__main__':
    main()