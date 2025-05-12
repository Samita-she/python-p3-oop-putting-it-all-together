from flask import Flask
from lib.book import Book
from lib.shoe import Shoe

app = Flask(__name__)

@app.route('/')
def home():
    book = Book("Python OOP", 250)
    shoe = Shoe("Adidas", 9)
    shoe.cobble()
    return f"""
    <h1>My OOP Project</h1>
    <p>Book: {book.title}, {book.page_count} pages</p>
    <p>Shoe: {shoe.brand}, size {shoe.size}, condition: {shoe.condition}</p>
    """

if __name__ == '__main__':
    app.run(debug=True)
