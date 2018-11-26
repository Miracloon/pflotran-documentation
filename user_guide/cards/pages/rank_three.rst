Back to :ref:`card-index`

.. _rank-three:

Rank Three Array Specification
==============================
A rank three array constitutes a dataset with three values per time.  
Time must be specified in units and the scalar quantity must be in the units 
of the outer keyword. If TIME_UNITS and/or DATA_UNITS are not specified, SI 
is assumed.

Example
-------
 ::

  # Rank 3 Dataset: Specifies a transient gradient (dz_dx dz_dy dz_dz).
  TIME_UNITS hr
  # <time> <value> <value> <value>
  0.   4.56201E-05   2.50048E-05  0
  1.   4.6121E-05    2.97169E-05  0
  2.   5.55565E-05   3.14973E-05  0
  3.   6.97382E-05   3.06611E-05  0
  4.   8.53995E-05   2.8501E-05   0
  5.   9.94357E-05   2.49889E-05  0
  6.   0.00010842    2.09844E-05  0
  7.   0.000107846   1.68592E-05  0
  8.   9.43216E-05   1.7522E-05   0
  9.   7.70243E-05   1.76242E-05  0
  10.  5.28262E-05   2.02786E-05  0


  # Rank 3 Dataset: Specifies a transient datum.
  TIME_UNITS hr
  DATA_UNITS m
  # <time> <value> <value> <value>
  0    89.0467313   42.92071714   104.7889681
  1    89.0467313   42.92071714   104.788535
  2    89.0467313   42.92071714   104.7902681
  3    89.0467313   42.92071714   104.7931686
  4    89.0467313   42.92071714   104.796484
  5    89.0467313   42.92071714   104.7996226
  6    89.0467313   42.92071714   104.8018588
  7    89.0467313   42.92071714   104.8021498
  8    89.0467313   42.92071714   104.8017141
  9    89.0467313   42.92071714   104.799842
  10   89.0467313   42.92071714   104.7966171