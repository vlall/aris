#arista.py
import os
import subprocess
import commands

class Ip_Check:

	def __init__(self):
			
			public_IP = commands.getstatusoutput('curl -s checkip.dyndns.org | sed -e \'s/.*Current IP Address: //\' -e \'s/<.*$//\'') 
			local_IP = commands.getstatusoutput('ifconfig | grep -Eo \'inet (addr:)?([0-9]*\.){3}[0-9]*\' | grep -Eo \'([0-9]*\.){3}[0-9]*\' | grep -v \'127.0.0.1\'')
			self.public_IP = public_IP[1]
			self.local_IP=str(local_IP[1])

	def EOS_login(self, hostname='arista', hostpass='arista'):
			try:
				'''
				>admin
				>en
				>conf t
				>show vlan
				os.system('ssh' + hostname)
				password = (hostpass)
				'''
				print ('Connection successful!')
			except Exception:
				print('Connection failed')
	
	def connection(self):
		pass
	def trace_Route(self, IP):
		pass
	def arp_Table(self):
		pass

def main():
	x = Ip_Check()
	#test = subprocess.Popen(["ping","-W","2","-c", "1", "192.168.1.70"], stdout=subprocess.PIPE)
	#output = test.communicate()[0]
	#print output
	netStat=commands.getstatusoutput('netstat -n')
	# Add 2, for the label lines
	i = netStat[1].count('tcp')+2
	netStat = netStat[1].split('\n')[0:i]
	for tcp in netStat:
		print tcp
	print ('Public IP: ')+ x.public_IP
	print ('Local IP: ')+ x.local_IP

main()
