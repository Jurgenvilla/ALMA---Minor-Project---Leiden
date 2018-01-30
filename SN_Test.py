import numpy
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

    
A = imstat(sciname[0], mask = "'ALESS001.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[0])+'], 8.0arcsec]')
B = imstat(sciname[1], mask = "'ALESS002.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[1])+'], 8.0arcsec]')
C = imstat(sciname[2], mask = "'ALESS003.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[2])+'], 8.0arcsec]')
D = imstat(sciname[3], mask = "'ALESS005.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[3])+'], 8.0arcsec]')
E = imstat(sciname[4], mask = "'ALESS006.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[4])+'], 8.0arcsec]')
F = imstat(sciname[5], mask = "'ALESS007.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[5])+'], 8.0arcsec]')
G = imstat(sciname[6], mask = "'ALESS009.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[6])+'], 8.0arcsec]')
H = imstat(sciname[7], mask = "'ALESS010.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[7])+'], 8.0arcsec]')
I = imstat(sciname[8], mask = "'ALESS011.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[8])+'], 8.0arcsec]')
J = imstat(sciname[9], mask = "'ALESS013.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[9])+'], 8.0arcsec]')
K = imstat(sciname[10], mask = "'ALESS014.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[10])+'], 8.0arcsec]')
L = imstat(sciname[11], mask = "'ALESS015.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[11])+'], 8.0arcsec]')
M = imstat(sciname[12], mask = "'ALESS017.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[12])+'], 8.0arcsec]')
N = imstat(sciname[13], mask = "'ALESS018.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[13])+'], 8.0arcsec]')
O = imstat(sciname[14], mask = "'ALESS019.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[14])+'], 8.0arcsec]')
P = imstat(sciname[15], mask = "'ALESS022.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[15])+'], 8.0arcsec]')
Q = imstat(sciname[16], mask = "'ALESS023.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[16])+'], 8.0arcsec]')
R = imstat(sciname[17], mask = "'ALESS025.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[17])+'], 8.0arcsec]')
S = imstat(sciname[18], mask = "'ALESS029.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[18])+'], 8.0arcsec]')
T = imstat(sciname[19], mask = "'ALESS031.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[19])+'], 8.0arcsec]')
U = imstat(sciname[20], mask = "'ALESS035.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[20])+'], 8.0arcsec]')
V = imstat(sciname[21], mask = "'ALESS037.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[21])+'], 8.0arcsec]')
W = imstat(sciname[22], mask = "'ALESS039.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[22])+'], 8.0arcsec]')
X = imstat(sciname[23], mask = "'ALESS041.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[23])+'], 8.0arcsec]')
Y = imstat(sciname[24], mask = "'ALESS043.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[24])+'], 8.0arcsec]')
Z = imstat(sciname[25], mask = "'ALESS045.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[25])+'], 8.0arcsec]')
a = imstat(sciname[26], mask = "'ALESS049.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[26])+'], 8.0arcsec]')
b = imstat(sciname[27], mask = "'ALESS051.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[27])+'], 8.0arcsec]')
c = imstat(sciname[28], mask = "'ALESS055.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[28])+'], 8.0arcsec]')
d = imstat(sciname[29], mask = "'ALESS057.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[29])+'], 8.0arcsec]')
e = imstat(sciname[30], mask = "'ALESS059.2.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[30])+'], 8.0arcsec]')
f = imstat(sciname[31], mask = "'ALESS061.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[31])+'], 8.0arcsec]')
g = imstat(sciname[32], mask = "'ALESS063.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[32])+'], 8.0arcsec]')
h = imstat(sciname[33], mask = "'ALESS065.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[33])+'], 8.0arcsec]')
i = imstat(sciname[34], mask = "'ALESS066.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[34])+'], 8.0arcsec]')
j = imstat(sciname[35], mask = "'ALESS067.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[35])+'], 8.0arcsec]')
k = imstat(sciname[36], mask = "'ALESS068.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[36])+'], 8.0arcsec]')
l = imstat(sciname[37], mask = "'ALESS069.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[37])+'], 8.0arcsec]')
m = imstat(sciname[38], mask = "'ALESS070.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[38])+'], 8.0arcsec]')
n = imstat(sciname[39], mask = "'ALESS071.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[39])+'], 8.0arcsec]')
o = imstat(sciname[40], mask = "'ALESS072.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[40])+'], 8.0arcsec]')
p = imstat(sciname[41], mask = "'ALESS073.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[41])+'], 8.0arcsec]')
q = imstat(sciname[42], mask = "'ALESS074.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[42])+'], 8.0arcsec]')
r = imstat(sciname[43], mask = "'ALESS075.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[43])+'], 8.0arcsec]')
s = imstat(sciname[44], mask = "'ALESS076.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[44])+'], 8.0arcsec]')
t = imstat(sciname[45], mask = "'ALESS079.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[45])+'], 8.0arcsec]')
u = imstat(sciname[46], mask = "'ALESS080.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[46])+'], 8.0arcsec]')
v = imstat(sciname[47], mask = "'ALESS082.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[47])+'], 8.0arcsec]')
w = imstat(sciname[48], mask = "'ALESS083.4.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[48])+'], 8.0arcsec]')
x = imstat(sciname[49], mask = "'ALESS084.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[49])+'], 8.0arcsec]')
y = imstat(sciname[50], mask = "'ALESS087.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[50])+'], 8.0arcsec]')
z = imstat(sciname[51], mask = "'ALESS088.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[51])+'], 8.0arcsec]')
AA = imstat(sciname[52], mask = "'ALESS092.2.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[52])+'], 8.0arcsec]')
BB = imstat(sciname[53], mask = "'ALESS094.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[53])+'], 8.0arcsec]')
CC = imstat(sciname[54], mask = "'ALESS098.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[54])+'], 8.0arcsec]')
DD = imstat(sciname[55], mask = "'ALESS099.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[55])+'], 8.0arcsec]')
EE = imstat(sciname[56], mask = "'ALESS102.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[56])+'], 8.0arcsec]')
FF = imstat(sciname[57], mask = "'ALESS103.3.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[57])+'], 8.0arcsec]')
GG = imstat(sciname[58], mask = "'ALESS107.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[58])+'], 8.0arcsec]')
HH = imstat(sciname[59], mask = "'ALESS110.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[59])+'], 8.0arcsec]')
II = imstat(sciname[60], mask = "'ALESS112.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[60])+'], 8.0arcsec]')
JJ = imstat(sciname[61], mask = "'ALESS114.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[61])+'], 8.0arcsec]')
KK = imstat(sciname[62], mask = "'ALESS115.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[62])+'], 8.0arcsec]')
LL = imstat(sciname[63], mask = "'ALESS116.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[63])+'], 8.0arcsec]')
MM = imstat(sciname[64], mask = "'ALESS118.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[64])+'], 8.0arcsec]')
NN = imstat(sciname[65], mask = "'ALESS119.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[65])+'], 8.0arcsec]')
OO = imstat(sciname[66], mask = "'ALESS122.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[66])+'], 8.0arcsec]')
PP = imstat(sciname[67], mask = "'ALESS124.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[67])+'], 8.0arcsec]')
QQ = imstat(sciname[68], mask = "'ALESS126.1.NoPBCOR.mfs.image/'>0.00001", region='circle[['+str(coordinates[68])+'], 8.0arcsec]')

print  sciname[0], A['max'][0]/A['median'][0]
print  sciname[1], B['max'][0]/A['median'][0]
print  sciname[2], C['max'][0]/A['median'][0]
print  sciname[3], D['max'][0]/A['median'][0]
print  sciname[4], E['max'][0]/A['median'][0]
print  sciname[5], F['max'][0]/A['median'][0]
print  sciname[6], G['max'][0]/A['median'][0]
print  sciname[7], H['max'][0]/A['median'][0]
print  sciname[8], I['max'][0]/A['median'][0]
print  sciname[9], J['max'][0]/A['median'][0]
print  sciname[10], K['max'][0]/A['median'][0]
print  sciname[11], L['max'][0]/A['median'][0]
print  sciname[12], M['max'][0]/A['median'][0]
print  sciname[13], N['max'][0]/A['median'][0]
print  sciname[14], O['max'][0]/A['median'][0]
print  sciname[15], P['max'][0]/A['median'][0]
print  sciname[16], Q['max'][0]/A['median'][0]
print  sciname[17], R['max'][0]/A['median'][0]
print  sciname[18], S['max'][0]/A['median'][0]
print  sciname[19], T['max'][0]/A['median'][0]
print  sciname[20], U['max'][0]/A['median'][0]
print  sciname[21], V['max'][0]/A['median'][0]
print  sciname[22], W['max'][0]/A['median'][0]
print  sciname[23], X['max'][0]/A['median'][0]
print  sciname[24], Y['max'][0]/A['median'][0]
print  sciname[25], Z['max'][0]/A['median'][0]
print  sciname[26], a['max'][0]/A['median'][0]
print  sciname[27], b['max'][0]/A['median'][0]
print  sciname[28], c['max'][0]/A['median'][0]
print  sciname[29], d['max'][0]/A['median'][0]
print  sciname[30], e['max'][0]/A['median'][0]
print  sciname[31], f['max'][0]/A['median'][0]
print  sciname[32], g['max'][0]/A['median'][0]
print  sciname[33], h['max'][0]/A['median'][0]
print  sciname[34], i['max'][0]/A['median'][0]
print  sciname[35], j['max'][0]/A['median'][0]
print  sciname[36], k['max'][0]/A['median'][0]
print  sciname[37], l['max'][0]/A['median'][0]
print  sciname[38], m['max'][0]/A['median'][0]
print  sciname[39], n['max'][0]/A['median'][0]
print  sciname[40], o['max'][0]/A['median'][0]
print  sciname[41], p['max'][0]/A['median'][0]
print  sciname[42], q['max'][0]/A['median'][0]
print  sciname[43], r['max'][0]/A['median'][0]
print  sciname[44], s['max'][0]/A['median'][0]
print  sciname[45], t['max'][0]/A['median'][0]
print  sciname[46], u['max'][0]/A['median'][0]
print  sciname[47], v['max'][0]/A['median'][0]
print  sciname[48], w['max'][0]/A['median'][0]
print  sciname[49], x['max'][0]/A['median'][0]
print  sciname[50], y['max'][0]/A['median'][0]
print  sciname[51], z['max'][0]/A['median'][0]
print  sciname[52], AA['max'][0]/A['median'][0]
print  sciname[53], BB['max'][0]/A['median'][0]
print  sciname[54], CC['max'][0]/A['median'][0]
print  sciname[55], DD['max'][0]/A['median'][0]
print  sciname[56], EE['max'][0]/A['median'][0]
print  sciname[57], FF['max'][0]/A['median'][0]
print  sciname[58], GG['max'][0]/A['median'][0]
print  sciname[59], HH['max'][0]/A['median'][0]
print  sciname[60], II['max'][0]/A['median'][0]
print  sciname[61], JJ['max'][0]/A['median'][0]
print  sciname[62], KK['max'][0]/A['median'][0]
print  sciname[63], LL['max'][0]/A['median'][0]
print  sciname[64], MM['max'][0]/A['median'][0]
print  sciname[65], NN['max'][0]/A['median'][0]
print  sciname[66], OO['max'][0]/A['median'][0]
print  sciname[67], PP['max'][0]/A['median'][0]
print  sciname[68], QQ['max'][0]/A['median'][0]
