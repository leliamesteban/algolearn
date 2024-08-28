class StaticArray:
  """
  """
  def __init__(self, size):
    self._size = size
    self._elements = [None] * size

  def getItem(self, index):
    if index < 0 or index >= self._size:
      raise IndexError("Index out of range")
    return self._elements[index]

  def setItem(self, index, value):
    if index < 0 or index >= self._size:
          raise IndexError("Index out of range")
    self._elements[index] = value

  def __len__(self):
      return self._size
