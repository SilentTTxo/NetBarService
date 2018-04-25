from Service import say,IpWatcher,IpProductor
import time

if __name__ == '__main__':
    say("start")
    for i in range(50):
        ipWatcher = IpWatcher()
        ipWatcher.start()
        # ipWatcher.join()
    
    ipProductor = IpProductor()
    ipProductor.start()
    # ipProductor.join()

    # while True:
    #     time.sleep(1)