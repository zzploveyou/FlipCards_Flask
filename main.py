from flask import Flask, render_template
import csv
import os
import sys
app = Flask(__name__)
PATH = os.path.dirname(os.path.realpath(__file__))


@app.route('/')
def main():
    filename = sys.argv[1]
    words = []
    with open(filename) as f:
        reader = csv.reader(f)
        for items in reader:
            if not items[0].startswith("#"):
                words.append(items)
    return render_template('index.html', words=words)


if __name__ == '__main__':
    app.run()
