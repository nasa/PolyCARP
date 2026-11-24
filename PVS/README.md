PVS PolyCARP
==

[PVS version 8.1.3](https://github.com/SRI-CSL/PVS/releases/tag/pvs8.1.3) and [NASALib](https://github.com/nasa/pvslib) are required
to type-check and prove the PolyCARP development in PVS. Install NASALib as its README says.

## Checked versions

All 477 formulas are proved with these versions:

| Tool | Version |
|---|---|
| PVS | 8.1.3, the release of 2026-10-28 (tag [`pvs8.1.3`](https://github.com/SRI-CSL/PVS/releases/tag/pvs8.1.3), commit `50a70e713`) |
| NASALib | `master` at commit [`d70ebfc8`](https://github.com/nasa/pvslib/commit/d70ebfc8fcd562699aea4bcccbaf3d2c4d66796f) (2026-10-28) |

## Check the formalization

Run this command in the local directory `PVS`:

```
$ provethem --proveit-option 'add-path .' all-libraries
```

The option `add-path .` adds the directory `PVS` to the library path for this run. Thus the
libraries `PolyCARP_analysis` and `FM2019` find the library `PolyCARP`, and no other setting is
necessary. The file `all-libraries` lists the libraries in the order in which they are checked.

The output of that command should be

```
PolyCARP            Proving... [OK: 297 proofs]
PolyCARP_analysis   Proving... [OK: 131 proofs]
FM2019              Proving... [OK: 49 proofs]

*** Grand Totals: 477 proofs / 477 formulas. Missed: 0 formulas
*** Number of libraries: 3
```

On a MacBook with Apple silicon, the command took 12 minutes. The library `PolyCARP` takes the
longest, about 7 minutes.

To type-check without proving, add the option `-T`:

```
$ provethem -T --proveit-option 'add-path .' all-libraries
```

## Complete and incomplete proofs

The directory `summaries` holds the summary of each library from the run above. Every formula is
proved: no formula is `unfinished`, `untried` or `unchecked`. PVS lists each proved formula in one
of two ways:

- `proved - complete`: the proof succeeds, and every formula that the proof uses is also proved in
  this installation. These are the lemmas, TCCs and judgements that the proof uses, and the
  formulas that their proofs use, through the whole chain.
- `proved - incomplete`: the proof succeeds, but its chain contains a formula that is not proved in
  this installation, for example a NASALib lemma, TCC or judgement.

NASALib is fully proved, but its proofs take several hours, so the check above does not run them.
Thus `proved - incomplete` does not mean that a proof failed or is missing. After NASALib is proved
in the same installation, for example with its script `prove-all`, the check lists these formulas
as `proved - complete`.

## Use PolyCARP as a library in another development

To import PolyCARP in another PVS development, PVS must find the directory `PVS` of this repository
in the Unix environment variable `PVS_LIBRARY_PATH`, together with NASALib.

1. Clone this repository. In the commands below, replace `<polycarpdir>` with the absolute path of the
   local clone, and `<nasalibdir>` with the absolute path of the local directory where NASALib was
   cloned.

2. Add both directories to `PVS_LIBRARY_PATH`.

   In Bourne shell (bash or sh) or zsh:

   ~~~
   export PVS_LIBRARY_PATH="<nasalibdir>:<polycarpdir>/PVS:$PVS_LIBRARY_PATH"
   ~~~

   In C shell (csh or tcsh):

   ~~~
   setenv PVS_LIBRARY_PATH "<nasalibdir>:<polycarpdir>/PVS:$PVS_LIBRARY_PATH"
   ~~~

   If `PVS_LIBRARY_PATH` already contains NASALib, add only `<polycarpdir>/PVS`. To keep the setting,
   add the line to your shell startup file (for example `~/.bashrc`, `~/.zshrc` or `~/.cshrc`). Start
   PVS after you set the variable.

3. Import the theories with the library name as a prefix. To import all of PolyCARP, import its `top`
   theory:

   ~~~
   IMPORTING PolyCARP@top
   ~~~

   You can also import one theory, for example `IMPORTING PolyCARP@polygon_contain`. The libraries
   `PolyCARP_analysis` and `FM2019` are imported in the same way, for example
   `IMPORTING PolyCARP_analysis@top`.

4. Type-check your development once with the command `M-x typecheck` in PVS, or with
   `proveit -T <your theory file>`, to make sure that PVS finds PolyCARP.
