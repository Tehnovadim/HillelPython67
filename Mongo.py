from pymongo import MongoClient

uri = "mongodb+srv://a4omg6:Iq71CGWQkMvjJnpx@cluster0.fjthjwu.mongodb.net/"

client = MongoClient(uri)

db = client['book_database']

fantasy_collection = db['fantasy_books']
school_collection = db['school_books']

fantasy_collection.delete_many({})
school_collection.delete_many({})

fantasy_book = {
    "title": "Гра престолів",
    "price": 100,
    "year": 1996,
    "pages": 694
}
fantasy_collection.insert_one(fantasy_book)

school_books = [
    {"title": "Історія України для 9 класу", "class": 9, "pages": 320},
    {"title": "Математика для 10 класу", "class": 10, "pages": 400},
    {"title": "Фізика для 11 класу", "class": 11, "pages": 280},
    {"title": "Хімія для 8 класу", "class": 8, "pages": 260},
    {"title": "Біологія для 7 класу", "class": 7, "pages": 310}
]
school_collection.insert_many(school_books)

query = {"title": {"$regex": "^Історія"}}
history_books = list(school_collection.find(query))

for book in history_books:
    print(book)
