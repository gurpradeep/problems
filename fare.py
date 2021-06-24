def fare_in_words2(fare):
    i=1
    result=[]
    
    def getDesc(num,i):
        switch
    
    
    while fare!=0:
        num = fare//10
        result = getDesc(num,i) + result
        i++












def fare_in_words(fare):

    def ones(fare):
        switcher = {
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine'
        }
        return switcher.get(fare)

    def teens(fare):
        switcher = {
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen'
        }
        return switcher.get(fare)
    
    def tens(fare):
        switcher = {
            2: 'Twenty',
            3: 'Thirty',
            4: 'Forty',
            5: 'Fifty',
            6: 'Sixty',
            7: 'Seventy',
            8: 'Eighty',
            9: 'Ninety'
        }
        return switcher.get(fare)
    

    def two(fare):
        if not fare:
            return ''
        elif fare < 10:
            return ones(fare)
        elif fare < 20:
            return teens(fare)
        else:
            tenner = fare // 10
            rest = fare - tenner * 10
            return tens(tenner) + ' ' + ones(rest) if rest else tens(tenner)
    
    def three(fare):
        hundred = fare // 100
        rest = fare - hundred * 100
        if hundred and rest:
            return ones(hundred) + ' Hundred ' + two(rest) 
        elif not hundred and rest: 
            return two(rest)
        elif hundred and not rest:
            return ones(hundred) + ' Hundred'
    
    billion = fare // 1000000000
    million = (fare - billion * 1000000000) // 1000000
    thousand = (fare - billion * 1000000000 - million * 1000000) // 1000
    rest = fare - billion * 1000000000 - million * 1000000 - thousand * 1000
    
    if not fare:
        return 'Zero'
    
    result = ''
    if billion:        
        result = three(billion) + ' Billion'
    if million:
        result += ' ' if result else ''    
        result += three(million) + ' Million'
    if thousand:
        result += ' ' if result else ''
        result += three(thousand) + ' Thousand'
    if rest:
        result += ' ' if result else ''
        result += three(rest)
    return result

# Driver code

fare = 5648
print(fare_in_words2(fare))
print("The fare is:", fare_in_words(fare), "dollars")