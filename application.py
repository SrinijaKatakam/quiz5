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


@application.route('/searchoccurances', methods = ['GET', 'POST'])
def search_occurances():
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



if __name__ == '_main_':
    application.run()