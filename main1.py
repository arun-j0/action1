import sys

def main():
    message = sys.argv[1] if len(sys.argv)>1 else "No input"
    print(message)
    
if __name__ == "__main__":
    main()
    
    
    