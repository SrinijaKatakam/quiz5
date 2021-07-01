from flask import Flask, render_template, request, url_for
import os


application = Flask(__name__)


basedir = os.path.abspath(os.path.dirname(__file__))
words1 = os.path.join(basedir, 'static/AliceCleaneredit.txt')
words2 = os.path.join(basedir, 'static/AliceInWonderlandedit.txt')
words3 = os.path.join(basedir, 'static/CandideEnedit.txt')
words4 = os.path.join(basedir, 'static/CandideFredit.txt')


@application.route('/', methods=['GET', 'POST'])
def index():
    print("hello there")
    return render_template('index.html')


@application.route('/searchword', methods=['GET', 'POST'])
def search_word():
    word1 = []
    word2 = []
    word3 = []
    word4 = []
    files = []
    wordss1 = []
    wordss2 = []
    wordss3 = []
    wordss4 = []

    if request.method == 'POST':
        query_word = request.form.get('words')

        with open(words1, 'rb') as fileinput:
            for line in fileinput:
                for words in line.split():
                    word1.append(str(words))
        for values in word1:
            wordss1.append(values[2:-1])

        print(wordss1)

        if query_word in wordss1:
            movie_title1 = "AliceCleaneredit.txt"
            files.append(movie_title1)

        with open(words2, 'rb') as fileinput:
            for line in fileinput:
                for words in line.split():
                    word2.append(str(words))

        for values in word2:
            wordss2.append(values[2:-1])

        print(wordss2)

        if query_word in wordss2:
            movie_title2 = "AliceInWonderlandedit.txt"
            files.append(movie_title2)

        with open(words3, 'rb') as fileinput:
            for line in fileinput:
                for words in line.split():
                    word3.append(str(words))

        for values in word3:
            wordss3.append(values[2:-1])

        print(wordss3)

        if query_word in wordss3:
            movie_title3 = "CandideEnedit.txt"
            files.append(movie_title3)

        with open(words4, 'rb') as fileinput:
            for line in fileinput:
                for words in line.split():
                    word4.append(str(words))

        for values in word4:
            wordss4.append(values[2:-1])

        print(wordss4)

        if query_word in wordss4:
            movie_title4 = "CandideFredit.txt"
            files.append(movie_title4)

    return render_template("search_word.html", file = files)


if __name__ == '__main__':
    application.run()
