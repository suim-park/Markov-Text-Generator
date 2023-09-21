# Markov-Text-Generator :pencil:

## Python File: mtg.py
```Python
import random


# N-gram model train function
def train_ngram_model(tokens, n):
    ngram_model = {}
    for i in range(len(tokens) - n + 1):
        # Current N-1 tokens
        ngram = tuple(tokens[i : i + n - 1])
        # Next word
        next_word = tokens[i + n - 1]
        if ngram in ngram_model:
            ngram_model[ngram].append(next_word)
        else:
            ngram_model[ngram] = [next_word]
    return ngram_model


def predict_next_word(ngram_model, input_tokens, n, randomize=False):
    if n == 1:  # Use unigram model when n is 1
        uni_gen = generate_unigram(corpus)
        next_word = generate_text(uni_gen, randomize)
    else:
        ngram = tuple(input_tokens[-n + 1 :])  # Current N-1 tokens
        if ngram in ngram_model:
            if randomize:
                next_word = random.choice(ngram_model[ngram])
            else:
                # Select the most frequent word
                candidates = ngram_model[ngram]
                sorted_candidates = sorted(
                    candidates,
                    key=lambda word: (-candidates.count(word), candidates.index(word)),
                )
                next_word = sorted_candidates[0]
        else:
            # Backoff: Try with N-1 gram
            next_word = predict_next_word(ngram_model, input_tokens, n - 1, randomize)

    # Check for punctuation marks
    if next_word in (".", "?", "!"):
        input_tokens.append(next_word)
        return None

    return next_word


# Generate unigram
def generate_unigram(corpus):
    unigram_model = {}
    for word in corpus:
        if word in unigram_model:
            unigram_model[word] += 1
        else:
            unigram_model[word] = 1
    return unigram_model


# Text generation function
def generate_text(unigram_model, randomize=False):
    if randomize:
        # When randomize is True, select a random word among high-frequency words
        all_words = list(unigram_model.keys())
        next_word = random.choice(all_words)
    else:
        # When randomize is False, select the most frequent word
        next_word = max(unigram_model, key=lambda k: unigram_model[k])
    return next_word


def finish_sentence(sentence, n, corpus, randomize=False):
    # Train the N-gram model
    ngram_model = train_ngram_model(corpus, n)

    generated_tokens = sentence[:]
    while (
        len(generated_tokens) < 10
    ):  # Repeat until the length of generated_tokens is less than 10
        next_word = predict_next_word(ngram_model, generated_tokens, n, randomize)
        if next_word is None:
            break
        generated_tokens.append(next_word)

    return generated_tokens
```

## Test case

* __`Case 1`__
    - Test:
      ```Python
      sentence = ['she', 'was', 'not']
      n = 3
      corpus = nltk.word_tokenize(
      nltk.corpus.gutenberg.raw('austen-sense.txt').lower()
      )
      randomize = False
      ```
  - Output: __deterministic on, backoff off__
    ```Python
    ['she', 'was', 'not', 'in', 'the', 'world', '.']
    ```
</br>

* __`Case 2`__
    - Test:
      ```Python
      sentence = ['she', 'was', 'not']
      n = 2
      corpus = nltk.word_tokenize(
      nltk.corpus.gutenberg.raw('austen-sense.txt').lower()
      )
      randomize = False
      ```
  - Output: __deterministic on, backoff off__
    ```Python
    ['she', 'was', 'not', 'be', 'a', 'very', 'well', ',', 'and', 'the']
    ```
</br>

* __`Case 3`__
    - Test:
      ```Python
      sentence = ['she', 'was', 'not']
      n = 1
      corpus = nltk.word_tokenize(
      nltk.corpus.gutenberg.raw('austen-sense.txt').lower()
      )
      randomize = False
      ```
  - Output: __deterministic on, backoff off__
    ```Python
    ['she', 'was', 'not', ',', ',', ',', ',', ',', ',', ',']
    ```
</br>

* __`Case 4`__
    - Test:
      ```Python
      sentence = ['she', 'was', 'not']
      n = 4
      corpus = nltk.word_tokenize(
      nltk.corpus.gutenberg.raw('austen-sense.txt').lower()
      )
      randomize = False
      ```
  - Output: __deterministic on, backoff off__
    ```Python
    ['she', 'was', 'not', 'in', 'the', 'habit', 'of', 'seeing', 'much', 'occupation']
    ```
</br>

* __`Case 5`__
    - Test:
      ```Python
      sentence = ['she', 'was', 'not', 'in']
      n = 5
      corpus = nltk.word_tokenize(
      nltk.corpus.gutenberg.raw('austen-sense.txt').lower()
      )
      randomize = False
      ```
  - Output: __deterministic on, backoff off__
    ```Python
    ['she', 'was', 'not', 'in', 'a', 'humour', ',', 'however', ',', 'to']
    ```
</br>

* __`Case 6`__
    - Test:
      ```Python
      sentence = ['she', 'was', 'for']
      n = 3
      corpus = nltk.word_tokenize(
      nltk.corpus.gutenberg.raw('austen-sense.txt').lower()
      )
      randomize = False
      ```
  - Output: __deterministic on, backoff on__
    ```Python
    ['she', 'was', 'for', 'ever', ',', 'and', 'the', 'two', 'miss', 'steeles']
    ```

</br>

* __`Case 7`__
    - Test:
      ```Python
      sentence = ['she', 'was', 'not']
      n = 3
      corpus = nltk.word_tokenize(
      nltk.corpus.gutenberg.raw('austen-sense.txt').lower()
      )
      randomize = True
      ```
  - Output: __stochastic on, backoff off__
    ```Python
    ['she', 'was', 'not', 'only', 'all', 'three', ',', 'is', 'not', 'engaged']
    ```
</br>

* __`Case 8`__
    - Test:
      ```Python
      sentence = ['Marianne's']
      n = 1
      corpus = nltk.word_tokenize(
      nltk.corpus.gutenberg.raw('austen-sense.txt').lower()
      )
      randomize = False
      ```
  - Output: __determistic on, backoff off__
    ```Python
    ["Marianne's", ',', ',', ',', ',', ',', ',', ',', ',', ',']
    ```
</br>

* __`Case 9`__
    - Test:
      ```Python
      sentence = ['Marianne's']
      n = 1
      corpus = nltk.word_tokenize(
      nltk.corpus.gutenberg.raw('austen-sense.txt').lower()
      )
      randomize = True
      ```
  - Output: __stochastic on, backoff off__
    ```Python
    ["Marianne's", 'hinder', 'atoning', 'weakness', 'gentleman', 'remainder', 'conveyed', 'mohrs', 'tongue', 'wit']
    ```
</br>

* __`Case 10`__
    - Test:
      ```Python
      sentence = ['but', 'her']
      n = 2
      corpus = nltk.word_tokenize(
      nltk.corpus.gutenberg.raw('austen-sense.txt').lower()
      )
      randomize = False
      ```
  - Output: __determistic on, backoff off__
    ```Python
    ['but', 'her', ',', 'and', 'the', 'same', 'time', ',', 'and', 'the']
    ```
</br>

* __`Case 11`__
    - Test:
      ```Python
      sentence = ['he', 'was', 'not', 'in']
      n = 5
      corpus = nltk.word_tokenize(
      nltk.corpus.gutenberg.raw('austen-sense.txt').lower()
      )
      randomize = False
      ```
  - Output: __determistic on, backoff off__
    ```Python
    ['he', 'was', 'not', 'in', 'spirits', ',', 'however', ';', 'he', 'praised']
    ```
</br>

* __`Case 12`__
    - Test:
      ```Python
      sentence = ['he', 'received', 'the', 'letter']
      n = 4
      corpus = nltk.word_tokenize(
      nltk.corpus.gutenberg.raw('austen-sense.txt').lower()
      )
      randomize = False
      ```
  - Output: __determistic on, backoff on__
    ```Python
    ['he', 'received', 'the', 'letter', ',', 'the', 'ring', ',', 'formed', 'altogether']
    ```
</br>

* __`Case 13`__
    - Test:
      ```Python
      sentence = ['he', 'received', 'the', 'letter']
      n = 4
      corpus = nltk.word_tokenize(
      nltk.corpus.gutenberg.raw('austen-sense.txt').lower()
      )
      randomize = True
      ```
  - Output: __stochastic on, backoff off__
    ```Python
    ['he', 'received', 'the', 'letter', 'south-east', 'execution', 'genuine', 'wanton', 'opposite', 'instructions']
    ```
</br>

* __`Case 14`__
    - Test:
      ```Python
      sentence = ['her', 'mind']
      n = 2
      corpus = nltk.word_tokenize(
      nltk.corpus.gutenberg.raw('austen-sense.txt').lower()
      )
      randomize = True
      ```
  - Output: __stochastic on, backoff off__
    ```Python
    ['her', 'mind', '.']
    ```
</br>

* __`Case 15`__
    - Test:
      ```Python
      sentence = ['they', 'require']
      n = 2
      corpus = nltk.word_tokenize(
      nltk.corpus.gutenberg.raw('austen-sense.txt').lower()
      )
      randomize = False
      ```
  - Output: __determistic on, backoff on__
    ```Python
    ['they', 'require', 'so', 'much', 'more', 'than', 'she', 'was', 'not', 'be']
    ```
