# A brief outline for questions solution 
* Q1 
  **Analysing tweets and calculating degree of profanity**
    * Files included are-
      - checker.py - the module containing the functions for the questin
      - driver.py - the main program to run the analysis
      - tweets.txt - a sample txt file for input
      - racial_slurs - a sample set of words to check against in the tweets
      - result - compiled sentences and their degree of profanity written side by side
    * General overview of the code -
      - Created module named checker.py and drivercode file for it named driver.py
      - The code reads the racial_slurs.txt file and tweets.txt file and processes them and following things are done 
         - The tweets are seperated into sentences list
         - The sentence in this list is further stripped of any punctuations and turned to lower case
      - Further, each sentence in the tweet is checked for racial slurs
      - The count of racial slurs is then used to get degree of profanity which equals -> (count of racial slurs) / (number of words in sentence)
* Q2 
  **Interesting data set I discovered recently**
    * Files included are-
      - dataset_story.txt - the answer to the question asked
    * Overview on how I came upon this -
      - So, after hearing this question i was a bit confused as how to approach it cause yea I've mostly played with Kaggle datasets and any other dataset didn't quite struck in my mind. So I ventured to find a new dataset which is interesting and I genuinely might like and then I stumbled upon World Bank's datasets among which I found data set named World Development Indicator and after analysing the database and seeing how it's curated and what things it is  actually capable of I found it quite interesting.
* Q3
  **Extracting required data from a URL**
    * Files included are-
      - extract_data.sh - the shell script to get the extracted data as specified in the question
      - extracted_mf_data.csv - the required extracted data in .csv format
    * General overview of the code -
      - Code first downloads the txt file from the given URL
      - curl is used to download our txt file
      - The file is then read using awk command and
        - The delimiter is set to ';'
        - Check for if number of columns are greater than 1
        - Printing 4th and 5th column to our output file
      - The second step is done so as to prevent empty records in our output CSV file
