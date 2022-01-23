def generateParenthesis(num):
    result=[]
    prefix = ""
    if num > 0:
        generateParenthesisHelper(prefix,num,num,result)

    return result

def generateParenthesisHelper(prefix,openingTagCount,closingTagCount,result):

    if closingTagCount==0:
        result.append(prefix)

    if openingTagCount > 0:
        generateParenthesisHelper(prefix+"(",openingTagCount-1,closingTagCount,result)

    if openingTagCount< closingTagCount:
        generateParenthesisHelper(prefix+")",openingTagCount,closingTagCount-1,result)


print(generateParenthesis(3))