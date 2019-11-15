class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    # If current has reached end of capacity, insert last item and reset current
    if self.current == self.capacity -1:
      self.storage[self.current] = item
      self.current = 0
    else:
      # otherwise insert item at current's index and add 1 to current's value
      self.storage[self.current] = item
      self.current = self.current + 1

  def get(self):
    # Check to see if there are None values in the list
    if None in self.storage:
      new_list = []
      # If there are then loop through the list, make a new array and only add values that aren't equal to None
      for i in self.storage:
        if i != None:
          new_list.append(i)
      return new_list
    return self.storage

buffer = RingBuffer(5)

buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.append('d')