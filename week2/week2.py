#Cagil Benibol
#2212637 , cagil.benibol@metu.edu.tr

import numpy as np
import math as m
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import scipy.stats as stats
from scipy.stats import norm

mt1, mt2, fin, lab, hw, att = np.loadtxt(
	'data4.txt',
	skiprows = 1,
	unpack = True
	)

def mean(x):
	l=len(x)
	sum=0
	for i in range (0,l):
		sum = x[i] + sum
	mean= sum//l
	return mean
def median(x):
	a=sorted(x)
	l=len(x)
	if l %2 == 0:
		med=(a[int((l/2)-1)]+a[int(l/2)])/2
	else:
		med= a[int( ( (l+1) /2)-1)]
	return med
def std(x,xmean):
	l=len(x)
	stdu=0
	for i in range (0,l):
		stdu = (x[i] - xmean)**2 + stdu
	std=m.sqrt((stdu)//float(l-1))
	return std
def skew(x,xmean,xstd):
	l=len(x)
	skewu=0
	for i in range (0,l):
		skewu = (x[i] - xmean)**3 + skewu
	skew=(skewu)//(100*xstd)
	return skew
def plot(x,bins,name):
	n, bins, patches = plt.hist(x, bins, facecolor='blue', alpha=0.5, normed=True)
	plt.title(name + 'Grades')
	plt.xlabel('Grades')
	plt.ylabel('Number')
	fit = stats.norm.pdf(np.linspace(np.max(x), np.min(x), len(x)), mean(x), std(x,mean(x)))
	plt.plot(np.linspace(np.max(x), np.min(x), len(x)), fit, 'r-')
	plt.grid(True)
	plt.savefig(name + 'Grades.pdf')
	plt.show()
#stats
mumt1 = mean(mt1)
mumt2 = mean(mt2)
mufin = mean(fin)
mulab = mean(lab)
muatt = mean(att)
memt1= median(mt1)
memt2= median(mt2)
mefin= median(fin)
melab= median(lab)
meatt= median(att)
sdmt1 = std(mt1,mumt1)
sdmt2 = std(mt2,mumt2)
sdfin = std(fin,mufin)
sdlab = std(lab,mulab)
sdatt = std(att,muatt)
skewmt1 = skew(mt1,mumt1,sdmt1)
skewmt2 = skew(mt2,mumt2,sdmt2)
skewfin = skew(fin,mufin,sdfin)
skewlab = skew(lab,mulab,sdlab)
skewatt = skew(att,muatt,sdatt)
bins = 20
#print
print('mt1(mean,median,std,skew):',mumt1,memt1,sdmt1,skewmt1)
print('mt2(mean,median,std,skew):',mumt2,memt2,sdmt2,skewmt2)
print('lab(mean,median,std,skew):',mulab,melab,sdlab,skewlab)
print('fin(mean,median,std,skew):',mufin,mefin,sdfin,skewfin)
print('att(mean,median,std,skew):',muatt,meatt,sdatt,skewatt)
#	PLOTS
plot(mt1,bins,'MT1 ')
plot(mt2,bins,'MT2 ')
plot(lab,bins,'Lab ')
plot(fin,bins,'Final ')
plot(att,bins,'Attendance ')
