import matplotlib
matplotlib.use('Agg')
import aplpy
import pylab
#import numpy 
#from astropy import units as u
#from astropy.coordinates import SkyCoord

#module load montage/4.0
#ipython --pylab
#import montage_wrapper

#c = SkyCoord('3h31m39.54s','-27d41m19.65s',frame='icrs') #ALESS122.1 coordinates
#print c #in degrees

gc = aplpy.FITSFigure('ALESS122.1test.image.fits')
gc.show_colorscale()
gc.add_colorbar()
gc.colorbar.set_width(0.3)
gc.add_beam()
gc.beam.set_color('white')
gc.beam.set_edgecolor('white')
gc.beam.set_alpha(0.45)
gc.show_colorscale(vmin=None, vmid=None, vmax=None,cmap='gist_earth', pmin=0.8, pmax=99.99999,stretch='linear',  interpolation='nearest')
gc.axis_labels.set_xtext('Right Ascension (J2000)')
gc.axis_labels.set_ytext('Declination (J2000)')
gc.show_contour('ALESS122.1test.image.fits', colors='white', levels = [-3*57.64736e-6, -2*57.64736e-6, 2*57.64736e-6,3*57.64736e-6, 4*57.64736e-6, 5*57.64736e-6, 7*57.64736e-6])
gc.show_markers(52.91475,-27.68879167, facecolor = 'r', marker = 'o', s=50)
gc.add_label(52.91458333, -27.68663889, text = 'ALESS122.1 (Continuum)', weight = 'bold', size = 'xx-large', color = 'white')
gc.recenter(52.91475,-27.68879167, radius = 0.00225)
#gc.show_contour('ALESS122.1test.image.fits', colors='white', levels = [2*57.64736e-6, 3*57.64736e-6, 4*57.64736e-6, 5*57.64736e-6])
gc.savefig('ALESS122.1.png')
gc.close()

#c = SkyCoord('3h31m44.02s','-27d38m35.52s',frame='icrs') #ALESS070.1 coordinates
#print c #in degrees

hc = aplpy.FITSFigure('ALESS070.1test.image.fits')
hc.show_colorscale()
hc.add_colorbar()
hc.colorbar.set_width(0.3)
hc.add_beam()
hc.beam.set_color('white')
hc.beam.set_edgecolor('white')
hc.beam.set_alpha(0.45)
hc.show_colorscale(vmin=None, vmid=None, vmax=None,cmap='gist_earth', pmin=0.8, pmax=99.99999,stretch='linear',  interpolation='nearest')
hc.axis_labels.set_xtext('Right Ascension (J2000)')
hc.axis_labels.set_ytext('Declination (J2000)')
hc.show_contour('ALESS070.1test.image.fits', colors='white', levels = [-3*56.27053e-6, -2*56.27053e-6, 2*56.27053e-6, 3*56.27053e-6, 4*56.27053e-6, 5*56.27053e-6])
hc.show_markers(52.93341667, -27.6432, facecolor = 'r', marker = 'o', s=50)
hc.add_label(52.93319167, -27.64105556, text = 'ALESS070.1 (Continuum)', weight = 'bold', size = 'xx-large', color = 'white')
hc.recenter(52.93341667, -27.6432, radius = 0.00225)
#hc.show_contour('ALESS070.1test.image.fits', colors='white', levels = [2*56.27053e-6, 3*56.27053e-6, 4*56.27053e-6, 5*56.27053e-6])
hc.savefig('ALESS070.1.png')
hc.close()

