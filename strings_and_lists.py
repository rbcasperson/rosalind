def s_and_l(text, a, b, c, d):
	b += 1
	d += 1
	
	first = str[a:b]
	second = str[c:d]
	
	return first + " " + second
	
	
text = "teMebaE5ZlwgSDshJ4O1t12RUMyD5XXVrvVGOts3xxbZkKelKSZFHzwoKHuCBK7Lhm2Koqp5ZTT31KC3PhrynomerusTN2h1IsEyFtkY3J9l7S3AnwCmultifasciata12b1frMUVnKRKuKzDiNVGWbVKphyLrcurAUP"
a = 80
b = 90
c = 115
d = 127

answer = s_and_l(text, a, b, c, d)

print answer #Phrynomerus multifasciata
