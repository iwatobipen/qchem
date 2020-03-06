# qchem
This script generates psi4 input file from SMILES strings


## Usage
$python psi4inpgen.py "SMILES strings"

```
$python psi4inpgen.py -h
positional arguments:
  smi              SMILES strings of inputmolecule

optional arguments:
  -h, --help       show this help message and exit
  --basis BASIS    BASIS SETS : default sto-3g
  --method METHOD  DFT method : default hf
  --output OUTPUT  outputfile name : input

```

After running the script, input.in file is generated.
Then pass the file to geomeTRIC
```
$geometric-optimize --psi4 input.in
```


## Requirements

- openbabel
- pybel (python wrapper of openbabel)
- geomeTRIC
- jinja2
