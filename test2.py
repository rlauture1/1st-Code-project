f = open("myfile303.py", "w")
mylist = [1, 2 ,6 ,56, 78]
f.write("\n".join(map(lambda x: str(x), mylist)))
f.close()