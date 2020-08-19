class Grandfather:

  def father(self):
    print("From Grandfather ......")

class Father(Grandfather):

  def father(self):
    super().father()
    print("From Father ......")

class Son(Father):
  def father(self):
     super().father()
     print("From Son ......")

x = Son()

x.father()