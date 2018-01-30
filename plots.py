basename = ['uid___A002_Xae4720_X55dd.ms.split.cal', 
            'uid___A002_Xae4720_X5c8.ms.split.cal', 
            'uid___A002_Xae4720_X766.ms.split.cal',
            'uid___A002_Xae6c13_X230c.ms.split.cal',
            'uid___A002_Xae6c13_X2481.ms.split.cal']

#Plot Antennas
for name in basename:
        plotants(vis=basename[name], figfile=basaname[name]+'_plotants.png')

#Plot Channel vs Amp
'''this is done to check if we need to 
flag some data in the edges or somewhere 
else because they could have abnormal high amplitudes'''
#plotms(vis=basename[name], xaxis='channel', yaxis='amp', averagedata=T, avgbaseline=T, avgtime='1e8', avgscan=T)
             
#Plot Amp vs Time
'''To check outlying points''' 
#for name in basename:
    #plotms(vis=basename[name], xaxis='time', yaxis='amp', averagedata=T, avgchannel='128', coloraxis='field', iteraxis='spw')
    
#Plot UVdist vs Amp
'''To check flux calibrator and see which
points need to be flagged'''
#plotms(vis=basename[0], xaxis='uvdist', yaxis='amp', field='ALESS001.1', averagedata=T, avgchannel='128', avgtime='1e8', coloraxis='scan')  
#plotms(vis=basename[0], xaxis='uvdist', yaxis='amp', averagedata=T, avgchannel='128', avgtime='1e8', coloraxis='scan', iteraxis='field')
