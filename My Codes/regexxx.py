import re
txt = "The girl is from Spain"
x = re.search("^The.*Spain$", txt)
print(x)

y = re.findall("ai", txt)
print(y)