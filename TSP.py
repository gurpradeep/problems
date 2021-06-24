import numpy as np

def TSPRecursive(distances,check,current,start,memo):
  
    keys = tuple(sorted(check.keys()))
    if (keys, current) in memo:
        return memo[(keys, current)]

    minimum = np.inf
    for i in range(len(distances)):
        if i!=current and i!=start and i not in check:
            print("current",i)
            check[i]=1
            minimum=min(minimum,distances[current][i]+TSPRecursive(distances,check,i,start,{}))
            print('From {} To {}'.format(i,current))
            del check[i]
  
    if minimum==np.inf:
      return distances[current][start]

    memo[(keys,current)]=minimum
    return memo[(keys,current)]
    

def TSP(distances):
    check={}
    minimum = np.inf
    for i in range(len(distances)):
        print("start:",i)
        minimum=min(minimum,TSPRecursive(distances,check,i,i,{}))
    return minimum

print(TSP([
      [0, 10, 20],
      [12, 0, 10],
      [19, 11, 0],
]))