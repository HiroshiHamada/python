# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 11:42:10 2017

@author: z270
"""

##############################
# 3D plot 基本的な流れ

#    numpy, pyplot, mpl_toolkit.mplot3dをimportしておく。
#    np.arangeでx,yそれぞれの描画範囲を指定。
#    np.meshgridで2次元メッシュを作成
#    func(X,Y)よりZの値を算出
#    X, Y, Zの値を用いて描画

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# plot用　　関数定義
def func(x,y):
    return x**2+y**2

x = np.arange(-5,5,0.25)
y = np.arange(-5,5,0.25)

X, Y = np.meshgrid(x,y)

Z = func(X,Y)

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_wireframe(X,Y,Z)
plt.show()



####  メッシュに色づけする方法  #############

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm



x = np.arange(-5,5,0.05)
y = np.arange(-5,5,0.05)

X, Y = np.meshgrid(x,y)

Z = func(X,Y)

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X,Y,Z,cmap=cm.coolwarm)
plt.show()


