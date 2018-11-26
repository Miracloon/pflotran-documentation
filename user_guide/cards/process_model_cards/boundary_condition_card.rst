Back to :ref:`card-index`

.. _boundary-condition-card:

BOUNDARY_CONDITION
==================
This card links a particular :ref:`flow-condition-card` and 
:ref:`transport-condition-card` to the appropriate :ref:`region-card` to
define a boundary condition. 
It is set up similar to the :ref:`initial-condition-card` card, 
by first creating a list of flow and/or transport conditions, and then 
appling them to appropriate REGIONs using this card.

Required Cards:
---------------
BOUNDARY_CONDITION <name>
  Opens the BOUNDARY_CONDITION block, where <string> is the name of the 
  boundary condition (name is optional).

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

  BOUNDARY_CONDITION
    FLOW_CONDITION left_face
    REGION left_face
  /

  BOUNDARY_CONDITION recharge
    FLOW_CONDITION recharge
    TRANSPORT_CONDITION tracer_recharge
    REGION Top
  /