from pymongo import MongoClient
from dotenv import load_dotenv
import os

class DatabaseConnection:
    def __init__(self):
        load_dotenv()
        self.client = MongoClient(os.getenv('MONGODB_URI', 'mongodb://localhost:27017/'))
        self.db = self.client['store_management']
        self.products = self.db['products']

    def add_product(self, product_data):
        return self.products.insert_one(product_data)

    def get_all_products(self):
        return list(self.products.find())

    def update_product(self, product_id, update_data):
        return self.products.update_one({'_id': product_id}, {'$set': update_data})

    def mark_as_sold(self, product_id):
        return self.products.update_one(
            {'_id': product_id},
            {'$set': {'sold': True}}
        )

    def get_product_by_id(self, product_id):
        return self.products.find_one({'_id': product_id})

    def get_products_by_category(self, category):
        return list(self.products.find({'category': category}))