import yaml

# variables/counters declaration
in_yaml = False
content = []
counter = 0

# Read input file
with open('README.md', 'r') as f:
    lines = f.readlines()

# Loop through all the lines
for line in lines:

    counter = counter + 1

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

print(content)
