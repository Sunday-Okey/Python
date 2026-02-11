# HTTP Package
# import urllib.request
# import json
# import textwrap
from fractions import Fraction

def add_fractions(numerator1, denominator1, numerator2, denominator2):
    a = Fraction(f'{numerator1 / denominator1}') + Fraction(f'{numerator2 / denominator2}')
    return a.numerator, a.denominator


# print(add_fractions(1, 2, -1, 3))
print(Fraction(1, 2) + Fraction(-1, 3))

# https://www.googleapis.com/books/v1/volumes?q=isbn:1101904224

# with urllib.request.urlopen("https://www.googleapis.com/books/v1/volumes?q=isbn:1101904224") as f:
#     text = f.read()
#     decodedtext = text.decode("utf-8")
#     # print(textwrap.fill(decodedtext, width=50))
    
# # print()

# obj = json.loads(decodedtext)
# print(obj['kind'])

# print(obj['items'][0]['searchInfo']['textSnippet'])
# print(type(obj))