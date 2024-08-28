import sys

def add(a,b):
    a = int(a)
    b = int(b)
    print(f"Additon: {a+b}")
    
def main():
    if len(sys.argv)==3:
        add(sys.argv[1],sys.argv[2])
    else:
        print("Something went wrong")

if __name__=="__main__":
    main()    
    