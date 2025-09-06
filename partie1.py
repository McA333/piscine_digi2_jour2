def read_on_line(filename) :

    filename = open(str(filename), 'r')
    print(filename.readlines(1))
    filename.close()

def write_text(filename, text) :

    text = str(text)

    filename = open(str(filename), 'w')
    filename.write(text)
    filename.close()

def copy_characters(input_file, output_file, nb) :

    nb = int(nb)

    input_file = open(str(input_file), 'r')
    copy_box = input_file.read(nb)
    input_file.close()

    output_file = open(str(output_file), 'a')
    output_file.write('\n' * 2)
    for character in copy_box :
        output_file.write(character)
    output_file.close()

def read_all_lines(filename) :

    filename = open(str(filename), 'r')
    lines = (filename.readlines())
    jump_line_by_two = lines[::2]

    print(lines)
    print(jump_line_by_two)

#read_on_line(input("Entrer le nom du fichier à ouvrir :"))
#write_text(input("Entrer un nom de fichier à creer : "), input("Entrer le texte : "))
#copy_characters(input("Entrer le fichier source : "), input("Entrer le fichier destination : "), input("Entrer le nombre de caractère à copier :"))
#read_all_lines(input("Entrer le nom du fichier : "))