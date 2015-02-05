import arbitraryfit as f
import numpy as np
import matplotlib.pyplot as plt

def linear(c,x):
  return c[0] + c[1]*x

# 1/(1+e^(a+bx))
def logit(c,x):
  return 1./(1+np.exp(-linear(c,x)))

def fitlogit(x,y):
  return f.arbitraryfit(x,y,"blue",logit,[1,1])

# x = income
# y = yes car ==1  no car ==0


if __name__=="__main__":
  x=np.random.uniform(0,100000,20)
  x=np.array(sorted(x))
  y=np.random.randint(0,2,20)
  y=np.array(sorted(y))
  params=fitlogit(x,y)
  print x
  print "--------------"
  print logit(params,x)
  plt.show()
