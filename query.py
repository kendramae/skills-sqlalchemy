"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Start here.


# Part 2: Write queries

# Get the brand with the **id** of 8.
brand = Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
models = Model.query.filter(Model.name == 'Corvette',
                            Model.brand_name == 'Chevrolet').all()

# Get all models that are older than 1960.
old_models = Model.query.filter(Model.year > 1960).all()

# Get all brands that were founded after 1920.
brands = Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".
cor_models = Model.query.filter(Model.name.like("Cor%")).all()

# Get all brands with that were founded in 1903 and that are not yet discontinued.
brands = Brand.query.filter(Brand.founded == 1903,
                            Brand.discontinued.is_(None)).all()

# Get all brands with that are either discontinued or founded before 1950.
brands = Brand.query.filter((Brand.founded < 1950) | (Brand.discontinued.isnot(None))).all()

# Get any model whose brand_name is not Chevrolet.
models = Model.query.filter(Model.brand_name != "Chevrolet").all()

# Fill in the following functions. (See directions for more info.)


def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    models = db.session.query(Model.name,
                              Model.brand_name,
                              Brand.headquarters).join(Brand).filter(Model.year
                                                                     == year).all()

    for model, brand_name, headquarters in models:
        print "{} {}. Headquarters: {}".format(model, brand_name, headquarters)


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    brands = Brand.query.all()
    for brand in brands:
        print "{}:".format(brand.name.encode("utf-8").upper())
        models = set([m.name for m in brand.models])
        for m in models:
            print "{}".format(m)
        print "\n"


# -------------------------------------------------------------------

# Part 2.5: Advanced and Optional


def search_brands_by_name(mystr):
    string = "%" + mystr + "%"
    brands = Brand.query.filter(Brand.name.like(string)).all()
    return brands


def get_models_between(start_year, end_year):
    models = Model.query.filter(Model.year > start_year,
                                Model.year < end_year).all()
    return models

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
#           This will return a BaseQuery object that is the question itself

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
#           An association table manages the relationships between different 
#           tables in a database, teaching the program how to link the foreign key
#           in one table to the primary key of another.
