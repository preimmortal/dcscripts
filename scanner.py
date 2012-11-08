import os
import subprocess
import time
from datetime import datetime

__dir__ = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(__dir__, 'scanner.log')

while 1:
    try:
        subprocess.check_call("ping www.google.com -n 1", shell=True)
    except:
		time.sleep(1)
		try:
			subprocess.check_call("ping www.google.com -n 1", shell=True)
		except:
			print "No Internet Access, writing to log"
			dctime = datetime.now()
			if dctime.hour>12:
				dctime.hour-=12
				xm = "pm"
			else:
				xm = "am"
			dcstring = "DISCONNECT: %02d:%02d:%02d %s on %02d/%02d/%d\n" % (dctime.hour,dctime.minute,dctime.second,xm,dctime.month,dctime.day,dctime.year)
			log = open(filepath, 'a')
			log.write(dcstring)
			log.close()
			subprocess.call("n_reset.bat")
    time.sleep(3)

