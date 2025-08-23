import os
import threading

def read_count():
    try:
        with open("./count.txt", 'r', encoding="utf8") as f:
            return int(f.read().strip())
    except (FileNotFoundError, ValueError):
        return 1

def save_count(n):
    with open("./count.txt", 'w', encoding="utf8") as f:
        f.write(str(n))

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
    save_count(n)

n = read_count()

autoCommit()
set_interval(autoCommit, 86400) #24시간 마다 실행