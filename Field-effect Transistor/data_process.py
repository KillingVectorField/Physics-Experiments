from matplotlib import pyplot as plt
import os
import numpy as np

os.chdir(r"C:\Users\billy\OneDrive\Books\iPad 同步\近代物理实验\体效应管")

V=np.array([13.00,12.50,12.00,11.50,11.00,10.50,10.00,9.50,9.00,8.50,8.00,7.50,
            7.00,6.50,6.00,5.50,5.00,4.50,4.00,3.80,3.50,3.40,3.20,
            3.00,2.70,2.50,2.30,2.10,1.80,1.50,1.20,0.90,0.60,0.30,0])

I=np.array([352,308,306,306,306,306,306,306,307,308,309,311,
            312,312,314,325,325,325,325,329,360,359,355,
            350,336,323,308,289,258,224,186,145,99,52,0])

P=np.array([95.5,87.4,80.2,74.9,63.2,52.4,39.0,28.0,18.5,11.5,6.2,2.0])

f=np.array([8995,8994,8992,8989,8985,8980,8973,8963,8953,8943,8934,8917])/1000

y_label_settings={'fontsize':'medium', 'verticalalignment':'top','rotation':"horizontal"}

fig = plt.figure()
host = fig.add_subplot(111)

par1 = host.twinx()
par2 = host.twinx()

#host.set_xlim(0, 2)
par2.set_ylim(8.9,9.05)

host.set_xlabel(r"$V$/V")
host.set_ylabel(r"$I$/mA",**y_label_settings)
par1.set_ylabel(r"$P$%",**y_label_settings)
par2.set_ylabel(r"$f$/GHz",**y_label_settings)

color1 = plt.cm.viridis(0)
color2 = plt.cm.viridis(0.5)
color3 = plt.cm.viridis(.9)

p1, = host.plot(V,I,'x-', color=color1,label="$I$")
p2, = par1.plot(V[0:len(P)],P,'x-', color=color2, label="$P$")
p3, = par2.plot(V[0:len(f)],f,'x-', color=color3, label="$f$")

lns = [p1, p2, p3]
host.legend(handles=lns, loc='best')

# right, left, top, bottom
par2.spines['right'].set_position(('outward', 60))      
# no x-ticks                 
par2.xaxis.set_ticks([])
# Sometimes handy, same for xaxis
#par2.yaxis.set_ticks_position('right')

plt.savefig("feature_curve", bbox_inches='tight')

l=np.array([0,3.9,6.1,8.5,12.9,17.1,18.7,20.1,24.8])
I_l=np.array([2,30,58.5,93,119,83,58.5,37.0,2.2])

plt.plot(l,I_l,'x-')
plt.xlabel(r"$l$/mm")
plt.ylabel(r"$I$/mA")
plt.savefig("I_l")
plt.show()

E=np.abs(np.sin(2*np.pi*l/48.9))

plt.plot(E[E.argsort()],I_l[E.argsort()],'x-')
plt.xlabel(r"$E\propto\sin(2\pi l/\lambda_g)$")
plt.ylabel(r"$I$/mA")
plt.savefig("I_E")
plt.show()