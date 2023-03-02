#!/bin/bash

read -p "WARNING: This script will modify all .m3u and .m3u8 files in the current directory, and the changes made by the script are irreversible. Please make backups if necessary. Do you want to continue? (Y/N)" answer

if [[ "$answer" == "Y" || "$answer" == "y" ]]; then
# loop through each .m3u and .m3u8 file in the current directory

for filepath in *.m3u *.m3u8; do
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
