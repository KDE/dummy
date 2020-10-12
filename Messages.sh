#!/bin/sh

# blah
# more blah

$XGETTEXT `find . -name \*.cc -o -name \*.cpp -o -name \*.h` -o $podir/dummy.pot
