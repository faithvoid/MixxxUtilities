import os

# specify the directory where the .m3u files are located
directory = os.getcwd()

# loop through each .m3u file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".m3u"):
        filepath = os.path.join(directory, filename)
        
        # read the contents of the .m3u file
        with open(filepath, "r") as f:
            lines = f.readlines()
        
        # modify the lines to remove the folder data
        modified_lines = []
        for line in lines:
            if line.startswith("#") or line.strip() == "":
                # ignore comments and empty lines
                modified_lines.append(line)
            else:
                # remove the folder data
                filename = os.path.basename(line.strip())
                modified_lines.append(filename + "\n")
        
        # write the modified contents back to the .m3u file
        with open(filepath, "w") as f:
            f.writelines(modified_lines)