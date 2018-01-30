mslist = ['../../uid___A002_Xae4720_X5c8.ms.split.cal',
          '../../uid___A002_Xae4720_X766.ms.split.cal',
          '../../uid___A002_Xae6c13_X2481.ms.split.cal',
          '../../uid___A002_Xae4720_X55dd.ms.split.cal',
          '../../uid___A002_Xae6c13_X230c.ms.split.cal']
  
#sciname = ['ALESS070.1'] #spw = '0:36~120,1:10~90,2,3'          
#sciname = ['ALESS122.1'] #spw = '0,1,2:10~120,3:10~60'   

#sciname = ['ALESS070.1', 'ALESS122.1']   

#sciname = ['ALESS070.1']   
sciname = ['ALESS122.1']   

for target in sciname:
	clean(vis = mslist,
    imagename = target+'test',
    field = target,
    mode = 'mfs',
    #spw = '0:36~120,1:10~90,2,3',
    spw = '0,1,2:10~120,3:10~60',
    imagermode = 'csclean',
    interactive = F,
    niter = 500,
    threshold = '0.0006mJy',
    imsize = [360, 360],
    cell = '0.46arcsec',
    uvtaper = True,
    outertaper = ['2.1arcsec', '1.1arcsec'],
    weighting = 'briggs',
    robust = 0.5)   


#exportfits(imagename = 'ALESS070.1test.image', fitsimage = 'ALESS070.1test.image.fits')
exportfits(imagename = 'ALESS122.1test.image', fitsimage = 'ALESS122.1test.image.fits')
