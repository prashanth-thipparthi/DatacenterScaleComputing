#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

current_patent = None
current_patent_info = None
current_patent_citations = []

def outputPatentInfo():
    global current_patent
    global current_patent_info
    global current_patent_citations

    if current_patent != None and current_patent_info != None:
        try:
            #print("check print")
            #print("abcd",current_patent_citations)
            #for i in current_patent_citations:
            print("%s,%s,%d" % (current_patent,','.join(map(str,current_patent_info)),len(current_patent_citations)))
        except ValueError:
	    print("value error")
            #
            # Something wrong in number format
            #
            pass
        except Exception as e:
            print("Something died", e)

    current_patent = None
    current_patent_info = None
    current_patent_citations = []

def main():
    global current_patent
    global current_patent_info
    global current_patent_citations

    current_patent = None
    debug = False

    # input comes from STDIN
    for line in sys.stdin:
        # parse the input we got from mapper.py
        line = line.rstrip()
        if line:
            #print(line)
            key, value = line.split('\t', 1)
            #print(key)
            #print(value)
            # convert count (currently a string) to int
            try:
                patent = long(key)
            except ValueError:
            # key was not a number, so silently
            # ignore/discard this line
                continue

        # this IF-switch only works because Hadoop sorts map output
        # by key (here: word) before it is passed to the reducer

            if current_patent != patent:
                #print(len(current_patent_citations))
                outputPatentInfo()

            current_patent = patent
            fields = value.split(',')
            #print(len(fields))
            if len(fields) > 1:
                current_patent_info = fields
            else:
                #print(value)   
                citations = value.split('\t')
                if len(citations) == 3 and citations[1] == citations[2] :
                    current_patent_citations.append(value)
        
    # do not forget to output the last word if needed!
    outputPatentInfo()


main()
