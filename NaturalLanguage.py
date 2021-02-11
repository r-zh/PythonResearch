import nltk
from sqlparse.filters import output

sentences = "At eight o'clock on Thursday morning Arthur didn't feel very good."

tokens = nltk.word_tokenize(sentences)

#>>> tokens
#['At', 'eight', "o'clock", 'on', 'Thursday', 'morning', 'Arthur', 'did', "n't", 'feel', 'very', 'good', '.']

tagged = nltk.pos_tag(tokens)

#tagged[0:6]
#[('At', 'IN'), ('eight', 'CD'), ("o'clock", 'JJ'), ('on', 'IN'),('Thursday', 'NNP'), ('morning', 'NN')]

for i in range(len(sentences)):
    print(sentences[i])
    print(len(sentences[i]))

    ss = sid.polarity_scores(sentences[i])

    print(ss)
    print(ss['neg'])
    print(ss['neu'])
    print(ss['pos'])

