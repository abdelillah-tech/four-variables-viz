#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 22:53:05 2019

@author: 96abdou96
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib
import csv
import copy
import pandas as pd

data = []
#path = "/Users/macbookpro/Desktop/tmanyik/"
file_colors = "Countries-Continents.csv"
file_life = "life_expectancy_years.csv"
file_income = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
file_population = "population_total.csv"


countries0 = []
countries1 = []
countries2 = []
countries3 = []
years = []

x=[]
with open(file_income, 'r') as csvfile:
    line = 0
    reader = csv.reader(csvfile)
    for row in reader :
        if line == 0 :
            line = 1
            years = row[1:220]
            pass
        else :
            x.append([row[0],[np.nan if i=='' else float(i) for i in row[1:220]]])
            countries0.append(row[0])
xc = copy.deepcopy(x)

y=[]
with open(file_life, 'r') as csvfile:
    line = 0
    reader = csv.reader(csvfile)
    for row in reader :
        if line == 0 :
            line = 1
            pass
        else :
            y.append([row[0],[np.nan if i=='' else float(i) for i in row[1:]]])
            countries1.append(row[0])
yc = copy.deepcopy(y)

area=[]
with open(file_population, 'r') as csvfile:
    line = 0
    reader = csv.reader(csvfile)
    for row in reader :
        if line == 0 :
            line = 1
            pass
        else :
            area.append([row[0],[np.nan if i=='' else float(i) for i in row[1:220]]])
            countries2.append(row[0])
areac = copy.deepcopy(area)  

color = []
with open(file_colors, 'r') as csvfile:
    line = 0
    reader = csv.reader(csvfile)
    for row in reader :
        if line == 0 :
            line = 1
            pass
        else :
            color.append([row[1],row[0]])
            countries3.append(row[1])
    color = sorted(color, key=lambda kv: kv[0])
colorc = copy.deepcopy(color)

setter = [i[0] for i in color]
listof = []
for i in setter :
    if (i in countries0) and (i in countries1) and (i in countries2) and (i in countries3):
        listof.append(i)
    else :
        pass

for i in xc :
    if i[0] not in listof :
        x.remove(i)
   
for i in yc :
    if i[0] not in listof :
        y.remove(i)  

for i in areac :
    if i[0] not in listof :
        area.remove(i)  
        
for i in colorc :
    if i[0] not in listof :
        color.remove(i)
  

x = [i[1] for i in x]
x = np.array(x)
y = [i[1] for i in y]
y = pd.DataFrame(y)
y.fillna(y.mean(),inplace=True)
y = np.array(y)
area = [i[1] for i in area]
area = 10e-6 * np.array(area)
color = [i[1] for i in color]
color = np.array(color)

colors = []
for cont in color :
    if cont == 'Africa' :
        colors.append(0)
    if cont == 'Asia' :
        colors.append(1)
    if cont == 'Europe' :
        colors.append(2)
    if cont == 'South America' :
        colors.append(3)
    if cont == 'North America' :
        colors.append(4)
    if cont == 'Oceania' :
        colors.append(5)

mappa = ['brown','yellow','red','orange','green','blue']
label = ['Africa','Asia','Europe','South America','North America','Oceania']

colors = np.array(colors)
fig = plt.figure()
plt.xscale('log')
plt.xlim(300,120000)
plt.ylim(10,90)
plt.xlabel('log$_{10}$(income per person)')
plt.ylabel("life expectancy years")
plt.grid(True)

p = plt.legend(loc = 'upper left',scatterpoints=1, handles =(plt.plot()), frameon=False, labelspacing=1, title='population = 10$^{6}$ x Area')


kk = plt.scatter(x[:,0], y[:,0], s=area[:,0], c=colors, cmap=matplotlib.colors.ListedColormap(mappa),alpha=0.8)   
cb = plt.colorbar(kk)
loca = np.arange(0,max(colors),max(colors)/float(len(mappa)))
cb.set_ticks(loca)
cb.set_ticklabels(label)

def update(i):
    n =i%(2018-1800)
    x1 = x[:,n]
    y1 = y[:,n]
    z1 = area[:,n]
    k = np.array([x1,y1])
    k = np.transpose(k)
    kk.set_offsets(k)
    kk.set_sizes(z1)
    p = plt.legend(loc = 'upper left', scatterpoints=1, handles =(plt.plot()), frameon=False, labelspacing=1, title='population = 10$^{6}$ x Area\n'+8*" "+"year : "+years[n])  
    

anim = FuncAnimation(fig, update, interval=150)   
plt.show()






