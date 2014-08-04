import urllib

# urllib may help. DON'T TRY ALL NOTHINGS, since it will never
# end. 400 times is more than enough.

count = 0
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345'

while count <= 400:
    sock =  urllib.urlopen(url)
    content = sock.read()
    # TODO probably keep looping until 400 or some condition
    print content.rsplit(' ', 1)[0]
    sock.close()
    count = count + 1