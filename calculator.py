import re

class Calculator:
  def is_equation(self, msg):
    msg = msg.replace("(", "")
    msg = msg.replace(")", "")
    return re.match(r"^[\s]*[\d\+\-\*\/]+[\w\s]*$", msg)

  def calculate(self, msg):
    result = ""
    try:
      result = eval(msg)
    except:
      result = "Invalid Equation!"
    return result