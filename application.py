from flask import Flask, render_template, request, url_for
import os
import string


application = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
word_file = os.path.join(basedir, 'static/doc1.txt')

filename1 = "as.txt"
filename2 = "bs.txt"
filename3 = "cs.txt"
filename4 = "ds.txt"
filename5 = "es.txt"
filename6 = "fs.txt"
filename7 = "gs.txt"
filename8 = "hs.txt"


@application.route('/', methods=['GET', 'POST'])
def index():
    word1 = []
    text_file = ""
    number_of_words = 0
    if request.method == 'POST':
        word = request.form.get('words')
        filename = request.form.get('filename')

        word = word.lower()
        word = [''.join(c for c in s if c not in string.punctuation) for s in word]
        word = "".join(word)
        words_file = os.path.join(basedir, 'static/' + filename)
        with open(words_file, "a") as output:
            output.write(str(word))

        with open(word_file, "a") as output:
            output.write(str(word))

        text_file = filename
        with open(word_file, 'rb') as fileinput:
            for line in fileinput:
                for words in line.split():
                    word1.append(str(words)[2:-1])

        number_of_words = len(word1)

    return render_template('index.html', textfile = text_file, number = number_of_words)


@application.route('/searchocc', methods = ['GET', 'POST'])
def search_occ():
    wordss = []
    if request.method == 'POST':
        word_entered = request.form.get('word')
        with open(word_file, 'rb') as fileinput:
            for line in fileinput:
                for words in line.split():
                    wordss.append(str(words)[2:-1])
        wordss_line = " ".join(wordss)
        print(wordss_line)
        res = [i for i in range(len(wordss_line)) if wordss_line.startswith(word_entered, i)]
        print(res)
        print(len(res))
        total_length = len(res)
    return render_template('index.html', occu = total_length)


@application.route('/searchtexts', methods=['GET', 'POST'])
def search_texts():
    wordsss1 = []
    wordsss2 = []
    wordsss3 = []
    wordsss4 = []
    wordsss5 = []
    wordsss6 = []
    wordsss7 = []
    wordsss8 = []
    if request.method == 'POST':
        wordss1 = request.form.get('wordss1')
        wordss2 = request.form.get('wordss2')
        wordss3 = request.form.get('wordss3')
        wordss4 = request.form.get('wordss4')
        wordss5 = request.form.get('wordss5')
        wordss6 = request.form.get('wordss6')
        wordss7 = request.form.get('wordss7')
        wordss8 = request.form.get('wordss8')

        filename1 = request.form.get('filename1')
        filename2 = request.form.get('filename2')
        filename3 = request.form.get('filename3')
        filename4 = request.form.get('filename4')
        filename5 = request.form.get('filename5')
        filename6 = request.form.get('filename6')
        filename7 = request.form.get('filename7')
        filename8 = request.form.get('filename8')

        words_file1 = os.path.join(basedir, 'static/' + filename1)
        words_file2 = os.path.join(basedir, 'static/' + filename2)
        words_file3 = os.path.join(basedir, 'static/' + filename3)
        words_file4 = os.path.join(basedir, 'static/' + filename4)
        words_file5 = os.path.join(basedir, 'static/' + filename5)
        words_file6 = os.path.join(basedir, 'static/' + filename6)
        words_file7 = os.path.join(basedir, 'static/' + filename7)
        words_file8 = os.path.join(basedir, 'static/' + filename8)

        with open(words_file1, "a") as output:
            output.write(str(wordss1))

        with open(words_file1, 'rb') as fileinput:
            for line in fileinput:
                for words in line.split():
                    wordsss1.append(str(words)[2:-1])

        word_len1 = len(wordss1)

        with open(words_file2, "a") as output:
            output.write(str(wordss2))

        with open(words_file2, 'rb') as fileinput:
            for line in fileinput:
                for words in line.split():
                    wordsss2.append(str(words)[2:-1])

        word_len2 = len(wordss2)

        with open(words_file3, "a") as output:
            output.write(str(wordss1))

        with open(words_file3, 'rb') as fileinput:
            for line in fileinput:
                for words in line.split():
                    wordsss3.append(str(words)[2:-1])

        word_len3 = len(wordss3)

        with open(words_file4, "a") as output:
            output.write(str(wordss1))

        with open(words_file4, 'rb') as fileinput:
            for line in fileinput:
                for words in line.split():
                    wordsss4.append(str(words)[2:-1])

        word_len4 = len(wordss4)

        with open(words_file5, "a") as output:
            output.write(str(wordss5))

        with open(words_file5, 'rb') as fileinput:
            for line in fileinput:
                for words in line.split():
                    wordsss5.append(str(words)[2:-1])

        word_len5 = len(wordss5)

        with open(words_file6, "a") as output:
            output.write(str(wordss6))

        with open(words_file6, 'rb') as fileinput:
            for line in fileinput:
                for words in line.split():
                    wordsss6.append(str(words)[2:-1])

        word_len6 = len(wordss6)

        with open(words_file7, "a") as output:
            output.write(str(wordss7))

        with open(words_file7, 'rb') as fileinput:
            for line in fileinput:
                for words in line.split():
                    wordsss7.append(str(words)[2:-1])

        word_len7 = len(wordss7)

        with open(words_file8, "a") as output:
            output.write(str(wordss8))

        with open(words_file8, 'rb') as fileinput:
            for line in fileinput:
                for words in line.split():
                    wordsss8.append(str(words)[2:-1])

        word_len8 = len(wordss8)



    return render_template('index.html', len1 = word_len1, len2 = word_len2, len3 = word_len3, len4 = word_len4, len5 = word_len5, len6 = word_len6, len7 = word_len7, len8 = word_len8, files1 = filename1, files2 = filename2, files3 = filename3, files4 = filename4, files5 = filename5, files6 = filename6, files7 = filename7, files8 = filename8)


@application.route('/removestopwords', methods = ['GET', 'POST'])
def remove_stopwords():
    stops = []
    word_file1 = []
    word_files1 = []
    word_file2 = []
    word_files2 = []
    word_file3 = []
    word_files3 = []
    word_file4 = []
    word_files4 = []
    word_file5 = []
    word_files5 = []
    word_file6 = []
    word_files6 = []
    word_file7 = []
    word_files7 = []
    word_file8 = []
    word_files8 = []
    stop_words = os.path.join(basedir, 'static/shortliststopwords.txt')
    with open(stop_words, 'rb') as fileinput:
        for line in fileinput:
            for words in line.split():
                stops.append(str(words)[2:-1])

    file1 = os.path.join(basedir, 'static/'+filename1)
    with open(file1, 'rb'):
        for line in fileinput:
            for words in line.split():
                word_file1.append(str(words)[2:-1])

    initial1 = len(word_file1)
    for word in word_file1:
        if word not in stops:
            word_files1.append(word)

    after1 = len(word_files1)
    total1 = initial1 - after1

    file2 = os.path.join(basedir, 'static/' + filename2)
    with open(file2, 'rb'):
        for line in fileinput:
            for words in line.split():
                word_file2.append(str(words)[2:-1])

    initial2 = len(word_file2)
    for word in word_file2:
        if word not in stops:
            word_files2.append(word)

    after2 = len(word_files2)
    total2 = initial2 - after2

    file3 = os.path.join(basedir, 'static/' + filename3)
    with open(file3, 'rb'):
        for line in fileinput:
            for words in line.split():
                word_file3.append(str(words)[2:-1])

    initial3 = len(word_file3)
    for word in word_file3:
        if word not in stops:
            word_files3.append(word)

    after3 = len(word_files3)
    total3 = initial3 - after3

    file4 = os.path.join(basedir, 'static/' + filename4)
    with open(file4, 'rb'):
        for line in fileinput:
            for words in line.split():
                word_file4.append(str(words)[2:-1])

    initial4 = len(word_file4)
    for word in word_file4:
        if word not in stops:
            word_files4.append(word)

    after4 = len(word_files4)
    total4 = initial4 - after4

    file5 = os.path.join(basedir, 'static/' + filename5)
    with open(file5, 'rb'):
        for line in fileinput:
            for words in line.split():
                word_file5.append(str(words)[2:-1])

    initial5 = len(word_file5)
    for word in word_file5:
        if word not in stops:
            word_files5.append(word)

    after5 = len(word_files5)
    total5 = initial5 - after5

    file6 = os.path.join(basedir, 'static/' + filename6)
    with open(file6, 'rb'):
        for line in fileinput:
            for words in line.split():
                word_file6.append(str(words)[2:-1])

    initial6 = len(word_file6)
    for word in word_file6:
        if word not in stops:
            word_files6.append(word)

    after6 = len(word_files6)
    total6 = initial6 - after6

    file7 = os.path.join(basedir, 'static/' + filename7)
    with open(file7, 'rb'):
        for line in fileinput:
            for words in line.split():
                word_file7.append(str(words)[2:-1])

    initial7 = len(word_file7)
    for word in word_file7:
        if word not in stops:
            word_files7.append(word)

    after7 = len(word_files7)
    total7 = initial7 - after7

    file8 = os.path.join(basedir, 'static/' + filename8)
    with open(file8, 'rb'):
        for line in fileinput:
            for words in line.split():
                word_file8.append(str(words)[2:-1])

    initial8 = len(word_file8)
    for word in word_file8:
        if word not in stops:
            word_files8.append(word)

    after8 = len(word_files8)
    total8 = initial8 - after8
    return render_template('index.html', lens1 = total1, lens2 = total2, lens3 = total3, lens4 = total4, lens5 = total5, lens6 = total6, lens7 = total7, lens8 = total8, files1 = filename1, files2 = filename2, files3 = filename3, files4 = filename4, files5 = filename5, files6 = filename6, files7 = filename7, files8 = filename8)

if __name__ == '_main_':
    application.run()