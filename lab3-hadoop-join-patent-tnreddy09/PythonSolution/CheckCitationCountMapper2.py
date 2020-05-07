#!/usr/bin/env python
"""mapper.py"""

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # split the line into CSV fields
    line = line.rstrip()
    if line:
        words = line.split(",")
        if len(words) < 2:
            #
            # It's a citation
            #
            lineSplit = line.split('\t')
            try:
                if len(lineSplit) == 3:
                    print('%s\t%s\t%s' % (lineSplit[1], lineSplit[0], lineSplit[2]))
                else:
                    print('%s\t%s\t%s' % (lineSplit[1], lineSplit[0],""))
            except Exception as e:
                # improperly formed citation number
                print("Exception ", e);
                pass
        else:
            #
            # It's patent info 
            #
            try:
               if words[0] != '"PATENT"':       
                   print('%s\t%s' % (words[0], ','.join(words[1:])))
            except Exception as e:
                # improperly formed citation number
                print("Exception ", e);
                pass

