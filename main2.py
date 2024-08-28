import sys


def greet(first,last):
    print(f"Hellooooo! ,{first} {last}")



def main():
    if len(sys.argv)!=3:
        print("Unexpected no of argumensts")
        sys.exit(1)
    greet(sys.argv[1],sys.argv[2])
        
if __name__ == "__main__":
    main()