#!/usr/bin/env python
"""mapper.py"""

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # split the line into CSV fields
    words = line.split(",")
    if len(words) == 2:
        #
        # It's a citation
        #
        try:
            if words[0] != '"CITING"': 
                cite = long(words[0])
                citation = long(words[1])    
                print('%s\t%s' % (words[0], words[1]))
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

