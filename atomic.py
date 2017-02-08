MASS = {
    "H": 1.00794,
    "He": 4.002602,
    "Li": 6.941,
    "Be": 9.012182,
    "B": 10.811,
    "C": 12.0107,
    "N": 14.0067,
    "O": 15.9994,
    "F": 18.9984032,
    "Ne": 20.1797,
    "Na": 22.98976928,
    "Mg": 24.3050,
    "Al": 26.9815386,
    "Si": 28.0855,
    "P": 30.973762,
    "S": 32.065,
    "Cl": 35.453,
    "Ar": 39.948,
    "K": 39.0983,
    "Ca": 40.078,
    "Sc": 44.955912,
    "Ti": 47.867,
    "V": 50.9415,
    "Cr": 51.9961,
    "Mn": 54.938045,
    "Fe": 55.845,
    "Co": 58.933195,
    "Ni": 58.6934,
    "Cu": 63.546,
    "Zn": 65.38,
    "Ga": 69.723,
    "Ge": 72.64,
    "As": 74.92160,
    "Se": 78.96,
    "Br": 79.904,
    "Kr": 83.798,
    "Rb": 85.4678,
    "Sr": 87.62,
    "Y": 88.90585,
    "Zr": 91.224,
    "Nb": 92.90638,
    "Mo": 95.96,
    "Tc": 98,
    "Ru": 101.07,
    "Rh": 102.90550,
    "Pd": 106.42,
    "Ag": 107.8682,
    "Cd": 112.411,
    "In": 114.818,
    "Sn": 118.710,
    "Sb": 121.760,
    "Te": 127.60,
    "I": 126.90447,
    "Xe": 131.293,
    "Cs": 132.9054519,
    "Ba": 137.327,
    "La": 138.90547,
    "Ce": 140.116,
    "Pr": 140.90765,
    "Nd": 144.242,
    "Pm": 145,
    "Sm": 150.36,
    "Eu": 151.964,
    "Gd": 157.25,
    "Tb": 158.92535,
    "Dy": 162.500,
    "Ho": 164.93032,
    "Er": 167.259,
    "Tm": 168.93421,
    "Yb": 173.054,
    "Lu": 174.9668,
    "Hf": 178.49,
    "Ta": 180.94788,
    "W": 183.84,
    "Re": 186.207,
    "Os": 190.23,
    "Ir": 192.217,
    "Pt": 195.084,
    "Au": 196.966569,
    "Hg": 200.59,
    "Tl": 204.3833,
    "Pb": 207.2,
    "Bi": 208.98040,
    "Po": 209,
    "At": 210,
    "Rn": 222,
    "Fr": 223,
    "Ra": 226,
    "Ac": 227,
    "Th": 232.03806,
    "Pa": 231.03588,
    "U": 238.02891,
    "Np": 237,
    "Pu": 244,
    "Am": 243,
    "Cm": 247,
    "Bk": 247,
    "Cf": 251,
    "Es": 252,
    "Fm": 257,
    "Md": 258,
    "No": 259,
    "Lr": 262,
    "Rf": 265,
    "Db": 268,
    "Sg": 271,
    "Bh": 272,
    "Hs": 270,
    "Mt": 276,
    "Ds": 281,
    "Rg": 280,
    "Cn": 285,
    "Uut": 284,
    "Uuq": 289,
    "Uup": 288,
    "Uuh": 293,
    "Uuo": 294}

# If this is a nice list we can just .index or [slice] to get atomic numbers
ATOMIC_NUMBER = [
    "ZERO", "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg",
    "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn",
    "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb",
    "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In",
    "Sn", "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm",
    "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta",
    "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At",
    "Rn", "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk",
    "Cf", "Es", "Fm", "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt",
    "Ds", "Rg", "Cn", "Uut", "Uuq", "Uup", "Uuh", "Uuo"]


COVALENT_RADII = {
    # Covalent radii revisited -- DOI:10.1039/B801115J
    "H": 0.25, ## 0.31 !! temporary for methyl
    "He": 0.28,
    "Li": 1.28,
    "Be": 0.96,
    "B": 0.84,
    "C": 0.76,  # for sp3; sp2 = 0.73; sp = 0.69
    "C_1": 0.69,
    "C_2": 0.73,
    "C_R": 0.73,
    "C_3": 0.76,
    "N": 0.71,
    "O": 0.3, ## 0.66 !! temporary for ZIFs
    "F": 0.57,
    "Ne": 0.58,
    "Na": 1.66,
    "Mg": 1.41,
    "Al": 1.21,
    "Si": 1.11,
    "P": 1.07,
    "S": 1.05,
    "Cl": 1.02, ## 0.31 used for ZIFs !! temporary for ZIFs, 1.02 is correct
    "Ar": 1.06,
    "K": 2.03,
    "Ca": 1.76,
    "Sc": 1.7,
    "Ti": 1.6,
    "V": 1.53,
    "Cr": 1.39,
    "Mn": 1.61,  # low spin = 1.39
    "Fe": 1.52,  # low spin = 1.32
    "Co": 1.5,  # low spin = 1.26
    "Ni": 1.24,
    "Cu": 1.32,
    "Zn": 1.22,
    "Ga": 1.22,
    "Ge": 1.2,
    "As": 1.19,
    "Se": 1.2,
    "Br": 1.2,
    "Kr": 1.16,
    "Rb": 2.2,
    "Sr": 1.95,
    "Y": 1.9,
    "Zr": 1.5,  # 1.75  !! temporarily added to correct the UIO cluster bonding problem 
    "Nb": 1.64,
    "Mo": 1.54,
    "Tc": 1.47,
    "Ru": 1.46,
    "Rh": 1.42,
    "Pd": 1.39,
    "Ag": 1.45,
    "Cd": 1.44,
    "In": 1.42,
    "Sn": 1.39,
    "Sb": 1.39,
    "Te": 1.38,
    "I": 1.39,
    "Xe": 1.4,
    "Cs": 2.44,
    "Ba": 2.15,
    "La": 2.07,
    "Ce": 2.04,
    "Pr": 2.03,
    "Nd": 2.01,
    "Pm": 1.99,
    "Sm": 1.98,
    "Eu": 1.98,
    "Gd": 1.96,
    "Tb": 1.94,
    "Dy": 1.92,
    "Ho": 1.92,
    "Er": 1.89,
    "Tm": 1.9,
    "Yb": 1.87,
    "Lu": 1.87,
    "Hf": 1.75,
    "Ta": 1.7,
    "W": 1.62,
    "Re": 1.51,
    "Os": 1.44,
    "Ir": 1.41,
    "Pt": 1.36,
    "Au": 1.36,
    "Hg": 1.32,
    "Tl": 1.45,
    "Pb": 1.46,
    "Bi": 1.48,
    "Po": 1.4,
    "At": 1.5,
    "Rn": 1.5,
    "Fr": 2.6,
    "Ra": 2.21,
    "Ac": 2.15,
    "Th": 2.06,
    "Pa": 2,
    "U": 1.96,
    "Np": 1.9,
    "Pu": 1.87,
    "Am": 1.8,
    "Cm": 1.69,
}
METALS = [3, 4, 11, 12, 13, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
          37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 55, 56, 57,
          58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74,
          75, 76, 77, 78, 79, 80, 81, 82, 83, 87, 88, 89, 90, 91, 92, 93, 94,
          95, 96, 97, 98, 99, 100, 101, 102, 103]
