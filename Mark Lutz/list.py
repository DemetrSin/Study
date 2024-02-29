matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print([matrix[i][i] for i in range(3).__reversed__()])
sum_gen = (sum(row * 2) for row in matrix)
print([i for i in sum_gen])
print(list(map(sum, matrix)))


l = list('spam and param')
l[4: 8] = []  # deletion
print(l)


# CHAPTER 7
initial_lst = [1, 2, 3]
lst_to_add = [4, 5, 6]
print(initial_lst + lst_to_add)  # [1, 2, 3, 4, 5, 6]
print(initial_lst * 2)  # [1, 2, 3, 1, 2, 3]
print(str(initial_lst) + '34')  # type str! [1, 2, 3]34
print(initial_lst + list('34'))  # [1, 2, 3, '3', '4']
print(list(map(lambda x: x * 2, initial_lst)))  # [2, 4, 6]
initial_lst[1:]  # Statement seems to have no effect cause of ⇓
sliced_lst = initial_lst[1:]  # slice everytime return NEW lst
print(sliced_lst)  # [2, 3]

new_lst = [1, '2', [3], {4}, {5: 'five'}]
print(new_lst)
d = new_lst[-1]  # Lists index returns AN OBJECT!
print(type(d))  # <class 'dict'>
new_lst[1:3] = {'some': 'value', 'another': 'value'}  # it takes only keys
print(new_lst)  # [1, 'some', 'another', {4}, {5: 'five'}]
new_lst[1:3] = {'some': 'value'}, {'another': 'value'}  # it takes dicts
print(new_lst)  # [1, {'some': 'value'}, {'another': 'value'}, {4}, {5: 'five'}]
new_lst[1:3] = {}  # it deletes sliced objects
print(new_lst)  # [1, {4}, {5: 'five'}]
new_lst = [1, '2', [3], {4}, {5: 'five'}]
new_lst[1:3] = {'some': 'value', 'another': 'value', 1: '1', 2: '2'}
print(new_lst)  # [1, 'some', 'another', 1, 2, {4}, {5: 'five'}]
new_lst[1:3] = [1, '2', '22', 45, 56]
print(new_lst)  # [1, 1, '2', '22', 45, 56, 1, 2, {4}, {5: 'five'}]
new_lst = [1, '2', [3], {4}, {5: 'five'}]
new_lst[1:3] = (45, 25, 48), (29, [66]), (78,)
print(new_lst)  # [1, (45, 25, 48), (29, [66]), (78,), {4}, {5: 'five'}]
initial_lst[1:2] = [[4, 5]]  # replace/insert
print(initial_lst)  # [1, [4, 5], 3]
initial_lst = [1, 2, 3]
initial_lst[1:1] = [[4, 5]]  # just insert
print(initial_lst)  # [1, [4, 5], 2, 3]
initial_lst = [1, 2, 3]
initial_lst[1:2] = []  # deletion
print(initial_lst)  # [1, 3]


new_lst = [1, '2', [3], {4}, {5: 'five'}]
initial_lst = [1, 2, 3]
initial_lst[:0] = new_lst  # insert to start
print(initial_lst)  # [1, '2', [3], {4}, {5: 'five'}, 1, 2, 3]

initial_lst = [1, 2, 3]
initial_lst[len(initial_lst):] = new_lst  # insert to end
print(initial_lst)  # [1, 2, 3, 1, '2', [3], {4}, {5: 'five'}]

initial_lst = [1, 2, 3]
initial_lst.extend(new_lst)  # also insert to end
print(initial_lst)  # [1, 2, 3, 1, '2', [3], {4}, {5: 'five'}]

initial_lst = [1, 2, 3]
initial_lst.append(new_lst)  # it appends exactly list as object without unpack
print(initial_lst)  # [1, 2, 3, [1, '2', [3], {4}, {5: 'five'}]]

# Method .sort() Make changes in place in list
lst_for_sort = ['aBe', 'abc', 'ABD']
lst_for_sort.sort()
print(lst_for_sort)  # ['ABD', 'aBe', 'abc']
lst_for_sort.sort(key=str.lower)
print(lst_for_sort)  # ['abc', 'ABD', 'aBe']

# Embedded function sorted() returns new list
lst_for_sort = ['aBe', 'abc', 'ABD']
lst = sorted(lst_for_sort, key=str.lower)  # makes new lst without changing in objects
print(lst)  # ['abc', 'ABD', 'aBe']
lst = sorted([x.lower() for x in lst_for_sort])  # makes changes in objects!
print(lst)  # ['abc', 'abd', 'abe']

"""Append and pop often makes LIFO logic"""