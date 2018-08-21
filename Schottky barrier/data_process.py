from matplotlib import pyplot as plt
import pandas as pd
import os
import numpy as np
import statsmodels.api as sm
from scipy import constants


os.chdir(r"C:\Users\billy\OneDrive\Books\iPad 同步\近代物理实验\热激活法测肖特基势垒高度")
V_I=pd.read_csv(r"V-I.csv")

V_I=V_I.sort_values(by='I(μA)')

x_label_settings={'fontsize':'medium', 'horizontalalignment':'right'}
y_label_settings={'fontsize':'medium', 'verticalalignment':'top','rotation':"horizontal"}

if False:
    plt.plot(V_I['V(mV)'],V_I['I(μA)'],'x-')
    plt.xlabel("$V$/mV",**x_label_settings)
    plt.ylabel("$I/\mu\mathrm{A}$",**y_label_settings)
    plt.savefig(r"V-I")
    plt.show()

V_I2=pd.read_csv(r"all.csv")

if False:
    plt.plot(V_I2['V(mV)'],V_I2['I(μA)'],'x-')
    plt.xlabel("$V$/mV",**x_label_settings)
    plt.ylabel("$I/\mu\mathrm{A}$",**y_label_settings)
    plt.savefig(r"V-I2")
    plt.show()

I_T=pd.read_csv(r"I-T.csv")

V_I2_lm=sm.OLS(V_I2.loc[2:13]['dV/dI'].values,
               sm.add_constant(V_I2.loc[2:13]['1/I'].values))
V_I2_lm_result=V_I2_lm.fit()
print(V_I2_lm_result.summary())

'''
V_I2=V_I2.rename(columns={"dV/dI": "a", "1/I": "c"})
import statsmodels.formula.api as fsm
V_I2_lm_=fsm.ols(formula="a ~ c",data=V_I2.loc[2:13])
print(V_I2_lm_.fit().summary())
'''

if False:
    plt.plot(V_I2.loc[2:13]['1/I'], V_I2.loc[2:13]['dV/dI'],'rx')
    x_val=np.array(plt.gca().get_xlim())
    y_val=x_val*V_I2_lm_result.params[1]+V_I2_lm_result.params[0]
    plt.plot(x_val,y_val,'b-')
    plt.xlabel('$1/I$(A$^{-1}$)',**x_label_settings)
    plt.ylabel(r'$\frac{\mathrm{d}V}{\mathrm{d}I}$($\Omega$)',**y_label_settings)
    plt.savefig(r"lmfit1")
    plt.show()
    
I_T_lm=sm.OLS(I_T['log(I/T^2)'].values,sm.add_constant(I_T['1000/I'].values))
I_T_lm_result=I_T_lm.fit()
print(I_T_lm_result.summary())

if False:
    plt.plot(I_T['1000/I'],I_T['log(I/T^2)'],'rx')
    x_val=np.array(plt.gca().get_xlim())
    y_val=x_val*I_T_lm_result.params[1]+I_T_lm_result.params[0]
    plt.plot(x_val,y_val,'b-')
    plt.xlabel(r'$1000/T (\mathrm{K}^{-1})$',**x_label_settings)
    plt.ylabel(r'$\ln \frac{I}{T^2}$',**y_label_settings)
    plt.savefig(r"lmfit2")
    plt.show()


from scipy import optimize as opt

def V(I,n,R,A,qphi):
    '''全都是SI'''
    return (I*R + n*constants.k *300.4290/ constants.e *np.log(1+I/(2.83*1e-7*A*300.4290**2*np.exp(-qphi*constants.e/(constants.k*300.4290)))))

nonlinear=opt.curve_fit(V,V_I2['I(μA)'].values*1e-6,
                        V_I2['V(mV)'].values*1e-3,
                        p0=(1.317,-65,30*1e4,0.68))
#nonlinear=opt.curve_fit(V,V_I2['I(μA)'].values,V_I2['V(mV)'].values)
print(nonlinear)

if False:
    nonlin_x=np.linspace(V_I2['I(μA)'].values[0],V_I2['I(μA)'].values[-1])
    nonlin_y=V(nonlin_x*1e-6,nonlinear[0][0],nonlinear[0][1],nonlinear[0][2])*1e3
    plt.plot(V_I2['I(μA)'],V_I2['V(mV)'],'rx')
    plt.xlabel("$I/\mu\mathrm{A}$",**x_label_settings)
    plt.ylabel("$V$/mV",**y_label_settings)
    plt.plot(nonlin_x,nonlin_y,'b-')
    plt.legend(("data","non-linear curve fit"))
    plt.savefig(r"nonlinear")
    plt.show()