### SSMAP: Protein Contact Map Generator ###

**Description:** This project uses Python to generate a contact map for protein, which is color-coded based on its secondary structure. The map is then saved as a PNG image file. This is done using the BioPython library to parse PDB and DSSP files, numpy for mathematical operations, and matplotlib for visualization.

![Image](https://user-images.githubusercontent.com/26382402/255214871-2a430882-1989-4d99-800e-2def4ccafa57.png)

## Usage ##

1. Clone this repository to your local machine.
2. Ensure that the required Python libraries are installed: BioPython, numpy, and matplotlib. If they are not installed, use the following command:
`pip install biopython numpy matplotlib`

1. Place your PDB and DSSP files in the same directory as the script.
2. Update the 'pdb_file' and 'dssp_file' variables in the script to match the names of your PDB and DSSP files.
3. Run the script using Python.
`python contact_map_generator.py`
The contact map will be saved as a PNG image file in the same directory, with the name based on your PDB file name. 
## Resources ##

- [BioPython Documentation](https://biopython.org/wiki/Documentation)
- [Numpy Documentation](https://numpy.org/doc/)
- [Matplotlib Documentation](https://matplotlib.org/stable/users/index.html)

## Support ##

If you encounter any issues while using this script, please raise an issue in this GitHub repository.
