from sys import argv

script, infile, outfile = argv

open(outfile, 'w').write(open(infile).read())