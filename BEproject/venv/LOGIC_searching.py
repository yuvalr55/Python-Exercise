from collections import Counter, OrderedDict
from os import listdir
from os.path import isfile, join


def scan_regular_file(mypath):
    try:
        for file in listdir(mypath):
            if isfile(join(mypath, file)):
                yield str(mypath + '\\' + file)

    except Exception as err:
        print(err)


def each_words_from_file(mypath):
    try:
        for file in scan_regular_file(mypath):
            with open(file, 'r') as path_dir:
                all_words = list(path_dir.read().split())
            list_each_word = []
            for word in all_words:
                result = "".join((char if char.isalpha() else "") for char in word.lower())
                list_each_word.append(result)
            for word, count in Counter(list_each_word).items():
                if count == 1:
                    yield word

    except Exception as err:
        print(err)


def reading_and_append_lines(pathWordsFile, mypath):
    try:
        with open(str(pathWordsFile), "w+") as txt:
            txt.writelines(''.join(f'{word}\n' for word in each_words_from_file(mypath)))
            txt.seek(0)
            lines = txt.readlines()
        return lines

    except Exception as err:
        print(err)


def sort_a_list_of_lines(pathWordsFile, pathDirectory):
    try:
        lines = reading_and_append_lines(pathWordsFile=pathWordsFile, mypath=pathDirectory)
        listLines = list(map(lambda s: s.strip(), lines))
        counterWords = Counter(listLines)
        return list(OrderedDict(sorted(counterWords.items(), key=lambda t: t[1], reverse=True)).items())

    except Exception as err:
        print(err)
