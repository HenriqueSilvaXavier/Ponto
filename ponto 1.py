n=input("Digite um número grande: ")
l=len(n)-1
c=""
k=0
lista=[]
while (l-k)>=0:
	c="{}{}".format(n[l-k], c)
	k=k+1
	if k%3==0:
		c=".{}".format(c)
for n in c:
	lista.append(n)
if lista[0]==".":
	lista[0]=""
c=""
for n in lista:
	c=c+n
print("O valor com pontos é", c)