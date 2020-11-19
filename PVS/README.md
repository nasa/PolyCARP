PVS PolyCARP
==

[PVS version 7.1](http://pvs.csl.sri.com) and the development version
of the [NASA PVS Library](https://github.com/nasa/pvslib) are required
to type-check and prove the PolyCARP development in PVS. Type the following
command in a Unix shell within the local directory `PVS`.

```
$ provethem --addpath 
```

The output of that command is

```
PolyCARP                 [OK: 294 proofs]
PolyCARP_analysis        [OK: 131 proofs]
FM2019                   [OK: 49 proofs]

*** Grand Totals: 474 proofs / 474 formulas. Missed: 0 formulas.
*** Number of libraries: 3
```

 To include PolyCARP in other PVS developments, the local directory
`PVS` has to be added to the Unix environment variable
`PVS_LIBRARY_PATH`.  Depending upon your shell, one of the following lines
has to be added to your startup script.  In C shell (csh or tcsh), put this line in
`~/.cshrc`, where `<polycarppvsdir>` is the absolute path to the local
directory `PVS` in the PolyCARP distribution:

~~~
setenv PVS_LIBRARY_PATH "<polycarppvsdir>:$PVS_LIBRARY_PATH"
~~~

In Borne shell (bash or sh), put this line in either `~/.bashrc or ~/.profile`:

~~~
export PVS_LIBRARY_PATH="<polycarppvsdir>/nasalib:$PVS_LIBRARY_PATH"
~~~

