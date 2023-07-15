#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 15:26:43 2023

@author: ludovica
"""

"""
Created on Sat Jul 15 12:44:22 2023

@author: ludovica ais
"""

import numpy as np
import os

# specify the path of the folder
folder = ".../saltbridges"

# save the name of the files. NB: to avoid mistake the file name should be the aminoacid that are interacting amd their position in the chain
# example 'GLU34-LYS13'

names=['']
for nome_file in os.listdir(folder):
    if nome_file.endswith(".dat"):
        # apri il file in lettura
        with open(os.path.join(folder, nome_file), 'r') as file:
            names.append(os.path.splitext(nome_file)[0])
            
# analyze the distance between the aminoacids during time and gives 1 or 0 at at time t if their distance is < 5 Å.
# this is done for all the files and the outout is the array data which contains the time series of (0,1) of all the files
data= np.array([],int)
n=True
for nome_file in os.listdir(folder):
    if nome_file.endswith(".dat"):
        # apri il file in lettura
        with open(os.path.join(folder, nome_file), 'r') as file:
            time = []
            values = []
    # leggi il file riga per riga
            for riga in file:
                # rimuovi eventuali spazi iniziali e finali e dividi la riga in due colonne
                dati = riga.strip().split()
                time.append(int(dati[0]))
                if float(dati[1])<=5:
                    values.append(int(1))
                else:
                    values.append(int(0))
            if n==True:
                data=np.append(data, time)
                n=False
            data=np.column_stack((data, values))
           
# the final output is a file.txt with the first row containing the interacting aminoacids.
#From the second out in the first column there is the time and the others and (1,0) value for each bridge forming or not of the aminoacids in the files. 
array_finale = np.vstack([names, data])
np.savetxt('/saltbridtest.txt', array_finale, fmt='%15s', delimiter=' ')