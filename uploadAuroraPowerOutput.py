import os
import re
from datetime import date

#pvOutput API key
myAPIkey =<pvOutput API Key>
#pvOutput SystemID
mySystemID = <pvOutput SystemID>

today = date.today().strftime("%Y%m%d")
stream = os.popen("sudo aurora -a2 -k1  /dev/ttyUSB0")
output =stream.read()
output = re.sub(" +",",",output).split(",")
output = (float(output[1])*1000)

cmd = 'curl -d "d=' + str(today) +'" -d "g='+ str(output) +'" -H "X-Pvoutput-Apikey: ' + myAPIkey + '" -H "X-Pvoutput-SystemId: ' + mySystemID +'" https://pvoutput.org/service/r2/addoutput.jsp'
os.system(cmd)
