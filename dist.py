from math import *
import random
import matplotlib.pyplot as pl
from scipy.special import iv
import numpy as np
#-------------------------------------------------------------------------------------------#
class Binomial(): 
	
	def __init__(self):
		n=self.trial=random.randrange(10,50) #randomly generate the number of trials
		p=self.probability=random.uniform(0.3,0.7) #randomly generate the probability of success
		self.x=[] #define a list for plotting
		self.y=[] #define a list for plotting
		for i in range(n+1):
			r=i
			self.x.append(r)
			c=(factorial(n))/(factorial(n-r)*factorial(r)) #ncr
			q=1-p
			s=n-r
			P=c*(p**r)*(q**s)
			self.y.append(P)
		
	def graph(self):
		pl.plot(self.x,self.y)
		pl.show()
	def rand(self):
		return self.y
	def NumberOfTrials(self):
		return self.trial
	def ProbabilityOfSuccess(self):
		return self.probability
#-----------------------------------------------------------------------------------------#
class Poisson():

	def __init__(self):
		u=self.mean=random.uniform(0,50.0)
		self.x=[]
		self.y=[]
		for i in range(50):
			self.x.append(i)
			f=((u**i)*exp(-u))/factorial(i);
			self.y.append(f)

	def graph(self):
		pl.plot(self.x,self.y)
		pl.show()
	def rand(self):
		return self.y
	def getMean(self):
		return self.mean		
#-----------------------------------------------------------------------------------------#
class Normal():

	def __init__(self):
		u=self.mean=random.uniform(30,100.0)
		self.x=[]
		self.y=[]
		s=self.standardDeviation=random.uniform(1,30)
		for i in range(-100,200):
			self.x.append(i)
			f=(1/(s*sqrt(2*pi)))*exp(-((i-u)**2)/(2*(s**2)))
			self.y.append(f)
	def graph(self):
		pl.plot(self.x,self.y)
		pl.show()
	def rand(self):
		return self.y
	def getMean(self):
		return self.mean
	def getSD(self):
		return self.standardDeviation
#-----------------------------------------------------------------------------------------------------------------------------------------------
class LogNormal():

	def __init__(self):
		m=self.mean=random.uniform(50,100)
		v=self.standardDeviation=random.uniform(1,30)
		u=log((m**2)/(sqrt(v+(m**2))))
		s=sqrt(log(1+(v/m**2)))		
		self.x=[]
		self.y=[]
		for i in range(1,200):
			self.x.append(i)
			f=(1/(i*s*sqrt(2*pi)))*exp(-((log(i)-u)**2)/(2*(s**2)))
			self.y.append(f)
	def graph(self):
		pl.plot(self.x,self.y)
		pl.show()
	def rand(self):
		return self.y
	def getMean(self):
		return self.mean
	def getSD(self):
		return self.standardDeviation

#---------------------------------------------------------------------------------------------------------------------------------------------
class Rayleigh():
	def __init__(self):
		self.s=random.uniform(0,30.0);
		self.x=[]
		self.y=[]
		for i in range(1,200):
			self.x.append(i)
			f=i*exp(-(i**2)/(2*(self.s**2)))/(self.s**2)
			self.y.append(f)
	def graph(self):
		pl.plot(self.x,self.y)
		pl.show()
	def rand(self):
		return self.y
	def getSD(self):
		return self.s
class Gamma():
	def __init__(self):
		self.k=random.randrange(1,10)
		self.t= random.uniform(0.5,5)
		self.x=[]
		self.y=[]
		for i in range(0,21):
			self.x.append(i)
			f=((i**(self.k-1))*exp(-i/self.t))/((self.k**self.t)*gamma(self.k))
			self.y.append(f)
	def graph(self):
		pl.plot(self.x,self.y)
		pl.show()
	def rand(self):
		return self.y
	def getK(self):
		return self.k
	def getTheta(self):
		return self.t
class Rice():
	def __init__(self):
		self.v=random.uniform(0.2,5)
		self.s=1
		self.x=[]
		self.y=[]
		for i in np.arange(0,10,0.01):
			self.x.append(i)
			f=i*exp(-((i**2)+(self.v**2))/(2*self.s**2))*iv(0,(i*self.v)/(self.s**2))/(self.s**2)
			self.y.append(f)
	def graph(self):
		pl.plot(self.x,self.y)
		pl.show()
	def rand(self):
		return self.y
class Chi_Squared():
	def __init__(self):
		self.k=random.randrange(1,10)
		self.x=[]
		self.y=[]
		for i in np.arange(0,20,0.01):
			self.x.append(i)
			t1=i**((self.k/2)-1)
			t2=exp(-i/2)
			t3=2**(self.k/2)
			t4=gamma(float(self.k)/2)

			f=(t1*t2)/(t3*t4)
			self.y.append(f)
	def graph(self):
		pl.plot(self.x,self.y)
		pl.show()
	def rand(self):
		return self.y
	def getK(self):
		return self.k
class Beta():
	def __init__(self):
		self.a=random.uniform(0.1,4)
		self.b=random.uniform(0.1,4)
		self.x=[]
		self.y=[]
		for i in np.arange(0,1,0.01):
			self.x.append(i)
			t1=gamma(self.a+self.b)
			t2=gamma(self.a)*gamma(self.b)
			t3=i**(self.a-1)
			t4=(1-i)**(self.b-1)
			f=(t1/t2)*t3*t4
			self.y.append(f)
	def graph(self):
		pl.plot(self.x,self.y)
		pl.show()
	def getAlpha(self):
		return self.a
	def getBeta(self):
		return self.b			
