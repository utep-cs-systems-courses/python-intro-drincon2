# Import libraries
import sys
import re

# Files
file_input = sys.argv[1]
file_output = sys.argv[2]

# Word count dictionary
word_dict = {}

# Read file_input
with open(file_input, "r") as input_file:
    for line in input_file:
        # Remove white spaces and empty new lines
        line = line.strip()
        # Ignore case of words
        line = line.lower()
        # Split lines into words using empty spaces as parameter
        words = re.split('[ +,.]', line)

        # Iterate the collection stored in words
        for word in words:
            # Increment word count if the current word already exists in word_dict,
            # otherwise, save the new word in word_dict
            if word in word_dict:
                word_dict[word] = word_dict[word] + 1
            else:
                word_dict[word] = 1

# Print the contents of word_dict
for key in word_dict:
    print(key, ":", word_dict[key])
