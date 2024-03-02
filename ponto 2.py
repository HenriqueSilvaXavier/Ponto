def add(n, p, lista):
	i=p
	lista2=[]
	while i<len(lista):
		lista2.append(lista[i])
		del lista[i]
	lista.append(n)
	for k in range(0, len(lista2)):
		lista.append(lista2[k])
		
número=input("Digite um número: ")
número2=[]
for k in número:
	número2.append(k)
c=len(número2)-1
q=2
s=0
while c-q-s>0:
	add(".", c-q-s, número2)
	q=q+2
	s=s+1
número=""
for k in número2:
	número=número+k
print(número)