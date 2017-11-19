from math import pow,sqrt
import sys

bodies=[ ['Kerbol','Kerbin','Mun'] , [1.172332*pow(10,18),3.5316000*pow(10,12),6.5138398*pow(10,10)] , [261600000.0,600000.0,200000.0] ]


if len(sys.argv)<3:
	print
	print 'Not enough arguments: '+str(len(sys.argv)-1)+' arg(s) given while 2 are required'
	print
	print 'Usage: python Escape_Velocity.py <body> <radius(m)>'
	print 'List of bodies: '+str(bodies[0])
	sys.exit()	
	
if len(sys.argv)>3:
	print
	print 'Too many arguments: '+str(len(sys.argv)-1)+' args given while 2 are required'
	print
	print 'Usage: python Escape_Velocity.py <body> <radius(m)>'
	print 'List of bodies: '+str(bodies[0])  
	sys.exit()
 
 
body=next((i for i,b in enumerate(bodies[0]) if b == sys.argv[1]),-1)

if body == -1:
	print
	print 'No body with name \''+sys.argv[1]+'\' found ...'
	print 'List of bodies: '+str(bodies[0])
	sys.exit()	

mu=bodies[1][body]
eqr=bodies[2][body]
r=float(sys.argv[2])

v=sqrt(2*mu/r)
v2=sqrt(pow(2090.4,2)-(2*3.530461*pow(10,12)*(700000-84159286))/(700000.0*84159286))

print 'Escape velocity: '+str(v)
print v2
