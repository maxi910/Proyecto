import random

def matrizdzn(matrix, filename="matrix_data.dzn"):
    with open(filename, 'w') as f:
        f.write("matrix = [|\n")
        for row in matrix:
            row_str = ", ".join(map(str, row))
            f.write(f"  {row_str} |\n")
        f.write("|];\n")

    print(f"El archivo se guardo '{filename}'")




