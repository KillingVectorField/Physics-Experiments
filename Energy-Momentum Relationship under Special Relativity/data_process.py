from matplotlib import pyplot as plt
import pandas as pd
import os
import numpy as np
from scipy import constants

os.chdir(r"C:\Users\billy\OneDrive\Books\iPad 同步\近代物理实验\相对论能量动量关系\1400012141")
Co60=pd.read_csv(r"60Co_594V_数据文件.txt", sep=" ",header= None,engine="python")
#Co60=pd.read_fwf(r"60Co_594V_数据文件.txt",header= None,engine="python")
Co60=Co60.iloc[:,1:3]
Co60.columns = ["n","counts"]

Cs137=pd.read_csv(r"137Cs_594V_数据文件.txt", sep=" ",header= None,engine="python")
Cs137=Cs137.iloc[:,1:3]
Cs137.columns = ["n","counts"]


y_label_settings={'fontsize':'medium', 'verticalalignment':'top','rotation':"horizontal"}
plt.plot(Co60['n'],Co60['counts'],".")
plt.plot(Cs137['n'],Cs137['counts'],".")
#x_val=np.array(plt.gca().get_xlim())
#y_val=x_val*slope+intercept
#plt.plot(x_val,y_val,'r--')
plt.xlabel("$n$")
plt.ylabel("Counts",**y_label_settings)
plt.text(28, 776, "0.184 MeV")
plt.text(145,647, "0.662 MeV")
plt.text(267, 182, "1.173 MeV")
plt.text(304,119, "1.333 MeV")
plt.legend(['$^{60}$Co','$^{137}$Cs'])
plt.savefig("Co60_Cs137")
plt.show()

x=np.linspace(0,2.25,num=100)
y_classic=x**2/1.022
y_relativity=np.sqrt(x**2+0.511**2)-0.511
plt.xlabel("$pc$/MeV")
plt.ylabel("$E_k$/MeV",**y_label_settings)
plt.ylim([0,2.5])
plt.plot(x,y_classic,"-")
plt.plot(x,y_relativity,"-")
plt.plot([2.201,1.922,1.715,1.469,1.218,0.992],[1.747,1.475,1.239,1.018,0.782,0.550],"x")
plt.legend(['non-relativity','relativity',"observed data"])
plt.savefig("relationship")
plt.show()

