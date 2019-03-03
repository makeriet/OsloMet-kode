#source: https://gist.githubusercontent.com/mick001/aaf569cd0f027d511782/raw/9b08b6b728bc1b95d02dffe2c01d6461bfc9d942/letter_frequency.py
# The following code takes as input a string of text, and then it outputs the barplot of the
# frequencies of occurrence of letters in the string.
import pylab as pl
import numpy as np

string1 = """ Example string """

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",".",",",";","-","_","+"]

# The following functon takes a list and a string of characters, it calculates how often a certain character appears
# and then it outputs a list with character and frequency

def frequencies(string,letters):
    list_frequencies = []
    for letter in letters:
        freq = 0
        for i in string:
            if i == letter:
                freq += 1
        if freq != 0:
            list_frequencies.append(letter)
            list_frequencies.append(freq)
    return list_frequencies

print(frequencies(string1,alphabet))

# This function returns a list containing 2 lists with letter and frequencies
def fix_lists_letter(list_1):
    list_letters = []
    list_letters.append(list_1[0])
    list_freq = []
    for i in range(1,len(list_1)):
        if i % 2 == 0:
            list_letters.append(list_1[i])
        else:
            list_freq.append(list_1[i])
    if len(list_letters) != len(list_freq):
        return "Some error occurred"
    else:
        final_list = [list_letters,list_freq]
        return final_list

first_count = frequencies(string1,alphabet)

final = fix_lists_letter(first_count)

letter_s = final[0]
freq = final [1]

print("Number of character used:",sum(freq), sep=" ")

# Enable the following to sort (in descending order)
"""
#The follwing function sorts the letters and frequencies in descending order.
def sort_all(c):
    letters = c[0]
    freq = c[1]
    final_letter = []
    final_freq = []
    for i in range(0,len(letters)):
        maximum = max(freq)
        ind = freq.index(maximum)
        final_freq.append(freq[ind])
        final_letter.append(letters[ind])
        letters.remove(letters[ind])
        freq.remove(freq[ind])

    to_return = [final_letter,final_freq]
    return to_return


the_very_final = sort_all(final)

letter_s = the_very_final[0]
freq = the_very_final[1]"""


# Relative frequencies
def get_rel_freq(list_1):
    list_to_ret = []
    for i in list_1:
        list_to_ret.append(i/sum(list_1))
    return list_to_ret

freq = get_rel_freq(freq)


fig = pl.figure()
ax = pl.subplot(111)
width=0.8
ax.bar(range(len(letter_s)), freq, width=width)
ax.set_xticks(np.arange(len(letter_s)) + width/2)
ax.set_xticklabels(letter_s, rotation=45)
pl.show()
