from ase.build import bulk
from koopmans.kpoints import Kpoints
from koopmans.workflows import SinglepointWorkflow

# Use ASE to create bulk silicon
atoms = bulk('Si')

# Create the workflow
workflow = SinglepointWorkflow(atoms = atoms,
        ecutwfc = 40.0,
        kpoints = Kpoints(grid=[8, 8, 8], path='LGXKG', cell=atoms.cell),
        calculator_parameters = {'pw': {'nbnd': 10}})

# Run the workflow
workflow.run()
