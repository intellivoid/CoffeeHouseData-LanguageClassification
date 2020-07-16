#!/bin/sh

# This file cleans the data in the langdetect folder by sorting
# the data and removing duplicated enteries.

for file in langdetect/*; do
    [ -f "$file" ] || continue
    echo "Processing ${file}"
    sort -u "${file}" > "${file}.clean"
    rm "${file}"
    mv "${file}.clean" "${file}"
done