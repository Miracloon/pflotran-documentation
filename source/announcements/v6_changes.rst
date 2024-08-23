.. _v5-changes:

Changes in PFLOTRAN 6.0
-----------------------
The following has changed in PFLOTRAN 6.0:

 * PETSc release updated to 3.21

 * Fixed bug when using relative paths to files

 * Added buffer erosion and copper corrosion model waste form process model

 * Fixed bug in mineral tst rate expression affinity factor derivative

 * Added tightly coupled well model for sco2 and hydrate

 * Added analytical waste form mechanism

 * Added error message in ufd decay when a material is not found for the kd values

 * Added exponential freezing curve in hydrate mode

 * Added temperature dependence to Lambda reaction sandbox

 * Added the ability to output cell IDs (local, ghosted, petsc, natural) for debugging purposes

 * Added the option to read well model constraints from FLOW_CONDITIONS

 * Added an error message when SUBSURFACE_TRANSPORT is specified in the SIMULATION block but a CHEMISTRY block does not exist.

 * Deprecated -stochastic command line argument in favor of -multi_realization

 * Added heterogeneous Waxman-Smits clay conductivity for ERT process model

 * Added sco2 as a component in HYDRATE mode

 * Fixed mass balance file headers for GENERAL mode 

 * Added CI scripting to catch trailing spaces in source files

 * Added heterogeneous Archie parameters to material property

 * Added error messaging to ensure that ERT electrodes are mapped to a cell

 * Improved DBASE error messaging when a parameter is not found in the database

 * Added screen output of number of grid cells, min/max grid cells per process, and number of active and inactive cells

 * Added wedge and pyramid shape function for geomechanics

 * Added pressure-regulated source term in source/sink sandbox

 * Added SCO2 (supercritical CO2) process model

 * Eliminated the printing of min/max/mean in gold files for regression tests with one cell

 * Added the ability to print REGIONs to HDF5 files for debugging conceptual models

 * Added 'atm' as a pressure unit

 * Refactored geomechanics tet shape function

 * Added error messaging when a CHARACTERISTIC_CURVE is used without a flow mode

 * Refactored ERT to use a mixture of two solution concentrations when calculating bulk conductivity (e.g., differing ionic strengths)

 * Implemented stress/strain linkage between geomechanics and ERT

 * Expanded EOS IF97 density/enthalpy to "region 3"

 * Added the ability to run transport with solely immobile species

 * Added the parameter process model

 * Refactored the source/sink sandbox to use REGIONs instead of coordinates and cell IDs

 * Added heterogeneous surface electrical conductivity for ERT

 * Added anisotropic tortuosity

 * Added error messaging when tracer is factored into ERT electrical conductivity but no tracer transport is simulated

 * Refactored kinetic reaction inhibition and added SMOOTHSTEP as an option
