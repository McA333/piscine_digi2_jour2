def native_csv_read(file) :

    with open(file, 'r') as file :
        lines = (file.readlines())
        print(lines)

native_csv_read("../orders.csv")