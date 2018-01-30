#Converting data to FITS 
import os

sciname = ['ALESS001.1.NoPBCOR.mfs.image', 'ALESS002.1.NoPBCOR.mfs.image', 'ALESS003.1.NoPBCOR.mfs.image', 
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

for target in sciname:
    exportfits(imagename = target, fitsimage = target+'.fits')
               
os.system('mv *.fits FITS_NoPBCOR_mfs/')               
