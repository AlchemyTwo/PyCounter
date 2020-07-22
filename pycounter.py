import sys
import os
import collections

if "-h" in sys.argv:
    print("Please use: wordcounter [filename] [number of top words to display].")
    print("Created by Dan Earnshaw, July 2020")

else:
    filename = sys.argv[1]

    if os.path.isfile(filename):

        words = {}

        with open(filename) as file:
            for line in file:
                currentline = line.split()
                for word in currentline:
                    if word.lower() in words:
                        words[word.lower()] += 1
                    else:
                        words[word.lower()] = 1

        top = collections.Counter(words)
        print(top.most_common(int(sys.argv[2])))

    else:
        print("This is not a valid text file.")
        
