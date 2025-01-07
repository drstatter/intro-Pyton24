def print_row(size, char):
    for _ in range(size):
        print(char, end='')
#print_row(4,"#")


def print_triangle(base, char="*"):
    for i in range(base):
        print_row(i+1, char)
        print()

print_triangle(3,"#")
print_triangle(3)
def main():
    base= int(input("type the base "))
    char="$"
    print_triangle(base, char)
if __name__ == "__main__":
    main()