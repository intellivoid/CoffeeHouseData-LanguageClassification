from googletrans import Translator
import csv
import os
import six
import sys

"""
This file takes data from input.txt file and uses Google Translate to translate
each line into a data file. This is programmed to translate from English Input
to all of the supported languages.
"""

def get_language_codes():
    codes = ["af","sq","am","ar","hy","az","eu","be","bn","bs","bg","ca","ceb","zh-CN","zh","zh-TW","co","hr","cs","da","nl","eo","et","fi","fr","fy","gl","ka","de","el","gu","ht","ha","haw","he","hi","hmn","hu","is","ig","id","ga","it","ja","jv","kn","kk","km","rw","ko","ku","ky","lo","la","lv","lt","lb","mk","mg","ms","ml","mt","mi","mr","mn","my","ne","no","ny","or","ps","fa","pl","pt","pa","ro","ru","sm","gd","sr","st","sn","sd","si","sk","sl","so","es","su","sw","sv","tl","tg","ta","tt","te","th","tr","tk","uk","ur","ug","uz","vi","cy","xh","yi","yo","zu","la"]
    return codes

def generate_data(input, current, total):
    translator = Translator()
    current_count = 0
    for language_code in progressBar(get_language_codes(), prefix='Translating:', suffix="({0}/{1})".format(current, total), length=50):
        language_code = language_code.lower()
        try:
            results = translator.translate(input, src='en', dest=language_code)
            if results.text != input:
                with open("langdetect/{0}.dat".format(language_code), mode="a", encoding="utf8") as f:
                    f.write(results.text + "\n")
                    if isinstance(results.pronunciation, six.string_types):
                        if results.pronunciation != results.text:
                            if results.pronunciation != input:
                                f.write(results.pronunciation + "\n")
            with open("langdetect/en.dat".format(language_code), mode="a", encoding="utf8") as f:
                f.write(input + "\n")
        except KeyboardInterrupt:
            print("\nCanceled")
            sys.exit()
        except:
            pass
        current_count += 1

def progressBar(iterable, prefix='', suffix='', decimals=1, length=100, fill='|', printEnd="\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    total = len(iterable)
    # Progress Bar Printing Function
    def printProgressBar (iteration):
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
        sys.stdout.flush()
    # Initial Call
    printProgressBar(0)
    # Update Progress Bar
    for i, item in enumerate(iterable):
        yield item
        printProgressBar(i + 1)
    # Print New Line on Complete
    print()

total_lines = sum(1 for line in open('input.txt', encoding="utf-8"))
current_line = 1
with open("input.txt", encoding="utf-8") as file_in:
    for line in file_in:
        generate_data(line, current_line, total_lines)
        current_line += 1
