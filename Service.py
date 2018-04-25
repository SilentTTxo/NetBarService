import win32com.client
import threading
import os
import socket
import time
import logging

from multiping import MultiPing


logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


sk = win32com.client.Dispatch("SAPI.SpVoice")

# say fuck♂you
def say(str):
    sk.speak(str)


IpMap = {}

# 消费IP
def pingAll():
    logger.info("start search...")
    hostname = socket.getfqdn(socket.gethostname())
    ip = socket.gethostbyname(hostname)

    ipPrefix = ".".join(ip.split(".")[:-1])
    logger.debug("ipPrefix: %s",ipPrefix)

    ips = [ipPrefix + "." + str(ends) for ends in range(2,254)]
    # logger.debug(ips)
    
    mp = MultiPing(ips)
    mp.send()
    responses, no_responses = mp.receive(0.5)
    logger.debug(responses.keys())

    for ip in responses.keys():
        if ip not in IpMap:
            IpMap[ip] = True
            say("IP尾号为" + ip.split(".")[-1] + "的铂金大神，已上线")
            logger.info("%s\tonline",ip)
    
    for ip in no_responses:
        if ip in IpMap:
            IpMap.pop(ip)
            say("IP尾号为" + ip.split(".")[-1] + "的铂金大神，已下线")
            logger.info("%s\toffline",ip)
    