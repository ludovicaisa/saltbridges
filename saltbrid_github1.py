#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: ludovica aisa
"""

import numpy as np
import os

# specify the path of the folder
folder = ".../saltbridges"

# save the name of the files. NB: to avoid mistake the file name should be the aminoacids that are interacting and their position in the chain
# example 'GLU34-LYS13'
names=['']
for nome_file in os.listdir(folder):
    if nome_file.endswith(".dat"):
        # apri il file in lettura
        with open(os.path.join(folder, nome_file), 'r') as file:
            names.append(os.path.splitext(nome_file)[0])
            
# analyze the distance between the aminoacids during time and gives 1 or 0 at at time t if their distance is < 5 Å.
# this is done for all the data cointained in the files
#the outout is an array data which contains the time series of (0,1) for each file
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
           
# the final output is a file.txt with the first row containing the names of the aminoacids that form the salt bridge.
#From the second row: the first column represents the simulation time and the other columns are the time series for each bridge of two aminoacids data contained in the directory
# with (1,0) values: 1 the salt bridge is present, 0 the salt bridge is not present. 
array_finale = np.vstack([names, data])
np.savetxt('/saltbridtest.txt', array_finale, fmt='%15s', delimiter=' ')
