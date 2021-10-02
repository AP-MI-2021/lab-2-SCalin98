'''
Acesta este fisierul main.cpy pentru laboratorul nr. 2
'''
import sys


def is_palindrome(n)->bool :
     #Subprogramul verifica daca un numar natural dat are proprietatea de a fi palindrom
     #Parametrul de intrare : n, numar natural, acesta furnizeaza numarul al carui trasatura de palindrom o verificam
     #Valoarea de iesire : true, daca numarul n este palindrom, false in caz contrar
     if n<0 :return False
     elif n < 10:return True
     else :
       reversN = 0
       # Copiem numarul n in nVerificat, intrucat trebuie sa impartim succesiv numarul n la 10 pentru a obtine, una cate una, cifrele sale si, totodata, sa comparam numarul n cu reversul sau
       nVerificat = n
       while int(nVerificat > 0) :
         ultCif = int(nVerificat%10)
         reversN = (reversN * 10) + ultCif
         nVerificat = int(nVerificat / 10)
       if reversN == n : return True
       else : return False
def test_is_palindrome() :
    #Subprogramul testeaza subprogramul is_palindrome pentru trei cazuri de numere naturale si un numar negativ
    #In caz de rezultat eronat din partea subprogramului testat, prezentul subprogram afiseaza in consola un mesaj in acest sens
    assert is_palindrome(0) == True, '0 nu este palindrom'
    assert is_palindrome(100) == False, '100 este palindrom'
    assert is_palindrome(122221) == True, "122221 nu este palindrom"
    assert is_palindrome(-1221) == False, 'Numar negativ este palindrom'
def get_n_choose_k(n: int, k: int) -> int :
    #Subprogramul calculeaza si returneaza combinari de n luate cate k
    #Parametrii de intrare : n, k numere intregi
    #Return : valoarea comb. n luate cate k
    if n == 0 or n == 1 or n == k: return 1
    elif n == 2 and k == 1 : return 2
    else :
         #Construim triunghiul lui Pascal, retinand insa doar cate doua siruri, valoarea cautata fiind un element al celui de-al doilea sir construit.
         currentRow = 3 #Incepem cu al 3lea rand din tr. lui Pascal, deoarece daca valoarea cautata s-ar fi aflat pe primele doua randuri, atunci subprog. ar fi returnat o valoare conform instructiunilor de mai sus
         first_row = []
         first_row.append(0) #Lucrez cu indici de la 1, deci am nevoie de un element suplimentar pentru a nu iesi cu indicii din afara sirului
         first_row.append(2)
         first_row.append(1)
         second_row = []
         second_row.append(0)
         second_row.append(0)
         second_row.append(0)
         while currentRow<=n : #Valoarea cautata se afla pe al n-lea rand din triunghiul lui Pascal
             second_row.append(0) #Construind progresiv triunghiul lui Pascal, obtinem siruri mai lungi cu cate un element pana la sirul care contine valoarea cautata
             currentColumn = 1
             while currentColumn < currentRow :   #Construim cel de-al doilea sir adunand doua cate doua elemente din primul sir.
                  if currentColumn == 1 : second_row[currentColumn] = currentRow
                  else : second_row[currentColumn] = first_row[currentColumn-1] + first_row[currentColumn]
                  currentColumn = currentColumn + 1
             second_row.append(1) # Ultimul element al unui rand este intotdeauna 1. Penultimul element al sirului 2 (denumit currentRow) este suma dintre penultimul si ultimul element al sirului 1 (denumit firstRow)
                                  # Ultimul element al primului sir, precum si penultimul element al sirului 2 sunt accesate cu index-ul currentColumn.
                                  # Ca sa nu iesim cu index-ul din afara primului sir, bucla de executia continua pana cand currentColumn = currentRow. Ramane de adaugat ultimul element in sirul 2.
             indexFirstRow  = 1
             while indexFirstRow < currentRow :
                  first_row[indexFirstRow] = second_row[indexFirstRow]
                  indexFirstRow = indexFirstRow + 1
             first_row.append(1) # Primul rand a devenit al doilea rand
             currentRow = currentRow + 1 # Trecem la urmatoarea pereche de randuri
         return second_row[k]

def test_get_n_choose_k():
    #Subprogramul testeaza subprog. get_n_choose_k pentru eventuale erori
    #In caz de rezultat eronat, acesta va afisa cate un mesaj corespunzator
    assert get_n_choose_k(2,2) == 1, 'Combinari de 2 luate cate 2 nu este 1'
    assert get_n_choose_k(0,0) == 1, 'Combinari de 0 luate cate 0 nu este 1'
    assert get_n_choose_k(300,299) == 300, 'Combinari de 300 luate cate 299 nu este 300'
    assert get_n_choose_k(20,15) == 15504, 'Combinari de 20 luate cate 15 nu este 15504'

def meniuGeneral():
    print("Introduceti cifra corespunzatoare optiunii dumneavoastra")
    print("1.is_palindrome")
    print("2.get_n_choose_k")
    print("3.test_is_palindrome")
    print("4.test_get_n_choose_k")
    print("5.Opreste aplicatia")
def main():
  # interfata de tip consola aici
    aplicatieDeschisa = 6
    while aplicatieDeschisa != 5 :
        meniuGeneral()
        aplicatieDeschisa = int(input("Optiunea dumneavoastra : "))
        if(aplicatieDeschisa == 1) :
            print("Introduceti numarul pe care doriti sa-l verificati : ")
            nrDeVerif = int(input("Numarul de verificat : "))
            valoareRetur = is_palindrome(nrDeVerif)
            if valoareRetur ==  True : print("Este palindrom")
            else : print("Nu este palindrom")
        elif(aplicatieDeschisa == 2) :
            n = int(input("Introduceti n : "))
            k = int(input("Introduceti k : "))
            print("Combinari de n luate cate k = ", get_n_choose_k(n,k))
        elif(aplicatieDeschisa == 3) : test_is_palindrome()
        elif(aplicatieDeschisa == 4) : test_get_n_choose_k()

if __name__ == '__main__':
  main()
