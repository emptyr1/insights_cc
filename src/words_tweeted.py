##################################################################################
# Example of program that calculates the total number of times each word has been tweeted.
# Author: Mudit Uppal (www.muppal.com)
# Email: mudit.uppal@yahoo.com
##################################################################################

import sys
from collections import Counter

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(output_file, 'w+') as out_file:
    with open(input_file) as filef:
        words = Counter(filef.read().split())
        wordlist = sorted(words.items())
        for word in wordlist:
            out_file.write('{:<30}{}\n'.format(*word))
