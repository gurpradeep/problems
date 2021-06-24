import collections
def possible_matches(S, words):
    waiting_list = collections.defaultdict(list)
    for w in words:
        it = iter(w[1:])
        val = w[0]
        waiting_list[val].append(it)
    
    for c in S:
        if c not in waiting_list:
            continue
        wait = waiting_list.pop(c)
        for it in wait:
            nxt = next(it, None)
            waiting_list[nxt].append(it)
    
    return len(waiting_list[None])

plagiarised = "abcde"
students = ["a","bb","acd","ace"]

print("The content was copied from", possible_matches(plagiarised, students), "students")