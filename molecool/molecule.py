"""
Manipulates bonds
"""

from .measure import calculate_distance

def build_bond_list(coordinates, max_bond=1.5, min_bond=0):
    """Calculate bonds in a meolcule based on a distance criteria.

    The pairwise distance between atoms is computed. If it is in the range
    'min_bond' to 'max_bond', the atoms are counted as bonded.

    Parameters
    ----------
    coordinates : np.ndarray
        The coordinates of the atoms.
    max_bond: float (optional)
        The maximum distance for two atoms to be considered bonded. The default is 1.5.
    min_bond: float (optional)
        The minimum distance for two points to be condisered bonded. The default is 0.0


    Returns
    -------
    bonds : dict
        A dictionary where the keys are tuples of the bonded atom indices, and the associated
        values are the bond lengths.


    """

    if min_bond < 0:
       raise ValueError(F"{min_bond} entered for minimum bond length. Minimum bond length cannot be less than zero!")

    # Find the bonds in a molecule (set of coordinates) based on distance criteria.
    bonds = {}
    num_atoms = len(coordinates)

    for atom1 in range(num_atoms):
        for atom2 in range(atom1, num_atoms):
            distance = calculate_distance(coordinates[atom1], coordinates[atom2])
            if distance > min_bond and distance < max_bond:
                bonds[(atom1, atom2)] = distance

    return bonds
