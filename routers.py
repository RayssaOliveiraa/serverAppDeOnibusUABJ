import time
class Routers ():

  #formatação do dicionario {id : ["nome da parada", lat, lon]}

  list_routers = {1 : ["EAB", -8.320136, -36.395283], 2 : ["UABJ", -8.326928, -36.405400], 3 : ["ENTRADA DA COHAB1", 30, 50], 4 : ["PRAÇA DA CRIANÇA", -8.343899, -36.413806], 5 : ["LUX HOTEL", -8.342682, -36.418480], 6 : ["TREVO DE ACESSO", 30, 50], 7 : ["EREM JOÃO MONTEIRO", -8.339226, -36.432339], 8 : ["POSTO PEDROVIA", -8.337277, -36.430400],9 : ["CENTRO", -8.335175, -36.422512], 10 : ["BANCO DO BRASIL", -8.336437, -36.423642],11 : ["FÓRUM", -8.337182, -36.419071], 12 : ["PLACA DO HOSPITAL SANTA FÉ", -8.331891, -36.413549]}

  def decodeRouter(self, dicionario):
    for id in range(1, len(self.list_routers) + 1):
  
      if (dicionario['lat'] <= self.list_routers[id][1] + 0.00006 and dicionario['lat'] >= self.list_routers[id][1] - 0.00006) and (dicionario['lon'] <= self.list_routers[id][2] + 0.00005 and dicionario['lon'] >= self.list_routers[id][2] - 0.00005):
        print(self.list_routers[id][0])
        hora = int(time.strftime("%H")) - 3
        return self.list_routers[id][0] + " " + time.strftime('%A %B, %d %Y {}:%M:%S'.format(hora))
      