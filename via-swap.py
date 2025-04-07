#!/env/python3

import json
import math
import sys
import pathlib

# Expect at least one argument (input filename)
if len(sys.argv) < 2:
	print("Input file not specified.")
	print("Expected format is: swap.py filename.layout.json")
	print("eg. python3 ./swap.py lily58.layout.json")
	exit()

# Convert argument to a Path
inputFile = pathlib.Path(sys.argv[1])

# Make sure the input filename ends with .layout.json
if inputFile.name[-12:] != '.layout.json':
	print("Invalid input file.")
	print("Must be a *.layout.json file exported from Via.")
	exit()

# Check if input file actually exists
if not inputFile.exists():
	print("Input file not found.")
	exit()

# Make sure it's a file, not a directory
if inputFile.is_dir():
	print("Input file is a directory, not a JSON file.")
	exit()

# Grab the first part of the input filename
# eg. If the inputFile is "lily58.layout.json", then we want "lily58"
nameChunks = inputFile.name.split('.')
nameWithoutExtension = nameChunks[0]

# Put the output file in the same directory as the input file
# and give it the same name, but with "flipped" in the name.
# eg. /tmp/lily58.layout.json becomes /tmp/lily58.flipped.json
outputFileName = nameWithoutExtension + '.flipped.json'
outputFile = pathlib.Path(inputFile.parent, outputFileName)

with inputFile.open() as original:
	with outputFile.open('w') as flipped:

		# Load the input file as JSON
		data = json.load(original)
		
		newLayers = []

		# Iterate through the 'layers' attribute of the JSON.
		#
		# The 'layers' attribute is an array of arrays.
		# Each array contains the entire keymap for that layer.
		# 
		# So in order to flip each layer, we split the layer's
		# key list in half and swap the two halves around.
		for l in data['layers']:
			size = math.floor(len(l) / 2)
			newLayers += [l[size:] + l[:size]]
			
		# Update the original JSON with the flipped layout
		data['layers'] = newLayers

		# Write the updated JSON to the output file
		flipped.write(json.dumps(data, indent = 4))

		print("Wrote to "+outputFile.name)
