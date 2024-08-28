class Multiplication:
  """
  Instantiate a multiplication operation.
  Numbers will be multiplied by the given multiplier.

  :param multiplier:
  :type multiplier: int
  """
  def __init__(self, multiplier):
    self.multiplier = multiplier
  
  def multiply(number: int, multiplier: int) -> int:
    """
    Multiply a given number by a given multiplier.
  
    :param number: The number to multiply.
    :type number:
  
    :param multiplier: The multiplier.
    :type multiplier: int

    :return: The result of the multiplication
    :rtype: int
    """
    return number * multiplier

multiplication = Multiplication(2)

print(multiplication.multiply(5))
