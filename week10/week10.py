#Cagil Benibol
#2212637 , cagil.benibol@metu.edu.tr, cagil.benibol@gmail.com
#python 3.7.4

import numpy as np
import matplotlib.pyplot as plt
import math as m
N_MC = 10000 # number of Monte Carlo Experiments
nBins = 50 #number of bins for Histograms
data_x, data_y1, data_y2, data_y3 =[], [], [], []  #create list that hold x and y
#do experiments
for  i in range(N_MC):
# generate MC data
	x = np.random.uniform()

# I took the integral
#https://www.wolframalpha.com/input/?i=integral%28%282%2F%281-exp%28-2%29%29%29*exp%28-2*x%29%29+from+0+to+x
#then find inverse of the function 
#by https://www.wolframalpha.com/input/?i=y%3D%282+e%5E%282+-+x%29+sinh%28x%29%29%2F%28e%5E2+-+1%29+find+x
#The integral is x^3 hence the inverse is x=y^1/3
	y1 = 0.5*( np.log( (-m.exp(2)) / ( (-m.exp(2)-x) + (x*m.exp(2))) ) )
	y2 = m.pow(x,1/3)
	#y3 = -np.log(1-x)
	data_x.append(x)
	data_y1.append(y1)
	data_y2.append(y2)
	#data_y3.append(y3)

#setup figure
fig=plt.figure(figsize=(25,5))
fig_x=fig.add_subplot(1,3,1)
fig_y1=fig.add_subplot(1,3,2)
fig_y2=fig.add_subplot(1,3,3)
#fig_y3=fig.add_subplot(1,4,4)

fig_x.hist(data_x,nBins)
fig_x.set_xlabel('r')

fig_y1.hist(data_y1,nBins)
fig_y2.hist(data_y2,nBins)
#fig_y3.hist(data_y3,nBins)

fig_y1.set_ylabel('P_A(x)')
fig_y2.set_ylabel('P_B(x)')
#fig_y3.set_ylabel('P(x)')
fig_y1.set_xlabel('x(r)')
fig_y2.set_xlabel('x(r)')
#fig_y3.set_xlabel('x(r)')
plt.savefig('week10_graph.png')
plt.show()
