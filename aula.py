

vetor = [None,None,None,None]
topo = -1

def push (vetor,elemento):
    global topo
    if topo +1 <len(vetor):
       vetor[topo+1] = elemento
       topo+=1
       return vetor
    else:
        print("Pilha cheia!!")

def pop(vetor):
    global topo
    elemento=vetor[topo]
    vetor[topo] = None
    topo-=1
    return elemento


vetor =push(vetor,2)
print(vetor)
vetor =push(vetor,4)
print(vetor)
vetor =push(vetor,6)
print(vetor)

_ = pop(vetor)
print(vetor)




