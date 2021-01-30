class Calculator:
  def is_equation(self, msg):
    try:
      self.result = eval(msg)
      return True
    except:
      self.result = "Invalid math expression!"
      return False

  def calculate(self):
    return self.result