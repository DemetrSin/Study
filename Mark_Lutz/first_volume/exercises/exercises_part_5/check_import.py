import exercise_part_5


print([x for x in exercise_part_5.__dict__ if not x.startswith('__')])
# ['file_faker', 'count_lines', 'count_chars', 'test']
print(dir(exercise_part_5))
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__',
# '__package__', '__spec__', 'count_chars', 'count_lines', 'file_faker', 'test']
