
'llvm-prove.py test.ll'

A simple helper script to use LLVM's optimizer as a prover.  LLVM makes a very bad general prover, but can often be moderately effective on proof examples extracted from programs.  The language of the proof to attempt is a single LLVM IR function returning i1 (boolean) which is the condition attempting to be proven.  

To use, you must have defined LLVM_BASE_DIR pointing at a *build* (not install) directory of an LLVM build.  You will also need to run the tool from the checkout directory since some of the paths are relative.
