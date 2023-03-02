#!/bin/bash

# loop through each .m3u and .m3u8 file in the current directory
for filepath in *.m3u *.m3u8; do
    # modify the lines to remove the folder data
    sed -i '/^#/!s#.*/##' "$filepath"
done
