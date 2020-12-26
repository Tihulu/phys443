#Cagil Benibol
#2212637 , cagil.benibol@metu.edu.tr, cagil.benibol@gmail.com
#python 3.7.4

#libraries
import numpy as np
import math as m
import matplotlib.pyplot as plt

#given data
x=[1.0,2.0,3.0,4.0]
y=[2.2,2.9,4.3,5.2]
sigma=[0.2,0.4,0.3,0.1]
n=len(x)

#functions
def fitparameters(x,y,sigma):
	n=len(x)
	x_sum, y_sum, xy_sum, xsqr_sum, sigmasqr,sigmasqrinv_sum=0 , 0 , 0, 0, [], 0
	for i in range(n):
		sigmasqr.append(sigma[i]**2)
	for i in range(n):
		x_sum = x_sum + (x[i] / sigmasqr[i])
		y_sum = y_sum + (y[i] / sigmasqr[i])
		xy_sum = xy_sum + ((x[i]*y[i]) / sigmasqr[i])
		xsqr_sum = xsqr_sum + ((x[i]**2) / sigmasqr[i])
		sigmasqrinv_sum = sigmasqrinv_sum + (1/sigmasqr[i])
	# Determining the slope
	alpha = ( (y_sum*xsqr_sum) - (xy_sum*x_sum) ) / ( (sigmasqrinv_sum*xsqr_sum) - ((x_sum)**2) )
	beta = ( (sigmasqrinv_sum*xy_sum) - (y_sum*x_sum) ) / ( (sigmasqrinv_sum*xsqr_sum) - ((x_sum)**2) )
	#Obtaining error from covarience matrix
	D = ( (sigmasqrinv_sum*xsqr_sum) - (x_sum)**2 )
	alpha_sigma , alphabeta_sigma , beta_sigma = m.sqrt(xsqr_sum/D) , (-x_sum)/D , m.sqrt(sigmasqrinv_sum/D)

	return alpha, beta, alpha_sigma, alphabeta_sigma, beta_sigma, sigmasqr

#vars
alpha, beta, alpha_sigma, alphabeta_sigma, beta_sigma, sigmasqr= fitparameters(x,y,sigma)

# chi-square and error
y_est, y_error, chisqr = [], [], 0
for i in range(n):
	y_est.append(alpha + beta*x[i])
for i in range(n):
	chisqr = chisqr + (((y[i]-y_est[i])**2)/sigmasqr[i])

#printing vars and stats
print("alpha:", alpha, "\nbeta:", beta, "\nalpha*beta:", alpha*beta, "\nalpha s.dev.:" , alpha_sigma,
 "\nbeta s.dev. :", beta_sigma, "\nalpha*beta s.dev.:", alphabeta_sigma, "\nchi-square:", chisqr)

numb_of_calculated_data_points=2 #alpha and beta
dof= n - numb_of_calculated_data_points
fit_quality=chisqr/dof
if fit_quality <= 1:
	print('A good fit with ', dof,'dof, and chi-square value is',chisqr,'.')
else:
	print('A bad fit with ', dof,'dof, and chi-square value is',chisqr,'.')

#graph
plt.plot(x, y_est, label='Fit') 
plt.errorbar(x, y, yerr = sigma, fmt ='.',label='Given Values and Errors') 
plt.title('x vs. y')
plt.ylabel('y')
plt.xlabel('x')
plt.grid(True)
plt.savefig('week9_graph.pdf')
plt.legend()
plt.show()

#When we look at to the chi-square table for 2 dof,
#chi-square value (0.646) is near to 0.575(75%) which is far from 1.386(50%).
#Probablity is near to 75% but less than it. It is between 70 and 75 percent.