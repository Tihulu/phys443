import numpy as np
import matplotlib.pyplot as plt
N_MC = 10000 # number of Monte Carlo Experiments
nBins = 50 #number of bins for Histograms
data_x, data_y = [], []  #create list that hold x and y
#do experiments
for  i in range(N_MC):
# generate MC data
	x = np.random.uniform()
	y = -20000*np.log(1-x)
	data_x.append(x)
	data_y.append(y)
##setup figure
fig=plt.figure(figsize=(13,5))
fig_x=fig.add_subplot(1,2,1)
fig_y=fig.add_subplot(1,2,2)#
fig_x.hist(data_x,nBins)
fig_x.set_xlabel('r')
fig_y.hist(data_y,nBins)
fig_y.set_ylabel('x(r)')
plt.show()
