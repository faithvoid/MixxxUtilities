import os
import shutil

# Prompt user for confirmation before running the script
confirm = input("WARNING: This script will modify all .m3u and .m3u8 files in the current directory, and the changes made by the script are irreversible. You will be asked if you want to back up your .m3u/.m3u8 file(s) in the next prompt. Do you want to continue? (Y/N): ").lower()

if confirm == 'y':
    # Prompt user for backup before modification
    backup = input("Do you want to generate a backup of the .m3u/.m3u8 file(s) before modification? (Y/N): ").lower()

    # Get the list of .m3u and .m3u8 files in the current directory
    playlist_files = [f for f in os.listdir('.') if f.endswith('.m3u') or f.endswith('.m3u8')]

    # Loop through each playlist file and modify the lines to remove the folder data
    for filepath in playlist_files:
        with open(filepath, 'r+') as f:
            # Read the lines from the playlist file
            lines = f.readlines()

            # Create a backup of the file if user selects "Y"
            if backup == 'y':
                shutil.copy2(filepath, filepath + '.bak')

            # Move the file pointer back to the beginning of the file
            f.seek(0)

            # Truncate the file to remove any existing content
            f.truncate()

            # Loop through each line in the file and modify it
            for line in lines:
                if not line.startswith('#'):
                    line = os.path.basename(line)

                # Write the modified line back to the playlist file
                f.write(line)

else:
    print("Script terminated.")
    exit(1)
