import ast

class Lastupdate():
  
  @staticmethod
  def saveLastUpdate(data):
    f = open("SaveFiles/lastUpdate.bin", "wb")
    f.write("{}".format(data).encode())
    f.close()
    
  @staticmethod
  def saveLastPoint(ponto):
    if ponto != None:
      f = open("SaveFiles/lastPoint.bin", "wb")
      f.write("{}".format(ponto).encode())
      f.close()
      
  @staticmethod
  def readLastUpdate():
    try:
      f = open("SaveFiles/lastUpdate.bin", "rb")
      data = f.readline().decode()
      fixed_data = ast.literal_eval(data)
      f.close()
    except:
      print("Ocorreu algum erro")
      
    return fixed_data
    
  @staticmethod
  def readLastPoint():
    try:
      f = open("SaveFiles/lastPoint.bin", "rb")
      data = f.readline().decode()
      f.close()
      return data
    except:
      print("Ocorreu algum erro")