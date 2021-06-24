def word_break(s, words):
    def dfs(i):
        if i == len(s): # we have constructed the entire target s
            return True

        for word in words:
            if s[i:].startswith(word): # is this a valid path
                if dfs(i + len(word)):
                      return True # any path leads to true is fine

        return False

    return dfs(0)

inputs = ["aaa", "aab", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"]
inputs2 = ["aa", "a c", "a aa aaa aaaa aaaaa aaaaaa aaaaaaa aaaaaaaa aaaaaaaaa aaaaaaaaaa"]
for i in range(len(inputs)):
     print("Word break : ",word_break(inputs[i], inputs2[i].split()))