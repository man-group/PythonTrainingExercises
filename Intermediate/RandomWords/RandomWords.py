"""Write a function that randomises letters in words after the first N letters.

It will be called randomWords(words, n) where words is a list of words and n
the number of leading letters of each word to keep in order the remainder are
to be randomly jumbled up.

The code in main will call your function with different values of n to see
how much unscrambled text in each word you need to understand it.

Example:
Words please, <cr> to exit: Numeric is a hedge fund operating out of offices in Boston
   0: imeNucr si a deghe dfnu rntpigeao out of ifosfce in otnBso
   1: Nmuerci is a hedeg fudn oantrgiep out of ofsfcie in Bontos
   2: Nucermi is a heedg fudn opertaign out of ofiscfe in Botson
   3: Numrcei is a hedge fund operantgi out of offseic in Boston
   4: Numeicr is a hedge fund operingat out of offisec in Bostno
   5: Numeric is a hedge fund operaigtn out of offices in Boston
   6: Numeric is a hedge fund operatngi out of offices in Boston
   7: Numeric is a hedge fund operating out of offices in Boston
   8: Numeric is a hedge fund operating out of offices in Boston

So you need about 4 or so letters to understand the sentence.

HINT: The random module is useful, it has a function shuffle(sequence) that
return the sequence randomly shuffled. 

Created on 26 Feb 2015

@author: paulross
"""
import random

def randomWords(words, n):
    pass

def main():
    # Loop round until the user just gives a <cr> i.e. enter response.
    while True:
        line = raw_input('Words please, <cr> to exit: ')
        words = line.split()
        if len(words) == 0:
            # User wants to quit
            break
        max_len = max([len(w) for w in words])
        for n in range(max_len):
            print '%4d: %s' % (n, ' '.join(randomWords(words, n)))

if __name__ == '__main__':
    main()
    print 'Bye, bye.'
