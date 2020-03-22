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
