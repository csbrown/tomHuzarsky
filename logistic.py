import numpy as np
import math
import mpmath as mp
import pickle
import sys
import matplotlib.pyplot as plt


def linear(c,x):
  return c[0] + c[1]*x

# 1/(1+e^-(a+bx))
# a = c[0], b = c[1]
# 2 = 1+e^-(a+bx)
# ln(1) = -(a+bx)
# x = -a/b
def logit(c,x):
  return 1./(1+np.exp(-linear(c,x)))



if __name__=="__main__":

  #change this so that your function fits nicely on screen... start, stop, count
  b = 5
  a = -2.5*b
  c = [a,b]
  x = np.linspace(-10,10,1000)
  y = logit(c,x)
  plt.plot(x,y)



  #xx=np.random.uniform(-10,10,20)
  #xx=np.array(sorted(xx))
  #pickle.dump(xx, open("xx","wb"))
  #yy=np.random.randint(0,2,20)
  #yy=np.array(sorted(yy))
  #pickle.dump(yy, open("yy","wb"))  

  xx = pickle.load(open("xx","rb"))
  yy = pickle.load(open("yy","rb"))
  xx[0] = -1
  yy[0] = 1 


  plt.plot(xx,yy,'ro')
 
  plt.show()
