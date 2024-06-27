# -*- coding:utf-8 -*
import os

print(
""" 
On dispose d'un tableau de n*n cases, n est un entier qui sera choisi par l'utilisateur.
Le principe est de reussir a placer n pions dans le tableau de telle sorte qu'aucun pion ne soit sur la trajectoire de l'autre

""")
dim_table=3 # Variable representant le nombre de pions sur chaque cote de la table.
# Boucle de validation de la variable dim_table
while dim_table<=3:
    try: dim_table=int(input("Entrer le nombre 'n':     "))
    except ValueError:
        print("Veillez entrer un nombre entier")
        dim_table=3
    else:
        if dim_table<0: print("Votre nombre entier est negatif, veillez entrer une valeur positive.")
        elif dim_table<=3: print("Le nombre doit etre superieure ou egal a '4'.")

# Creation de la table devant contenir les differents pions
liste_initiale=[['.' for i in range(dim_table)] for i in range(dim_table)]
print("Voici a quoi ressemble votre table des le depart:\n")
for i in range(dim_table):
    print(liste_initiale[i],"\n")
print("Vous allez maintenant choisir un a un les differentes positions de vos pions dans la table:\n Les lignes tout comme les colonnes sont numerotes de 0 a {}\n".format(dim_table-1))
continuer=True # Variable permettant de savoir si l'on a bien terminer le jeu ou pas
stockage_positions=[] # Creation d'une liste qui stoquerra les positions interdites aux pions
gain=[] # Creation d'une liste qui accueillera un nouvel element a chaque bon positionnement d'un pion sur la table. Selon sa longueur l'on pourra passer ou pas la variable 'continuer' a 'False'
while continuer:
    (pos_row,pos_col)=(-1,-1) # Ce tuple stoque les positions ( Suivant la ligne et la colonne ) d'un pion
    while pos_row<0 or pos_row>dim_table-1 or pos_col<0 or pos_col>dim_table-1:
        try: (pos_row,pos_col)=(int(input("Indiquer un numero de ligne:     ")),int(input("Indiquer un numero de colonne:     ")))
        except ValueError:
            print("Que des nombres entiers sont pris en charge")
            (pos_row,pos_col)=(-1,-1)
        else:
            if pos_row<0 or pos_col<0: print("Veillez n'indiquer que des valeurs positives.")
            elif pos_row>=dim_table or pos_col>=dim_table: print("Le plus grand numero accepté est '{}'.".format(dim_table-1))
    
    if len(gain)==0:
        liste_initiale[pos_row][pos_col]='X'
        m=-1
        for i in range(dim_table):
            m+=1
            for j in range(dim_table):
                locked_pos_row_1=pos_row-m ####  Cette variable et les trois autres qui suivent representent des lignes
                locked_pos_row_2=pos_row+m ####     ou des colonnes bloquées
                locked_pos_col_1=pos_col-m ####  Un tuple formé de deux de ces variables contitue un emplacement inaccessible
                locked_pos_col_2=pos_col+m ####     pour un pion; celui-ci est donc stoqué dans la liste stockage_positions
                if (0<=locked_pos_row_1<=dim_table-1 and 0<=locked_pos_col_1<=dim_table-1):stockage_positions.append((locked_pos_row_1,locked_pos_col_1))
                if (0<=locked_pos_row_1<=dim_table-1 and 0<=locked_pos_col_2<=dim_table-1):stockage_positions.append((locked_pos_row_1,locked_pos_col_2))
                if (0<=locked_pos_row_2<=dim_table-1 and 0<=locked_pos_col_1<=dim_table-1):stockage_positions.append((locked_pos_row_2,locked_pos_col_1))
                if (0<=locked_pos_row_2<=dim_table-1 and 0<=locked_pos_col_2<=dim_table-1):stockage_positions.append((locked_pos_row_2,locked_pos_col_2))
                if  (i!=pos_row and j==pos_col) or (i==pos_row and j!=pos_col):
                    stockage_positions.append((i,j))
        gain.append(1)
        for i in range(dim_table):
            print(liste_initiale[i],"\n")
    else:
        meme_direction=True # Indique si un pion se trouve sur la meme trajectoire qu'un autre pion deja en place
        if (pos_row,pos_col) in stockage_positions:
            print("Ces parametres ne sont pas valides, vous vous trouvez sur une meme trajectoire avec l'une des reines")
            continue
        else:
            m=-1
            for i in range(dim_table):
                m+=1
                for j in range(dim_table):
                    locked_pos_row_1=pos_row-m
                    locked_pos_row_2=pos_row+m
                    locked_pos_col_1=pos_col-m
                    locked_pos_col_2=pos_col+m
                    if (0<=locked_pos_row_1<=dim_table-1 and 0<=locked_pos_col_1<=dim_table-1):stockage_positions.append((locked_pos_row_1,locked_pos_col_1))
                    if (0<=locked_pos_row_1<=dim_table-1 and 0<=locked_pos_col_2<=dim_table-1):stockage_positions.append((locked_pos_row_1,locked_pos_col_2))
                    if (0<=locked_pos_row_2<=dim_table-1 and 0<=locked_pos_col_1<=dim_table-1):stockage_positions.append((locked_pos_row_2,locked_pos_col_1))
                    if (0<=locked_pos_row_2<=dim_table-1 and 0<=locked_pos_col_2<=dim_table-1):stockage_positions.append((locked_pos_row_2,locked_pos_col_2))
                    if  (i!=pos_row and j==pos_col) or (i==pos_row and j!=pos_col):
                        stockage_positions.append((i,j))
            meme_direction=False
            if meme_direction==False:
                liste_initiale[pos_row][pos_col]='X'
                gain.append(1)
                for i in range(dim_table):
                    print(liste_initiale[i],"\n")

    if len(gain)==dim_table:
        print("Bravo, vous venez de terminer la partie avec brio")
        continuer=False


os.system("pause")