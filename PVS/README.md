PVS PolyCARP
==

[PVS version 8.0](http://pvs.csl.sri.com) and [NASALib](https://github.com/nasa/pvslib) are required
to type-check and prove the PolyCARP development in PVS.

To make NASALib available to PVS, include its absolute path to the Unix environment variable `PVS_LIBRARY_PATH`.
Depending upon your shell, one of the following commands must be run before trying to check the formalization.

In C shell (csh or tcsh), run the command below replacing `<nasalibdir>` with the absolute path to the local
directory where NASALib was cloned:

~~~
setenv PVS_LIBRARY_PATH "<nasalibdir>:$PVS_LIBRARY_PATH"
~~~

In Borne shell (bash or sh) or zsh, you can use:

~~~
export PVS_LIBRARY_PATH="<nasalibdir>:$PVS_LIBRARY_PATH"
~~~

Then, you can run the following command within the local directory `PVS` to check the formalization.

```
$ provethem 
```

The output of that command should be

```
PolyCARP                 [OK: 297 proofs]
PolyCARP_analysis        [OK: 131 proofs]
FM2019                   [OK: 49 proofs]

*** Grand Totals: 477 proofs / 477 formulas. Missed: 0 formulas.
*** Number of libraries: 3
```

To include PolyCARP in other PVS developments, the local directory
`PVS` has to be added to the Unix environment variable `PVS_LIBRARY_PATH` as well.

In C shell (csh or tcsh), run the command below replacing `<polycarppvsdir>` with the absolute path to the local
directory where this repository was cloned:

~~~
setenv PVS_LIBRARY_PATH "<polycarppvsdir>/PVS:$PVS_LIBRARY_PATH"
~~~

In Borne shell (bash or sh) os zsh, you can use:

~~~
export PVS_LIBRARY_PATH="<polycarpdir>/PVS:$PVS_LIBRARY_PATH"
~~~

