#!/bin/sh

# blah
# more blah
# More testing
# Testing round 3
# Make sure Neon works - next round of checks - should work now?

$XGETTEXT `find . -name \*.cc -o -name \*.cpp -o -name \*.h` -o $podir/dummy.pot
