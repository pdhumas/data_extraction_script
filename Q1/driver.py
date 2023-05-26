'''
Assumptions:
-> Tweets are stored in tweets.txt
-> Each different tweet is in a single line without new line character in it
-> Each tweet can have multiple sentences
-> Racial slurs to check are stored in racial_slurs.txt file

The degree of profanity is measured by count of slurs in a sentence per words in a sentence
'''
# importing functions from checker module
from checker import check_tweet
from checker import split_tweet
from checker import get_slurs_set

# reading the racial_slurs file
racial_slurs = open("racial_slurs.txt", "r")
# since racial_slurs is a IOwrapper object
# extracting string from it and setting it to another variable
for string in racial_slurs:
    data = string
# using get_slurs_set to get the racial slurs in a set
# set is used to stroe slurs as it will help in faster searching
r_slurs = get_slurs_set(data)
#print(r_slurs)

# reading the tweets file
tweets = open("tweets.txt", "r")
for line in tweets:
    sentences = split_tweet(line)
    # print(sentences)
    check_tweet(sentences,r_slurs)