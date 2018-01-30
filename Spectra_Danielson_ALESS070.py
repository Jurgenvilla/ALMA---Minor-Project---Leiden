import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from matplotlib import gridspec

#Frequency
def Line(Redshift, Emission_Frequency):
	return Emission_Frequency*(1.0 + Redshift)
	
#Data	
Frequency, Flux = np.loadtxt('070_UVB.dat', usecols = (0,1), unpack = True) 	
Gal             = fits.open('070.1_X.-99.4_UVB.2d.fits')
IMG             = Gal[0].data

#Plot_1
#plt.subplots(figsize = (12,6))
gs  = gridspec.GridSpec(2, 1, height_ratios=[2, 0.8])
ax0 = plt.subplot(gs[0])

#Spectrum and Line Plot
Line0 = ax0.plot(Frequency, Flux, '-', lw = 1, c = 'b', label = r'$ALESS070.1\ -\ UVB$')
Line1 = ax0.axvline(Line(2.0918, 1215.67), ymin = 0, ymax = 1500, alpha = 0.8, ls = 'dashed', lw = 1.4 ,color = 'g', label = r'$Lyman\ \alpha$ ( $\mathrm{z}$ $=$ $2.0918$)')
ax0.set_ylim([-1180, 1900])
#ax0.set_ylabel(r'$Flux\ [10^{9} erg^{-1} cm^{-2} \AA ^{-1}]$', fontsize = 15)
ax0.set_ylabel(r'$Arbitrary\ Flux$', fontsize = 15)
ax0.get_yaxis().set_label_coords(-0.1,0.5)

#Spectrum 2D-plot
ax1 = plt.subplot(gs[1], sharex = ax0)
plt.set_cmap('YlOrRd')
ax1.imshow(IMG, origin = 'lower', vmin = -2.5, vmax = 3.5, aspect = 'auto')
ax1.set_xlabel(r'$Wavelength\ [\AA]$', fontsize = 15)
ax1.set_ylabel(r'$Pixel\ Value$', fontsize = 15)
ax1.set_xlim([3738, 3780])
ax1.get_yaxis().set_label_coords(-0.1,0.5)
plt.setp(ax0.get_xticklabels(), visible = False)

ax0.legend(loc = 'best', frameon = False, prop={'size':15})

plt.tight_layout()
plt.subplots_adjust(hspace=.0)
plt.savefig('ALESS070_UVB.png')
plt.clf()
#plt.show()

#==========================================================================================
#Plot_2
#plt.subplots(figsize = (12,6))
gs  = gridspec.GridSpec(2, 1, height_ratios=[2, 0.8])
ax0 = plt.subplot(gs[0])

#Spectrum and Line Plot
Line0 = ax0.plot(Frequency, Flux, '-', lw = 1, c = 'b', label = r'$ALESS070.1\ -\ UVB$')
Line1 = ax0.axvline(Line(2.319, 1215.67), ymin = 0, ymax = 1500, alpha = 0.8, ls = 'dashed', lw = 1.4 ,color = 'g', label = r'$Lyman\ \alpha$ ( $\mathrm{z}$ $=$ $2.3190$)')
ax0.set_ylim([-1180, 1900])
#ax0.set_ylabel(r'$Flux\ [10^{9} erg^{-1} cm^{-2} \AA ^{-1}]$', fontsize = 15)
ax0.set_ylabel(r'$Arbitrary\ Flux$', fontsize = 15)
ax0.get_yaxis().set_label_coords(-0.1,0.5)

#Spectrum 2D-plot
ax1 = plt.subplot(gs[1], sharex = ax0)
plt.set_cmap('YlOrRd')
ax1.imshow(IMG, origin = 'lower', vmin = -2.5, vmax = 3.5, aspect = 'auto')
ax1.set_xlabel(r'$Wavelength\ [\AA]$', fontsize = 15)
ax1.set_ylabel(r'$Pixel\ Value$', fontsize = 15)
ax1.set_xlim([4014, 4056])
ax1.get_yaxis().set_label_coords(-0.1,0.5)
plt.setp(ax0.get_xticklabels(), visible = False)

ax0.legend(loc = 'best', frameon = False, prop={'size':15})

plt.tight_layout()
plt.subplots_adjust(hspace=.0)
plt.savefig('ALESS070_UVB_MyLine.png')
plt.clf()
#plt.show()
