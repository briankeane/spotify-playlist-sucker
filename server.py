from flask import Flask, redirect, url_for, request, render_template
import os

app = Flask(__name__)
PORT = os.environ.get('PORT') or 5000

@app.route('/')
def todo():
  return render_template('todo.html', items=items)


@app.route('/new', methods=['POST'])
def new():
    return redirect(url_for('todo'))


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=PORT, debug=True)