#Cagil Benibol
#2212637 , cagil.benibol@metu.edu.tr

import numpy as np
import math as m
import matplotlib.pyplot as plt

#stats, vars
numb, tl,size = np.loadtxt('week5data.txt',skiprows = 1,unpack = True)
n=len(numb)
dof=n-1
t=2.145 #from t table
#functions
def plot(numb, tl,size,pin1,pin2):
	zero=[0,0]
	plt.title('week5')
	plt.xlabel('Price(TL)')
	plt.ylabel('Size(m^2)')
	plt.plot(tl, size , 'r*', label="Price(TL)")
	plt.plot(pin1, pin2 , 'b*', label="Mean (Confidence Interval %95)")
	plt.grid(True)
	plt.savefig('week5.pdf')
	plt.legend()
	plt.show()
def mean(x):
	l=len(x)
	sum=0
	for i in range (0,l):
		sum = x[i] + sum
	mean= sum//l
	return mean

def std(x,xmean):
	l=len(x)
	stdu=0
	for i in range (0,l):
		stdu = (x[i] - xmean)**2 + stdu
	std=m.sqrt((stdu)//float(l-1))
	return std
#main

#stats
mu_tl=mean(tl)
mu_size=mean(size)
std_tl=std(tl,mu_tl)
std_size=std(size,mu_size)


#Sample size is small we need to look up for t table (page45).
#Since the deg. of freedom is 14 and the confidence level is 95%,we can easily find that t eqauls to 2.145.

#Finding intervals with the confidence level of 95%
tl_minusplus=( (t*std_tl)//(m.sqrt(n)) )
interval_tl=[(mu_tl - tl_minusplus), (mu_tl + tl_minusplus)]
size_minusplus=( (t*std_size)//(m.sqrt(n)) )
interval_size=[(mu_size - size_minusplus), (mu_size + size_minusplus )]

#print
print('The degrees of freedom:',dof, ' ,The t from the table:',t,' ,The sample size',n)
#print(mu_tl, ':is the mean of the prices, ',mu_size, ':is the mean of the sizes')
print('The standard deviation of the price:',std_tl,'TL',', The standard deviation of the size',std_size,'m^2')
print('Average price is :',mu_tl,'+/-',tl_minusplus,'TL')
print('Average price interval is (with 95% confidence):', interval_tl,'TL')
print('Average house size is :',mu_size,' +/-',size_minusplus,'m^2')
print('Average size interval is (with 95% confidence):', interval_size,'m^2')
plot(numb, tl,size,interval_tl,interval_size)