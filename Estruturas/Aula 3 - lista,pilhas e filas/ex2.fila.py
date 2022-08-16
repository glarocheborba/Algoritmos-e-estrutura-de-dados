from black import put_trailing_semicolon_back


class fila:
    def __init__(self):
        self.queue = [None]* 5
        self.qinit = 0
        self.qend = 0

    def enqueue(self, x):
        if self.qend >= len(self.queue):
            self.qend = 0
        if self.qinit >= len(self.queue):
            self.qinit = 0
        
        if self.qinit == self.qend:
            self.queue[self.qinit] = x
            self.qend += 1
        else:
            self.queue[self.qend] = x
            self.qend += 1

    def dequeue(self):
        self.queue[self.qinit] = None
        self.qinit += 1

q = fila()
while True: 
    n = int(input('1-enfileirar \n2-desenfileirar \n3-Primeiro da fila\n '))
    if n == 1:
        if q.qend >= len(q.queue):
            q.qend = 0
        if q.queue[q.qend] != None:
            print('Fila cheia!') 
        else:
            q.enqueue(input('Digite: '))
            print(q.queue)
    elif n == 2:
        q.dequeue()
        print(q.queue)
    elif n == 3: 
        primeiro = q.queue[q.qinit]
        if primeiro == None:
            print('Fila vazia!')
        else:
            print(primeiro)
    else:
        pass
