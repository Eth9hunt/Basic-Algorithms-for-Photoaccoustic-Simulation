import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
import time
def Cartcircle():
    global xc,yc
    xc = []
    yc = []
    num_sens=70         # number of sensors
    radi=15            # radius of circle
    Cenx,Ceny=(0,0)   # Centor position
    sensor_angle = 3*math.pi/2 # sensor angle
    space= np.linspace(1,2,num_sens)
    for i in range(0,num_sens):
        angle = space[i]*(sensor_angle)
        xc.append(radi*math.cos(angle)+Cenx);
        yc.append(radi*math.sin(angle)+Ceny);        
    plt.scatter(xc,yc)
    plt.show()
    return xc,yc


def f(Z):
    return Z
fig = plt.figure()

tau=0.01 # reflection coefficient
gama=0.1 # absorption coefficient
delta = .1 # spacing betweent twoo points
x = y = np.arange(-30.0, 30.0, delta) # points generation
X, Y = np.meshgrid(x, y) # mesh generation

Z1 = np.exp((-X**2)- Y**2)
Z2 = np.exp(-(X)**2 - (Y - 1)**2)
Z =(Z2-Z1)
v2=30
v1=0
amp=np.arange(1,10,gama) # array for absorption
c=1
g=0 # gain of absorption


ih=15 # define location of inhomoginity
im = plt.imshow(f(Z), animated=True)
Y[40,100]=22

def updatefig(*args):
    global X, Y, v1, v2, c, g,Za
    #X[10,c*10]=100
    #Y[10,c*10]=100
    v2=(v2-1)    
    c+=1
    g=amp[c]       #first part 
    v2=(v2-1)          
    Z2 = np.exp(-(X - v1)**2 - (Y - v2)**2)       
    Z =(1/g)*(Z2)
    
    if v2==-30:
        v2=30
        
        # for repetation # put v2=30 here
        c=0
    if v2==ih:
        c=0
    if v2<ih:             
               #second part
        
        Z4=c/500*np.sin(np.sqrt(np.pi*1/c*((X)**2+(Y-ih)**2)))        
        Z=Z4
    
    if v2==28:
        Za=Z
    im.set_array(f(Z))
    
    return im,
print('Size of mesh: ', Y.shape)
print('absorption coefficient: ', gama)
print('reflection coefficient: ', tau)
print('inhomognity location is: ',ih)
print(X.shape)

 
plt.colorbar()

ani = animation.FuncAnimation(fig, updatefig, interval=0.0001, blit=True)
plt.show()

plot2=plt.figure()
Zb=Z
plt.plot(Z)
plt.show()

