# Solution: Change 'map' to 'ocr' in the URL

alphabet = "abcdefghijklmnopqrstuvwxyz"
riddle = list("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.")

num_letters = 26
for idx, char in enumerate(riddle):
    if(riddle[idx] in alphabet):
        posn = alphabet.index(riddle[idx]) + 2
        if(posn >= num_letters):
            posn = posn - num_letters
        riddle[idx] = alphabet[posn]
print ''.join(riddle)