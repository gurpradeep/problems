def break_query(query, dict):
    """
    :type query: str
    :type dict: List[str]
    :rtype: List[str]
    """
    return helper(query, set(dict), {})
    
def helper(query, dict, result):
    if not query: 
        return []
    
    if query in result: 
        return result[query]
    
    res = []
    for word in dict:
        if not query.startswith(word):
            continue
        if len(word) == len(query):
            res.append(word)
        else:
            resultOfTheRest = helper(query[len(word):], dict, result)
            for item in resultOfTheRest:
                item = word + ' ' + item
                res.append(item)
    result[query] = res
    return res

query = "vegancookbook"
dict = ["an", "book", "car", "cat", "cook", "cookbook", "crash", 
        "cream", "high", "highway", "i", "ice", "icecream", "low", 
        "scream", "veg", "vegan", "way"]
print(break_query(query, dict))
query = "highwaycarcrash"
print(break_query(query, dict))