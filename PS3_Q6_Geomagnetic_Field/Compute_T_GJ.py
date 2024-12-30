import numpy as np
import matplotlib.pyplot as plt

hbk=np.loadtxt(r"D:\CP\Practice\Year3-Computational-Physics-Practice\PS3_Q6_Geomagnetic_Field\HBK.csv",skiprows=1,unpack=True,delimiter=',',usecols=(1,2))
her=np.loadtxt(r"D:\CP\Practice\Year3-Computational-Physics-Practice\PS3_Q6_Geomagnetic_Field\HER.csv",skiprows=1,unpack=True,delimiter=',',usecols=(1,2))
kmh=np.loadtxt(r"D:\CP\Practice\Year3-Computational-Physics-Practice\PS3_Q6_Geomagnetic_Field\KMH.csv",skiprows=1,unpack=True,delimiter=',',usecols=(1,2))
tsu=np.loadtxt(r"D:\CP\Practice\Year3-Computational-Physics-Practice\PS3_Q6_Geomagnetic_Field\TSU.csv",skiprows=1,unpack=True,delimiter=',',usecols=(1,2))

x=1e3*np.array([0,950,1700])
y=1e3*np.array([150,1000,0])
x_dash=1e3*900
y_dash=1e3*40
mu0 = np.pi*4e2                 # permeability of free space (nTm/A)
h = 1000*1e3                   # height of equivalent current system (m)
const = (mu0/(2.0*np.pi*h))


T_dash=np.zeros((2,6))
for i in range(0,2):
    for j in range(0,6):
        if j<3 and i==0:
          T_dash[i][j]=1/(1+((x_dash-x[j])/h)**2)
        if j>=3 and i==1:
            T_dash[i][j]=-1/(1+((y_dash-y[j-3])/h)**2)

print(T_dash)
      
T=np.zeros((6,6))
for i in range(0,6):
    for j in range(0,6):
        if i<3 and j<3:#first half of matrix:x components
            T[i][j]=1/(1+((x[i]-x[j])/h)**2)
        if i>=3 and j>=3:#second half of matrix:y components
            T[i][j]=-1/(1+((y[i-3]-y[j-3])/h)**2)


def gauss_jor(T):
    N=len(T[0])
    I=np.eye(N)
    TI=np.hstack([T,I])
    for j in range(0,N):
        pivot_row=np.argmax([np.abs(TI[i][j]) for i in range(j,N)])+j #return i (where max element lies)
        TI[[j,pivot_row]]=TI[[pivot_row,j]]#switch row
        TI[j,:]/=TI[j,j]#normalization
        for i in range (0,N):
            if i!=j:
              TI[i,:]-=TI[i,j]*TI[j,:] #rest of the element should be 0
    return TI[:,N:]

inverse_T=gauss_jor(T)
her_x=her[0]
her_y=her[1]
hbk_x=hbk[0]
hbk_y=hbk[1]
tsu_x=tsu[0]
tsu_y=tsu[1]
kmh_x=kmh[0]
kmh_y=kmh[1]
Current_I=[]#vector at each timesteps
for i in range(0,len(her_x)):#times
    B=np.array([her_x[i],hbk_x[i],tsu_x[i],her_y[i],hbk_y[i],tsu_y[i]])
    I=np.dot(inverse_T,B)#A vector
    Current_I.append(I)

B_kmh_x=[]
B_kmh_y=[]
for current_vecs in Current_I:
    B=np.dot(T_dash,current_vecs)
    B_kmh_x.append(B[0])
    B_kmh_y.append(B[1])
times=np.linspace(0,100,len(B_kmh_x))
plt.plot(times,B_kmh_y,label='calculated')
plt.plot(times,kmh_y,label='observed')
plt.ylabel('By(nT)')
plt.xlabel('Pseudo times')
plt.grid()
plt.legend()
plt.show()




        


        



            
                 
