def fibo(n: int):
    elozo = 0
    most = 1
    veg = 0
    aktszam = [0,1]
    for i in range(n-1):
        most = aktszam[len(aktszam) -1]
        elozo = aktszam[len(aktszam) -2]
        aktszam.append(most + elozo)

    veg = aktszam[len(aktszam)-1]

    return veg


bekert = int(input())

print(fibo(bekert))