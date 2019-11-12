def getNumbers(s: str):
    result = []
    temp = ""
    numbers = "0123456789"
    for char in s:
        if char in numbers:
            temp += char
        elif temp is not "":
            result.append(int(temp))
            temp = ""
    if temp is not "":
        result.append(int(temp))
    return result

    
text = "een123zin45 6met-632meerdere+7777getallen" 
print(getNumbers(text))