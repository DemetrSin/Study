import pickle


with open('some.txt', 'w') as file:
    for line in range(10):
        file.write('some text\n')

with open('some.txt', 'r') as file:
    for line in file:
        print(line.rstrip())

n = 45
s = 'spam'
d = {'b': 1, 2: 'a'}
l = [1, '25', {49: 50}]
s = {1, 2, 3}

with open('some.txt', 'w') as file:
    file.write(f"{str(n)}\n {s}\n {str(d)}\n {str(l)}\n {str(s)}\n")

sd = "{'b': 1, 2: 'a'}"
ev = eval(sd)
print(ev['b'])  # 1


# Pickle
d = {1: '1', 2: '2'}
with open('data.pkl', 'wb') as file:
    pickle.dump(d, file)


with open('data.pkl', 'rb') as file:
    v = pickle.load(file)
    print(v)  # {1: '1', 2: '2'}
