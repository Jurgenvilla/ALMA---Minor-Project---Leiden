import numpy as np
import os

print 'Please introduce:\n'
print'Gaussian amplitude in mJy/beam\n'
Amplitude = input()
print'Mean frequency in GHz\n'
Mean      = input()
print'Sigma in GHz\n'
Sigma     = input()
print'Constant in mJy/beam\n'
Const     = input()

Flux = (Amplitude)/2.0

c = 3e5     #Speed of light in km/s

def X1(Amp, mu, sigma, flux):
	return np.sqrt( -2.0*sigma**2*np.log( (flux)/Amp ) ) + mu
	
def Radio_Velocity(Emi_freq):
	return c*(1.0 - Emi_freq/138.0)	
	
X1 = X1(Amplitude, Mean, Sigma, Const, Flux)	
X2 = 2.0*Mean - X1
	
print('The range in GHz is X1 = %0.2f and X2 = %0.2f'%(X1,X2))
print('The range in km/s is X1 = %0.2f and X2 = %0.2f'%(Radio_Velocity(X1),Radio_Velocity(X2)))
print('Emission frequency in %g km/s and %g GHz'%(Radio_Velocity(Mean),Mean))
