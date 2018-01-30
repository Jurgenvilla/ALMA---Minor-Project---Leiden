import numpy
import os
import matplotlib.pyplot as plt

#All science targets have fieldID 2~70

sciname = ['ALESS001.1.image', 'ALESS002.1.image', 'ALESS003.1.image', 'ALESS005.1.image',
           'ALESS006.1.image', 'ALESS007.1.image', 'ALESS009.1.image', 'ALESS010.1.image',
           'ALESS011.1.image', 'ALESS013.1.image', 'ALESS014.1.image', 'ALESS015.1.image',
           'ALESS017.1.image', 'ALESS018.1.image', 'ALESS019.1.image', 'ALESS022.1.image',
           'ALESS023.1.image', 'ALESS025.1.image', 'ALESS029.1.image', 'ALESS031.1.image',
           'ALESS035.1.image', 'ALESS037.1.image', 'ALESS039.1.image', 'ALESS041.1.image',
           'ALESS043.1.image', 'ALESS045.1.image', 'ALESS049.1.image', 'ALESS051.1.image',
           'ALESS055.1.image', 'ALESS057.1.image', 'ALESS059.2.image', 'ALESS061.1.image',
           'ALESS063.1.image', 'ALESS065.1.image', 'ALESS066.1.image', 'ALESS067.1.image',
           'ALESS068.1.image', 'ALESS069.1.image', 'ALESS070.1.image', 'ALESS071.1.image',
           'ALESS072.1.image', 'ALESS073.1.image', 'ALESS074.1.image', 'ALESS075.1.image',
           'ALESS076.1.image', 'ALESS079.1.image', 'ALESS080.1.image', 'ALESS082.1.image',
           'ALESS083.4.image', 'ALESS084.1.image', 'ALESS087.1.image', 'ALESS088.1.image',
           'ALESS092.2.image', 'ALESS094.1.image', 'ALESS098.1.image', 'ALESS099.1.image',
           'ALESS102.1.image', 'ALESS103.3.image', 'ALESS107.1.image', 'ALESS110.1.image',
           'ALESS112.1.image', 'ALESS114.1.image', 'ALESS115.1.image', 'ALESS116.1.image',
           'ALESS118.1.image', 'ALESS119.1.image', 'ALESS122.1.image', 'ALESS124.1.image',
           'ALESS126.1.image']

#6arcsec radius    
#sciname1 = ['180,180', '179,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,179', '180,180', '180,180', '180,179', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '181,180', '181,180', '179,180', '179,180', '180,179', '180,180', '180,180', '180,179', '179,180', '180,179', '180,180', '179,180', '180,179', '180,181', '180,179', '180,180', '180,180', '180,180', '180,179', '179,180', '180,180', '180,180', '179,180', '179,180', '179,180', '179,180', '179,180', '180,181', '179,180', '179,180', '179,180', '179,180', '179,180', '180,180', '179,180', '179,180', '179,180', '181,180', '180,179', '179,180', '180,181', '180,180', '179,180', '179,180', '180,181', '180,180', '180,180', '179,180']

#Point Source
#sciname1 = ['180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180', '180,180']

#1arcsec radius
#sciname1 = ['180,180', '179,180', '180,180', '180,180', 
            #'180,180', '181,179', '180,180', '180,180', 
            #'180,180', '180,180', '180,180', '180,179', 
            #'180,180', '180,180', '180,179', '180,180', 
            #'180,180', '180,180', '180,180', '180,180', 
            #'180,180', '181,180', '181,180', '179,180', 
            #'179,181', '181,179', '180,180', '180,180', 
            #'180,179', '179,181', '179,179', '180,180', 
            #'179,180', '180,179', '180,181', '179,178', 
            #'180,180', '180,180', '180,180', '180,179', 
            #'179,180', '180,180', '180,180', '179,181', 
            #'179,180', '179,180', '178,179', '177,180', 
            #'179,177', '179,180', '178,179', '178,181', 
            #'178,182', '179,179', '180,180', '178,178', 
            #'178,179', '177,180', '181,180', '180,179', 
            #'179,180', '183,179', '180,180', '179,179', 
            #'179,179', '180,181', '180,180', '180,180', 
            #'179,180']
#0.5arcsec radius            
sciname1 =  ['180,180', '179,180', '180,180', '180,180', 
             '180,180', '180,180', '180,180', '180,180',
             '180,180', '180,180', '180,180', '180,179', 
             '180,180', '180,180', '180,179', '180,180',
             '180,180', '180,180', '180,180', '180,180',
             '180,180', '181,180', '181,180', '179,180',
             '179,180', '180,179', '180,180', '180,180',
             '180,179', '179,180', '180,179', '180,180',
             '179,180', '180,179', '180,181', '180,179',
             '180,180', '180,180', '180,180', '180,179',
             '179,180', '180,180', '180,180', '179,180', 
             '179,180', '179,180', '179,180', '179,180',
             '180,181', '179,180', '179,180', '179,180',
             '179,180', '179,180', '180,180', '179,180', 
             '179,180', '179,180', '181,180', '180,179', 
             '179,180', '180,181', '180,180', '179,180',
             '179,180', '180,181', '180,180', '180,180',
             '179,180']           


#Spectrum extraction
for target in sciname:
    
    print 'Working on image:%s'%target
    
    index = sciname.index(target)
    #cubeStat   = imstat(target, region='circle[['+str(coordinates[index])+'], 0.5arcsec]')
    #x2extract  = cubeStat['maxpos'][0]
    #y2extract  = cubeStat['maxpos'][1]
    extractBox = "%s" % (sciname1[index])                    # copy the position to a string
    #print x2extract, y2extract
    cubeSpec   = imval(target, box = extractBox, stokes = 'I')
    #print sciname1[index]
    #print extractBox

    #Make sure vector and array arithmetic options are loaded
    cubeStat = imstat(target)
    cubeHead = imhead(target, mode="list")
    nSpec    = cubeStat['trc'][3] + 1                                # get the number of frequency channels. 
    f0       = float(cubeHead['crval4'])                             # reference freq in Hz
    df       = float(cubeHead['cdelt4'])                             # channel width in Hz
    i0       = cubeHead['crpix4']                                    # reference pixel
    freqSpec = (numpy.arange(nSpec) - i0)*df + f0


    plt.clf()                                                        # clear the plot (figure)
    flag = '%s' % str(target)
    plt.plot(freqSpec/1.e9, cubeSpec['data'], 'b-', label="%s.png" % flag) 
    plt.xlabel("Freq (GHz)")
    plt.ylabel("Flux Density (mJy/beam)")
    plt.legend()
    plt.grid()
    plt.savefig("%s.png" % flag)
    
    spectrum = numpy.vstack((freqSpec/1.e9, cubeSpec['data']))
    numpy.savetxt("%s.txt" % flag, numpy.transpose(spectrum))
    
os.system('mv *.png Monday_Jaquie/0.5arcsec/Spectra/')
os.system('mv *.txt Monday_Jaquie/0.5arcsec/Spectra_txt/')
