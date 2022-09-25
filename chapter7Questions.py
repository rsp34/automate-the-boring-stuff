import re
numRegex = re.compile(r'''(\d{1,3}(,\d{3})+)?
                          (^\d{1,3}$)?  # match 0 or more comma separate groups
                      ''',re.VERBOSE)


print(numRegex.search('42').group())
print(numRegex.search('1,234').group())
print(numRegex.search('6,368,745').group())
print(numRegex.search('12,34,567').group())
print(numRegex.search('1234').group())

# nameRegex = re.compile('[A-Z][a-z]* Watanabe')
# print(nameRegex.search('Haruto Watanabe').group())
# print(nameRegex.search('Alice Watanabe').group())
# print(nameRegex.search('RoboCop Watanabe').group())
# print(nameRegex.search('haruto Watanabe').group())
# print(nameRegex.search('Mr. Watanabe').group())
# print(nameRegex.search('Watanabe').group())
# print(nameRegex.search('Haruto watanabe').group())

sentenceRegex = re.compile('Alice|Bob|Carol eats|pets|throws apples|cats|baseballs',re.I )
print(sentenceRegex.search('Alice eats apples.').group())
print(sentenceRegex.search('Bob pets cats.').group())
print(sentenceRegex.search('Carol throws baseballs.').group())
print(sentenceRegex.search('Alice throws Apples.').group())
print(sentenceRegex.search('BOB EATS CATS.').group())
print(sentenceRegex.search('RoboCop eats apples.').group())
print(sentenceRegex.search('ALICE THROWS FOOTBALLS.').group())
print(sentenceRegex.search('Carol eats 7 cats.').group())