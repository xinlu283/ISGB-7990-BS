#!/usr/bin/env python
# coding: utf-8
import math
import numpy as np
import pandas as pd

# # S=current price
# # K=strike price
# # sigma = volatility
# # t = time to maturity
# # r = risk free interest rate
# # d = dividend yield per year

#we impoet the data from the csv doc "data.csv"
#the first line in data is current price

data1 = pd.read_csv('data.csv',header = None)
data2 = list(data1.split(' '))
index =['s','k','sigma','t','r','d']
data = dict(zip(index,data2))

def td1(s,k,r,d,sigma,t):
    return (math.log(s/k)+(r-d+(sigma^2)/2)*t)/sigma/math.sqrt(t)

def td2(d1,sigma,t):
    return d1-sigma*math.sqrt(t)

def N(x):
    return 0.5*(1+math.erf(x/math.sqrt(2)))

d1=td1(data['s'],data['k'],data['r'],data['d'],data['sigma'],data['t'])
d2=td2(d1,data['sigma'],data['t'])

C = lambda s,d,t,nd1,k,r,nd2:s*math.exp(-d*t)*nd1-k*math.exp(-r*t)*nd2
print (C(data['s'],data['d'],data['t'],N(d1),data['k'],data['r'],N(d2)))

P = lambda s,d,t,nd1,k,r,nd2:k*math.exp(-r*t)*(-nd2)-s*math.exp(-d*t)*(-nd1)
print (P(data['s'],data['d'],data['t'],N(d1),data['k'],data['r'],N(d2)))

