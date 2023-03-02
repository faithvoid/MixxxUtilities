#!/bin/bash

# loop through each .m3u file in the current directory
for filepath in *.m3u; do
    # modify the lines to remove the folder data
    sed -i '/^#/!s#.*/##' "$filepath"
done
