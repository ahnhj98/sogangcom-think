import requests
r = requests.get("https://www.vox.com/2018/9/25/17901082/trump-un-2018-speech-full-text")
r.encoding ='utf8'
data = str(r.text)
begin = data.find("Madam President, Mr. Secretary-General")
end = data.rfind("Thank you very much. Thank you. (Applause.)") + len('Thank you very much. Thank you. (Applause.)')
print('begin= ', begin, ', end= ', end, ', len= ', end-begin)
print('begin with :', data[begin:begin+150])
print('end with :', data[end-150:end])
data = data[begin:end]
data = data.replace('<p', '')
words = data.split()

mydict={}
word = words
for w in word:
    if w in mydict:
        mydict[w]+=1
    else:
        mydict[w]=1
print(mydict)

for k in sorted(mydict, key=mydict.__getitem__, reverse=True):
	print('%s: %s' %(k,mydict[k]))
