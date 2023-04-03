def searchForLetters(inputString:str,letters:str='aieou') ->str:
    return str(set(inputString).intersection(set(letters)))