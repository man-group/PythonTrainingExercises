"""Your job is to write a speech for your CEO. You have a list of meaningful
phrases that he is fond of such as "knowledge optimization initiatives" and
your task is to weave them in to a speech.

You also have the opening words "Our clear strategic direction is to invoke..."
and some useful joining phrases such as "whilst not forgetting".

The speech that you will write takes the opening words and randomly jumbles the
phrases alternated with joining phrases to make a more complete, if meaningless,
speech. After execution the speech might need some light editing.

Note to my current employer: This is no reflection whatsoever on the
organisation that I work for. This all comes from one of my former CEOs,
Stephen Elop, during his tenure at Nokia. The code is mine but the words are
all his, slightly transliterated ("<big corp.>" replaces "Nokia",
"<little corp.>" replaces "Symbian" and "<other corp.>" replaces "Microsoft"). 

Created on 19 Feb 2016

@author: paulross
"""
import random
import textwrap

OPENING_WORDS = ['Our', 'clear', 'strategic', 'direction', 'is', 'to', 'invoke',]

PHRASE_TABLE = (
    ("accountable",         "transition",           "leadership"),
    ("driving",             "strategy",             "implementation"),
    ("drilling down into",  "active",               "core business objectives"),
    ("next billion",        "execution",            "with our friends in <other corp.>"),
    ("creating",            "next-generation",      "franchise platform"),
    ("<big corp.>'s",       "volume and",           "value leadership"),
    ("significant",         "end-user",             "experience"),
    ("transition",          "from <small corp.>",   "to <other corp.>'s platform"),
    ("integrating",         "shared",               "services"),
    ("empowered to",        "improve and expand",   "our portfolio of experience"),
    ("deliver",             "new",                  "innovation"),
    ("ramping up",          "diverse",              "collaboration"),
    ("next generation",     "mobile",               "ecosystem"),
    ("focus on",            "growth and",           "consumer delight"),
    ("management",          "planning",             "interlocks"),
    ("necessary",           "operative",            "capabilities"),
    ("knowledge",           "optimization",         "initiatives"), 
    ("modular",             "integration",          "environment"),
    ("software",            "creation",             "processes"),
    ("agile",               "working",              "practices"),
)

INSERTS = ('for', 'with', 'and', 'as well as', 'by',
           'whilst not forgetting',
           '. Of course',
           '. To be absolutely clear',
           '. We need',
           'and unrelenting',
           'with unstoppable',
)

def get_phrase():
    """Return a phrase by choosing words at random from each column of the PHRASE_TABLE."""
    return [random.choice(PHRASE_TABLE)[i] for i in range(3)]

def get_insert():
    """Return a randomly chosen set of words to insert between phrases."""
    return random.choice(INSERTS)

def write_speech(n):
    """Write a speech with the opening words followed by n random phrases
    interspersed with random inserts."""
    phrases = OPENING_WORDS
    while n:
        phrases.extend(get_phrase())
        if n > 1:
            phrases.append(get_insert())
        n -= 1
    text = ' '.join(phrases) + '.'
    print textwrap.fill(text)

if __name__ == '__main__':
    write_speech(40)
