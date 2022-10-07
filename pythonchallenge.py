string = "http://www.pythonchallenge.com/pc/def/map.html"
print(string)
print(len(string))

lst = []

for i in range(len(string)):
    lst.append(chr(ord(string[i]) + 2))

new = ''.join(str(elem) for elem in lst)
print(lst)
new = new.replace('{','a')
print(new)
