#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Funtion to check input
def Chek(a):
    c=list(a)
    D=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    f=0
    for i in c:
        if i not in D:
            f+=1
    if f>0:
        print('Not a valid HEXADECIMAL')
    if f==0:
        return(True)


# In[3]:


#Function for converting str HEX no.
#import timeit
def HEXA(a):
    li=[]
    if a==0:
        li=['0']
    while a>0:
        q=a//16

        r=a%16
        if r<=9:
            r=str(r)
        if r==10:
            r='A'
        if r==11:
            r='B'
        if r==12:
            r='C'
        if r==13:
            r='D'
        if r==14:
            r='E'
        if r==15:
            r='F'
    
        li.append(r)
        a=q
    li.reverse()
    return "".join (li)
a=123

#print(timeit.timeit('HEXA(a)','from __main__ import HEXA, a'))


# In[4]:


#Function for HEX multiplication -List based multiplication
def Mult(a,b):
    if (int(a,16))==0 or (int(b,16)==0):
        return('0')
    
    m=(len(a)*len(b))+1
    result=[0]*(m)
    x=0
    y=0
    for i in range (len(a)-1,-1,-1):
        carry=0
        n1=int(a[i],16)
        y=0
        for j in range(len(b)-1,-1,-1):
            n2=int(b[j],16)
            summ=n1*n2+result[x+y]+carry
            carry=summ // 16
            result[x+y]= summ % 16
            y+=1
        if (carry>0):
            result[x+y] +=carry
        x +=1
    
    i=len(result)-1
    while (i>=0 and result[i]==0):
        i-=1
    if i==-1:
        return('0')

    s=''   
    while (i >=0):
        s+=HEXA((result[i]))
        i -=1
    return (s)


# In[5]:


#Function for HEX addition
def ADDHEX(a,b):
    if (int(a,16))==0 and (int(b,16)==0):
        return('0')
    m=max(len(a),len(b))+1
    result=[0]*m
    y=0
    a1=''
    b1=''
    for i in range(m-len(a)):
        a1+='0'
    
    for i in range (m-len(b)):
        b1+='0'
    a2=a1+a
    b2=b1+b
    carry=0
    for i in range (m-1,-1,-1):
        n1=int(a2[i],16)
        n2=int(b2[i],16)
        summ=n1+n2+carry
        carry=summ//16
        result[y]=summ%16
        y+=1
        

    i=len(result)-1
    while i>=0 and result[i]==0:
        i-=1
    s=''
    while i>=0:
        s+=HEXA(result[i])
        i-=1
        
    return(s)


# In[6]:


#Function for HEX subtraction
def findDiff(a, b): 
    
    if int(a,16)==0 and int(b,16)==0:
        return('0')
    m=max(len(a),len(b))
    result=[0]*m
    n1 = len(a)  
    n2 = len(b) 
    a=a[::-1] 
    b = b[::-1] 
  
    carry = 0
    y=0
    x=0
    for i in range(n2):
        sub = ((int(a[i],16))-(int(b[i],16))-carry) 
          
        if (sub < 0): 
          
            sub = sub + 16
            carry = 1
              
        else: 
            carry = 0
  
        result[y] =  (sub)
        y+=1
       
    for i in range(n2,n1): 
      
        sub = ((int(a[i],16)) - carry) 
           
        if (sub < 0): 
          
            sub = sub + 16
            carry = 1
          
        else: 
            carry = 0
        result[x+y]=sub
        x+=1

        
    i=len(result)-1
    while (i>=0 and result[i]==0):
        i-=1
    if i==-1:
        return('0')

    s=''   
    while (i >=0):
        s+=HEXA((result[i]))
        i -=1
        
    return (s)


# In[7]:


#Function for Karatsuba algorithm
def karatsuba(x, y):
    if len(x) < 2 or len(y) < 2:
        PRO=Mult(x,y)
        return (PRO)

    m2 = max(len(x), len(y)) // 2

    ix, iy = len(x) - m2, len(y) - m2
    a, b = (x[:ix]), (x[ix:])
    c, d = (y[:iy]), (y[iy:])
    if a=='':
        a='0'
    if b=='':
        b='0'
    if c=='':
        c='0'
    if d=='':
        d='0'
    
    z1=ADDHEX(a,b)
    z2=ADDHEX(c,d)
    A = karatsuba(a, c)
    C = karatsuba(b, d)
    D = karatsuba(z1, z2)
   
    
    RES4=ADDHEX(A,C)
    B=findDiff(D,RES4)
    A1=['0']*(2*m2)
    B1=['0']*(m2)
    A2=''. join(A1)
    B2=''. join(B1)
    A+=A2
    B+=B2    
    PROD1=ADDHEX(A,B)
    PROD=ADDHEX(PROD1,C)
   
    return (PROD)


# In[11]:


#import timeit
def Calcuator(a,b):
    if Chek(a):
        if Chek(b):
            a1=''
            b1=''
            m=max(len(a),len(b))//2
            if len(b)<m:
                for i in range(len(a)-len(b)):
                    b1+='0'
            if (len(a)<m):
                for i in range(len(b)-len(a)):
                    a1+='0'
            a=a1+a        
        
            b=b1+b
        
            F=karatsuba(a,b)
            print(F)
            with open('file.txt', 'w') as f:
                print('ANS',F,file=f)

import random
D=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
a=''
b=''
for k in range(10):
    i=random.randint(0,15)
    j=random.randint(0,15)
    a+=D[i]
    b+=D[j]
Calcuator(a,b)
#with open ('time.txt','w') as P:
    #print('TIME',(timeit.repeat('Calcuator(a,b)','from __main__ import Calcuator , a, b',repeat=2,number=1)),P)


# In[12]:


#Check with inbuilt function
C=int(a,16)*int(b,16)
D=HEXA(C)
print(D)


# In[ ]:




