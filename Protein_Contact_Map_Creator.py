#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
from Bio.PDB import *
from Bio.PDB.DSSP import DSSP
import os

# Load the PDB file
pdb_file = "4afb.pdb"  
pdb_id = PDBParser().get_structure('X', pdb_file)

# Load the DSSP file
dssp_file = "4afb.dssp"  
model = pdb_id[0]
dssp = DSSP(model, dssp_file)

# Initialize the contact map
residues = [res for res in model.get_residues() if res.get_id()[0] == ' ' and 'CA' in res]
n_residues = len(residues)
contact_map = np.zeros((n_residues, n_residues), dtype=int)

# Fill the contact map
for i, res1 in enumerate(residues):
    for j, res2 in enumerate(residues):
        diff = res1['CA'].coord - res2['CA'].coord
        dist = np.sqrt(np.sum(diff * diff))
        if dist < 8.0:  # 8.0 is a commonly used distance cutoff for contact maps
            contact_map[i, j] = 1

# Color the contact map based on the secondary structure
for i, res1 in enumerate(residues):
    for j, res2 in enumerate(residues):
        if contact_map[i, j] == 1:
            key = (res1.get_parent().get_id(), res1.get_id())
            if key in dssp:
                ss, phi, psi = dssp[key][2:5]
                if ss == 'H':  # alpha helix
                    contact_map[i, j] = 2
                elif ss == 'E':  # beta sheet
                    if psi < 0:  # anti-parallel
                        contact_map[i, j] = 3
                    else:  # parallel
                        contact_map[i, j] = 4

# Plot the contact map
plt.imshow(contact_map, cmap='gnuplot', interpolation='none', vmin=0, vmax=4, origin='lower')

# Add labels to the axes
plt.xlabel('Residue Position')
plt.ylabel('Residue Position')

# Add a color bar as a legend
cbar = plt.colorbar(ticks=[0, 1, 2, 3, 4])
cbar.set_label('Secondary Structure')
cbar.set_ticklabels(['No contact', 'Original structure', 'Alpha helix', 'Anti-parallel beta sheet', 'Parallel beta sheet'])

# Save the plot as a .png image
base_name = os.path.basename(pdb_file).split('.')[0]  # extract the base name from the pdb file path
plt.savefig(f"{base_name}_contact_map.png")




