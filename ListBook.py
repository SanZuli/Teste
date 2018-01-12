import os
spc=("""
""")

def comarq():
    try:   
        luiz=open("BN","r")
        luiz.closed
    except FileNotFoundError:
        il=open("BN","w")
        

def create():
     b1=input("Nome do livro:")
     b2=input("Gênero:")
     b3=input("Autor(a):")
     b4=input("Estado Da Leitura:")

     e1=(b1+spc+b2+spc+b3+spc+b4)
     c1=open(b1, "w")
     c1.write(e1);
     c1.closed
     
     c2=open("BN", "r")
     c3=c2.read()
     c4=open("BN","w")
     c5=(c3+spc+b1)
     c4.write(c5)
     c4.closed

     print("Pronto",b1,"Foi adicionado aos seus livros")
     comeco();


def comeco():
    a= input("""
    [1]Ver meus livros
    [2]Adicionar novo livro
    [3]Editar livro existente
    [4]Apagar livro
    """)

    if a=="1":
          h1=open("BN","r")
          h2=h1.read()
          print(h2)
          h1.closed
          h3=input("Continuar[ENTER]")
          comeco();
         
    if a== "2":
        create();

    if a=="3":
        f1=input ("Qual livro deseja abir?: ")
        b1=f1
        b1=input("Nome do livro:")
        b2=input("Gênero:")
        b3=input("Autor(a):")
        b4=input("Estado Da Leitura:")
        c6=open( b1, "w")
        e1=(b1+spc+b2+spc+b3+spc+b4+spc)
        c6.write(e1)
        os.remove(f1)

    if a=="4":
        g1=input ("Qual livro deseja apagar?: ")
        g2=input ("Tem certeza? [S/N]")
        if g2 in ["S", "s"]:
            os.remove (g1)
            print("Livro Apagado")
            comeco();
        if g2 in ["N", "n"]:
            comeco();

comarq();
comeco();
