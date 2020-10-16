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
mt1 = df['mt1'].values.tolist()
mt2 = df['mt2   '].values.tolist()
fin = df['fin'].values.tolist()
lab = df['hw'].values.tolist()
att = df['Att.'].values.tolist()
#stats
mumt1 = np.mean(mt1)
mumt2 = np.mean(mt2)
mufin = np.mean(fin)
mulab = np.mean(lab)
muatt = np.mean(att)
sdmt1 = np.std(mt1)
sdmt2 = np.std(mt2)
sdfin = np.std(fin)
sdlab = np.std(lab)
sdatt = np.std(att)
bins = 20

#	PLOTS
#mt1
n, bins, patches = plt.hist(mt1, bins, facecolor='blue', alpha=0.5, normed=True)
plt.title('MT1 Grades')
plt.xlabel('Grades')
plt.ylabel('Number')
fit = stats.norm.pdf(np.linspace(np.max(mt1), np.min(mt1), 100), mumt1, sdmt1)
plt.plot(np.linspace(np.max(mt1), np.min(mt1), 100), fit, 'r-')
plt.grid(True)
plt.savefig('Mt1_Grades.pdf')
plt.show()
#mt2
n, bins, patches = plt.hist(mt2, bins, facecolor='blue', alpha=0.5, normed=True)
plt.title('MT2 Grades')
plt.xlabel('Grades')
plt.ylabel('Number')
fit = stats.norm.pdf(np.linspace(np.max(mt2), np.min(mt2), 100), mumt2, sdmt2)
plt.plot(np.linspace(np.max(mt2), np.min(mt2), 100), fit, 'r-')
plt.grid(True)
plt.savefig('Mt2_Grades.pdf')
plt.show()
#fin
n, bins, patches = plt.hist(fin, bins, facecolor='blue', alpha=0.5, normed=True)
plt.title('Final Grades')
plt.xlabel('Grades')
plt.ylabel('Number')
fit = stats.norm.pdf(np.linspace(np.max(mt2), np.min(mt2), 100), mufin, sdfin)
plt.plot(np.linspace(np.max(fin), np.min(fin), 100), fit, 'r-')
plt.grid(True)
plt.savefig('Final_Grades.pdf')
plt.show()
#lab
n, bins, patches = plt.hist(lab, bins, facecolor='blue', alpha=0.5, normed=True)
plt.title('Lab Grades')
plt.xlabel('Grades')
plt.ylabel('Number')
fit = stats.norm.pdf(np.linspace(np.max(lab), np.min(lab), 100), mulab, sdlab)
plt.plot(np.linspace(np.max(lab), np.min(lab), 100), fit, 'r-')
plt.grid(True)
plt.savefig('Lab_Grades.pdf')
plt.show()
#att
n, bins, patches = plt.hist(att, bins, facecolor='blue', alpha=0.5, normed=True)
plt.title('Att Grades')
plt.xlabel('Grades')
plt.ylabel('Number')
fit = stats.norm.pdf(np.linspace(np.max(lab), np.min(lab), 100), muatt, sdatt)
plt.plot(np.linspace(np.max(att), np.min(att), 100), fit, 'r-')
plt.grid(True)
plt.savefig('Att_Grades.pdf')
plt.show()