mslist = ['uid___A002_Xae4720_X5c8.ms.split.cal',
          'uid___A002_Xae4720_X766.ms.split.cal',
          'uid___A002_Xae6c13_X2481.ms.split.cal',
          'uid___A002_Xae4720_X55dd.ms.split.cal',
          'uid___A002_Xae6c13_X230c.ms.split.cal']

## for ms in mslist:
##     listobs(ms,listfile=ms+'.listobs')

#All science targets have fieldID 2~70
sciname = ['ALESS001.1', 'ALESS002.1', 'ALESS003.1', 'ALESS005.1',
           'ALESS006.1', 'ALESS007.1', 'ALESS009.1', 'ALESS010.1',
           'ALESS011.1', 'ALESS013.1', 'ALESS014.1', 'ALESS015.1',
           'ALESS017.1', 'ALESS018.1', 'ALESS019.1', 'ALESS022.1',
           'ALESS023.1', 'ALESS025.1', 'ALESS029.1', 'ALESS031.1',
           'ALESS035.1', 'ALESS037.1', 'ALESS039.1', 'ALESS041.1',
           'ALESS043.1', 'ALESS045.1', 'ALESS049.1', 'ALESS051.1',
           'ALESS055.1', 'ALESS057.1', 'ALESS059.2', 'ALESS061.1',
           'ALESS063.1', 'ALESS065.1', 'ALESS066.1', 'ALESS067.1',
           'ALESS068.1', 'ALESS069.1', 'ALESS070.1', 'ALESS071.1',
           'ALESS072.1', 'ALESS073.1', 'ALESS074.1', 'ALESS075.1',
           'ALESS076.1', 'ALESS079.1', 'ALESS080.1', 'ALESS082.1',
           'ALESS083.4', 'ALESS084.1', 'ALESS087.1', 'ALESS088.1',
           'ALESS092.2', 'ALESS094.1', 'ALESS098.1', 'ALESS099.1',
           'ALESS102.1', 'ALESS103.3', 'ALESS107.1', 'ALESS110.1',
           'ALESS112.1', 'ALESS114.1', 'ALESS115.1', 'ALESS116.1',
           'ALESS118.1', 'ALESS119.1', 'ALESS122.1', 'ALESS124.1',
           'ALESS126.1']


#Imaging at the requested resolution of 2.3"
for target in sciname:
    clean(vis = mslist,
          imagename = target+'.NoPBCOR.mfs',
          field = target,
          mode = 'mfs',
          spw = '0~3',
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

#for target in sciname:
    #rms = imstat(target+'.mfs.image', region='box [[64pix, 214pix], [300pix, 310pix]]')['rms'][0]*1.e6
    #head1 = imhead(target+'.mfs.image', mode='list')
    #beammaj = head1['beammajor']['value']
    #beammin = head1['beamminor']['value']
    #print target + ' -> rms = ' + str(round(rms, 1)) + ' uJy - beam = ' + str(round(beammaj, 2)) + ' x ' + str(round(beammin, 2))

## ALESS001.1 -> rms = 50.0 uJy - beam = 2.37 x 2.24
## ALESS002.1 -> rms = 50.7 uJy - beam = 2.38 x 2.25
## ALESS003.1 -> rms = 50.8 uJy - beam = 2.38 x 2.25
## ALESS005.1 -> rms = 51.6 uJy - beam = 2.38 x 2.26
## ALESS006.1 -> rms = 49.7 uJy - beam = 2.38 x 2.25
## ALESS007.1 -> rms = 48.4 uJy - beam = 2.38 x 2.25
## ALESS009.1 -> rms = 52.3 uJy - beam = 2.37 x 2.25
## ALESS010.1 -> rms = 51.7 uJy - beam = 2.38 x 2.26
## ALESS011.1 -> rms = 52.2 uJy - beam = 2.38 x 2.26
## ALESS013.1 -> rms = 50.1 uJy - beam = 2.38 x 2.25
## ALESS014.1 -> rms = 50.2 uJy - beam = 2.39 x 2.26
## ALESS015.1 -> rms = 51.3 uJy - beam = 2.39 x 2.26
## ALESS017.1 -> rms = 50.1 uJy - beam = 2.39 x 2.26
## ALESS018.1 -> rms = 49.8 uJy - beam = 2.39 x 2.26
## ALESS019.1 -> rms = 52.2 uJy - beam = 2.39 x 2.26
## ALESS022.1 -> rms = 51.2 uJy - beam = 2.4 x 2.26
## ALESS023.1 -> rms = 52.1 uJy - beam = 2.4 x 2.26
## ALESS025.1 -> rms = 51.6 uJy - beam = 2.4 x 2.26
## ALESS029.1 -> rms = 51.1 uJy - beam = 2.4 x 2.26
## ALESS031.1 -> rms = 53.9 uJy - beam = 2.4 x 2.26
## ALESS035.1 -> rms = 52.9 uJy - beam = 2.41 x 2.26
## ALESS037.1 -> rms = 50.2 uJy - beam = 2.4 x 2.26
## ALESS039.1 -> rms = 51.8 uJy - beam = 2.41 x 2.26
## ALESS041.1 -> rms = 52.9 uJy - beam = 2.41 x 2.26
## ALESS043.1 -> rms = 51.1 uJy - beam = 2.41 x 2.26
## ALESS045.1 -> rms = 51.5 uJy - beam = 2.42 x 2.27
## ALESS049.1 -> rms = 54.3 uJy - beam = 2.42 x 2.26
## ALESS051.1 -> rms = 50.3 uJy - beam = 2.42 x 2.27
## ALESS055.1 -> rms = 52.7 uJy - beam = 2.42 x 2.27
## ALESS057.1 -> rms = 52.9 uJy - beam = 2.43 x 2.27
## ALESS059.2 -> rms = 50.5 uJy - beam = 2.43 x 2.27
## ALESS061.1 -> rms = 50.8 uJy - beam = 2.43 x 2.27
## ALESS063.1 -> rms = 50.5 uJy - beam = 2.43 x 2.27
## ALESS065.1 -> rms = 52.2 uJy - beam = 2.43 x 2.27
## ALESS066.1 -> rms = 49.7 uJy - beam = 2.43 x 2.27
## ALESS067.1 -> rms = 51.0 uJy - beam = 2.43 x 2.27
## ALESS068.1 -> rms = 52.6 uJy - beam = 2.42 x 2.27
## ALESS069.1 -> rms = 53.1 uJy - beam = 2.43 x 2.27
## ALESS070.1 -> rms = 52.8 uJy - beam = 2.43 x 2.27
## ALESS071.1 -> rms = 52.6 uJy - beam = 2.43 x 2.27
## ALESS072.1 -> rms = 52.0 uJy - beam = 2.43 x 2.27
## ALESS073.1 -> rms = 53.3 uJy - beam = 2.43 x 2.27
## ALESS074.1 -> rms = 51.3 uJy - beam = 2.44 x 2.27
## ALESS075.1 -> rms = 52.9 uJy - beam = 2.45 x 2.26
## ALESS076.1 -> rms = 51.8 uJy - beam = 2.44 x 2.27
## ALESS079.1 -> rms = 51.2 uJy - beam = 2.45 x 2.27
## ALESS080.1 -> rms = 53.3 uJy - beam = 2.46 x 2.27
## ALESS082.1 -> rms = 52.6 uJy - beam = 2.47 x 2.27
## ALESS083.4 -> rms = 51.4 uJy - beam = 2.47 x 2.28
## ALESS084.1 -> rms = 51.3 uJy - beam = 2.47 x 2.27
## ALESS087.1 -> rms = 52.5 uJy - beam = 2.47 x 2.27
## ALESS088.1 -> rms = 54.8 uJy - beam = 2.47 x 2.28
## ALESS092.2 -> rms = 54.4 uJy - beam = 2.47 x 2.26
## ALESS094.1 -> rms = 53.1 uJy - beam = 2.47 x 2.27
## ALESS098.1 -> rms = 55.8 uJy - beam = 2.48 x 2.28
## ALESS099.1 -> rms = 54.5 uJy - beam = 2.48 x 2.27
## ALESS102.1 -> rms = 54.3 uJy - beam = 2.48 x 2.27
## ALESS103.3 -> rms = 53.9 uJy - beam = 2.49 x 2.27
## ALESS107.1 -> rms = 57.9 uJy - beam = 2.5 x 2.27
## ALESS110.1 -> rms = 56.2 uJy - beam = 2.51 x 2.28
## ALESS112.1 -> rms = 53.3 uJy - beam = 2.51 x 2.28
## ALESS114.1 -> rms = 58.3 uJy - beam = 2.51 x 2.28
## ALESS115.1 -> rms = 54.7 uJy - beam = 2.5 x 2.28
## ALESS116.1 -> rms = 54.9 uJy - beam = 2.52 x 2.28
## ALESS118.1 -> rms = 56.8 uJy - beam = 2.52 x 2.28
## ALESS119.1 -> rms = 54.6 uJy - beam = 2.51 x 2.28
## ALESS122.1 -> rms = 57.3 uJy - beam = 2.52 x 2.28
## ALESS124.1 -> rms = 55.7 uJy - beam = 2.53 x 2.28
## ALESS126.1 -> rms = 56.1 uJy - beam = 2.53 x 2.28

#Creating pbcor images and conversion to fits
#for target in sciname:
    #impbcor(imagename = target+'.mfs.image',
            #pbimage = target+'.mfs.flux',
            #outfile = target+'.mfs.image.pbcor',
            #mode = 'divide')

    #exportfits(imagename = target+'.mfs.image.pbcor',
               #fitsimage = target+'.mfs.image.pbcor.fits')

    #exportfits(imagename = target+'.mfs.flux',
               #fitsimage = target+'.mfs.flux.fits')

