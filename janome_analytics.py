from janome.tokenizer import Tokenizer
import collections

with open('search_tweets.txt', 'r', encoding='UTF-8') as f:
    text = f.read()
t = Tokenizer()

c = collections.Counter(token.base_form for token in t.tokenize(text)
                        if token.part_of_speech.startswith('名詞,固有名詞'))
print(c.most_common()[:30])
