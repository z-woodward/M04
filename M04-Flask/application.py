from flask import Flask
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


class books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(250), nullable=False)
    author = db.Column(db.String(80), nullable=False)
    publisher = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f"{self.id} - {self.book_name} - {self.author} - {self.publisher}"

@app.route('/')
def hello_world():
    return "asdfadsfa dsfadsfa hello world aaaaaaaahhh oh no i'm dying" 

@app.route('/books')
def get_books():
    book = books.query.all()
    output = []
    for books in book:
        books_data = {'id':book.id,'book_name':book.book_name,'author':book.author,'publisher':book.publisher}
    output.append(books_data)
    return output