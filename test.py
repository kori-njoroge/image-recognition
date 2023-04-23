from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# create the database engine
db_string = "mysql+pymysql://root:MyPass@localhost:3306/imageDB"
engine = create_engine(db_string)

# create the session
Session = sessionmaker(bind=engine)
session = Session()

# create the declarative base
Base = declarative_base()

# define a class for the products table
class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    barcode = Column(String)
    description = Column(String)

# query the database for a product with a specific barcode
barcode = '6161101861168'
product = session.query(Product).filter_by(barcode=barcode).first()

# print the description of the product
print(product.description)
