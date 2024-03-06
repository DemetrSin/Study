""" String "change"(it's can't be changed because of immutable type,
 so operations creates new string which can be assigned to a variable) operations """
s = 'spam'
b = s[:-1] + 'j'
print(b)  # spaj
lst = [i for i in s]
lst[0] = 'c'
m_lst = ''.join(lst)
print(m_lst)  # cpam

s = 'HelloTro!'
s = s[:5] + ' Python' + s[-1:]
print(s)  # Hello Python!
s = 'HelloTro!'
s = s[:5] + ' Everyone ' + s[5:]
print(s)  # Hello Everyone Tro!
s = 'spammy'
s = s[:3] + 'xx' + s[5:]  # or s.replace('mm', 'xx')
print(s)  # spaxxy

s = 'xxxSPAMxxxSPAMxxx'
where = s.find('SPAM')
if where != -1:
    s = s[:where] + 'EGGS' + s[(where + 4):]  # or s.replace('SPAM', 'EGGS', 1)
    print(s)  # xxxEGGSxxxSPAMxxx
else:
    print('Not found')

# Bytearray
bar = bytearray(b'spam')
bar.extend(b'eggs')
print(bar.decode())
print(s.find('ams'))
print('{1}, eggs and {0}'.format('spam', 'SPAM'))


s = r'C:\anything\txt.txt'  # raw string literal
print(s[slice(1, 3)])


""" They are same
print(chr(ord(n) + 1))
print(str(int(n) + 1))
"""


B = '1101'
I = 0
while B != '':
    I = I * 2 + (ord(B[0]) - ord('0'))
    B = B[1:]

print(int('1101', 2))  # 13
print(bin(13))  # 0b1101


s = 'HelloTro!'
sub = 'Tro!'
print(s[-len(sub):] == sub)  # True


print(''.join(sorted('something')))  # eghimnost
print([' '.join(x + '20' for x in 'something')])  # ['s20 o20 m20 e20 t20 h20 i20 n20 g20']
