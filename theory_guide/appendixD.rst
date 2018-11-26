Python Tools
============

Extracting Aqueous Secondary Species, Minerals and Gases from a Thermodynamic Database
--------------------------------------------------------------------------------------

A python script is available to help the user extract secondary species,
gases and minerals from the thermodynamic database for a given set of
primary species. Surface complexation reactions are not included. The
python script can be found in ``./tools/contrib/sec_species/rxn.py`` in
the PFLOTRAN Git repository. The current implementation is based
on the ``hanford.dat`` database. Input files are ``aq_sec.dat``,
``gases.dat`` and ``minerals.dat``. In addition, for each of these files
there is a corresponding file containing a list of species to be
skipped: ``aq_skip.dat``, ``gas_skip.dat`` and ``min.dat``. Before
running the script it is advisable to copy the entire directory
``sec_species`` to the local hard drive to avoid conflicts when updating
the PFLOTRAN repository. To run the script simply type in a terminal
window:

``python rxn.py``

The user has to edit the ``rxn.py`` file to set the list of primary
species. For example,

``pri=[’Fe++’,’Fe+++’,’H+’,’H2O’]``

Note that the species H2O must be include in the list of primary
species. Output appears on the screen and also in the file ``chem.out``,
a listing of which appears below. The number of primary and secondary
species, gases and minerals is printed out at the end of the
``chem.out`` file.

``chem.out``

::

    PRIMARY_SPECIES
    Fe++
    Fe+++
    H+
    H2O
    /
    SECONDARY_SPECIES
    O2(aq)
    H2(aq)
    Fe(OH)2(aq)
    Fe(OH)2+
    Fe(OH)3(aq)
    Fe(OH)3-
    Fe(OH)4-
    Fe(OH)4--
    Fe2(OH)2++++
    Fe3(OH)4(5+)
    FeOH+
    FeOH++
    HO2-
    OH-
    /
    GASES
    H2(g)
    H2O(g)
    O2(g)
    /
    MINERALS
    Fe
    Fe(OH)2
    Fe(OH)3
    FeO
    Ferrihydrite
    Goethite
    Hematite
    Magnetite
    Wustite
    /
    ================================================
    npri =  4  nsec =  14  ngas =  3  nmin =  9

    Finished!
