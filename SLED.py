import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

#Values from Gaby,  Huynh and my data
CO_122     = [0.64, 3.991, 3.34]
CO_122_err = [0.07, 0.750, 0.41]
CO_122_Q   = [1.0, 3.0, 4.0]

#Values from Rangwalaet al, 2011 and Kazimierz et al, 2015
Arp220     = [410, 1549, 3168, 4550, 3660, 4070, 3460, 3260, 2920, 1280, 840, 450]
Arp220_err = [41, 311, 634, 330, 170, 80, 170, 200, 270, 90, 60, 100]
Arp220_Q   = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13]

#Values from Riechers et al, 2013
#HFLS3     = [0.074, 0.315, 0.717, 2.74, 2.90, 2.77]
#HFLS3_err = [0.024, 0.028, 0.094, 0.68, 0.77, 0.45]
#HFLS3_Q   = [1, 2, 3, 6, 7, 9]

#Values from Carilli eta l. 2010 for GN20
GN20     = [0.21, 0.64, 1.5, 2.2, 1.8]
GN20_err = [0.05, 0.16, 0.2, 0.7, 0.2]
GN20_Q   = [1, 2, 4, 5, 6]

#Normalization CO(1-0)
Normalization_1 = CO_122[0]/Arp220[0]
Arp220          = np.multiply(Arp220, Normalization_1)
Arp220_err      = np.multiply(Arp220_err, Normalization_1)
#Arp220_err    = np.multiply(Arp220_err, Normalization) #Not sure about re'scaling the uncertainties

#Normalization_2 = CO_122[0]/HFLS3[0]
#HFLS3           = np.multiply(HFLS3, Normalization_2)

Normalization_3 = CO_122[0]/GN20[0]
GN20            = np.multiply(GN20, Normalization_3)
GN20_err        = np.multiply(GN20_err, Normalization_3)

#RADEX
#Test            = [1, 2, 3, 7]
#Temperature     = [1.774e-2, 6.803e-2, 1.412e-1, 1.524E-01]
#Integrated      = np.multiply(Temperature, 1.0645*621.0)
#Normalization_3 = CO_122[0]/Integrated[0]
#Final           = np.multiply(Integrated, Normalization_3)
#F               = interp1d(Arp220_Q, Arp220, kind='cubic')
#X               = np.linspace(1, 13, num = 50)

#plt.errorbar(Arp220_Q, Arp220, yerr = Arp220_err, fmt = 'o', label = 'Arp 220', markersize = 4.5)
plt.errorbar(Arp220_Q, Arp220, yerr = Arp220_err, fmt = 'o', label = 'Arp 220', markersize = 6, color = 'y')
#plt.errorbar(HFLS3_Q, HFLS3, fmt = 'o', label = 'HFLS3', markersize = 6)
plt.errorbar(GN20_Q, GN20, yerr = GN20_err, fmt = 'o', label = 'GN20', markersize = 6, color = 'r')
#plt.errorbar(X, F(X), fmt = '-')
plt.errorbar(CO_122_Q, CO_122, yerr = CO_122_err, fmt = 'o', label = 'ALESS122.1', markersize = 6, color = 'k')
plt.legend(frameon = False)
plt.xlim(0,13.5)
plt.ylim(0, 8)
plt.xlabel(r"$\mathrm{Quantum\ Number}\ \mathrm{J}_{\mathrm{upper}}$", fontsize = 18)
plt.ylabel(r"$\mathrm{I}_{\mathrm{CO}}\ [\mathrm{Jy\ km}\ \mathrm{s}^{-1}]$", fontsize = 18)
plt.grid()
#plt.show()
plt.savefig("SLED122_new.png")

