def mostFrequentLetter(string):
    string = string.lower()
    string = string.replace(' ', '')
    answer = string[0]
    
    for i in range (1, len(string)):
        if string.count(answer) < string.count(string[i]):
            answer = string[i]
    return answer


print(mostFrequentLetter("1234"))