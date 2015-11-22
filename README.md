llvm-prove is simple helper script to use LLVM's optimizer as a prover.  LLVM makes a very bad general prover, but can often be moderately effective on proof examples extracted from programs.  The language of the proof to attempt is a single LLVM IR function returning i1 (boolean) which is the condition attempting to be proven.  

```
llvm-prove.py test.ll
```

Where test.ll looks like:

```
define i1 @my_test(i1 %var1, i32 %var2) {
  %res = ... LLVM IR code ...
  ret i32 %res
}
```

To use, you must have defined LLVM_BASE_DIR pointing at a *build* (not install) directory of an LLVM checkout.  You will also need to run the tool from the checkout directory since some of the paths are relative.
