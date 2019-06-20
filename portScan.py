import time
import socket
from . import createDB

#TODO：输入网址，然后解析后扫描
def func_DNS(domain):
    try:
        return socket.gethostbyname(domain)
    except Exception as e:
        print (e)

def scanStart(ip, port_list, timeout):
    isOpen = "[OPEN]"
    result =[]

    for port in port_list:
        conn=createDB.get_db()
        cursor=conn.cursor()
        createTime=str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

        #开始辣
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout) #超时时间
        result_code = s.connect_ex((ip, port)) #开放则返回0
        if result_code == 0:
            cursor.execute(
                'INSERT INTO scanInfo (ip,port,state,createTime)'
                ' VALUES (%s,%s,"open",%s)',(ip,port,createTime)
                )
            conn.commit()
            conn.close()
            #后面记得把print去掉            
            print(isOpen,port)
            result.append(port)
        else:
            continue
        s.close()
    return result

#扫描所有端口
def scanAll(ip, startPort, endPort, timeout=3):
    start_time=time.time()
    port_list = range(int(startPort),int(endPort)+1) #range的参数得是int才可以
    result =  scanStart(ip, port_list, timeout)
    end_time=time.time()
    use_time=end_time-start_time
    print("用时:",use_time)
    return result

#可以再搞一个扫描常用端口的

# if __name__ == '__main__':
#     scanAll("127.0.0.1",1050,1100)