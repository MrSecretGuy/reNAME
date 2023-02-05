import os

def print_ascii_art():
    """
    Prints the ASCII art logo of "reNAME".
    """
    print("""
               _   _          __  __ ______ 
              | \ | |   /\   |  \/  |  ____|
      _ __ ___|  \| |  /  \  | \  / | |__   
     | '__/ _ \ . ` | / /\ \ | |\/| |  __|  
     | | |  __/ |\  |/ ____ \| |  | | |____ 
     |_|  \___|_| \_/_/    \_\_|  |_|______|
    """)

def batch_rename(path, ext, static_name):
    """
    Batch renames files in a folder.

    Args:
    - path (str): Path to the folder.
    - ext (str): File extension to target within the folder.
    - static_name (str): Static part of the files' new names.

    Returns:
    None
    """
    count = 0
    for filename in os.listdir(path):
        if filename.endswith(ext):
            # Create the new name for each file using the given format
            new_name = (f"{static_name}-{str(count).zfill(len(str(len([i for i in os.listdir(path) if i.endswith(ext)]))))}"
                        f".{ext}")
            # Rename the file
            os.rename(os.path.join(path, filename), os.path.join(path, new_name))
            count += 1
    #Print out the amount of files renamed
    print(f"Renamed {count} files!")

# Print the ASCII art logo
print_ascii_art()

# Ask the user for the path to the folder, file extension, and static part of the new name
path = input("Enter the path to the folder: ")
ext = input("Enter the file extension: ")
static_name = input("Enter the static part of the new name: ")

# Call the batch_rename function to rename the files
batch_rename(path, ext, static_name)
