import time, sys
import socket
import queue
import threading

class PortScaner(object):

    #TODO：输入网址，然后解析后扫描
    def func_DNS(domain):
        try:
            return socket.gethostbyname(domain)
        except Exception as e:
            print (e)

    #返回端口列表
    def get_port_lists(self, start_port, end_port):
        if start_port >= 1 and end_port <= 65535 and start_port <= end_port:
            return list(range(start_port, end_port+1))
        else:
            return list(range(1, 65535+1))


    class PortScan(threading.Thread):

        #init部分
        def __init__(self, port_queue, ip, timeout = 3):
            threading.Thread.__init__(self)
            self.__port_queue = port_queue
            self.__ip = ip
            self.__timeout = timeout

        #扫描调用
        def run(self):
            while True:
                #队列为空时终止
                if self.__port_queue.empty():
                    break
                isOpen = "[OPEN]"
                port = self.__port_queue.get()
                ip  = self.__ip
                timeout = self.__timeout

                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.settimeout(timeout)
                    result_code = s.connect_ex((ip, port))
                    if result_code == 0:
                        #print的话不会按顺序输出，这个是多线程的原因...
                        #stdout.write可以解决，但是不会end=\n
                        sys.stdout.write(isOpen+'\t'+str(port)) #wite的内容不能是int，所以要转成str
                        sys.stdout.write('\n')
                except Exception as e:
                    print(e)
                finally:
                    s.close()

def main():
    ip = "127.0.0.1" # 扫描的ip
    thread_num = 100 # 线程数量
    start_time = time.time() # 脚本开始执行的时间
    port_scner = PortScaner()
    port_list = port_scner.get_port_lists(1050,1100) #在这里输入端口范围
    port_queue = queue.Queue() # 使用queue模块, 线程专用
    threads = [] # 所开线程列表

    #加入队列，开启线程
    for port in port_list:
        port_queue.put(port)
    for t in range(thread_num):
        threads.append(port_scner.PortScan(port_queue, ip, timeout = 3))
    # 启动线程
    for thread in threads:
        thread.start()
    # 阻塞线程
    for thread in threads:
        thread.join()
    end_time = time.time() # 脚本结束执行的时间
    print("用时:",end_time-start_time)

# if __name__ == '__main__':
#     main()