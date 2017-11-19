from math import pow,sqrt,fabs,pi,floor
import sys

bodies=[ ['Kerbol','Kerbin','Mun'] , [1.172332*pow(10,18),3.5316000*pow(10,12),6.5138398*pow(10,10)] , [261600000.0,600000.0,200000.0] ]


if len(sys.argv)<4:
	print
	print 'Not enough arguments: '+str(len(sys.argv)-1)+' arg(s) given while 3 are required'
	print
	print 'Usage: python Hohman_Transfer.py <body> <initial_radius(m)> <target_radius(m)>'
	print 'List of bodies: '+str(bodies[0])
	sys.exit()	
	
if len(sys.argv)>4:
	print
	print 'Too many arguments: '+str(len(sys.argv)-1)+' args given while 3 are required'
	print
	print 'Usage: python Hohman_Transfer.py <body> <initial_radius(m)> <target_radius(m)>'
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

r=float(sys.argv[2])+eqr

target_r=float(sys.argv[3])+eqr



v1=sqrt( mu/r )

a2=(r+target_r)/2
v2=sqrt( mu*((2/r)-(1/a2)) )
v3=sqrt( mu*((2/target_r)-(1/a2)) )

v4=sqrt( mu/target_r )

dv1=fabs(v2-v1)
dv2=fabs(v4-v3)
dvtot=dv1+dv2

t=pi*sqrt(pow(a2,3)/(mu))

d=int(t//(3600*6))
h=int(t%(3600*6)//3600)
m=int(t%(3600*6)%3600//60)
s=int(t%(3600*6)%3600%60)


print 'Hohman transfer: '+str(v1)+' -> '+str(v2)+' ... '+str(v3)+' -> '+str(v4)
print 'DeltaV:          '+str(dv1)+' + '+str(dv2)+' = '+str(dvtot)+' m/s'
print 'Time:            '+str(d)+'d'+str(h)+'h'+str(m)+'m'+str(s)+'s ('+str(t)+' seconds)'




