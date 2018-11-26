Back to :ref:`card-index`

.. _initial-condition-card:

INITIAL_CONDITION
=================
This card links a particular :ref:`flow-condition-card` and 
:ref:`transport-condition-card` to the appropriate :ref:`region-card` to
define an initial condition. 
It is set up similar to the :ref:`boundary-condition-card` card, 
by first creating a list of flow and/or transport conditions, and then 
appling them to appropriate REGIONs using this card.

Required Cards:
---------------
INITIAL_CONDITION <name>
  Opens the INITIAL_CONDITION block, where <string> is the name of the 
  initial condition (name is optional).

FLOW_CONDITION <name>
  If a :ref:`flow-condition-card` has been defined, specify it here by the 
  given name of the flow condition.

TRANSPORT_CONDITION <name>
  If a :ref:`transport-condition-card` has been defined, specify it here by the 
  given name of the transport condition.
  
REGION <name>
 Specifies the name of the :ref:`region-card` that the set of flow and/or 
 transport conditions will be applied to.

Examples
--------

 ::

  INITIAL_CONDITION
    FLOW_CONDITION Piezometric_Surface
    TRANSPORT_CONDITION U_source
    REGION all
  /
  
  INITIAL_CONDITION
    FLOW_CONDITION initial
    REGION left_region
  /
  
  INITIAL_CONDITION soilA_layer_initial
    TRANSPORT_CONDITION initial
    REGION soilA_layer
  /