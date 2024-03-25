def file_faker(filename, lines_num):
    with open(filename, 'w') as file:
        for x in range(lines_num):
            file.write(f"This is the {x} row of fake content\n")


def count_lines(filename):
    with open(filename) as file:
        return len(file.readlines())


def count_chars(filename):
    with open(filename) as file:
        return len(file.read())


def test(filename):
    return count_lines(filename), count_chars(filename)


# print(count_lines('t.txt'))  # 10000
# print(count_chars('t.txt'))  # 368890
# print(test('t.txt'))  # (10000, 368890)


if __name__ == '__main__':
    print(test('../../../t.txt'))








