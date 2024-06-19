
# Try them out
empty_int = int()
empty_string = str()
empty_bool = bool()
empty_float = float()

empty_list = list()
empty_set = set()

if []:
    print('It is true')
else:
    print('It is false')

# Then replace with values, 0, '', [] and actual strings numbers list and so on.

is_populated = [5,6]
if len(is_populated) > 0:
    print('do stuff')
else:
    print('is_populated is false')