import os
import xlwt
import eyed3

# Set the root directory to the current working directory
root_dir = os.getcwd()

# Iterate through each subdirectory in the root directory
for subdir, dirs, files in os.walk(root_dir):
    # Create a new Excel workbook
    workbook = xlwt.Workbook(encoding="utf-8")
    # Create a new worksheet
    worksheet = workbook.add_sheet("Song Info")
    # Set the column headers
    headers = ["Artist", "Song", "Album", "Genre"]
    for col, header in enumerate(headers):
        worksheet.write(0, col, header)

    # Create an empty list to hold the song information
    song_info = []

    # Iterate through each file in the subdirectory
    for file in files:
        # Check if the file is an MP3 file
        if file.endswith(".mp3"):
            # Get the full file path
            file_path = os.path.join(subdir, file)
            # Load the MP3 file metadata
            audio_file = eyed3.load(file_path)
            # Get the artist, title, album, and genre metadata
            artist = audio_file.tag.artist
            title = audio_file.tag.title
            album = audio_file.tag.album
            genre = audio_file.tag.genre.name if audio_file.tag.genre else ""

            # Add the song information to the list
            song_info.append((artist, title, album, genre))

    # Sort the song information list by artist name
    song_info.sort(key=lambda x: x[0])

    # Write the sorted song information to the Excel worksheet
    for row, info in enumerate(song_info):
        worksheet.write(row+1, 0, info[0])
        worksheet.write(row+1, 1, info[1])
        worksheet.write(row+1, 2, info[2])
        worksheet.write(row+1, 3, info[3])

    # Save the Excel workbook in the subdirectory
    output_file = os.path.join(subdir, os.path.basename(subdir) + ".xls")
    workbook.save(output_file)
