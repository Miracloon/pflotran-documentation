Back to :ref:`card-index`

.. _dataset-card:

DATASET
=======
**THIS CARD IS BEING DEPRECIATED/PHASED-OUT. The new, experimental** 
**implementation can be found here:** :ref:`dataset-new-card`

Specifies a data set to be associated with parameters sets in the model.


Required Cards:
---------------
DATASET <optional string>
 Opens the DATASET block with the name of the data set in the string.  
 If the name is not provided, the NAME entry below must be included.

NAME <string>
 Name of the data set if not included with DATASET card.  
 **Note:** this string overwrites the name specified with the DATASET.

FILENAME <string>
 Name of the file containing data.

TYPE <string>
 Reserved for future application where the data set can be a single scalar or 
 vector value or a functional relationship.  The TYPE is currently fixed at 
 HETEROGENEOUS by default.  Other types report an unsupported error message.

REALIZATION_DEPENDENT
 A toggle card that will load the data set based on the realization ID.  
 For instance, if the data set is tied to PERMEABILITY within a 
 :ref:`material-property-card` and the realization ID is 99, PFLOTRAN searches 
 for an HDF5 data set labeled "PERMEABILITY99".  For POROSITY, it will search 
 for "POROSITY99".

Examples
--------
Reading heterogeneous permeability and porosity for the Hanford unit for 
realization ID = 99.  The name of the data sets within the HDF5 file are 
PERMEABILITY99 and POROSITY99, respectively.

 ::

  DATASET perm
    FILENAME hanford_unit.h5
    REALIZATION_DEPENDENT
  END

  DATASET poros
    FILENAME hanford_unit.h5
    REALIZATION_DEPENDENT
  END

  MATERIAL_PROPERTY hanford_unit
    ...
    POROSITY DATASET poros
    PERMEABILITY 
      ...
      DATASET perm
      ...
    /
    ...
  END
