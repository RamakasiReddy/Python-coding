import os

# Specify the directory path
directory = '/New folder'

# Check if the directory exists
if os.path.isdir(directory):
    print("Contents of the directory:")
    for item in os.listdir(directory):
        print(item)
else:
    print("The specified directory does not exist.")