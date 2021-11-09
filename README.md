# auroraCurlToPvOutput
short python script to upload Power One Aurora PVI-3600 solar inverter 
output to pvOutput https://pvoutput.org/
using python to run cli aurora "C" program http://www.curtronics.com/Solar/AuroraData.html#GetIt to download data from inverter
and construct  a curl command that uploads it to pvOutput.com

The script is run as a cron job on a raspberry pi -2.
