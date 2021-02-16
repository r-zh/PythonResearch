import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer



if __name__ == "__main__":

    sentences = "At eight o'clock on Thursday morning Arthur didn't feel very good."

    tokens = nltk.word_tokenize(sentences)

    #>>> tokens
    #['At', 'eight', "o'clock", 'on', 'Thursday', 'morning', 'Arthur', 'did', "n't", 'feel', 'very', 'good', '.']

    tagged = nltk.pos_tag(tokens)

    #tagged[0:6]
    #[('At', 'IN'), ('eight', 'CD'), ("o'clock", 'JJ'), ('on', 'IN'),('Thursday', 'NNP'), ('morning', 'NN')]

    sid = SentimentIntensityAnalyzer()

    while sentences != "end":
        ss = sid.polarity_scores(sentences)
        print(ss)
        sentences = input("please enter the next sentence: ")

'''
    for i in range(len(sentences)):
        print(sentences[i])
        print(len(sentences[i]))
'''



