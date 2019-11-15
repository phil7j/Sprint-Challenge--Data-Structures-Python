class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    if self.current == self.capacity -1:
      self.storage[self.current] = item
      self.current = 0
    else:
      self.storage[self.current] = item
      self.current = self.current + 1

  def get(self):
    if None in self.storage:
      new_list = []
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