import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

c        = 9.716e-15     #Light speed Mpc/s
Hov      = 2.26855e-18   #Hubble constant 1/s, 70km/s/Mpc 
OM       = 0.3
OL       = 0.7
Alpha_CO = 1

Name  = ['ALESS015.1','ALESS017.1','ALESS022.1','ALESS070.1','ALESS070.1',
         'ALESS076.1','ALESS088.1','ALESS112.1','ALESS116.1',
         'ALESS122.1']

Mean1 = [150.9453, 137.7893, 150.8221, 138.8847, 140.3927,
         139.1758, 139.2503, 139.1659, 151.1735,
         152.4379] 

Z, Amp, Mean, sigma, Const, X1, X2, SCO, Err_sco, Err_mean = np.loadtxt('Data_1.txt', usecols = (0,1,2,3,4,5,6,7,8,9), unpack = True)

def H(z,Om,Ol):
	return Hov*np.sqrt(Om*(1+z)**3 + (1-Om-Ol)*(1+z)**2 + Ol)

def f(z,Om,Ol):
  h = lambda x: 1./(H(x,Om,Ol)/c) 
  #print  integrate.quad(h,0.,z)[1]            
  return integrate.quad(h,0.,z)[0]
  
def r(z,Om,Ol):
  if (1-Om-Ol) == 0: 
    return f(z,Om,Ol)      
  
  if (1-Om-Ol) > 0:
    return (1./((Hov/c)*(np.sqrt(np.abs(1-Om-Ol)))))*np.sinh((Hov/c)*np.sqrt(np.abs(1-Om-Ol))*f(z,Om,Ol))

  if (1-Om-Ol) < 0:
    return (1./((Hov/c)*(np.sqrt(np.abs(1-Om-Ol)))))*np.sin((Hov/c)*np.sqrt(np.abs(1-Om-Ol))*f(z,Om,Ol))


def Dl(z,Om,Ol):
	return (1+z)*r(z,Om,Ol) 
      
#def S_CO(A, Mu, Sigma, C, x1, x2):
  #g = lambda y: A*np.exp( -(y - Mu)**2/(2.0*Sigma**2) ) + C
  #print  integrate.quad(g, x1, x2)[1]*1e-3
  #return integrate.quad(g, x1, x2)[0]

print '--------------------------------------------------------------------------------------------'
print 'ALESS68.1 has no measured redshift'

for i in range(0, len(Z)):
  Distance        = Dl(Z[i], OM, OL)
  #Total_Flux      = S_CO(Amp[i], Mean[i], sigma[i], Const[i], X1[i], X2[i])
  #Total_Flux      = Total_Flux*1e-3
  Line_Luminosity = 3.25e7*(1.0+Z[i])**-3 *Mean1[i]**-2 *SCO[i]*Distance**2 
  CO_Luminosity   = Line_Luminosity/0.31
  Molecular_mass  = Alpha_CO*CO_Luminosity
  
  #Err_Line_Luminosity = 3.25e7*(1.0+Z[i])**-3*Distance**2*(SCO[i]/Mean[i]**2)*( Err_sco[i]/SCO[i]+((2.0/Mean[i])*Err_mean[i])*Mean[i]**2)
  Err_Line_Luminosity = 3.25e7*(1.0+Z[i])**-3*Distance**2*(SCO[i]*Mean1[i]**-2)*( Err_sco[i]/SCO[i] + 2.0*Err_mean[i]/Mean1[i])
 
  print('Error in Total Flux : %g'%Err_sco[i])  
  print('Error in Line luminosity = %g'%abs(Err_Line_Luminosity))
  Err_tot = (Line_Luminosity/0.31)*(Err_Line_Luminosity/Line_Luminosity + 0.06/0.31)
  print('Errror in Lco(1-0) and mass assuming alpha = 1 = %g'%abs(Err_tot))
  print('\n Name = %s \n Distance = %g \n Total Flux = %g \n luminosity = %g \n L_CO(1-->0) = %g \n M_H2 = %g \n'%(Name[i], Distance, SCO[i], Line_Luminosity, CO_Luminosity, Molecular_mass))
  
  del Distance, Line_Luminosity, CO_Luminosity, Molecular_mass
  
  print '--------------------------------------------------------------------------------------------'
  
