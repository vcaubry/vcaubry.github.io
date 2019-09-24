from flask_frozen import Freezer
from app import app

freezer = Freezer(app)

# @freezer.register_generator
# def product_details():
#     for product in models.Product.all():
#         yield {'product_id': product.id}


if __name__ == '__main__':
    freezer.freeze()