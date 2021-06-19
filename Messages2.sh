#!/bin/sh

# blah
# more blah
# More testing

$XGETTEXT `find . -name \*.cc -o -name \*.cpp -o -name \*.h` -o $podir/dummy.pot
