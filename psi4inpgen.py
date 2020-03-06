import pybel
from jinja2 import Template
from argparse import ArgumentParser

tmpl = Template("""molecule {
{{FC}} {{MP}}
{{XYZ}}
}

set basis {{BASIS}}

gradient('{{METHOD}}')


""")

def getArgs():
    parser = ArgumentParser()
    parser.add_argument("smi", type=str, help="SMILES strings of inputmolecule")
    parser.add_argument("--basis", type=str, help='BASIS SETS', default="sto-3g")
    parser.add_argument("--method", type=str, help="DFT method", default="hf")
    parser.add_argument("--output", type=str, help="outputfile name", default="input")
    return parser

if __name__=="__main__":

    parser = getArgs()
    args = parser.parse_args()
    obmol = pybel.readstring("smi", args.smi)
    obmol.make3D()
    xyz = obmol.write('xyz').split("\n")[2:]

    xyz = "\n".join(xyz)
    output = tmpl.render(FC=obmol.charge,
                         MP=obmol.spin,
                         XYZ=xyz,
                         BASIS=args.basis,
                         METHOD=args.method)
    with open(f"{args.output}.in", "w") as f:
        for line in output:
            f.write(line)



