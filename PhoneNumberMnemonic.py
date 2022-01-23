PHONE_DIGIT_LETTERS ={"0":["0"],
        "1":[""],
        "2":["a","b","c"],
        "3":["d","e","f"],
        "4":["g","h","i"],
        "5":["j","k","l"],
        "6":["m","n","o"],
        "7":["p","q","r","s"],
        "8":["t","u","v"],
        "9":["w","x","y","z"]}

def letterCombinations(phoneNumber):

    currentMnemo = ['0']*len(phoneNumber)
    mnemonicsFound=[]

    letterCombinationsHelper(0,phoneNumber,currentMnemo,mnemonicsFound)

    return mnemonicsFound

def letterCombinationsHelper(idx,phoneNumber,currentMnemo,mnemonicsFound):
    if idx == len(phoneNumber):
        mnemonic =''.join(currentMnemo)
        mnemonicsFound.append(mnemonic)
    else:
        digit = phoneNumber[idx]
        letters = PHONE_DIGIT_LETTERS[digit]
        for letter in letters:
            currentMnemo[idx]= letter
            letterCombinationsHelper(idx+1,phoneNumber,currentMnemo,mnemonicsFound)


   

print(letterCombinations("23"))