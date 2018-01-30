mslist = ['uid___A002_Xae4720_X5c8.ms.split.cal',
          'uid___A002_Xae4720_X766.ms.split.cal',
          'uid___A002_Xae6c13_X2481.ms.split.cal',
          'uid___A002_Xae4720_X55dd.ms.split.cal',
          'uid___A002_Xae6c13_X230c.ms.split.cal']

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
          imagename = target,
          field = target,
          mode = 'frequency',
          width = '62.5 MHz',
          spw = '0~3',
          interactive = F,
          niter = 0,
          imsize = [360, 360],
          cell = '0.46arcsec',
          weighting = 'briggs',
          robust = 0.5)
