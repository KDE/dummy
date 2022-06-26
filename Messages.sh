#!/bin/sh

# blah
# more blah
# More testing
# Testing Part 3

$XGETTEXT `find . -name \*.cc -o -name \*.cpp -o -name \*.h` -o $podir/dummy.pot
