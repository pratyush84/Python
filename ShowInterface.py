from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import sys
import pexpect
import string


switch_ip="<IPADDR>"
switch_un="user"
switch_pw="s3cr3t"

child=pexpect.spawnu('ssh %s@%s' % (switch_un, switch_ip))
child.logfile=sys.stdout
child.timeout=4
child.expect('Password:')
child.sendline(switch_pw)
child.expect('>')
child.sendline('en')
child.expect('Password:')
child.sendline('cisco')
child.expect('#')

child.sendline('show running-config interface GigabitEthernet 1/0/1')

child.expect('#')
data=child.before
child.sendline('exit')
child.expect(pexpect.EOF)

list1=data.splitlines()

desc=None
avlan=None
mode1=None
nego=None
vvlan=None
duplex=None
bps=None
action=None

for member in list1:
	if "description" in member:
		desc=member.split('"')
		desc=desc[1]
		desc=desc.lstrip()

	if "switchport access" in member:
		avlan=member.split("vlan")
		avlan=avlan[1]
		avlan=avlan.lstrip()
	
	if "switchport mode" in member:
		mode1=member.split("mode")
		mode1=mode1[1]
		mode1=mode1.lstrip()
		
	if "switchport nonegotiate" in member:
		nego=member.split("switchport")
		nego=nego[1]
		nego=nego.lstrip()
	
	if "switchport voice" in member:
		vvlan=member.split("vlan")
		vvlan=vvlan[1]
		vvlan=vvlan.lstrip()

	if "duplex" in member:
		duplex=member.split("duplex")
		duplex=duplex[1]
		duplex=duplex.lstrip()
	
	if "storm-control" in member:
		if "broadcast level bps" in member:
			bps=member.split("bps")
			bps=bps[1]
			bps=bps.lstrip()
		elif "action" in member:
			action=member.split("action")
			action=action[1]
			action=action.lstrip()
			
	
	if "spanning-tree" in member:
		sptree=member.split("spanning-tree")
		sptree=sptree[1]
		sptree=sptree.lstrip()


with open('/home/my/bckupconfig121.yaml','w') as f:
	f.write('---\n')
	f.write('IfGB101Desc: %s\n' % desc)
	f.write('IfGB101AVlan: %s\n' % avlan)
	f.write('IfGB101Mode: %s\n' % mode1)
	f.write('IfGB101Nego: %s\n' % nego)
	f.write('IfGB101VVlan: %s\n' % vvlan)
	f.write('IfGB101Duplex: %s\n' % duplex)
	f.write('IfGB101Strmbps: %s \n' % bps)
	f.write('IfGB101Strmact: %s\n' % action)
	f.write('IfGB101SPtree: %s\n' % sptree)
	f.close()
	
	




