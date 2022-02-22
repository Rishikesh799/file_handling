"""
###Q== PROGRAME TO COMBINE ANY LINE FROM FIRST FILE WITH SECOND FILE

f=open("story.txt","r",newline="")
d=open("rishi.txt","r",newline="")
s=open("paya.txt","w",newline="")
dataf = f.readlines()
print(dataf)
datad = d.readlines()
print(datad)
s.write(datad[2])
s.write(dataf[1])
f.close()
d.close()
s.close()
--------------------------------------------------------------------------------------------------------------------
###Q== WAP TO READ DATA FROM TXT FILE AND COUNT ALL THE WORDS HAVING "t" AS LAST CHARACTERS.[TAKE FILE=story.txt]
a=open("story.txt","r")
data = a.read()
d1=data.split()
print(d1)
co=0
for i in d1:
    if i.endswith("t"):
        co=co+1
print(co)
a.close()
print(a.closed)
----------------------------------------------------------------------------------------------------------------------
###Q==WAP TO READ DATA FROM TXT FILEAND DISPLAY AND COUNT ALL THE LINES HAVING "t" AS LAST CHARACTERS.[TAKE FILE=story.txt]
a=open("story.txt")
data=a.readlines()
print(data)
co=0
for i in data:
    if (i.rstrip()).endswith("t"):
        print(i.rstrip())
        co=co+1
print(co)
a.close()
print(a.closed)
"""













