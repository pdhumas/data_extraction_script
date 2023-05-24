# data_extraction_script
Extracting required data from a URL 
Code first downloads the txt file from the given URL

curl is used to download our txt file

The file is then read using awk command
- The delimiter is set to ';'
- Check for if number of columns are greater than 1
- Printing 4th and 5th column to our output file
The second step is done so as to prevent empty records in our output CSV file
