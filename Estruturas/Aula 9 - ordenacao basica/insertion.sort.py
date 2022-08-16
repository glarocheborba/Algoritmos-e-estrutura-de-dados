def insertionsort(v,n):
    for i in range(1,n):
        aux = v[i]
        j = i - 1
        while j >= 0 and v[j] > aux:
            v[j+1] = v[j]
            j-= 1
        v[j+1] = aux
        
def main():
    comando = input()
    lista = comando.split()
    lista_ordenada = []
    n = 0
    for j in lista:
        lista_ordenada.append(int(j))
        n += 1
    insertionsort(lista_ordenada, n)

    print(lista_ordenada)

if __name__ == '__main__':
    main()
    