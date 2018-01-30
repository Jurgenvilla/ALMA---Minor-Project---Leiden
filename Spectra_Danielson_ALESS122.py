import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from matplotlib import gridspec
from astropy.wcs import WCS

#Frequency
def Line(Redshift, Emission_Frequency):
	return Emission_Frequency*(1.0 + Redshift)
	
#Data	
Frequency, Flux = np.loadtxt('122.1_composite.dat', usecols = (0,1), unpack = True) 	
#Gal             = fits.open('1692_V2a.4.2.0180.1.2d.fits')
Gal             = fits.open('1692_V2a.4.2.0180.1.2d.fits')[0]
#IMG             = Gal[0].data
data    = Gal.data
wcs     = WCS(Gal.header)
WCScut  = wcs[:,:]
DATAcut = data[:,:]

#Plot_1
fig = plt.figure()
plt.set_cmap('YlOrRd')
#plt.subplots(figsize = (12,6))
gs  = gridspec.GridSpec(2, 1, height_ratios=[2, 0.8])
ax0 = plt.subplot(gs[0])

#Spectrum and Line Plot
Line0 = ax0.plot(Frequency, Flux, '-', lw = 1, c = 'b', label = r'$ALESS0122.1\ Comp.$')
Line1 = ax0.axvline(Line(2.0197, 1334.53), ymin = 0, ymax = 100, alpha = 0.8, ls = '--', lw = 1.4 ,color = 'r', label = r'$CII$ ( $\mathrm{z}$ $=$ $2.0197$)')
Line2 = ax0.axvline(Line(2.0229, 1393.76), ymin = 0, ymax = 100, alpha = 0.8, ls = '--', lw = 1.4 ,color = 'g', label = r'$SiIV$ ( $\mathrm{z}$ $=$ $2.0229$)')
Line3 = ax0.axvline(Line(2.0282, 1640.00), ymin = 0, ymax = 100, alpha = 0.8, ls = '-.', lw = 1.4 ,color = 'k', label = r'$HeII$ ( $\mathrm{z}$ $=$ $2.0282$)')
Line4 = ax0.axvline(Line(2.0222, 1909.00), ymin = 0, ymax = 100, alpha = 0.8, ls = ':', lw = 1.4 ,color = 'r', label = r'$CIII$ ( $\mathrm{z}$ $=$ $2.0222$)')
Line5 = ax0.axvline(Line(2.0222, 1548.89), ymin = 0, ymax = 100, alpha = 0.8, ls = '-.', lw = 1.4 ,color = 'r', label = r'$CIV$ ( $\mathrm{z}$ $=$ $2.0222$)')
Line6 = ax0.axvline(Line(2.0222, 1550.77), ymin = 0, ymax = 100, alpha = 0.8, ls = '-', lw = 1.4 ,color = 'r', label = r'$CIV$ ( $\mathrm{z}$ $=$ $2.0222$)')
Line7 = ax0.axvline(Line(2.0222, 1526.72), ymin = 0, ymax = 100, alpha = 0.8, ls = '--', lw = 1.4 ,color = 'y', label = r'$SiII$ ( $\mathrm{z}$ $=$ $2.0222$)')
ax0.set_ylim([6, 100])
ax0.set_ylabel(r'$Flux\ [10^{9} erg^{-1} cm^{-2} \AA ^{-1}]$', fontsize = 15)
ax0.get_yaxis().set_label_coords(-0.1,0.5)

#Spectrum 2D-plot
#ax1 = plt.subplot(gs[1], sharex = ax0)
#ax1 = plt.subplot(projection = WCScut)
ax1 = fig.add_subplot(gs[1], sharex = ax0)
ax1.set_xlim([3835, 6660])
#ax1.set_xlabel(r'$Wavelength\ [\AA]$', fontsize = 15)
#ax1.set_ylabel(r'$Pixel\ Value$', fontsize = 15)
#ax1.get_yaxis().set_label_coords(-0.1,0.5)

ax1 = plt.subplot(gs[1], projection = WCScut)
#plt.setp(ax1.get_xaxis(), visible = False)
#plt.setp(ax1.get_yaxis(), visible = False)
ax1.imshow(DATAcut, origin = 'lower', vmin = -4.9, vmax = 8.0, aspect = 'auto')
ax1.coords[0].set_axislabel(r'$Wavelength\ [\AA]$', fontsize = 15)
ax1.coords[1].set_axislabel(r'$Pixel\ Value$', fontsize = 15, minpad = 2.1)
plt.setp(ax0.get_xticklabels(), visible = False)
ax0.legend(loc = 'best', frameon = False, prop={'size':10})

#plt.tight_layout()
plt.subplots_adjust(hspace=.0)
plt.savefig('ALESS122_Composite.png')
plt.close(fig)
#plt.show()

#======================================================================================================================

#Plot_2
fig = plt.figure()
plt.set_cmap('YlOrRd')
#plt.subplots(figsize = (12,6))
gs  = gridspec.GridSpec(2, 1, height_ratios=[2, 0.8])
ax0 = plt.subplot(gs[0])

#Spectrum and Line Plot
Line0 = ax0.plot(Frequency, Flux, '-', lw = 1, c = 'b', label = r'$ALESS0122.1\ Comp.$')
Line1 = ax0.axvline(Line(2.0252, 1334.53), ymin = 0, ymax = 100, alpha = 0.8, ls = '--', lw = 1.4 ,color = 'r', label = r'$CII$ ( $\mathrm{z}$ $=$ $2.0252$)')
Line2 = ax0.axvline(Line(2.0252, 1393.76), ymin = 0, ymax = 100, alpha = 0.8, ls = '--', lw = 1.4 ,color = 'g', label = r'$SiIV$ ( $\mathrm{z}$ $=$ $2.0252$)')
Line3 = ax0.axvline(Line(2.0252, 1640.00), ymin = 0, ymax = 100, alpha = 0.8, ls = '-.', lw = 1.4 ,color = 'k', label = r'$HeII$ ( $\mathrm{z}$ $=$ $2.0252$)')
Line4 = ax0.axvline(Line(2.0252, 1909.00), ymin = 0, ymax = 100, alpha = 0.8, ls = ':', lw = 1.4 ,color = 'r', label = r'$CIII$ ( $\mathrm{z}$ $=$ $2.0252$)')
Line5 = ax0.axvline(Line(2.0252, 1548.89), ymin = 0, ymax = 100, alpha = 0.8, ls = '-.', lw = 1.4 ,color = 'r', label = r'$CIV$ ( $\mathrm{z}$ $=$ $2.0252$)')
Line6 = ax0.axvline(Line(2.0252, 1550.77), ymin = 0, ymax = 100, alpha = 0.8, ls = '-', lw = 1.4 ,color = 'r', label = r'$CIV$ ( $\mathrm{z}$ $=$ $2.0252$)')
Line7 = ax0.axvline(Line(2.0252, 1526.72), ymin = 0, ymax = 100, alpha = 0.8, ls = '--', lw = 1.4 ,color = 'y', label = r'$SiII$ ( $\mathrm{z}$ $=$ $2.0252$)')
ax0.set_ylim([6, 100])
ax0.set_ylabel(r'$Flux\ [10^{9} erg^{-1} cm^{-2} \AA ^{-1}]$', fontsize = 15)
ax0.get_yaxis().set_label_coords(-0.1,0.5)

#Spectrum 2D-plot
#ax1 = plt.subplot(gs[1], sharex = ax0)
#ax1 = plt.subplot(projection = WCScut)
ax1 = fig.add_subplot(gs[1], sharex = ax0)
ax1.set_xlim([3835, 6660])
#ax1.set_xlabel(r'$Wavelength\ [\AA]$', fontsize = 15)
#ax1.set_ylabel(r'$Pixel\ Value$', fontsize = 15)
#ax1.get_yaxis().set_label_coords(-0.1,0.5)

ax1 = plt.subplot(gs[1], projection = WCScut)
#plt.setp(ax1.get_xaxis(), visible = False)
#plt.setp(ax1.get_yaxis(), visible = False)
ax1.imshow(DATAcut, origin = 'lower', vmin = -4.9, vmax = 8.0, aspect = 'auto')
ax1.coords[0].set_axislabel(r'$Wavelength\ [\AA]$', fontsize = 15)
ax1.coords[1].set_axislabel(r'$Pixel\ Value$', fontsize = 15, minpad = 2.1)
plt.setp(ax0.get_xticklabels(), visible = False)
ax0.legend(loc = 'best', frameon = False, prop={'size':10})

#plt.tight_layout()
plt.subplots_adjust(hspace=.0)
plt.savefig('ALESS122_Composite_Mine.png')
plt.close(fig)
#plt.show()
