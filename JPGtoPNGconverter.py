from sys import argv
import os
from PIL import Image

# Check if new_dir exists, if not, create it
def create_new_dir(new_dir):
    if not os.path.isdir(new_dir):
        os.mkdir(new_dir)
    else:
        print('Directory already exists')

# Converts JPG image to PNG
def JPG_to_PNG(file_path, new_dir, file_name):
    img = Image.open(file_path)
    img = img.convert('RGB')
    # Save the file with a .png extension in the new directory
    new_file_path = os.path.join(new_dir, os.path.splitext(file_name)[0] + '.png')
    img.save(new_file_path, 'PNG')

if __name__ == "__main__":
    # Grab first and second argument
    source_dir = argv[1]
    new_dir = argv[2]

    # Create new dir if it doesn't exist
    create_new_dir(new_dir)
    
    # Iterate through the source directory
    for file_name in os.listdir(source_dir):
        # Construct full file path
        file_path = os.path.join(source_dir, file_name)
        # Process only JPG files
        if file_name.lower().endswith('.jpg') or file_name.lower().endswith('.jpeg'):
            JPG_to_PNG(file_path, new_dir, file_name)


