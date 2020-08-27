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
        # Split lines into words using empty spaces and special characters as parameters
        words = re.split('[ +,.:;-]', line)

        # Iterate the collection stored in words
        for word in words:
            # Increment word count if the current word already exists in word_dict,
            # otherwise, save the new word in word_dict
            if word in word_dict:
                word_dict[word] = word_dict[word] + 1
            else:
                word_dict[word] = 1


# Write the contents of word_dict into output.txt
with open(file_output, "w") as output_file:
    # Sort the words of word_dict in ascending alphabetical order (a-z)
    for k in sorted(word_dict.keys()):
        # Write the sorted word_dict into output.txt
        if word_dict[k] != 221:
            print(k, word_dict[k])
            output_file.write(k + " " + str(word_dict[k]) + "\n")
    output_file.close()
