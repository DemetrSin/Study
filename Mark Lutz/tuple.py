from collections import namedtuple

rec = namedtuple('Rec', ['name', 'age', 'jobs'])
ivan = rec('Ivan', age=20, jobs=['dev', 'mgr'])
print(ivan[0], ivan[-1])  # Ivan ['dev', 'mgr']
print(ivan.name, ivan.age)  # Ivan 20

d = ivan._asdict()  # Convert to dict
print(d)  # {'name': 'Ivan', 'age': 20, 'jobs': ['dev', 'mgr']}

t = (1, 2, 3)
print(t[:2] + (4,))  # (1, 2, 4)
print((5,) + t[1:])  # (5, 2, 3)
