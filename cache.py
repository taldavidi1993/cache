"""
Implement a cache class that stores given item. The cache is limited to a given `size` and will discard the
least recently used item if it needs the space.

Clearly document design choices, algorithm and possible optimizations.
While we require you to implement one memory allocation algorithm,
also document future looking design considerations.

Implementation Notes:
* While the interface below is written in Python, feel free to implement the Cache in the language of your choosing.
* Do not use standard library data structures - write your own. (like Python's `collections` module etc.)

*** Requirements ***
1. Working code (obviously).
2. Unit tests (using a unit testing library of your choosing)
3. Documentation (as describe in the 2nd paragraph above)
"""


"""
class Key is for to make correlation between the key and is value. the object in the cache will be "Key" 
"""

class Key:
  def __init__(self, key, value):
    self.key=key
    self.value=value


class Cache:
  """
    there is 3 fields for object "cache" . the elements will "save" in array, we want the limit size, and first
    will be a filed that will helps us in case of "full" cache. when the cache is full for the first time, the
    element we want to remove will be in index 0 at the array
    space complexity -O(1)
    time complexity-O(1)

  """

  def __init__(self, size: int):
    self.array=[]
    self.size=size
    self.first=0

  """
    get method -
     space complexity -O(1)
     time complexity-O(size) in worth case
      unlike dictionary here we have limited size.
      although  average runtime for get is O(1) in dictionary ,the limited size makes a upper bounder
      for the get runtime
   """
  def get(self, key) :
    for element in self.array:
      if key==element.key:
        return element.value
    return "there is no "+str(key)+" in this cache"
  """
    set method -
     1.we will create a Key object type
     2.the first if is to check if the cache not full
      a. if there is more space we will add the new element to field array 
      b. otherwise, the cache is full so we need to remove our first element that set in the cache,  we 
      will use the field first. after we add the new element the cache is still full, but in our next set we 
      want to remove the second that add to the cache and so on..that's why we add to first 1.
      the % is for the case we "full our cache more thant 1 time" .example: 
      let size be 3 and we add 3 element:
      {(ori:94)(sag:94)(shmuel:92)} 
      so first=0
      if we add 4 more elements :(noa:76),(sol:77),(shay:92),(tal:75)
      for noa first will be 0 so it replace ori 
      for sol first will be 1 so it replace sag 
      for shay first will be  2 so it replace shmuel
      now our cache is: {(noa:76)(sol:77)(shay:97)} the first element added to this is "noa" so 
      for adding "tal" first will be 3%3=0 
      
3.space complexity -O(1)
  time complexity-O(1) in worth case
"""

  def set(self, key, value):
    element = Key(key, value)
    if len(self.array)<self.size:
      self.array.append(element)
    else:
      self.array[self.first]=element
      self.first=(self.first+1) % self.size

  """
     str method -
      space complexity -O(1)
      time complexity-O(size) in worth case
    """
  def __str__(self):
    result="{"
    for i in self.array:
       result=result+"("+str(i.key)+":"+str(i.value)+")"
    result=result+"}"
    return result






