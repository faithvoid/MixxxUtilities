# MixxxUtilities
Various python/shell scripts for simplifying one's workflow in Mixxx. 

## m3ustrip - M3U/M3U8 Folder Information Stripper (for portable playlists)
Python and bash shell scripts that removes all folder information from Mixxx-exported .m3u/.m3u8 files in the current directory. Useful for carrying your sets (including hotcues, BPM, etc) on a USB if you combine it with the "Write Serato Metadata" function in Mixxx, as importing them without folder data will have the playlist default to the same folder the playlist file is in. Shell script works in Linux, unsure about macOS but probably, Windows users are left with the Python script to try for themselves. Includes m3ustrip-subfolder version so you can, for example, keep it on the root of your USB and run it when you've exported all your sets to the USB so all your playlists are portable! 

## setlistbackup.py - Back up your setlist information into a convenient spreadsheet!
Generates an .XLS spreadsheet file inside all subfolders the script is run in, which backs up ID3 metadata of artists/songs/albums and genres contained in the subfolder. Useful for backing up metadata to the cloud in case of data loss. Requires files to have proper ID3 metadata (but if you're a DJ you should be making sure of this anyway). Also this script isn't Mixxx-specific so use it on your DJ crates and playlists so you don't lose your track info! Requires python-eyed3 & python-xlwt.
