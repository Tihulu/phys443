#Cagil Benibol
#2212637 , cagil.benibol@metu.edu.tr

import numpy as np
import math as m
import matplotlib.pyplot as plt

#stats, vars
#lambd=.77
count, inter= np.loadtxt('week4.txt',skiprows = 1,unpack = True)
exp_val=[]
p=0.0
la=0
inter_sum=0
chisqr=0
n=3 #dof
for i in range (len(inter)):
	inter_sum=inter_sum + inter[i]
for i in range (len(inter)):
	la= (count[i]*inter[i]) + la
mu=la/inter_sum
print ('mean',mu)
std= inter.std()
print ('std:', std)
#functions
def plot(count, inter,exp_val):
	plt.title('week4')
	plt.xlabel('# of counts')
	plt.ylabel('# of Intervals')
	plt.plot(count, inter , 'r*', label="Given Data")
	plt.plot(count, exp_val , 'b-', label="Fit")
	#plt.semilogy()
	plt.grid(True)
	plt.savefig('week4.pdf')
	plt.legend()
	plt.show()
def write_to_file(count, inter,exp_val): 
	txt=open("week4out.txt","w") #to write txt file	
	txt.write('{:s} 	{:s} 	{:s}'.format("# of counts","# of Intervals(DATA)","# of Intervals(Fit)"))
	txt.write("\n")
	for i in range(len(count)):
		x= str(count[i])
		y= str(inter[i])
		z= str(exp_val[i])
		write=txt.write('    {:s} 	  		{:s} 				{:s}'.format(x,y,z))
		txt.write("\n")
	txt.close()
#poisson
for i in range (len(count)):
	p = ((m.exp(-1*mu)*(mu)**i) / m.factorial(i))
	exp_val.append(p*inter_sum)
#chi^2
for i in range (len(count)):
	chisqr=(((inter[i] - exp_val[i])**2) / exp_val[i]) + chisqr
print ('chi square:',chisqr)
print ('chi square/dof:',chisqr/n)
write_to_file(count, inter,exp_val)
plot(count, inter,exp_val)
z= (chisqr - mu)/std
print('z:',z)
#When we look at the table it shows us 0.82 probablity with 3 dof and 1.00 chi^2 value.82% is quiete confident, hence it is poisson.