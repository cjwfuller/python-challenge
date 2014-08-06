import urllib

# urllib may help. DON'T TRY ALL NOTHINGS, since it will never
# end. 400 times is more than enough.

count = 0
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
nothing = 12345

while count <= 400:
    sock =  urllib.urlopen(url + str(nothing))
    content = sock.read()
    print content
    parts = content.rsplit(' ', 1)
    if(len(parts) < 2):
        break
    nothing = parts[1]
    sock.close()
    count = count + 1