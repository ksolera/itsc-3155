from xml.etree.ElementTree import Comment


n = int(input("Enter an integer: "))

s = str(n)

i = len(s)-1

while i>=0:
    print(s[i])
    i-=1