#!/bin/bash

read -p "WARNING: This script will modify all .m3u and .m3u8 files in the current directory and its subdirectories, and the changes made by the script are irreversible. Please make backups if necessary. Do you want to continue? (Y/N)" answer

if [[ "$answer" == "Y" || "$answer" == "y" ]]; then
    # define function to modify a single file
    function modify_file {
        local filepath=$1
        # modify the lines to remove the folder data
        sed -i '/^#/!s#.*/##' "$filepath"
    }

    # loop through each .m3u and .m3u8 file in the current directory and its subdirectories
    find . -type f \( -name "*.m3u" -o -name "*.m3u8" \) | while read filepath; do
        modify_file "$filepath"
    done
    echo "All files modified successfully."
elif [[ "$answer" == "N" || "$answer" == "n" ]]; then
    echo "Script terminated."
    exit 0
else
    echo "Invalid input. Script terminated."
    exit 1
fi
