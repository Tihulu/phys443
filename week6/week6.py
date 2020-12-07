#Cagil Benibol
#2212637 , cagil.benibol@metu.edu.tr, cagil.benibol@gmail.com
#python 3.7.4

import numpy as np
import math as m
import matplotlib.pyplot as plt

#stats, vars
acdts, freq = np.loadtxt('week6data.txt',skiprows = 1,unpack = True)
bin=500
lambd=np.linspace(0.01,.50, num=bin) #lambda
LnLarr=[]
freq_sum=647
#functions
def LnL(freq_sum,freq,lambd):
	P=[]
	fact=1
	#L=1
	#for i in range (len(freq)):
	#	p = ((m.exp(-1*lambd)*((lambd)**freq[i])) / m.factorial(freq[i]))
	#	P.append(p) #poisson
	#for i in range (len(freq)):
	#	L=L*P[i]
	#print (P)
	#L= ((m.exp(-1*lambd*6)*((lambd)**freq_sum)) / fact)
	for i in range (len(freq)):
		fact= 	m.factorial(freq[i]) * fact
	LnL= (-len(freq)*lambd) + (m.log(lambd * freq_sum)) - m.log(fact)
	return LnL

def plot(x, y):
	plt.title('Ln-Likelihood Plot for Accident Data')
	plt.ylabel('Ln-Likelihood')
	plt.xlabel('Lambda')
	plt.plot(x, y , 'r-')
	plt.plot(0.3929,-2963.1613 ,'b*',label="1 sigma")
	plt.grid(True)
	plt.savefig('Ln-Likelihood Plot for Accident Data.pdf')
	plt.legend()
	plt.show()

def write_to_file(a, b): 
	txt=open("likelyhood.txt","w") #to write txt file	
	txt.write('{:s} 				{:s}'.format("lambda","Ln-Likelihood"))
	txt.write("\n")
	for i in range(len(a)):
		x= str(a[i])
		y= str(b[i])
		write=txt.write('{:s}	     			{:s}'.format(x,y))
		txt.write("\n")
	txt.close()
#main
for i in range (bin):
	l=lambd[i]
	LnLarr.append(LnL(freq_sum,freq,l))
print(max(LnLarr))
one_sigma=max(LnLarr) - 0.5
print(one_sigma)
write_to_file(lambd, LnLarr)
plot(lambd,LnLarr)


#When we look at the text file:week6data.txt
#We can see that maximum ln value (-2962.6612) which corresponds to 0.1671 lambda
#1sigma corresponds to 0.3929 lambda and -2963.1613 ln value.
