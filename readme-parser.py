import yaml
import sys
from pprint import pprint

# variables/counters declaration
in_yaml = False
content = []
counter = 0

# Read input file
with open('README.md', 'r') as f:
    lines = f.readlines()


all_lines = []
for line in lines:
    all_lines.append(line.replace("\n",""))

lines = all_lines

#print(lines)


content = []

# Loop through all the lines
for line in lines:
    counter = counter + 1

    if not in_yaml and line.startswith('```'):
        in_yaml = True
    elif in_yaml and line.startswith("```"):
        in_yaml = False
    elif in_yaml:
        content.append(line)
        
    
    
s = '\n'.join(content)

d = yaml.load(s)

pprint (d)


'''
    # check the line in yaml format or not
    if in_yaml:
        content.append(yaml.load(line))

    if not in_yaml and line.startswith("```"):
        in_yaml = True
        try:
            content.append(yaml.load(line))
        except:
            print(counter, line)
            print("Line is not in yaml format")

    if in_yaml and not line.startswith("```"):
        in_yaml = False

    # check for the tab in the line.
    if "\t" in line:
        print("ERROR: tab found in line", counter, line)
        
    # check for space in first column of the line! ignore if the line is empty 
    # and has 2 to 4 spaces in the begining of the line
    if line.startswith(" ") and line not in ['\n'] \
        and not line.startswith("   ") \
        and not line.startswith("  ") \
        and not line.startswith("    "):
        print("ERROR: space found in first column of the line", counter, line)
'''
