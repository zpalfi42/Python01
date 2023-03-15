import sys
import	random


def generator(text, sep=" ", option=None):
    '''
    Divide el texto de acuerdo al valor de sep y producirá las sub-strings.
    option especifica si una acción se realizará sobre las sub-strings antes de ser producidas.
    '''
    options = ["shuffle", "ordered", "unique"]
    if (isinstance(text, str) or (option not in options and option is not None)):
        print("ERROR")
        sys.exit()
    words = []
    aux = ""
    for	letter in text:
        if (letter == sep):
            words.append(aux)
            aux = ""
            continue
        aux += letter
    words.append(aux)
    
    if (option is "shuffle"):
        n = random.randint(0, len(words))
        if (n <= 0):
            n += 1
        while (len(words) % n == 0 or (len(words) % 2 == 0 and n % 2 == 0)):
            n += 1
        for word in range(len(words)):
            yield words[int((n * word) % len(words))]
            
    if (option is "ordered"):
        words.sort()
        for word in words:
            yield word
            
    if (option is "unique"):
        res = []
        for word in words:
            if (word not in res):
                res.append(word)
        for word in res:
            yield word
            
    if (option is None):
        for word in words:
            yield word
