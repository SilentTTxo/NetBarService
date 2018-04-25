import win32com.client
import threading
import os
import socket
import time

import queue

sk = win32com.client.Dispatch("SAPI.SpVoice")

# say fuck♂you
def say(str):
    sk.speak(str)

IpWatcherQueue = queue.Queue()
IpMap = {}

class IpProductor(threading.Thread):
    def __init__(self):
        super(IpProductor,self).__init__()

        hostname = socket.getfqdn(socket.gethostname())
        ip = socket.gethostbyname(hostname)

        self.ipPrefix = ".".join(ip.split(".")[:-1])
        print(self.ipPrefix) 
    
    def run(self):
        while True:
            for ipEnd in range(2,255):
                ipPing = "%s.%s" % (self.ipPrefix ,str(ipEnd))
                IpWatcherQueue.put(ipPing)
            
            time.sleep(0.01)

class IpWatcher(threading.Thread):
    def __init__(self):
        super(IpWatcher,self).__init__()

    def run(self):
        while True:
            ipPing = IpWatcherQueue.get()
            print ("ping " + ipPing)
            rs = os.popen("ping %s -n 1 -w 1" % ipPing).read()
            if "已接收 = 1" in str(rs):
                if ipPing not in IpMap:
                    IpMap[ipPing] = True
                    say("IP尾号为" + ipPing.split(".")[-1] + "的铂金大神，已上线")
            else:
                if ipPing in IpMap:
                    IpMap.pop(ipPing)
                    say(ipPing.split(".")[-1] + "已下线")