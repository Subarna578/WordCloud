#!/usr/bin/python
# -*- coding: utf-8 -*-


def calculate_frequencies(file_contents):
    file_contents = list(file_contents.split())

    # Here is a list of punctuations and uninteresting words you can use to process your text

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = [
        'the',
        'a',
        'to',
        'if',
        'is',
        'it',
        'of',
        'and',
        'or',
        'an',
        'as',
        'i',
        'me',
        'my',
        'we',
        'our',
        'ours',
        'you',
        'your',
        'yours',
        'he',
        'she',
        'him',
        'his',
        'her',
        'hers',
        'its',
        'they',
        'them',
        'their',
        'what',
        'which',
        'who',
        'whom',
        'this',
        'that',
        'am',
        'are',
        'was',
        'were',
        'be',
        'been',
        'being',
        'have',
        'has',
        'had',
        'do',
        'does',
        'did',
        'but',
        'at',
        'by',
        'with',
        'from',
        'here',
        'when',
        'where',
        'how',
        'all',
        'any',
        'both',
        'each',
        'few',
        'more',
        'some',
        'such',
        'no',
        'nor',
        'too',
        'very',
        'can',
        'will',
        'just',
        '\xe2\x80\xa6',
        'on',
        'in',
        'thus',
        "doesn't",
        'not',
        'then',
        'doesnt',
        'doesn\xe2\x80\x99t',
        'for',
        'get',
        'able',
        'i.e',
        ]

    frequencies = {}  # Creating the dictionary to count the occurences of word

    for word in file_contents:
        word = word.lower()  # convert all words to lowercase
        if word[-1] in punctuations or word[0] in punctuations:  # remove the punctuations

            # word[-1] for ending punctuations
            # word[0] for beginning punctuations like # (hashtag)..

            if word[0] in punctuations:
                word = word[1:len(word)]  # remove '#' if '#' present in word
            else:
                word = word[:len(word) - 1]  # remove other punctuations

            # Uninteresting words frequently appear in text and they create ambuigity, so
            # it's better to remove them

            if word not in uninteresting_words:
                if word not in frequencies:  # Check if the word is already in dictionary
                    frequencies[word] = 1
                else:
                    frequencies[word] += 1
        else:
            if word not in uninteresting_words:
                if word not in frequencies:
                    frequencies[word] = 1
                else:
                    frequencies[word] += 1

    # wordcloud

    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies)
    return cloud.to_array()
