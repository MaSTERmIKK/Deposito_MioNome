

controllo = True

def ciao(nome):
    if nome != "mirko":
        print ("ciao")

def ciao2(pippo):
    print(pippo)

def ciao3():
    print("nulla da riferire")

def controllore():
    x= input("vuoi finire?")
    if x == "yes":
        controllo = False

x = input()
y = input()

somma(x,y)
somma(11,22)
somma(numeri[1],numeri[2])

while controllo:
   ciao3()
   controllore()
   
   


















database={
    "utente1":["pino", "1234"],
    "utente2":["gerryscotti","098"]
}

def accesso(nome, passw):
    for credenziali in database.values():
        if nome==credenziali[0] and passw ==credenziali[1]:
            return True
    return False






