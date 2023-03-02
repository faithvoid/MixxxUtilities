import os

# get the list of .m3u and .m3u8 files in the current directory
playlist_files = [f for f in os.listdir('.') if f.endswith('.m3u') or f.endswith('.m3u8')]

# loop through each playlist file and modify the lines to remove the folder data
for filepath in playlist_files:
    with open(filepath, 'r+') as f:
# read the lines from the playlist file
        lines = f.readlines()
# move the file pointer back to the beginning of the file
        f.seek(0)
# truncate the file to remove any existing content
        f.truncate()

# loop through each line in the file and modify it
        for line in lines:
            if not line.startswith('#'):
                line = os.path.basename(line)
# write the modified line back to the playlist file
            f.write(line)