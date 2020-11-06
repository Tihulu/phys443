#Cagil Benibol
#2212637 , cagil.benibol@metu.edu.tr

import numpy as np
import math as m
import matplotlib.pyplot as plt

#stats, vars
lambd=.77
event, inter= np.loadtxt('week3.txt',skiprows = 1,unpack = True)
exp_val=[]
p=0.0
inter_sum=0
for i in range (len(inter)):
	inter_sum=inter_sum + inter[i]
#main
def plot(event, inter,exp_val):
	plt.title('Neutrinos from supernovae')
	plt.xlabel('# of Events')
	plt.ylabel('# of Intervals')
	plt.plot(event, inter , 'r*', label="Given Data")
	plt.plot(event, exp_val , 'b-', label="Fit")
	plt.semilogy()
	plt.grid(True)
	plt.savefig('Neutrinos from supernovae.pdf')
	plt.legend()
	plt.show()
def write_to_file(event, inter,exp_val): 
	txt=open("Neutrinos from supernovae.txt","w") #to write txt file	
	txt.write('{:s} 	{:s} 	{:s}'.format("# of Events","# of Intervals(DATA)","# of Intervals(Fit)"))
	txt.write("\n")
	for i in range(len(event)):
		x= str(event[i])
		y= str(inter[i])
		z= str(exp_val[i])
		write=txt.write('    {:s} 		{:s} 		{:s}'.format(x,y,z))
		txt.write("\n")
	txt.close()

for i in range (len(event)):
	p = ((m.exp(-1*lambd)*(lambd)**i) / m.factorial(i))
	exp_val.append(p*inter_sum)
write_to_file(event, inter,exp_val)
plot(event, inter,exp_val)


