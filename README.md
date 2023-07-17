# Saltbridges time series for protein simulation dynamics
analyzing the saltbridges obtained by simulation and though a binary time series: 1 states for when the bridge is present and 0 when is not, at time t of the simulation. The threshold of the distance between the two aminoacids defining (0,1) is 5Å.
It analyzes the files that contains information about the distance between two aminoacids over time, extracted from the salt bridges formations during the simulation.


## Requirements

- Python 3.x
- NumPy

## Instructions

- 1. Make sure your data for each bridge analyzed is in a file.dat (see GLU34-LYS13.dat as an example) and that the file name correspond to the name of the two aminoacids that are interacting.
- 2. The files need to be in the same directory that here is called 'saltbridges' specified in 'folder'. 
You should put your file in a new directory called saltbridges or change the variable 'folder' with the name of directory where your files are. 
- 3.  Run the script with the command 
  python saltbridtest.py
  or copy the script (make sure about the path of the directory where your files are)
- 4. The output file is a file.txt called saltbridtest.txt

## Data File Format

- The data files should have the `.dat` extension.
- Make sure that all the salt bridge data files in `.dat` format are present in the same folder as the `saltbridtest.py` file.

## Contributions

Contributions are welcome! If you would like to make improvements or fix issues in the code, you can fork the repository, make the changes in your branch, and submit a pull request.
If you use this script please cite it. Thank you & enjoy it!

