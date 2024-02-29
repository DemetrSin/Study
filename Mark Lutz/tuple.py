from collections import namedtuple

rec = namedtuple('Rec', ['name', 'age', 'jobs'])
ivan = rec('Ivan', age=20, jobs=['dev', 'mgr'])
print(ivan[0], ivan[-1])  # Ivan ['dev', 'mgr']
print(ivan.name, ivan.age)  # Ivan 20

d = ivan._asdict()  # Convert to dict
print(d)  # {'name': 'Ivan', 'age': 20, 'jobs': ['dev', 'mgr']}