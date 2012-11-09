#coding=utf-8

import subprocess, sys

def subprocess_call(*args, **kwargs):
    # 让python在windows的隐藏子进程中运行
    # also works for Popen.
    # It creates a new *hidden* window, so it will work in frozen apps (.exe).
    IS_WIN32 = 'win32' in str(sys.platform).lower()

    if IS_WIN32:
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags = subprocess.CREATE_NEW_CONSOLE | subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = subprocess.SW_HIDE
        kwargs['startupinfo'] = startupinfo
    retcode = subprocess.call(*args, **kwargs)

    return retcode