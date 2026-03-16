#Solve Using Copilot
import os

# Specify the directory path (use '.' for current directory)
path = "/OBS Video"  

# Get list of files and directories
contents = os.listdir(path)

# Print each item
print("Contents of directory:", path)
for item in contents:
    print(item)
