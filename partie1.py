def read_on_line(filename) :

    filename = open(str(filename), 'r')
    print(filename.readlines(1))
    filename.close()

#read_on_line(input("Entrer le nom du fichier à ouvrir :"))