import psycopg2

c = psycopg2.connect(
    host='Localhost',
    dbname='sp3',
    user='postgres',
    password='1234')
cur = c.cursor()

"""
Functie voor het aanmaken Postgres DB tabel.
"""

def create_table(): # hoeft maar één keer gedraait te worden,        --create_fav_category
    cur.execute("DROP TABLE IF EXISTS similar_products")
    cur.execute('CREATE TABLE similar_profile ('
                'id varchar PRIMARY KEY,'
                'product1 varchar,'
                'product2 varchar,'
                'product3 varchar,'
                'product4 varchar,'
                'product5 varchar);')
    c.commit()

def filtering(product, type):
    # Query die alle ids ophaalt waar die id != product en category_idcatergory = categorie
    cur.execute("SELECT id FROM products"
                " WHERE type = '{}' AND id != '{}'".format(type, product)
                )
    x = cur.fetchall()

    # Stopt alle id's in een lijst, en haalt daar 5 willekeurige waardes uit
    list_products = []
    for i in x:
        list(i)
        list_products.append(i[0])

    if len(list_products) < 5:
        return [product, product, product, product, product, product]
    else:
        p1 = list_products[0]
        p2 = list_products[1]
        p3 = list_products[2]
        p4 = list_products[3]
        p5 = list_products[4]

        return [product, p1, p2, p3, p4, p5]

def fill_table():
    cur.execute('SELECT id, type FROM products')
    list_products = cur.fetchall()

    count = 0

    for ids in list_products:
        product = list(ids)

        list_products = filtering(product[0], product[1])

        try:
            cur.execute("INSERT INTO similar_products(id, p1, p2, p3, p4, p5)"
                        "VALUES ('{}','{}','{}','{}','{}','{}')".format(list_products[0], list_products[1], list_products[2],
                                                                        list_products[3], list_products[4], list_products[5]))
        except:
            print(product[0], product[1])
        c.commit()


def loop():
    create_table()
    fill_table()
    cur.close()

