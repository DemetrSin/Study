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


with sq.connect('saper.db') as con:
    cur = con.cursor()

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

    cur.execute("""
    SELECT name, sex, games.score FROM games
    JOIN users ON games.user_id = users.rowid
    """)
