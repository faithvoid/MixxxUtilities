import os

# get the list of .m3u and .m3u8 files in the current directory
playlist_files = [f for f in os.listdir('.') if f.endswith('.m3u') or f.endswith('.m3u8')]

# loop through each playlist file and modify the lines to remove the folder data
for filepath in playlist_files:
    with open(filepath, 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        f.truncate()
        for line in lines:
            if not line.startswith('#'):
                line = os.path.basename(line)
            f.write(line)