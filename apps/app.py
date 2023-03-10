from address.models import Address
from category.models import Category
from comments.models import Comment
from ecommerce_api.factory import app, db
from file_uploads.models import FileUpload, ProductImage, TagImage, CategoryImage
from orders.models import Order
from products.models import Product
from routes import blueprint
from tags.models import Tag
from users.models import User


app.register_blueprint(blueprint, url_prefix="/api")


@app.shell_context_processor
def make_shell_context():
    return dict(
        app=app,
        db=db,
        User=User,
        address=Address,
        order=Order,
        product=Product,
        tag=Tag,
        category=Category,
        comment=Comment,
        file_upload=FileUpload,
        tag_image=TagImage,
        category_image=CategoryImage,
        product_image=ProductImage,
    )


"""
Not used, to seed the database, it is as easy as running the seed_database.py python script
import click
import sys
@app.cli.command()
@click.option('--seed', default=None, help='seed the database')
def seed_db(value):
    sys.stdout.write('seed the database')
"""

if __name__ == "__main__":
    app.run(port=8080)
