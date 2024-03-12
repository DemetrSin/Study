import sqlite3 as sq
import random
from faker import Faker


def generate_random_users(num_users):
    faker = Faker()
    user_data = []
    for _ in range(num_users):
        name = faker.name()
        sex = random.choice((1, 2))
        age = random.randint(18, 80)
        score = random.randint(100, 2000)
        user_data.append((name, sex, age, score))
    return user_data


def generate_random_ratings(num_ratings):
    ratings_lst = []
    for _ in range(1, num_ratings + 1):
        user_id = _
        score = random.randint(200, 4000)
        time = random.randint(100000, 200000)
        ratings_lst.append((user_id, score, time))
    return ratings_lst


def read_ava(n):
    try:
        with open(f"ava/{n}.png", 'rb') as f:
            return f.read()
    except IOError as e:
        print(e)
        return False


def write_ava(name, data):
    try:
        with open(name, 'wb') as f:
            f.write(data)
    except IOError as e:
        print(e)
        return False

    return True


# with sq.connect('saper.db') as con:
#     cur = con.cursor()

    # cur.execute("""DROP TABLE IF EXISTS users""")
    # cur.execute("""CREATE TABLE IF NOT EXISTS users(
    # name TEXT NOT NULL,
    # sex INTEGER NOT NULL DEFAULT 1,
    # age INTEGER,
    # score INTEGER
    # )""")

    # cur.execute("""
    # SELECT * FROM users
    # WHERE old IN (20, 26) AND score > 1000 OR sex == 1
    # ORDER BY score DESC
    # LIMIT 2
    #  """)
    # result2 = cur.fetchone()
    # result = cur.fetchall()
    # print(result, result2)
    #
    # cur.execute("""UPDATE users SET score = 0""")
    # cur.execute("""UPDATE users SET score = 1000 WHERE user_id = 1""")
    # cur.execute("""UPDATE users SET score = score + 500 WHERE user_id > 1""")
    # cur.execute("""UPDATE users SET score = score + 700 WHERE name LIKE 'Linda'""")
    # cur.execute("""UPDATE users SET score = score + 100 WHERE name LIKE 'D%'""")
    # cur.execute("""UPDATE users SET score = score + 100 WHERE name LIKE 'P_t%'""")
    # cur.execute("""UPDATE users SET score = 800, old = 33 WHERE old > 27""")

    # cur.execute("DROP TABLE IF EXISTS games")
    # cur.execute("""
    # CREATE TABLE IF NOT EXISTS games(
    # user_id INTEGER,
    # score INTEGER,
    # time INTEGER
    # )""")

    # data_to_insert = [
    #     (1, 1001, 50),
    #     (2, 1002, 60),
    #     (3, 1003, 70),
    # ]
    #
    # cur.executemany("INSERT INTO games (user_id, score, time) VALUES (?, ?, ?)", data_to_insert)

    # user_data = generate_random_users(10)
    #
    # cur.executemany("""INSERT INTO users (name, sex, age, score) VALUES (?, ?, ?, ?)""", user_data)

    # ratings_data = generate_random_ratings(10)
    # cur.executemany("INSERT INTO games (user_id, score, time) VALUES (?, ?,?)", ratings_data)

    # cur.execute("""
    # SELECT name, sex, games.score FROM games
    # JOIN users ON games.user_id = users.rowid
    # """)

    # cur.execute("""
    # SELECT name, sex, sum(games.score) as score
    # FROM games
    # JOIN users ON games.user_id = users.rowid
    # GROUP BY user_id
    # ORDER BY score DESC
    # """)

    # cur.execute("""
    # SELECT score, smth FROM tab1
    # UNION SELECT val, type FROM tab2""")


cars_data = [
    ("Toyota Camry", 25000),
    ("Honda Accord", 27000),
    ("Ford Mustang", 35000),
    ("Chevrolet Corvette", 65000),
    ("Tesla Model 3", 45000)
]


# with sq.connect('another.db') as con:
#     con.row_factory = sq.Row
#     cur = con.cursor()

    # cur.execute("DROP TABLE IF EXISTS cars")

    # cur.execute("""
    #     CREATE TABLE IF NOT EXISTS cars(
    #     car_id INTEGER PRIMARY KEY AUTOINCREMENT,
    #     model TEXT,
    #     price INTEGER
    #     )""")

    # cur.execute("""INSERT INTO cars VALUES(1, 'Audi', 90000)""")
    # cur.execute("""INSERT INTO cars VALUES(2, 'Mercedes', 100000)""")
    # cur.execute("""INSERT INTO cars VALUES(3, 'Porshe', 200000)""")
    # cur.execute("""INSERT INTO cars VALUES(4, 'Toyota', 60000)""")

    # OR

    # for car in cars_data:
    #     cur.execute("INSERT INTO cars VALUES(NULL, ?, ?)", car)

    # OR

    # cur.executemany("INSERT INTO cars VALUES(NULl, ?, ?)", cars_data)


    # cur.execute("UPDATE cars SET price = :Price WHERE model LIKE 'T%'", {'Price': 0})

    # cur.executescript("""
    # DELETE FROM cars WHERE model LIKE 'H%';
    # UPDATE cars SET price = price + 300
    #  """)

    # cur.execute("CREATE TABLE IF NOT EXISTS cust (name TEXT, tr_in INTEGER, buy INTEGER)")
    #
    # cur.execute("INSERT INTO cars VALUES(NULL, 'Zapor', 1000)")
    # last_row_id = cur.lastrowid
    # buy_car_id = 2
    # cur.execute("INSERT INTO cust VALUES('Amid', ?, ?)", (last_row_id, buy_car_id))

    # cur.execute("SELECT model, price FROM cars")
    # row = cur.fetchone()
    # rows3 = cur.fetchmany(3)
    # rows = cur.fetchall()
    # print(row, rows3, rows)
    # print(cur.__next__())
    # for c in cur:
    #     print(c['model'], c['price'])


with sq.connect('another.db') as con:
    con.row_factory = sq.Row
    cur = con.cursor()

    con.executescript("""
        CREATE TABLE IF NOT EXISTS users(
        name TEXT,
        ava BLOB,
        score INTEGER
        )""")

    # img = read_ava('img')
    # if img:
    #     binary = sq.Binary(img)
    #     cur.execute("INSERT INTO users VALUES('Nick', ?, 1000)", (binary,))

    # cur.execute("SELECT ava FROM users LIMIT 1")
    # img = cur.fetchone()['ava']
    #
    # write_ava('out.png', img)


with sq.connect('another.db') as con:
    cur = con.cursor()

    for sql in con.iterdump():
        print(sql)


# con = None
# try:
#     con = sq.connect('test.db')
#     cur = con.cursor()
#
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#         );
#         BEGIN;
#         INSERT INTO cars VALUES(1, 'Audi', 90000);
#         INSERT INTO cars VALUES(2, 'BMW', 85000);
#         INSERT INTO cars VALUES(3, 'Mercedes-Benz', 95000);
#         INSERT INTO cars VALUES(4, 'Toyota', 30000);
#         INSERT INTO cars VALUES(5, 'Honda', 28000);
#         INSERT INTO cars VALUES(6, 'Ford', 32000);
#         INSERT INTO cars VALUES(7, 'Chevrolet', 34000);
#         UPDATE cars SET price = price + 1
#     """)
#
#     con.commit()
#
# except sq.Error:
#     if con: con.rollback()
#     print('Connection Error')
# finally:
#     if con: con.close()


