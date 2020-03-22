#代码用途：
#不同类型的插值多相式的生成
#以及其对应图像的对比
#made by 15746——mcy
import numpy as np  
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False
x1=np.linspace(-1,1,6)
x2=np.linspace(-1,1,11)
x3=np.linspace(-1,1,16)
y1=1/(1+36*x1**2)
y2=1/(1+36*x2**2)
y3=1/(1+36*x3**2)
def p(n,m):
    q1=1
    k=0
    k1=[]
    for i in range(len(n)):
        for j in range(len(n)):
            if j!=i:
                q1=q1*(n[i]-n[j])
                k1=k1+[n[j]]
        e1=m[i]/q1
        p1=np.poly1d(k1,r=True)*e1
        k1=[]
        q1=1
        k=k+p1
    return k
x=np.linspace(-1,1,50)
y=1/(1+36*x**2)
p1=p(x1,y1)
p2=p(x2,y2)
p3=p(x3,y3)
m=[p1,p2,p3]
