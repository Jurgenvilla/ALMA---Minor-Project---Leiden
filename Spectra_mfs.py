import numpy
import os

sciname1 = ['ALESS001.1.NoPBCOR.mfs.image', 'ALESS002.1.NoPBCOR.mfs.image', 'ALESS003.1.NoPBCOR.mfs.image', 
           'ALESS005.1.NoPBCOR.mfs.image', 'ALESS006.1.NoPBCOR.mfs.image', 'ALESS007.1.NoPBCOR.mfs.image', 
           'ALESS009.1.NoPBCOR.mfs.image', 'ALESS010.1.NoPBCOR.mfs.image', 'ALESS011.1.NoPBCOR.mfs.image', 
           'ALESS013.1.NoPBCOR.mfs.image', 'ALESS014.1.NoPBCOR.mfs.image', 'ALESS015.1.NoPBCOR.mfs.image',
           'ALESS017.1.NoPBCOR.mfs.image', 'ALESS018.1.NoPBCOR.mfs.image', 'ALESS019.1.NoPBCOR.mfs.image', 
           'ALESS022.1.NoPBCOR.mfs.image', 'ALESS023.1.NoPBCOR.mfs.image', 'ALESS025.1.NoPBCOR.mfs.image', 
           'ALESS029.1.NoPBCOR.mfs.image', 'ALESS031.1.NoPBCOR.mfs.image', 'ALESS035.1.NoPBCOR.mfs.image', 
           'ALESS037.1.NoPBCOR.mfs.image', 'ALESS039.1.NoPBCOR.mfs.image', 'ALESS041.1.NoPBCOR.mfs.image',
           'ALESS043.1.NoPBCOR.mfs.image', 'ALESS045.1.NoPBCOR.mfs.image', 'ALESS049.1.NoPBCOR.mfs.image', 
           'ALESS051.1.NoPBCOR.mfs.image', 'ALESS055.1.NoPBCOR.mfs.image', 'ALESS057.1.NoPBCOR.mfs.image', 
           'ALESS059.2.NoPBCOR.mfs.image', 'ALESS061.1.NoPBCOR.mfs.image', 'ALESS063.1.NoPBCOR.mfs.image', 
           'ALESS065.1.NoPBCOR.mfs.image', 'ALESS066.1.NoPBCOR.mfs.image', 'ALESS067.1.NoPBCOR.mfs.image',
           'ALESS068.1.NoPBCOR.mfs.image', 'ALESS069.1.NoPBCOR.mfs.image', 'ALESS070.1.NoPBCOR.mfs.image', 
           'ALESS071.1.NoPBCOR.mfs.image', 'ALESS072.1.NoPBCOR.mfs.image', 'ALESS073.1.NoPBCOR.mfs.image', 
           'ALESS074.1.NoPBCOR.mfs.image', 'ALESS075.1.NoPBCOR.mfs.image', 'ALESS076.1.NoPBCOR.mfs.image', 
           'ALESS079.1.NoPBCOR.mfs.image', 'ALESS080.1.NoPBCOR.mfs.image', 'ALESS082.1.NoPBCOR.mfs.image',
           'ALESS083.4.NoPBCOR.mfs.image', 'ALESS084.1.NoPBCOR.mfs.image', 'ALESS087.1.NoPBCOR.mfs.image', 
           'ALESS088.1.NoPBCOR.mfs.image', 'ALESS092.2.NoPBCOR.mfs.image', 'ALESS094.1.NoPBCOR.mfs.image', 
           'ALESS098.1.NoPBCOR.mfs.image', 'ALESS099.1.NoPBCOR.mfs.image', 'ALESS102.1.NoPBCOR.mfs.image', 
           'ALESS103.3.NoPBCOR.mfs.image', 'ALESS107.1.NoPBCOR.mfs.image', 'ALESS110.1.NoPBCOR.mfs.image',
           'ALESS112.1.NoPBCOR.mfs.image', 'ALESS114.1.NoPBCOR.mfs.image', 'ALESS115.1.NoPBCOR.mfs.image', 
           'ALESS116.1.NoPBCOR.mfs.image', 'ALESS118.1.NoPBCOR.mfs.image', 'ALESS119.1.NoPBCOR.mfs.image', 
           'ALESS122.1.NoPBCOR.mfs.image', 'ALESS124.1.NoPBCOR.mfs.image', 'ALESS126.1.NoPBCOR.mfs.image']

#All coordinates of science targets
coordinates = ['3h33m14.46s,-27d56m14.52s','3h33m2.69s,-27d56m42.76s','3h33m21.5s,-27d55m20.29s','3h31m28.91s,-27d59m9.02s',
               '3h32m56.96s,-28d1m0.68s','3h33m15.42s,-27d45m24.3s','3h32m11.34s,-27d52m11.93s','3h32m19.06s,-27d52m14.81s',
               '3h32m13.85s,-27d56m0.25s','3h32m48.99s,-27d42m51.8s','3h31m52.49s,-28d3m19.08s','3h33m33.37s,-27d59m29.57s',
               '3h32m7.3s,-27d51m20.75s','3h32m4.88s,-27d46m47.74s','3h32m8.26s,-27d58m14.19s','3h31m46.92s,-27d32m39.3s',
               '3h32m12.01s,-28d5m6.46s','3h31m56.88s,-27d59m39.33s','3h33m36.9s,-27d58m9.33s','3h31m49.79s,-27d57m40.76s',
               '3h31m10.51s,-27d37m15.42s','3h33m36.14s,-27d53m50.58s','3h31m45.03s,-27d34m36.74s','3h31m10.07s,-27d52m36.66s',
               '3h33m6.64s,-27d48m2.44s','3h32m25.26s,-27d52m30.53s','3h31m24.72s,-27d50m47.06s','3h31m45.06s,-27d44m27.32s',
               '3h33m2.22s,-27d40m35.45s','3h31m51.92s,-27d53m27.06s','3h33m3.82s,-27d44m18.2s','3h32m45.87s,-28d0m23.36s',
               '3h33m8.45s,-28d0m43.84s','3h32m52.27s,-27d35m26.27s','3h33m31.93s,-27d54m9.52s','3h32m43.2s,-27d55m14.34s',
               '3h32m33.33s,-27d39m13.57s','3h31m33.78s,-27d59m32.44s','3h31m44.02s,-27d38m35.52s','3h33m5.65s,-27d33m28.19s',
               '3h32m40.40s,-27d37m58.11s','3h32m29.29s,-27d56m19.71s','3h33m9.15s,-27d48m17.19s','3h31m27.19s,-27d55m51.34s',
               '3h33m32.34s,-27d59m55.63s','3h32m21.14s,-27d56m26.99s','3h31m42.8s,-27d48m36.88s','3h32m54s,-27d38m14.89s',
               '3h33m8.71s,-28d5m18.47s','3h31m54.5s,-27d51m5.64s','3h32m50.88s,-27d31m41.47s','3h31m54.76s,-27d53m41.49s',
               '3h31m38.14s,-27d43m43.41s','3h33m7.59s,-27d58m5.81s','3h31m29.92s,-27d57m22.74s','3h32m51.82s,-27d55m33.59s',
               '3h33m35.6s,-27d40m23.02s','3h33m25.04s,-27d34m1.11s','3h31m30.5s,-27d51m49.13s','3h31m22.66s,-27d54m17.22s',
               '3h32m48.86s,-27d31m13.3s','3h31m50.49s,-27d44m45.34s','3h33m49.7s,-27d42m34.59s','3h31m54.32s,-27d45m28.94s',
               '3h31m21.92s,-27d49m41.38s','3h32m56.64s,-28d3m25.16s','3h31m39.54s,-27d41m19.65s','3h32m4.04s,-27d36m6.37s',
               '3h32m9.61s,-27d41m7.68s']


Box = []
for target in sciname1:
    index = sciname1.index(target)
    cubeStat   = imstat(target, region='circle[['+str(coordinates[index])+'], 0.5arcsec]')
    x2extract  = cubeStat['maxpos'][0]
    y2extract  = cubeStat['maxpos'][1]
    extractBox = "%d,%d" % (x2extract, y2extract)                    # copy the position to a string
    Box.append(extractBox)
    
    
print Box
    
