import time
import string
import os, platform

true = 1
false = 0

def clear_screen():
        if platrform.system() == 'Linux': os.system('clear')
        if platform.system() == 'Windows': os.system('cls')

def stamp_list(lista):
        corr = 0
        x = 0
        if lista == Lista1:
                x=1
        elif lista == Lista2:
                x=2
        elif lista == Lista3:
                x=3
        if len(lista) > 0:
                print ""
                print "Lista",x,": "
                for x in lista.keys():
                        print lista[x]
                print ""
                time.sleep(1)
        else:
                print "La lista e' vuota, caricala o aggiungi elementi"

def agg_elem(lista, presa):
        num = len(lista)
        lista[num] = presa

def rim_elem(lista, presa):
        if lista.has_key(presa):
        else:
                print "non ho trovato ",presa

def salva_lista(lista, file):
        out_file = open(file,"w")
        for x in lista.keys():
                out_file.write(lista[x]+"\n")
        out_file.close()

def carica_lista(lista, file):
        f = open(file,"r")
        while true:
                line = f.readline()
                line = line[0:]
                if line == "":
                        break
                for x in line:
                        lista[x] = line
        f.close()


def stampa_menu():
        print " "
        print "----------lista priorita' 1----------"
        print "11 Visualizza la lista"
        print "12 Aggiungi un elemento"
        print "13 Rimuovi un elemento"
        print "14 Salva lista"
        print "15 Carica lista"
        print "----------lista priorita' 2----------"
        print "21 Visualizza la lista"
        print "22 Aggiungi un elemento"
        print "23 Rimuovi un elemento"
        print "24 Salva lista"
        print "25 Carica lista"
        print "----------lista priorita' 3----------"
        print "31 Visualizza la lista"
        print "32 Aggiungi un elemento"
        print "33 Rimuovi un elemento"
        print "34 Salva lista"
        print "35 Carica lista"
        print "-------------------------------------"
        print "0 Esci"
        print " "

opz_menu = 0
Lista1 = {}
Lista2 = {}
Lista3 = {}
stampa_menu()
while opz_menu != 35:
        opz_menu = input("Scegli un'opzione dal menu: ")
        if opz_menu == 11:
                stamp_list(Lista1)
        elif opz_menu == 12:
                elem = raw_input("Cosa devo aggiungere? ")
                agg_elem(Lista1, elem)
        elif opz_menu == 13:
                canc_elem = raw_input("Quale elemento vuoi rimuovere? ")
                rim_elem(Lista1, canc_elem)
        elif opz_menu == 14:
                nome = 'lista1.txt'
                salva_lista(Lista1, nome)
        elif opz_menu == 15:
                nome = 'lista1.txt'
                carica_lista(Lista1, nome)
        elif opz_menu == 0:
                break
                pass
        else:
                stampa_menu()
        time.sleep(0.5)
print "Cia' cia'"
print " "
time.sleep(1)
