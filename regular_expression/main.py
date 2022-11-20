import re

pattern = "this"
re_pattern = re.compile("search this inside")
re_pattern2 = re.compile("search this inside of this text please!")
re_pattern3 = re.compile(r"^([a-zA-Z]).(a)")

string = "search this inside of this text please!"

a = re.search(pattern, string)
b = re_pattern.search(string)  # search the pattern in the string and return match instances
c = re_pattern.findall(string)  # find all the parts in string that same with the pattern
d = re_pattern2.fullmatch(string)  # check if the string is 100% same with the pattern
e = re_pattern.match(string)  # check if the string starts with the pattern
print('b', b)
print('c', c)
print('d', d)
print('e', e)

print('a', a)
print('a', a.span())
print('a', a.end())
print('a', a.group())

f = re_pattern3.search(string)
print('f', f.group())
print('f[1]', f.group(1))
print('f[2]', f.group(2))

# email regex
re_email_pattern = re.compile(r"(^[a-zA-z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
string = "Leo@gmail.com"

email_search = re_email_pattern.search(string)

print(email_search)

# At least 8 char long
# contain any sort letters, numbers $%#@
pattern = re.compile(r"(^[a-zA-Z0-9$%#@]{8,}\d)")
string = "hell@$%#1"

search = pattern.fullmatch(string)
print(search)
