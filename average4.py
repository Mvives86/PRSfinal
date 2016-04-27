def main():
    sum = 0.0
    count = 0
    x = input("Please enter a number(hit enter 2'ce to exit): ")

    while x != "":
        n = eval(x)
        sum += n
        count += 1
        x = input("Please enter a number: ")
    print("\nThe average is: ", sum / count)

main()
