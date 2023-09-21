# Markov-Text-Generator :pencil:
## Information :computer:
* `Subject`: __Introduction to Natural Language Processing__
* `Professor`: __Patrick Wang__
* `Assignment`: __A bare-bones Markov text generator__
* `Name`: __Suim Park__

## Test case :pushpin:

* __`Case 1`__
    - Test
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
    - Test
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
    - Test
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
    - Test
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
    - Test
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
    - Test
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
    - Test
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
    - Test
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
    - Test
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
    - Test
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
    - Test
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
    - Test
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
    - Test
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
    ['he', 'received', 'the', 'letter', 'from', 'the', 'most', 'proper', 'situation', 'of']
    ```
</br>

* __`Case 14`__
    - Test
      ```Python
      sentence = ['her', 'mind']
      n = 3
      corpus = nltk.word_tokenize(
      nltk.corpus.gutenberg.raw('austen-sense.txt').lower()
      )
      randomize = True
      ```
  - Output: __stochastic on, backoff off__
    ```Python
    ['her', 'mind', 'was', 'heightened', 'by', 'circumstances', 'which', 'ought', 'not', 'to']
    ```
</br>

* __`Case 15`__
    - Test
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
