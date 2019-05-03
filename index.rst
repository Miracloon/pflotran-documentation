.. PFLOTRAN documentation master file, created by
   sphinx-quickstart on Thu Jul 14 07:37:39 2016.


**********************
PFLOTRAN Documentation
**********************
.. image:: /_static/pflotran_logo.jpg

PFLOTRAN is an open source, state-of-the-art massively parallel subsurface flow 
and reactive transport code. The code is developed under a GNU LGPL license 
allowing for third parties to interface proprietary software with the code, 
however any modifications to the code itself must be documented and remain open 
source. PFLOTRAN is written in object oriented, free formatted Fortran 2003. 
The choice of Fortran over C/C++ was based primarily on the need to enlist and 
preserve tight collaboration with experienced domain scientists, without which 
PFLOTRAN's sophisticated process models would not exist.

**The PFLOTRAN source code repository is on** `Bitbucket`_ **!** 

Need help beyond the documentation below? 
 | Search topics at or submit a question to the `pflotran-users`_ Google Group.
 | Email user questions to pflotran-users at googlegroups dot com
 | Email bug reports to pflotran-dev at googlegroups dot com

.. :download:`Click here <_build/latex/PFLOTRANdocumentation.pdf>` to 
   download a pdf version of the PFLOTRAN documentation. 

.. _Bitbucket: https://bitbucket.org/pflotran/pflotran/wiki/Home
.. _pflotran-users: https://groups.google.com/d/forum/pflotran-users

User's Guide
============

.. toctree::
   :maxdepth: 2
   
   /user_guide/how_to/introduction.rst
   /user_guide/how_to/installation/installation.rst
   /user_guide/how_to/running.rst
   /user_guide/how_to/creating_an_input_file.rst
   /user_guide/how_to/regression.rst
   /user_guide/how_to/visualization.rst
   /user_guide/how_to/benchmark.rst
   
.. The following are the hidden pages that are linked in the User's Guide:
.. toctree::
   :hidden:
   
   /user_guide/how_to/installation/linux.rst
   /user_guide/how_to/installation/mac.rst
   /user_guide/how_to/installation/windows_cygwin.rst
   /user_guide/how_to/installation/windows_visual_studio.rst
   /user_guide/how_to/installation/legacy_build.rst
   /user_guide/how_to/installation/machine_specific.rst
   /user_guide/how_to/installation/vm.rst
   /user_guide/how_to/installation/previous_petsc_releases.rst
   /user_guide/how_to/simple_flow_problem.rst
   /user_guide/how_to/running_fmdm.rst
   
.. _card-index:
   
Input Deck Cards
^^^^^^^^^^^^^^^^
   
Simulation Cards
----------------

.. toctree::
   :maxdepth: 1
   :glob:

   /user_guide/cards/simulation_cards/*
   
Process Model Cards
-------------------

.. toctree::
   :maxdepth: 1
   :glob:

   /user_guide/cards/process_model_cards/*
   
Chemistry Cards
---------------

.. toctree::
   :maxdepth: 1
   :glob:

   /user_guide/cards/chemistry_cards/*
 
Geomechanics Cards
------------------

.. toctree::
   :maxdepth: 1
   :glob:

   /user_guide/cards/geomechanics_cards/*
   
Utility Cards
-------------

.. toctree::
   :maxdepth: 1
   :glob:

   /user_guide/cards/utility_cards/*
   
.. The following are hidden pages that are linked in the Input Deck Cards:
.. toctree::
   :hidden:
   :glob:
   
   /user_guide/cards/pages/*
   /user_guide/cards/process_model_cards/grids/*

Theory Guide
============

.. toctree::
   :maxdepth: 2

   /theory_guide/tg_intro.rst
   /theory_guide/symbol_glossary.rst
   /theory_guide/mode_richards.rst
   /theory_guide/mode_th.rst
   /theory_guide/mode_general.rst
   /theory_guide/mode_mphase.rst
   /theory_guide/mode_immis.rst
   /theory_guide/mode_miscible.rst
   /theory_guide/mode_reactive_transport.rst
   /theory_guide/mode_geomechanics.rst
   /theory_guide/multiple_continuum.rst
   /theory_guide/appendixB.rst
   /theory_guide/reaction_sandbox.rst
   /theory_guide/appendixD.md
   /theory_guide/pm_waste_form.rst
   /theory_guide/pm_ufd_decay.rst
   /theory_guide/references.md
   
.. The following are the hidden pages that are linked in the Theory Guide:
.. toctree::
   :hidden:
   
   /theory_guide/wipp_source_sink.rst
   /theory_guide/wipp_waste_form.rst
   /theory_guide/wipp_soln_controls.rst

Developer's Guide
=================

.. toctree::
   :maxdepth: 2
   
   /developer_guide/software_productivity_sustainability.rst
   
QA Test Suite
=============

.. toctree::
   :maxdepth: 2
   
   /qa_tests/pc_sat_rel_perm.rst

..
   /qa_tests/intro_howto.rst
   /qa_tests/intro_thermal.rst
   /qa_tests/intro_flow.rst
   /qa_tests/intro_gas.rst
   /qa_tests/intro_transport.rst

..
  .. toctree::
     :hidden:
     
     include_toctree_thermal_steady.rst
     include_toctree_thermal_transient.rst
     include_toctree_flow_steady.rst
     include_toctree_flow_transient.rst
     include_toctree_gas_steady.rst
     include_toctree_transport_steady.rst
     include_toctree_transport_transient.rst

FAQ
===

.. toctree::
   :maxdepth: 2
   
   /user_guide/how_to/faq.rst
   
   
   
   
   
.. comment
   Indices and tables
   ==================
   * :ref:`genindex`
   * :ref:`modindex`
   * :ref:`search`

