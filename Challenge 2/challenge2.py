# Challenge Link: http://www.pythonchallenge.com/pc/def/map.html

import string

my_string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

difference = +2
new_string = "".join(
    (chr(97 + (ord(letter) - 97 + difference) % 26) for letter in my_string)
)
print(new_string)
