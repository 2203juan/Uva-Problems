from sys import stdin

def solve(a, b):

    hi = 0
    low = 0
    consumo_total = calcular_consumo(a)
    hi = consumo_total
    result = 0

    while(low+1 != hi):
      mid = low + ((hi-low)>>1)
      
      resta_abs = calcular_pago(consumo_total - mid) - calcular_pago(mid)
      
      if(resta_abs > b ):
        low = mid

      elif (resta_abs < b ):
        hi = mid

      elif resta_abs == b:
        result = mid
        break


    return calcular_pago(result)


def calcular_pago(cwh):

    if( cwh ==0 ):
      return 0
    result = 0
    if(cwh <= 100):
        return result + cwh*2
    result += 100*2
    if(cwh <= 10000):
        return result + (cwh-100)*3
    result += (10000-100)*3
    if(cwh <= 1000000):
        return result + (cwh-10000)*5
    result += (1000000-10000)*5
    return result + (cwh-1000000)*7

  
#print(calcular_pago(10123))


def calcular_consumo(dinero_or):

  
  consumo = 0
  dinero = dinero_or

  if( dinero_or <= 200 ):
      return consumo + (dinero_or //2)
  consumo = consumo + 100
  dinero = dinero - 200

  if( dinero_or <= 29700 ):
      return consumo + (dinero//3)
  consumo = consumo + 9900
  dinero = dinero - 29700

  if ( dinero_or <= 4950000 ):
      return consumo + (dinero//5)
  consumo = consumo + 990000

  dinero = dinero-4950000

  if(dinero_or > 4950000):
      return consumo + (dinero//7)


    
#print(calcular_consumo(30515))

def main():
  tsum,diff = map(int,stdin.readline().split())
  while tsum+diff!=0:
    print(solve(tsum, diff))
    tsum,diff = map(int,stdin.readline().split())
main()    

    
    
        
