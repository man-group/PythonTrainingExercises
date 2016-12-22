"""Given a (large) list of floats use a dict as a histogram to count how many
values fall into buckets for any given bucket size. 

Supposing we had a large stream of floats that fell into a normal distribution
then with a bucket size of 1 we might end up with a dictionary like this:

{-5: 9,
 -4: 233,
 -3: 5987,
 -2: 60325,
 -1: 242432,
 0: 383289,
 1: 241275,
 2: 60198,
 3: 6011,
 4: 238,
 5: 3}

So create a function float_list_to_int_dict(lst, bucket_size) that takes a list
of floats and a bucket_size and returns a dictionary that has a count of
how many items fall into each bucket.

Now create a function pformat_histogram() that will pretty format this dictionary
to produce something like this:

-5.000 [     9]: 
-4.000 [   233]: 
-3.000 [  5987]: +
-2.000 [ 60325]: ++++++++++
-1.000 [242432]: ++++++++++++++++++++++++++++++++++++++++
 0.000 [383289]: +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 1.000 [241275]: ++++++++++++++++++++++++++++++++++++++++
 2.000 [ 60198]: ++++++++++
 3.000 [  6011]: +
 4.000 [   238]: 
 5.000 [     3]: 


Created on 11 Mar 2015

@author: paulross
"""
import pprint
import random


def float_list_to_int_dict(lst, bucket_size):
    """Takes a list of floats and a bucket size and return a dict of
    { n : count, ...} where the count is the number of floats that drop into
    the range (n - 0.5) * bucket_size to (n + 0.5) * bucket_size."""
    # Your code goes here
    pass


def pprint_histogram(d, bucket_size, char='+', width=80, key_format='%6.3f'):
    """Pretty prints a dict of {key : count, ...} as ASCII.
    d is the dictionary that has the histogram counts.
    bucket_size is the size of each bucket represented by a difference of 1
    in the keys.
    char is the character to use for the histogram bars.
    width is the total width to use.
    key_format is used to turn the keys into strings."""
    print pformat_histogram(d, bucket_size, char, width, key_format)


def pformat_histogram(d, bucket_size, char='+', width=80, key_format='%6.3f'):
    """Pretty formats a dict of {key : count, ...} as ASCII.
    d is the dictionary that has the histogram counts.
    bucket_size is the size of each bucket represented by a difference of 1
    in the keys.
    char is the character to use for the histogram bars.
    width is the total width to use.
    key_format is used to turn the keys into strings.
    
    Returns a string."""
    # Your code goes here
    pass


def test_histogram_simple():
    values = [-2.0, -0.2, 0.0, 1.8, 2.0]
    bucket_size = 1
    histogram = float_list_to_int_dict(values, bucket_size)
    assert histogram == {-2: 1,
                         0: 2,
                         2: 2}


def test_histogram():
    values = [1.5438112059081175, 0.6494375526544238, 0.3457995816672214, -0.5328016134856572, -0.15124684525892165, 0.055610141637873305, 1.0290716525246435, 2.0385485579335545, 0.5281713827986787, 0.26331737617888923, -0.3162378783792704, -0.13835527247331939, 0.4490004636681801, 1.3122453585491205, -0.7196019736756133, -0.11661563398690139, -0.5677482364379377, 0.749029543109979, 0.910085838639317, 0.8148883411787945, -1.5759430241817372, 2.149666436616569, -1.3046970061256313, 0.6589858706427383, -1.0550594279416063, 0.2770195541422566, -1.3559250487938659, 0.6373992354814844, 0.3657518733471363, -1.9756587467724296, -0.916178882398654, -1.2115581719658575, -0.5752228942330344, -1.2146731128065653, 0.7350887236603592, -0.3082243430161092, 0.02160447542773487, -0.4549593183317705, -0.8934022565227727, -1.073981596425933, 1.1452692936732256, -0.6786531561539697, -1.971842628806122, 0.22891758722239547, 1.0198578524245387, 1.0019792366478892, 2.2264666681953496, 2.1230414868475966, -1.003801877583345, -1.5158494238545173, 2.155614209647323, 0.7482365402519784, -1.547240638533447, 0.01827226874451755, 0.10764719293616144, -0.30641541811062334, -1.0491048731752368, 0.8960453604847319, 1.1162689067770881, 2.170041603926618, -0.29848058939753136, -1.6994076363037336, -0.29325382005874895, -0.5022337237819419, 1.3062825900700044, 1.1200804188027949, 1.849134185794878, -0.7332979938648806, -0.425243909755029, -0.8069682149370704, 1.016071036651794, 0.26760166497202886, 0.03669697806950532, 1.6357237566279519, 0.8683313396582628, -1.3841908940052248, -1.8547580521742189, -0.12260109388841045, 0.90414527150969, -0.12079089331719184, -0.058742003617983325, -0.023250196761608836, 0.3211494350119429, -0.5907952315211763, -0.7237073332612101, 0.5182478134628232, 0.010271980116704302, -0.019275927339157204, 0.9025617739410835, -0.6700041398586063, -0.3634824189459107, 0.9832516052105776, 0.06754447913160126, 0.29004512289550716, 0.5296979829965157, 0.7698954921507436, 0.6723461101009319, 0.014768902653309594, 0.36202284090075454, 0.2964558028689242]
    bucket_size = 1
    histogram = float_list_to_int_dict(values, bucket_size)
    assert """-2.000 [ 7]: +++++++++++++
-1.000 [22]: ++++++++++++++++++++++++++++++++++++++++++
 0.000 [35]: +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 1.000 [27]: ++++++++++++++++++++++++++++++++++++++++++++++++++++
 2.000 [ 9]: +++++++++++++++++""" == pformat_histogram(histogram, bucket_size)


def main():
    LEN = 1000000
    bucket_size = 1
    # This will give us a normal distribution centred around 0.0 with a standard
    # deviation of 1.0
    mu, sigma = 0.0, 1.0
    lst = [random.normalvariate(mu, sigma) for _ in range(LEN)]
    d = float_list_to_int_dict(lst, bucket_size)
    pprint.pprint(d)
    pprint_histogram(d, bucket_size)


if __name__ == '__main__':
    main()
