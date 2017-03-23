from tkinter import *
import random

class Tabela():
    def __init__(self,master):
        self.master = master
        self.platno = Canvas(master,height=500,width=500)
        
        # Velikost začetne igre
        self.n = 2
        # Na začetku imamo privzeto samo pozitivna cela števila
        self.stevila = 1
        
        # Naročimo se na pritiske gumbov
        self.platno.bind_all('<Left>',self.premikLevo)
        self.platno.bind_all('<Right>',self.premikDesno)
        self.platno.bind_all('<Up>',self.premikGor)
        self.platno.bind_all('<Down>',self.premikDol)
        self.platno.bind_all('<space>',self.undo)

        # Glavni menu
        self.menu = Menu(master)
 
        # Dodamo izbire 
        self.menu.add_command(label="Nova igra", command=self.znova)
        self.menu.add_command(label="Pokaži rešitev", command=self.pokaziResitev)
        
        # Naredimo podmenu Izberi velikost
        velikost_menu = Menu(self.menu,tearoff=0)
        self.menu.add_cascade(label="Izberi velikost", menu=velikost_menu)

        # Naredimo podmenu Izberi števila
        predznak_menu = Menu(self.menu,tearoff=0)
        self.menu.add_cascade(label="Izberi števila", menu=predznak_menu)
        
        self.menu.add_command(label="Zapri aplikacijo", command=master.destroy)

        # Dodamo izbiri v Izberi števila
        predznak_menu.add_radiobutton(label="Pozitivna cela števila",command = self.nastaviStevila(1))
        predznak_menu.add_radiobutton(label="Tudi negativna cela števila",command = self.nastaviStevila(2))

        # Dodamo izbire v Izberi velikost
        # Na voljo bodo dimenzije od 2 do 7
        for i in range(2,8):
            velikost_menu.add_radiobutton(label=str(i)+"×"+str(i),
                                          command=self.nastaviTezavnost(i))

        # Nastavimo vrednost odštevalnika na začetka na None    
        self.timer=None

        # Začetni zaslon s sliko in gumbi
        slika = PhotoImage(file="slika_meni.ppm")
        self.slika1 = Label(master,image=slika,anchor=NW)
        self.slika1.image = slika 
        self.slika1.pack()
       
        self.gumbZacni = Button(master,text="ZAČNI IGRO",width=31,justify = CENTER,fg = "white",
		 bg = "black",relief="flat",font=("Times", "20","bold"),command=self.znova)
        self.gumbZacni.pack()

        self.gumbOIgri = Button(master,text="O IGRI",width=31,justify = CENTER,fg = "black",
		 bg = "white",relief="flat",font=("Times", "20","bold"),command=self.navodila)
        self.gumbOIgri.pack()

        self.gumbZapri = Button(master,text="ZAPRI APLIKACIJO",width=31,justify = CENTER,fg = "white",
		 bg = "black",relief="flat",font=("Times", "20","bold"),command=master.destroy)
        self.gumbZapri.pack()
        
        
    def navodila(self):
        messagebox.showinfo("Navodila", "Igro začnemo v zgornjem levem kotu (START), naša naloga pa je, da s smernimi tipkami potujemo do desnega kota spodaj (CILJ), pri tem pa moramo nabrati zahtevano vsoto števil.\n\nPremikamo se s puščicami. Z uporabo presledka lahko zadnjo potezo razveljavimo.")
     
    def generirajSez(self,n):
        """Generira seznam n podseznamov dolžine n, ki vsebujejo
           naključna cela števila."""
        self.seznamStevil = []
        for i in range(n):
            seznam = []
            for j in range(n):
                if self.stevila ==2:
                    st = random.choice([1,-1])*random.randint(1,5)
                else:
                    st = random.randint(1,5)
                seznam.append(st)
            self.seznamStevil += [seznam]
        
    def odstevalnik(self, preostalo = None):
        """Odštevalnik sporoča igralcu, koliko časa še ima do konca trenutne igre."""
        if preostalo !=None:
            self.preostalo = preostalo

        if self.preostalo <= 0:
            self.platno.itemconfigure(self.ura,text="Konec igre!")
            self.konec()
            
        else:
            if not self.konecIgre:
                self.platno.itemconfigure(self.ura,text="Imate še "+str(self.preostalo)+ " sekund"+self.koncnice(self.preostalo)+".")
                self.preostalo -= 1
                self.timer=self.platno.after(1000, self.odstevalnik)

    def premikLevo(self,event):
        """Preveri možnost premika in kliče metodo posodobi, da premik prikaže"""
        self.sredisceStaregaKvadrata=((self.x1+self.x2)/2,(self.y1+self.y2)/2)
        if self.x1 > (50+self.premik)and (self.x-1,self.y) not in self.sezZ and not self.konecIgre:
                self.x1 -= self.premik
                self.x2 -= self.premik
                self.x-=1
                self.posodobi()

    def premikDesno(self,event):
        """Preveri možnost premika in kliče metodo posodobi, da premik prikaže"""
        self.sredisceStaregaKvadrata=((self.x1+self.x2)/2,(self.y1+self.y2)/2)
        if self.x2 < (450-self.premik)and (self.x+1,self.y) not in self.sezZ and not self.konecIgre:
                self.x1 += self.premik
                self.x2 += self.premik
                self.x+=1
                self.posodobi()

    def premikGor(self,event):
        """Preveri možnost premika in kliče metodo posodobi, da premik prikaže"""
        self.sredisceStaregaKvadrata=((self.x1+self.x2)/2,(self.y1+self.y2)/2)
        if self.y1 > (50+self.premik)and (self.x,self.y-1) not in self.sezZ and not self.konecIgre:
                self.y1 -= self.premik
                self.y2 -= self.premik
                self.y-=1
                self.posodobi()

    def premikDol(self,event):
        """Preveri možnost premika in kliče metodo posodobi, da premik prikaže"""
        self.sredisceStaregaKvadrata=((self.x1+self.x2)/2,(self.y1+self.y2)/2)
        if self.y2 < (450-self.premik)and (self.x,self.y+1) not in self.sezZ and not self.konecIgre:
                self.y1 += self.premik
                self.y2 += self.premik
                self.y+=1
                self.posodobi()

    def posodobi(self):
        """Igralca premakne, nariše pot med starim in novim kvadratom in si zapomni
           premik. Uporabniku javi nove točke."""
        # Posodobimo položaj kroga
        self.platno.coords(self.jaz,self.x1, self.y1, self.x2, self.y2) 
        sredisceNovegaKvadrata=((self.x1+self.x2)/2,(self.y1+self.y2)/2)
        # Narišemo pot med starim in novim kvadratom
        self.crta=self.platno.create_line(self.sredisceStaregaKvadrata[0],self.sredisceStaregaKvadrata[1],
                                sredisceNovegaKvadrata[0],sredisceNovegaKvadrata[1],width=3)
    
        self.sezCrt.append(self.crta)
        self.sezZ.append((self.x,self.y))
        self.sezKoordinat.append((self.x1,self.y1,self.x2,self.y2))
        self.sredisceStaregaKvadrata=sredisceNovegaKvadrata

        self.nabraneT += self.seznamStevil[self.y][self.x]
        
        # Posodobimo tekst nabranih točk
        self.platno.itemconfigure(self.kolikoTrenutno, text="Imate "+str(self.nabraneT)+
                         " točk"+self.koncnice(self.nabraneT)+".")
        if (self.x,self.y)==(self.n-1,self.n-1):
            self.konec()
            
    def undo(self,event):
        """Razveljavi zadnjo potezo igralca.
        Sproži se ob pritisku tipke SPACE."""

        # Če smo prišli na cilj, ne dovolimo vračanja
        if not self.konecIgre:
            try:
                if (self.x ,self.y)!=(0,0):
                    self.nabraneT -= self.seznamStevil[self.y][self.x]
                    self.platno.itemconfigure(self.kolikoTrenutno,text="Imate "+str(self.nabraneT)+
                             " točk"+self.koncnice(self.nabraneT)+".")

                # Pobrišemo vse, kar je nastalo ob zadnji potezi
                # in premaknemo igralca
                self.platno.delete(self.sezCrt[-1])
                self.platno.delete(self.sezZ[-1])
                self.platno.coords(self.jaz,self.sezKoordinat[-2])
                self.sezZ=self.sezZ[:-1]
                self.sezCrt=self.sezCrt[:-1]
                self.sezKoordinat=self.sezKoordinat[:-1]
                self.x1,self.y1,self.x2,self.y2=self.sezKoordinat[-1]
                self.x,self.y=self.sezZ[-1]
                
            except:
                pass

    def znova(self):
        """Kliče se ob pritisku na ZAČNI IGRO/NOVA IGRA oziroma ob izbiri
           druge dimenzije tabele/drugih števil."""
        # unicimo menijske gumbe in pokažemo platno
        self.gumbZacni.destroy()
        self.gumbZapri.destroy()
        self.gumbOIgri.destroy()
        self.slika1.destroy()
        self.platno.pack()

        # Začetne pozicije igralca
        self.x1 = 50+400/(3*self.n)
        self.y1 = 50+400/(3*self.n)
        self.x2 = 50+800/(3*self.n)
        self.y2 = 50+800/(3*self.n)

        # Pobrišemo prejšnjo igro in ustvarimo nov seznam odvisen od dimenzije
        self.platno.delete(ALL)
        self.generirajSez(self.n)

        self.premik = 400/self.n
        self.nabraneT = self.seznamStevil[0][0]
        
        # Pokličemo funkcijo, ki izračuna možno pot
        self.izracunajTocke()

        self.ura = self.platno.create_text(50,20,text="",font=('Times', '20', 'bold italic'),anchor=W,fill="red")

        # Menijsko vrstimo aktiviramo
        self.master.config(menu=self.menu)

        # Vse morebitne prejšnje števce odstranimo
        if self.timer is not None:
            self.platno.after_cancel(self.timer)
            self.timer=None
        
        self.konecIgre=False
        self.odstevalnik(20*self.n+1)

        # Koliko tock potrebujemo na koncu
        self.kolikoNaKoncu = self.platno.create_text(450,470,text="" ,font=('Times', '18', 'bold italic'),anchor=E)
        self.platno.itemconfigure(self.kolikoNaKoncu, text="Zbrati morate "+str(self.tock)+" točk"+self.koncnice(self.tock)+".")
        
        # Koliko jih imamo trenutno           
        self.kolikoTrenutno = self.platno.create_text(50,40,text="",font=('Times', '18', 'bold italic'),anchor=W)
        self.platno.itemconfigure(self.kolikoTrenutno, text="Imate "+str(self.nabraneT)+" točk"+self.koncnice(self.nabraneT)+".")

        # Ura
        self.platno.itemconfigure(self.ura, text="Imate še "+str(self.preostalo)+ " sekund"+self.koncnice(self.preostalo)+".")

        # Prikaz za konec igre
        self.tekstKonec = self.platno.create_text(450,490,text="",font=('Times', '20', 'bold italic'),anchor=E)

        # Naredimo novo tabelo s števili iz novega seznama
        for i in range(self.n):
            for j in range(self.n):
                self.platno.create_rectangle(50+400*j/self.n,50+i*400/self.n,50+400*j/self.n+400/self.n,50+i*400/self.n+400/self.n,outline="red")
                self.platno.create_text(50+400*j/self.n+280/self.n,50+i*400/self.n+280/self.n,
                                        text=str(self.seznamStevil[i][j]),font=("Times", int(80/self.n))) 

        # Označimo start in cilj
        self.platno.create_rectangle(10,50,50,50+400/self.n,outline="black")
        self.platno.create_rectangle(450,450-400/self.n,490,450,outline="black")
        self.platno.create_text(30,50+200/self.n,
                                        text="\n".join("START"),justify=CENTER,font=("Times", int(45/self.n))) 
        self.platno.create_text(470,450-200/self.n,
                                        text="\n".join("CILJ"),justify=CENTER,font=("Times", int(50/self.n))) 

        try:
            self.platno.delete(self.jaz)
        except:
            pass

        # Nastavimo igralca na začetno pozicijo
        self.jaz = self.platno.create_oval(50+400/(3*self.n),50+400/(3*self.n),50+800/(3*self.n),50+800/(3*self.n),fill="black")
        
        # Koordinate kvadratov
        self.x=0
        self.y=0
        # Središče kvadrata        
        self.a=(self.x1+self.x2)/2
        self.b=(self.y1+self.y2)/2

        self.sezZ=[(0,0)] # Seznam zasedenih kvadratkov
        self.sezCrt=[] # Seznam crt, ki smo jih (bomo) narisali
        self.sezKoordinat=[(self.x1,self.y1,self.x2,self.y2)]

         
    def izracunajTocke(self):
        """Izračuna neko pot od levega zgornjega kota do desnega spodnjega kota, seštevek
           pa potem zahtevamo od uporabnika."""
        self.sez=[]
        for i in range(self.n):
            self.sez.append([])
        for el in self.sez:
            for i in range(self.n):
                el.append(0)
                
        self.sez[0][0]=1 #prva je že zasedena
        self.moznaResitev=[((self.x1+self.x2)/2,(self.y1+self.y2)/2)]
        self.tock = self.seznamStevil[0][0]
        trenutna=[0,0]
        while trenutna != [self.n-1,self.n-1]:
            mozneSmeri=[]
            if self.obstajaPotDomov([trenutna[0]+1,trenutna [1]]):
                mozneSmeri.append("desno")
            if self.obstajaPotDomov([trenutna[0]-1,trenutna [1]]):
                mozneSmeri.append("levo")
            if self.obstajaPotDomov([trenutna[0],trenutna [1]+1]):
                mozneSmeri.append("dol")
            if self.obstajaPotDomov([trenutna[0],trenutna [1]-1]):
                mozneSmeri.append("gor")
            kam=random.choice(mozneSmeri)
            (a,b)=self.moznaResitev[-1]
            if kam=="desno":
                trenutna=[trenutna[0]+1,trenutna [1]]
                self.moznaResitev.append((a+self.premik,b))
            elif kam=="levo":
                trenutna=[trenutna[0]-1,trenutna [1]]
                self.moznaResitev.append((a-self.premik,b))
            elif kam=="gor":
                trenutna=[trenutna[0],trenutna [1]-1]
                self.moznaResitev.append((a,b-self.premik))
            else: #dol
                trenutna=[trenutna[0],trenutna [1]+1]
                self.moznaResitev.append((a,b+self.premik))
            self.tock += self.seznamStevil[trenutna[1]][trenutna[0]]
            self.sez[trenutna[1]][trenutna[0]]=1

    def obstajaPotDomov(self,tocka):
        """Preverja, če lahko v trenutnem položaju prispemo do cilja/domov"""
        if tocka==[self.n-1,self.n-1]:
            return True #če smo že na cilju
        if tocka[0] <0 or tocka[0] > (self.n-1) or tocka[1]<0 or tocka[1] > (self.n-1):
            return False #če smo izven tabele, potem gotovo ne obstaja
        if self.sez[tocka[1]][tocka[0]] > 0:
            return False #če je ta točka že zasedena
        self.sez[tocka[1]][tocka[0]]=2 
        mozneT=[[tocka[0]+1,tocka[1]],[tocka[0]-1,tocka [1]],
                [tocka[0],tocka [1]+1],[tocka[0],tocka [1]-1]]
        for el in mozneT:
            if self.obstajaPotDomov(el):
                #če obstaja, pobrišemo vse dvojke
                self.sez[tocka[1]][tocka[0]]=0
                return True
        self.sez[tocka[1]][tocka[0]]=0 # če ne obstaja, potem zbrišemo "zadnjo" dvojko
        return False
    

    def pokaziResitev(self):
        """Pokaže rešitev, vendar igralcu ne dovoli več igranja."""
        self.konecIgre=True
        i=0
        while i<=len(self.moznaResitev)-2: #do predzadnjega
            self.platno.create_line(self.moznaResitev[i],self.moznaResitev[i+1],fill='red',width=6)
            i+=1
            
    def konec(self):
        """Igralcu sporoči, če je prišel na cilj z zahtevano količino točk in mu
$          ponudi novo igro"""
        self.konecIgre=True
        if (self.x,self.y)==(self.n-1,self.n-1) and self.nabraneT==self.tock:
            self.platno.itemconfigure(self.tekstKonec,text="Čestitamo, zmagali ste!",fill="blue")
            odgovor = messagebox.askokcancel("Čestitamo, zmagali ste!","Ponovna igra? \n\nSicer kliknite Cancel in izberite drugo velikost/števila,\nali pa si oglejte rešitev")
        else:
            self.platno.itemconfigure(self.tekstKonec,text="Tokrat vam žal ni uspelo.",fill="red")
            odgovor = messagebox.askokcancel("Tokrat vam žal ni uspelo.","Ponovna igra? \n\nSicer kliknite Cancel in izberite drugo velikost/števila,\nali pa si oglejte rešitev")
        if odgovor:
            self.znova()
        

    def nastaviTezavnost(self,n):
        """Nastavi novo dimenzijo, odvisno od n-ja, ter pokliče novo igro"""
        def pomozna():
            self.n=n
            self.znova()
        return pomozna

    def nastaviStevila(self,n):
        """Nastavi števila samo na pozitivna ali pa vsa cela števila ter
           pokliče novo igro"""
        def pomozna2():
            self.stevila = n
            self.znova()
        return pomozna2
            
    def koncnice(self,st):
        """Za lepši izpis"""
        stevilo = abs(st)%100
        if stevilo ==1:
            return "o"
        elif stevilo ==2:
            return "i"
        elif stevilo ==3 or stevilo==4:
            return "e"
        else:
            return ""
            
# Naredimo glavno okno
root = Tk()
root.title("Tabela števil")
aplikacija = Tabela(root)
root.mainloop()
