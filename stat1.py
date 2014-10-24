from Tkinter import *
from tkFileDialog import*
import xlrd
import re
import tkMessageBox
import matplotlib.pyplot as pl
import pylab 
from list import DynamicList
from dist import *

class app:
	def __init__(self,master):
		self.master=master
		self.start()
	def browse(self):
		self.filename = askopenfilename(title="open a file ...")
		self.filelocation.insert(0,self.filename)
	def start_processing(self):
		def mean(x):
        		sum = 0
        		for i in x:
               			sum=sum+i
        		mean=sum/len(x)
        		return mean

		def variance(x,u):
        		sum=0
        		for i in x:
                		sum=sum+(i-u)**2
        		var=sum/len(x)
        		return var


		
		self.pattern=re.compile(".*\.(xlsx|ods)")
		self.match = self.pattern.match(self.filename)
		if not self.match or self.filename is None:
        		tkMessageBox.showerror(title="Wrong Input",message="Invalid File Type")
		if False:
			print 'k'				
		else:
			self.wb=xlrd.open_workbook(self.filename)
			x=[]
			self.mean=[]
			self.var=[]
			self.std=[]
			m1=[]
			new=DynamicList()


			s=self.wb.sheet_by_index(0)
			for col in range(s.ncols):
				for row in range(s.nrows):
					x.append(s.cell(row,col).value)
				new.append(x)
				x=[]
			for col in range(s.ncols):
				self.mean.append(mean(new[col]))
				self.var.append(variance(new[col],self.mean[col]))
				self.std.append(variance(new[col],self.mean[col])**0.5)
			
			# for i in range(s.ncols):

			# 	m1.append("The values in column"+str(i)+" are "+str(new[i]))
			# 	m1.append('The mean of the values in col'+str(i+1)+' is '+str(self.mean[i]))
			# 	m1.append('The variance of the values in col'+str(i+1)+' is '+str(self.var[i]))
			# 	m1.append('The standard deviation of the values in col'+str(i+1)+' is '+str(self.std[i]))
        		
        		
			# m="\n".join(m1)	
			# tkMessageBox.showinfo(title="Output",message=m)
			top=Toplevel()
			t=Label(top,text=str(s.ncols)+" columns found").grid(row=0,column=3)
			x=1
			for i in range(s.ncols):

				m=Label(top,text="Mean "+str(i+1)+" :",height=4,fg="red").grid(row=x,column=0)
				meanl=Label(top,text=str(self.mean[i]),height=4,fg="blue").grid(row=x,column=1)


				v=Label(top,text="Variance "+str(i+1)+" :",height=4,fg="red").grid(row=x,column=2)
				variancel=Label(top,text=str(self.var[i]),height=4,fg="blue").grid(row=x,column=3)

				s=Label(top,text="Standard Deviation "+str(i+1)+" :",height=4,fg="red").grid(row=x,column=4)
				SDl=Label(top,text=str(self.std[i]),height=4,fg="blue").grid(row=x,column=5)
				
				x=x+1

	def plot_graph(self):
		self.pattern=re.compile(".*\.(xlsx|ods)")
		self.match = self.pattern.match(self.filename)
		if not self.match or self.filename is None:
        		tkMessageBox.showerror(title="Wrong Input",message="Invalid File Type")
			exit()

		self.wb=xlrd.open_workbook(self.filename)
		s=self.wb.sheet_by_index(0)
		top = Toplevel()
		self.varx=IntVar()
		self.vary=IntVar()
		top.title("Configuration")

		w=Label(top,text=str(s.ncols)+" columns found")
		w.pack()
		x=Label(top,text="Assign column to the x-axis")
		x.pack()
		for i in range(s.ncols):
			c=Radiobutton(top, text="Column "+str(i+1),variable=self.varx, value=i)
        		c.pack(anchor=W)
        	y=Label(top,text="Assign column to the y-axis")
        	y.pack()
        	for i in range(s.ncols):
        		d=Radiobutton(top,text="Column "+str(i+1),variable=self.vary,value=i)
        		d.pack(anchor=W)
		self.plott=Button(top,text="Plot Graph",command=self.sweg).pack()	
	def sweg(self):
		x=self.varx.get()
		y=self.vary.get()
        	new=DynamicList()
        	a=[]
        	wb=xlrd.open_workbook(self.filename)
        	s=wb.sheet_by_index(0)
        	for i in range(s.nrows):
                	a.append(s.cell(i,x).value)
        	new.append(a)
       		a=[]
        	for i in range(s.nrows):
               		a.append(s.cell(i,y).value)
        	new.append(a)
        	a=[]
        	pl.plot(new[0],new[1])

        	pl.title('X-Y graph')
        	pl.xlabel('Column '+str(x+1))
        	pl.ylabel('Column '+str(y+1))
        	pl.show()
	def histogram(self):
		self.pattern=re.compile(".*\.(xlsx|ods)")
                self.match = self.pattern.match(self.filename)
                if not self.match or self.filename is None:
                        tkMessageBox.showerror(title="Wrong Input",message="Invalid File Type")
                        exit()

                self.wb=xlrd.open_workbook(self.filename)
                s=self.wb.sheet_by_index(0)
                top = Toplevel()
		self.ok=IntVar()
		w=Label(top,text=str(s.ncols)+" columns found")
                w.pack()
                x=Label(top,text="Select a column")
                x.pack()
                for i in range(s.ncols):
                        c=Radiobutton(top, text="Column "+str(i+1),variable=self.ok, value=i)
                        c.pack(anchor=W)
		plot=Button(top,text="Plot",command=self.histo).pack()

	def histo(self):
		x=[]
		y=self.ok.get()
		self.wb=xlrd.open_workbook(self.filename)
		s=self.wb.sheet_by_index(0)
		for i in range(s.nrows):
			x.append(s.cell(i,y).value)
		pl.hist(x)
		pl.show()


	def start(self):
		self.master.title("StatLab 1.0")
		self.filelocation = Entry(self.master)
		self.filelocation["width"] = 30
		self.filelocation.focus_set()
		self.filelocation.pack(side="left")
		# self.filelocation.grid(row=1,column=0)
		self.open_file=Button(self.master,text="Browse..",command=self.browse).pack(side="left")
		# self.open_file.grid(row=1,column=1)
		self.submit = Button(self.master,text="Calculate",command=self.start_processing).pack(fill=X)
		
		self.plott = Button(self.master,text="Plot Config",command=self.plot_graph).pack(fill=X)
		
		self.hist=Button(self.master,text="Histogram",command=self.histogram).pack(fill=X)
		
		self.dist=Button(self.master,text="Distributions",command=self.distribution).pack(fill=X)
		
	def distribution(self):
		top=Toplevel()
		w=Label(top,text="Generate a curve based on the following distributions")
		w.pack()
		binomial=Button(top,text="Binomial",command=self.binomial).pack(fill=X)
		poisson=Button(top,text="Poisson",command=self.poisson).pack(fill=X)
		normal=Button(top,text="Normal",command=self.normal).pack(fill=X)
		lognormal=Button(top,text="Log-Normal",command=self.lognormal).pack(fill=X)
	
	def binomial(self):
		x=Binomial()
		x.graph()
	def poisson(self):
		x=Poisson()
		x.graph()
	def normal(self):
		x=Normal()
		x.graph()
	def lognormal(self):
		x=LogNormal()
		x.graph()
		
root = Tk()
App = app(root)
root.mainloop()


