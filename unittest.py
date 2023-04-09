
import random
from cache import *

names=["tal","omer","ori","noa","roni","sara","sol","shmuel","ron","shir","shay","sag"]
new_cache=Cache(3)
"""case1- setting a cache"""
print("---case1---")
for i in range(3):
  x=random.randint(56,100)
  name=random.choice(names)
  names.remove(name)
  new_cache.set(name,x)
  print(new_cache)
  print("_____________________")
print('\n')
"""case2- key is not in cache"""
print("---case2---")
for x in names:
  print(new_cache.get(x))
print('\n')
"""case3- get the value of a key"""
print("---case3---")
y=random.randint(0,2)
name=new_cache.array[y].key
print("the value of",str(name),"is", new_cache.get(name))
print('\n')
"""case4- adding to full cache"""
print("---case4.a---")
for i in range(3):
  x=random.randint(56,100)
  name=random.choice(names)
  names.remove(name)
  new_cache.set(name,x)
  print(new_cache)
  print("_____________________")
print('\n')
print("---case4.b---")
for i in range(3):
  x=random.randint(56,100)
  name=random.choice(names)
  names.remove(name)
  new_cache.set(name,x)
  print(new_cache)
  print("_____________________")
