import collections 
from collections import defaultdict

def get_total_cost(G_map, path_costs, drivers, user):

    city = defaultdict(defaultdict)

    def evaluate_path(curr_node,target_node, acc_sum,visited):
        print("Node:",curr_node)
        visited.add(curr_node)
        ret = -1
        neighbours = city[curr_node]
        if target_node in neighbours:
            ret = acc_sum + neighbours[target_node]
        else:
            for neighbour,value in neighbours.items():
                if neighbour in visited:
                    continue
                else:
                    ret = evaluate_path(neighbour,target_node,acc_sum + value,visited)
                    if ret!=-1:
                        break
        return ret
    
    for (source_node, dest_node), path_cost in zip(G_map,path_costs):
        city[source_node][dest_node]=path_cost
        city[dest_node][source_node]=path_cost
    
    results=[]
    #verify path
    for driver in drivers:
        if driver not in city or user not in city:
            ret = -1;
        else:
            visited = set()
            ret=evaluate_path(driver,user,0, visited)
            results.append(ret)

    return results

G_map = [["a","b"],["b","c"],["a","e"],["d","e"]]
path_costs = [12.0,23.0,26.0,18.0]
drivers = ["c", "d", "e", "f"]
user = "a"
all_path_costs = get_total_cost(G_map, path_costs, drivers, user)
print("Total cost of all paths", all_path_costs)