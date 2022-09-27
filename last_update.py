import ast

class Lastupdate():
  
  @staticmethod
  def saveLastUpdate(data, ponto):
    f = open("SaveFiles/lastUpdate.bin", "wb")
    f.write("{}\n{}".format(data, ponto).encode())
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
    f = open("SaveFiles/lastUpdate.bin", "rb")
    f.readline()
    data = f.readline().decode()
    f.close()
    return data