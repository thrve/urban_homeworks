#!/usr/bin/env python


my_dict = {
    'apple': 'яблоко',
    'pineapple': 'ананас',
    'orange': 'апельсин',
    'banana': 'банан',
    'watermelon': 'арбуз',
}

print(my_dict)
print(my_dict['apple'])
print(my_dict.get('melon'))
my_dict['grape'] = 'виноград'
my_dict['melon'] = 'дыня'
my_dict.pop('banana')
print(my_dict)


my_set = {1, 'wtf', True, 1, 3, 5, 1}
print(my_set)
my_set.add(False)
my_set.add(2.7)
print(my_set)
my_set.remove('wtf')
print(my_set)
