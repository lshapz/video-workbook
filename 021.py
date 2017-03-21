# dictionary comprehension

d = {"a": 1, "b": 2, "c": 3}


c = {k: v for k, v in d.items() if v <=1}
print(c)
#d.items()