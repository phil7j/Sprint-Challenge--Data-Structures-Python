class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    if self.current >= self.capacity:
      self.storage.insert(self.current,item)
      self.current = 0
    else:
      self.storage.insert(self.current,item)
      self.current = self.current + 1

  def get(self):
    return self.storage