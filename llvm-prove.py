#! /usr/bin/python
# A simple helper script to use LLVM's optimizer as a prover.  LLVM makes
# a very bad general prover, but can often be moderately effective on 
# proof examples extracted from programs.  The language of the proof to
# attempt is a single LLVM IR function returning i1 (boolean) which is the
# condition attempting to be proven.

# TODO:  Add some sanity checking
# - must have LLVM_BASE_DIR
# - validate input file format

import os
import subprocess
import sys

assert len(sys.argv) == 2
input_file = sys.argv[1]
assert os.path.exists(input_file)

cmd = "$LLVM_BASE_DIR/bin/opt -O3 -S %s" % (input_file)
output = subprocess.check_output(cmd, shell=True)

# This is horrible, but so is the subprocess API
# FIXME: use the raw popen/communicate APIs
cmd = "echo '%s' | $LLVM_BASE_DIR/bin/FileCheck result.FileCheck 2> /dev/null" % (output)
status = subprocess.call(cmd, shell=True)
if not status:
    print "Result proven"
else:
    cmd = "echo '%s' | $LLVM_BASE_DIR/bin/FileCheck disproven.FileCheck 2> /dev/null" % (output)
    status = subprocess.call(cmd, shell=True)
    if not status:
        print "Result disproven"
    else:
        print "Result could not be proven"



