#list
list = [2, 3, 4, 5]
len(list)

list[1] = 6

list.append(7)

list.remove(4)

list[2]
list[0::2]

list.extend([8,9,10,4])

list.pop()
list.insert(5,10)
list.count(4)
list.sort()
list.reverse()
list

#tuple

tuple = (12, 13, 14, 15, 15)

tuple.count(15)
tuple.index(14)

a, b = 1, 2
a
b

a, b = b, a
a
b

#dictionary
my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}

my_dict.get("c")
3

my_dict.items()
dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4)])

my_dict.keys()
dict_keys(['a', 'b', 'c', 'd'])

my_dict.pop("d")
4

my_dict.popitem()
('c', 3)

my_dict.setdefault("a", 15)
1

my_dict
{'a': 1, 'b': 2}

my_dict.setdefault("f", 25)
25

my_dict
{'a': 1, 'b': 2, 'f': 25}

my_dict.update({"c": 3, "d": 4, "e": 5})

my_dict.values()
dict_values([1, 2, 25, 3, 4, 5])

my_dict.clear()

my_dict
{}