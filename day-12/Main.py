
# CLEAR
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.clear()

print(car)

# method copy

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.copy()

print(x)
# method  fromkeys()

x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict)

# method get()

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("model")

print(x)
 # methods tems()

car = {
"brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()

print(x)

# try all of them eys(),	pop()popitem(), 	setdefault() ,	update(),	values() ;