#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 10:21:57 2020

@author: jason
"""

import pandas as pd

#set extents of data points, and distane between points (note than range finishes before max value)
xPos=range(-50,51,1)
yPos=range(-50,51,1)
zPos=range(50,51,1)

#create blank data frames for appending
coordList = pd.DataFrame(columns=['X', 'Y', 'Z'])
vectorList= pd.DataFrame(columns=['Vector'])


#set index counter to zero
dex=0

#iteratie throughx, y, and z coords
for x in xPos:
    print (x)

    for y in yPos:
            print(y)
            
            for z in zPos:
                #use .loc to fill in dataframe entries (keep this commented out for speed)
                #coordList.loc[dex, 'X']=x
                #coordList.loc[dex, 'Y']=y
                #coordList.loc[dex, 'Z']=z
                #coordList.loc[dex, 'Vector']=str('('+ x +' '+ y' '+ z + ')')
                vectorList.loc[dex, 'Vector']='(' + str(x) + ' ' + str(y) + ' ' + str(z) + ')'
                dex+=1

print(coordList)
print(vectorList)
coordList.to_csv('pointsOut.csv', index=False)
vectorList.to_csv('vectorsOut.csv', index=False)
    