#Cagil Benibol
#2212637 , cagil.benibol@metu.edu.tr, cagil.benibol@gmail.com
#python 3.7.4

import numpy as np
import math as m
import matplotlib.pyplot as plt

#vars to create grids
K = np.linspace(0, 50, 120)
pion = np.linspace(0, 50, 120)

#given vars
rho=.5
sigma_K=5
sigma_pi=4
K_0=25
Pi_0=16

#confidence level variable Q_0
[X, Y] = np.meshgrid(K, pion) # this creates grids from K and pion n x m
Q=( (1/(1-rho**2)) * ( (((X-K_0)**2)/(sigma_K**2)) + (((Y-Pi_0)**2)/(sigma_pi**2)) - ((2*rho) * (((X-K_0)*(Y-Pi_0))/(sigma_pi*sigma_K))) ))

	#plot
cr=plt.contourf(X,Y,Q , levels=(0,1,2.3,4.6,6.2,9.2)) #contour region #in order to find regions Q_0=(1,2.3,4.6,6.2,9.2) with the corresponding percentages (39%,68%,90%,95%,99%)
p=plt.plot(K_0,Pi_0, '.r', label="point") #the given point
#ploting legend
leg = [plt.Rectangle((0,0),1,1,fc = pc.get_facecolor()[0]) for pc in cr.collections]
plt.legend(leg,["39%","68%","90%","95%","99%"])
plt.title('Confidence Regions')
plt.xlabel('#K_γ')
plt.ylabel('#π_γ')
plt.grid(True)
plt.show()
plt.savefig('Confidence Regions.png')