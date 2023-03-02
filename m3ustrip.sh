#!/bin/bash

read -p "WARNING: This script will modify all .m3u and .m3u8 files in the current directory, and the changes made by the script are irreversible. You will be asked if you want to back up your .m3u/.m3u8 file(s) in the next prompt. Do you want to continue? (Y/N)" answer

if [[ "$answer" == "Y" || "$answer" == "y" ]]; then

  # Ask user if they want to generate a backup of the .m3u/.m3u8 file
  read -p "Do you want to generate a backup of the .m3u/.m3u8 file(s) before modification? (Y/N)" backup_answer

  # loop through each .m3u and .m3u8 file in the current directory
  for filepath in *.m3u *.m3u8; do

    # Generate backup if user selected "Y"
    if [[ "$backup_answer" == "Y" || "$backup_answer" == "y" ]]; then
      cp "$filepath" "$filepath.bak"
    fi

    # modify the lines to remove the folder data
    sed -i '/^#/!s#.*/##' "$filepath"
  done

elif [[ "$answer" == "N" || "$answer" == "n" ]]; then
  echo "Script terminated."
  exit 0
else
  echo "Invalid input. Script terminated."
  exit 1
fi
