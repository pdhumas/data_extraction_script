#!/bin/bash
#
#Performing data extraction from a URL and then saving it to a CSV file
url="https://www.amfiindia.com/spages/NAVAll.txt"

#downloading and saving the file
curl -o mf_data.txt "${url}"

output_file="extracted_mf_data.csv"
#extracting required data into output file
awk -F ";" 'BEGIN{OFS=","} NF>1 {print $4,$5}' mf_data.txt > "$output_file"
