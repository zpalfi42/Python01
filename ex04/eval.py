import	sys
from	_collections_abc import Iterable

class	Evaluator:
    def	zip_evaluate(coefs, words):
        if (not isinstance(coefs, Iterable)):
            raise	TypeError("coefs must be iterable")
        if (not isinstance(words, Iterable)):
            raise	TypeError("words must be iterable")
        if (len(coefs) != len(words)):
            return(-1)
        res = zip(coefs, words)
        return(sum(coef * len(word) for coef, word in res))
    
    def	enumerate_evaluate(coefs, words):
        if (not isinstance(coefs, Iterable)):
            raise	TypeError("coefs must be iterable")
        if (not isinstance(words, Iterable)):
            raise	TypeError("words must be iterable")
        if (len(coefs) != len(words)):
            return(-1)
        res1 = enumerate(coefs)
        return(sum(a * len(words[i]) for i, a in res1))