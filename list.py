prog_lang = ['c','c++', 'java', 'js', 'php']
print(prog_lang)
print(prog_lang[1])
prog_lang[2] = "perl"
print(prog_lang)
prog_lang.append("c++")
prog_lang.insert(0, "ruby")
print(prog_lang)
del prog_lang[3]
print(prog_lang)
prog_lang.remove('ruby')
print(prog_lang)
popped_one = prog_lang.pop(0)
print(f"my favourite programming language is {popped_one}\n")
prog_lang.sort()
print(prog_lang)
prog_lang.sort(reverse=True)
print(prog_lang)
prog_lang.reverse()
print(prog_lang)
for language in prog_lang:
    print(language)
    print("\n")
for num1 in range(1, 10, 2):
    print(num1)
numlist = list(range(1,6))
print(numlist)
squares = []
for val in range(1, 10):
    square = val ** 2
    squares.append(square)
print(squares)
digits = [1, 2, 3, 4]
print(sum(digits))
print(min(digits))
print(max(digits))
sqq = [ sq ** 2 for sq in range(1, 10)]
print(sqq)
print(prog_lang[0:2])
secondary_prog_lang = prog_lang[:]
print(secondary_prog_lang)