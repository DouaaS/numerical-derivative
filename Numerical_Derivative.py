#!/usr/bin/env python
# coding: utf-8

# In[64]:


import numpy as np
def numerical_derivative(x,f):
    df=np.zeros(len(f))
    ddf=np.zeros(len(f))
    dx=x[1]-x[0]
    dx_squared=dx**2

    for i in range (len(f)):

        if i==0:
            df[i]=(f[i+1]-f[i])/dx
        if i==len(f)-1:
            df[i]=(f[i]-f[i-1])/dx
        if i!=0 and i!= len(f)-1:
            df[i]=(f[i+1]-f[i-1])/(2*dx)
            
    for i in range (len(f)):

        if i==0:
            ddf[i]=(f[i+2]-(2*f[i+1])+f[i])/(dx_squared)

            
        if i==len(f)-1:
            ddf[i]=(-2*f[i-1] +f[i] +f[i-2])/(dx_squared)
            
            
        if i!=0 and i!= len(f)-1:
            
            ddf[i]=(f[i-1] -2*f[i] +f[i+1])/(dx_squared)
            
    return df, ddf

    
def main():
    f1=[25,443,8238,163074,3269642]
    x1=[1,2,3,4,5]
    f2=[1.2,1.1035156,0.925,0.6363281,0.2]
    x2=[0,0.25,0.5,0.75,1]
    print(numerical_derivative(x1,f1))
    print(numerical_derivative(x2,f2))
main()


# In[ ]:





# In[ ]:




