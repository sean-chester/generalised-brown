#!/usr/bin/env python
#                                       cluster.py
#                       &copy; Sean Chester (sean.chester@idi.ntnu.no)
#                       &copy; Leon Derczynski (leon@dcs.shef.ac.uk)
#                                      22 July 2015

import csv
import argparse

# Input parsing
parser = argparse.ArgumentParser(
	description='Prints out a tree with a specified number of leaves, given an ' + \
		'input file with an ordered list of merges. Each unique path identifies ' + \
		'one leaf. All word types that have the same path as each other belong to the ' + \
		'same leaf (and correspond to one Brown cluster).', \
	epilog='If the output is to be read by humans, consider piping results to ' + \
		'the sort command to print the leaves in depth-first order. (Then ' + \
		'similar leaves/clusters will appear nearer each other in the output.)')
parser.add_argument(
	'-in', '--input-file', \
	help="Input file containing ordered merges", \
	required=True, \
	dest='input', \
	metavar='INPUT_FILE')
parser.add_argument(
	'-c', '--num-classes', \
	type=int, \
	help="Number of leaves/classes/clusters to produce", \
	required=True, \
	dest='leaves', \
	metavar='NUM_CLASSES')
parser.add_argument(
	'-d', '--depth', \
	type=int, \
	help="Truncation depth for paths (i.e., no leaf appears farther than d-1 hops from the " + \
		"root). Note: setting this parametre likely results in fewer than NUM_CLASSES leaves, " + \
		"because the --num-classes filter is (logically) applied first.", \
	required=False, \
	dest='depth')
args = parser.parse_args()

# If depth wasn't passed as a parametre, give it a default value of being
# equal to --num-classes.
if args.depth is None:
	args.depth = args.leaves

# Actual processing -- read merge list in reverse and map each encountered
# word type onto a tree path in a dictionary.
tree = {}
with open( args.input ) as tsv:
	for line in reversed(list(csv.reader(tsv, delimiter="\t", quotechar=None))):
		merge_into = line[0]
		merge_from = line[1]
		if not merge_into in tree:
			tree[merge_into] = "0"
			tree[merge_from] = "1"
			args.leaves = args.leaves - 2
		elif args.leaves > 0:
			parent = tree[merge_into]
			if len( parent ) < args.depth:
				tree[merge_from] = parent + "1"
				tree[merge_into] = parent + "0"
			else:
				tree[merge_from] = parent
			args.leaves = args.leaves - 1
		else: 
			tree[merge_from] = tree[merge_into]
				
for (cluster, path) in tree.items():
	print( path + "\t" + cluster )

