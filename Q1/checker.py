'''
Creating a module containg the functions required for profanity analysis of tweets
This is the general function input and their output datatypes
- get_sulrs_set(str: file) --> (set: r_slurs)
- split_tweet(str: line) --> (list[str]: string_list)
- check_tweet(list[str]: sentences, set: r_slurs) --> void
- profanity_degree(str: sentence, set: r_slurs) --> (float: dop)
'''
#importing libraries to help me with better text analysis
# re is used to split sentences and strip them of any punctuations to analyse it easily
# nltk library is used here to break down the tweet into sentences
import re
from nltk.tokenize import sent_tokenize

def get_slurs_set(file):
# using regex to split data delimited by comma then
# stripping any whitespaces and storing as a set
    r_slurs = set(word.strip() for word in re.split(",", file))
    return r_slurs
##hello
#function to split tweets
def split_tweet(line):
    string_list = sent_tokenize(line)
    return string_list

# function to remove punctuations and then calculate for degree of profanity
# then store the sentences and degree of profanity into the result.txt
w = open("result.txt", 'w')
def check_tweet(sentences,r_slurs):
    for sentence in sentences:
        print(sentence)
        w.write(sentence)
        # have to remove punctuations as well so the slurs are easy to identify
        sentence = re.sub(r"[^\w\s]", "", sentence)
        dop = profanity_degree(sentence.lower(),r_slurs)
        print("->", round(dop, 3))
        write_string = " --> " +str(round(dop, 3)) + "\n"
        w.write(write_string)

# function to count the number of slurs per number of words in a sentence, i.e. Degree of Profanity
def profanity_degree(sentence, r_slurs):
    words = sentence.split()
    count = 0
    for word in words:
        if word in r_slurs:
            count += 1
    dop = count / len(words)
    return dop
