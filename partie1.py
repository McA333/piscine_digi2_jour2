def read_on_line(filename) :

    filename = open(str(filename), 'r')
    print(filename.readlines(1))
    filename.close()

def write_text(filename, text) :

    text = str(text)

    filename = open(str(filename), 'w')
    filename.write(text)
    filename.close()

#read_on_line(input("Entrer le nom du fichier à ouvrir :"))
#write_text(input("Entrer un nom de fichier à creer : "), input("Entrer le texte : "))