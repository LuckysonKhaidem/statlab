from math import *
import random
import matplotlib.pyplot as pl
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






