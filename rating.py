#This program calculates the maximum allowed loading factor giving a existing load and ambient temp profiles.

import numpy as np
import pandas as pd
import math

TOR = 65
R = 3.34375
n = 0.8
TAO = 8.659052158
TAOW = 59
HR = 1.98835

best = pd.read_csv('best.csv')
best = best['min'].tolist()
##Amb = best[0:24]
#mid = pd.read_excel('mid.xlsx')
#mid = mid['mid'].tolist()
#worst = pd.read_excel('worst.xlsx')
#worst = worst['max'].tolist()
#actual = pd.read_excel('actual.xlsx')
#actual = actual['actual'].tolist()
tr = pd.read_excel('TRs.xlsx')
tr1 = tr['6.4TR'].tolist()

def maxload(Load,Amb):
    a = 0.5
    AgingF = 0
    while AgingF<=1:
        Loada = np.array(Load)*a       #scaled load by factor a
        Loada = Loada.tolist()
        Factor = []
        UTOL = []
        UHSL = []
        TOL = []
        HSL = []
        TOi = 0
        Hi = 0
        for i in range (0,24):
            UTO = TOR*((Loada[i]**2*R+1)/(R+1))**n
            UTOL.append(UTO)
            UHS = HR*Loada[i]**(2*n)
            UHSL.append(UHS)
        for i in range (0,20):
            for j in range (0,24):
                TO = (UTOL[j]-TOi)*(1-math.exp(-1/TAO))+TOi
                TOL.append(TO)
                TOi = TOL[-1]
                HS = (UHSL[j]-Hi)*(1-math.exp(-60/TAOW))+Hi
                HSL.append(HS)
                Hi = HSL[-1]
            i= i+1
        TOL = TOL[-24:]
        HSL = HSL[-24:]
        for i in range (0,24):
            HSE = Amb[i]+TOL[i]+HSL[i]
            AF = math.exp((15000/383)-(15000/(HSE+273)))
            Factor.append(AF)   
        AgingF = np.mean(Factor)
        a = a+0.02
        maxload = max(Load)*(a-0.04) #revert to original value before exceeding limit
    print(max(Load),a)
    return maxload

loadmax = []
for i in range (0,365):
    Amb = best[i*24:i*24+24]
    Load = tr1[i*24:i*24+24]
    mload = max(Load)
    Load = np.array(Load)/mload  # normalize the actual loading profile to a 1.0 p.u. profile
    Load = Load.tolist()
    lmax = maxload(Load,Amb)
    loadmax.append(lmax)
