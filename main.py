# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from flask import render_template, redirect, url_for
from app import create_app
app = create_app()


@app.route("/index")
def index():
    return render_template('index.html')


@app.route("/")
def main():
    return redirect(url_for('index'))


if __name__ == '__main__':
  app.run(port=5001, host='0.0.0.0')

