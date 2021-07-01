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

        word = word.lower()
        word = [''.join(c for c in s if c not in string.punctuation) for s in word]
        word = "".join(word)
        with open('static/doc1.txt', "w") as output:
            output.write(str(word))

        text_file = "doc1.txt"
        with open(word_file, 'rb') as fileinput:
            for line in fileinput:
                for words in line.split():
                    word1.append(str(words)[2:-1])

        number_of_words = len(word1)

    return render_template('index.html', textfile = text_file, number = number_of_words)


if __name__ == '_main_':
    application.run()