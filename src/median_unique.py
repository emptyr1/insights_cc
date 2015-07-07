##################################################################################
# Example of program that calculates the median number of unique words per tweet.#
# Author: Mudit Uppal (www.muppal.com)
# Email: mudit.uppal@yahoo.com
##################################################################################

import sys
import collections
import numpy

input_file = sys.argv[1]
output_file = sys.argv[2]

def median(in_list):
    return numpy.median(numpy.array(in_list))

num_unique_wrds = []
with open(output_file, 'w+') as out_file:
    with open(input_file) as in_file:
        words = collections.Counter() #creates a tuple of words
        lines = in_file.readlines()
        for line in lines:
            words.update(line.split())
            count = len(words)  #number of unique words 
            num_unique_wrds.append(count)
            medianVal = median(num_unique_wrds)
            out_file.write("%.2f\n" % medianVal)
            words.clear() #clear out/empty words collection tuple
