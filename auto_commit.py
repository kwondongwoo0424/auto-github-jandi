import os
import threading

n = 1

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

def autoCommit():
    global n
    f = open("./README.md", 'a', encoding="utf8")
    f.write(" ")
    
    os.system("git add README.md")
    os.system(f'git commit -m "Update README.md {n}"')
    os.system("git push origin main")
    
    n+=1

autoCommit()
set_interval(autoCommit, 86400) #24시간 마다 실행