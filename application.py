from flask import Flask, render_template, request, url_for
import os
import string


application = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
word_file = os.path.join(basedir, 'static/doc1.txt')


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

if __name__ == '_main_':
    application.run()