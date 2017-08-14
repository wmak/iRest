from pync import Notifier
import time
import os

while True:
    print("Working")
    for i in range(20):
        print('{} minutes'.format(20-i))
        time.sleep(60)
    os.system('espeak -v +f4 "Start"')
    Notifier.notify('Rest eyes', sound='Blow')
    print("Resting")
    time.sleep(30)
    os.system('espeak -v +f4 "Half"')
    Notifier.notify('Halfway', sound='Bottle')
    time.sleep(30)
    os.system('espeak -v +f4 "done"')
    Notifier.notify('Rest done', sound='Ping')
