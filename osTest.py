from threading import Timer
import subprocess

child1=subprocess.Popen("mitmdump -s startport.py ")

# os.system("mitmdump -s startport.py ")


def endit():
    child1.kill()
    print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    # os.system("taskkill /f /t /im mitmdump.exe")

t=Timer(10,endit)
t.start()

#噢还先明确了使用的cmd
#曾经用过的方法：用os.system执行多条命令，第一条是mitm第二条sleep第三条taskkill
#然后又用了Timer来执行os.system--taskkill
#原来是因为，python是单线程的，这样就会一直停在那个os.system那里不动
#所以应该放到子线程里，在合适的时候kill/terminate