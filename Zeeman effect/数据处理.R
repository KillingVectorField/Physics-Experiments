T_0=read.csv("塞曼实验效应结果_effective_0T.csv",col.names = c('气压（mV)','光强（nA)'))
T1_full=read.csv("1T_full.csv",col.names = c('气压（mV)','光强（nA)'))
T2_full=read.csv('T2_full.csv',col.names = c('气压（mV)','光强（nA)'))
T1_pi=read.csv('T1_pi.csv',col.names = c('气压（mV)','光强（nA)'))
T1_sigma=read.csv('T1_sigma.csv',col.names = c('气压（mV)','光强（nA)'))
plot(T_0,type='l',col=4,ylim=c(0,2500))
grid()
#第二张9谱线图，1T
plot(T1_full,type='l',col='blue',xlim=c(0,2000),ylim=c(0,1500))#第一张无磁场图
grid()
T1_full_peaks=T1_full[c(203,281,358,432,513,590,671,743,829,1032,
          1110,1186,1260,1340,1417,1497,1570,1655),]
T1_full_adjusted<-T1_full_peaks[10:18,2]-54
T1_full_adjusted<- T1_full_adjusted/(2*T1_full_adjusted[1])
points(T1_full_peaks,col='red',pch='x')
abline(h=54,col='grey')
legend('top',col=c('red','grey'),lty=c(NA,1),pch=c('x',NA),legend=c('谱线峰值', '背景噪声'))
#第三张：9谱线图，0.8T
plot(T2_full,type='l',col='red',xlim=c(0,2000),ylim=c(0,1500))
lines(T1_full,lty=2,col='blue')
legend('top',col=c('red','blue'),lty=c(1,2),legend=c('B=0.8T', 'B=1T'))
grid()
#第四章，pi线和sigma线
T1_total=T1_pi[7:2594,2]+T1_sigma[1:2588,2]
T1_total=data.frame(c(99:2686),T1_total)
plot(T1_pi,type='l',col='red',xlim=c(0,2000),ylim=c(0,1500))
lines(T1_sigma,lty=1,col='blue')
lines(T1_total,lty=3,col='black')
sigma=expression(sigma)
pi=expression(pi)
legend('top',col=c('red','blue','black'),lty=c(1,1,3),legend=c(pi,sigma,'total' ))
grid()

plot(T1_total,type='l')

plot(c(0.5,1.5,3,3,4,3,3,1.5,0.5),type='b',col='red',xlab='谱线序号',ylab='相对强度')
lines(T1_full_adjusted,type='b',col='blue')
legend('topright',col=c('red','blue'),lty=c(1,1),legend=c('理论值', '实测值'))

x<-seq(from=-2,to=2,length.out = 9)
y<-c(-0.934,-0.698,-0.468,-0.242,0,0.232,0.478,0.695,0.955)
L=lm(y~x)
delta=expression(Delta)
yyy=expression(Delta*nu*(cm**(-1)))
plot(x,y,xlab=delta,ylab=yyy,col='red',pch='x')
abline(L,col='blue')

