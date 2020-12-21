#Cagil Benibol
#2212637 , cagil.benibol@metu.edu.tr


import numpy as np
import math as m
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import pandas as pd #pip3.8 install pandas
import scipy.stats as stats
from scipy.stats import norm
df = pd.read_excel("data4.xlsx","Sheet1")
x = df['mt1'].values.tolist()
y = df['mt2   '].values.tolist()
n=len(x)
data=sorted((i,j) for i,j in zip(x,y))
for i in range (n):
	x[i]=data[i][0]
	y[i]=data[i][1]
#print(x)
#print(y)
#stats

x_sum=0
y_sum=0
xx_sum=0
xy_sum=0
yy_sum=0
yfit=[]
for i in range (n):
	x_sum=x_sum + x[i]
	y_sum=y_sum + y[i]
	xx_sum=xx_sum + ((x[i])**2)
	yy_sum=yy_sum + ((y[i])**2)
	xy_sum=xy_sum + ((x[i])*(y[i]))
x_av=x_sum/n
y_av=y_sum/n
S_xx= xx_sum - ((x_sum**2)/n)
S_xy= xy_sum - ((x_sum*y_sum)/n)
S_yy=yy_sum - ((y_sum**2)/n)
B=S_xy/S_xx 
A=y_av - (B*x_av)
for i in range (n):
	yfit.append(A + (B*x[i]))

SST=S_yy
SSR=(SST**2)/S_xx 
SSE=SST - SSR
r=m.sqrt(1 - (SSE/SST))
r_2=r**2
print('r^2:',r_2)
sd=m.sqrt(SSE/(n-2))
print(sd,'sd')
MSE=sd**2
print(MSE, 'MSE')
MSR=SSR
print(MSR,'SSR, MSR')
print(SSE, 'SSE')
F=MSR/MSE
print(F, 'F')
B_sd= sd/(m.sqrt(S_xx))
t= B/(B_sd)
print(t,'t')
df= n-2
print(df,'dof')
#	PLOTS
#mt1
plt.title('Plot x-y')
plt.xlabel('X')
plt.ylabel('Y')
plt.plot(x,y, 'b-')
plt.plot(x,yfit, 'r-')
plt.grid(True)
plt.savefig('x_y.pdf')
plt.show()

#r^2 value is 0.779 which is about 78%. Y values are probably explained by x values where the corelation is high
#t value is 0.89 when we look at to the corresponding t table for 98 dof we can conclude that it is in 60% confidence level.
#When we look at F MSR is quiete large. Hence Linear model seems to be useful.