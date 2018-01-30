imfit(imagename = 'ALESS122.1.NoPBCOR.mfs.image/', excludepix = [-1e10,0], logfile = 'co_fit_122.log', region = 'ALESS122.1_Region.rgn')
imfit(imagename = 'ALESS070.1.NoPBCOR.mfs.image/', excludepix = [-1e10,0], logfile = 'co_fit_070.log', region = 'ALESS070.1_Region.rgn')

#deconvolve(imagename = 'ALESS122.1.NoPBCOR.mfs.image/', model = 'ALESS122.1.ModelDeconvolve', psf ='ALESS122.1.psf/', niter = 500, threshold = '0.0006mJy')
#deconvolve(imagename = 'ALESS070.1.NoPBCOR.mfs.image/', model = 'ALESS070.1.ModelDeconvolve', psf ='ALESS070.1.psf/', niter = 500, threshold = '0.0006mJy')
