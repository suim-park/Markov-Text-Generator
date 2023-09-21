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
