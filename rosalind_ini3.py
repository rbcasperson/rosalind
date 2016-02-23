def main(data):
    (corpus, params) = data.strip().split('\n')
    (word_one_start, word_one_end,
     word_two_start, word_two_end) = map(int, params.split(' '))
    word_one = corpus[word_one_start:word_one_end + 1]
    word_two = corpus[word_two_start:word_two_end + 1]
    return ' '.join([word_one, word_two])
