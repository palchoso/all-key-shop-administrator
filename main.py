import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import re
from game import Game
import os
from tkinter import *

def busqueda(event):
    search = buscador.get()
    i = 0
    search = search.replace(" ","+")
    print(search)


    URL = f"https://www.allkeyshop.com/blog/catalogue/category-pc-games-all/search-{search}/"
    uClient = uReq(URL) #descarga la pagina y la mete en uclient
    page_html = uClient.read() # lee la pag



    soup = BeautifulSoup(page_html, "html.parser")

    #title = (soup.find(id="a-size-base-plus a-color-base a-text-normal")).get_text()

    f=open("games.txt", "r+")
    num_lines = sum(1 for line in open('games.txt'))
    contents = [0] * num_lines

    while i < num_lines:
        contents[i] = f.readline()
        i += 1

    container = soup.find("li",{"class": "search-results-row"}) #coger todos los productos, devuelve lista

    name = str(container.find('h2', {'class': 'search-results-row-game-title'}).get_text())
    price = str(container.find('div', {'class': 'search-results-row-price'}).get_text())
    price = float(re.sub("\[|\]|\'|\€|\$|\%|\-", "", price))  # quita esos caracteres de precio

    if name + "\n" not in contents:
        f.write(name +"\n"+str(price)+"\n")
        game = Game(name, price, "none")
        gamelabel = Label(main,text=game.imp(),fg="black")
        gamelabel.pack()
    else:
      build()


    #i = 0
    #for line in contents:

     #   if line == name + "\n":
      #      i += 1
       #     break
        #i += 1
    #priceinfile = contents[i]
    #if priceinfile != str(price):
     #   fout = open("out.txt", "wt")
      #  for line in contents:
       #     print(f"{line}")
        #    fout.write(line.replace(priceinfile + "\n", str(price) + "\n", 1))
        #game = Game(name, price, priceinfile)
        # gamelabel = Label(main,text=game.imp(),fg="black")
        # gamelabel.pack()
        #f.close()
        #os.remove("games.txt")
       # fout.close()
        #os.rename("out.txt", "games.txt")
        #f = open("games.txt", "r+")

def exit(event):
    main.destroy()
    ventanadebusq.destroy()

def build(event):
    main.destroy()
    main.__init__()
    main.title("Game list")
    update = Button(main, text="Update")
    update.bind("<Button-1>", build)
    update.pack(side=BOTTOM)
    f = open("games.txt", "r+")
    fout = open("out.txt", "wt")
    num_lines = sum(1 for line in open('games.txt'))
    containers = [0] * num_lines
    towrite = [0] * num_lines
    i = 0
    while i < num_lines:
        containers[i] = f.readline()
        i += 1
    print(containers)
    i=0
    while i < len(containers):
        urluse = containers[i].replace(' ', '+').replace('\n', '')
        URL = f"https://www.allkeyshop.com/blog/catalogue/category-pc-games-all/search-{urluse}/"
        uClient = uReq(URL)  # descarga la pagina y la mete en uclient
        page_html = uClient.read()  # lee la pag
        soup = BeautifulSoup(page_html, "html.parser")
        container = soup.find("li", {"class": "search-results-row"})  # coger todos los productos, devuelve lista
        name = str(container.find('h2', {'class': 'search-results-row-game-title'}).get_text())
        price = str(container.find('div', {'class': 'search-results-row-price'}).get_text())
        price = float(re.sub("\[|\]|\'|\€|\$|\%|\-", "", price))  # quita esos caracteres de precio

        j = i + 1
        print(f"contents of j: {containers[j]} j={j}")
        print(f"contents of i: {containers[i]} i={i}")

        game = Game(name, price, containers[j])
        gamelabel = Label(main, text=game.imp(), fg="black")
        gamelabel.pack()

        towrite[i] = name
        towrite[j] = price
        i += 2
        print(towrite)
    for line in towrite:
        fout.write(str(line) + "\n")

    f.close()
    os.remove("games.txt")
    fout.close()
    os.rename("out.txt", "games.txt")
    f = open("games.txt", "r+")
    fout = open("out.txt", "wt")
    f.close()


main = Tk()
f1 = Frame(main)
f1.pack()
ventanadebusq = Tk()
main.title("Game list")
ventanadebusq.title("Search")
busq = Label(ventanadebusq,text="Search game: ",bg="red")
busq.pack(side=LEFT)
buscador = Entry(ventanadebusq)
buscador.pack(side=LEFT)
botonbusq = Button(ventanadebusq,text="Go!!")
botonbusq.pack(side=LEFT)
botonbusq.bind("<Button-1>",busqueda)
build(event=0)
quit = Button(ventanadebusq,text="Quit!!!")
quit.bind("<Button-1>", exit)
quit.pack(side=LEFT)



ventanadebusq.mainloop()

main.mainloop()



