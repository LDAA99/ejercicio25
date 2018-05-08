import numpy as np 
import matplotlib.pyplot as plt

G=6.674e-11 
Msol=1.989e30

mercurio=[2.13e-1, -3.73e-1, -5.06e-1]
Vmercurio=[1.89e-2, 1.51e-2, -4.99e-4]
tierra=[-6.86e-1, -7.33e-1, -6.64e-5]
Vtierra=[1.23e-2, -1.17e-2, 1.21e-6]
jupiter=[-3.62, -4.01, 9.75e-2]
Vjupiter=[5.52e-3, -4.7e-3, -1.04e-4]

alfa=np.linspace(0.0001, 5, 30)

betateo=G*Msol

betas=[]

#se tienen los datos de posicion y velocidad como vectores 
def norma(vector):
	a=np.sqrt(vector[0]**2+vector[1]**2+vector[2]**2)
	return a

#pasar de UA a metros
def cambio(x):
	metros=x*149597870700
	return metros

#calcular en funcion de alfa las observaciones
def beta(x, v, alfa):
	b=v**2/x**(1-alfa)
	return b

def proba(bteo, beta, sigma):
	n=np.exp(-(bteo-beta)**2/(2*sigma**2))
	return n

Nmercurio=norma(mercurio)
NVmercurio=norma(Vmercurio)

NewPosition=cambio(Nmercurio)
NewVel=cambio(NVmercurio)

#calcular los betas
for i in alfa:
	c=beta(NewPosition, NewVel, i)
	betas.append(c)

