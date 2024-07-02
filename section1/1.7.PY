def main():
    while True:
        print("String Operations Menu:")
        print("1. Convert to Uppercase")
        print("2. Convert to Lowercase")
        print("3. Check if Palindrome")
        print("4. Count Vowels")
        print("5. Count Consonants")
        print("6. Reverse String")
        print("7. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 7:
            break
        
        string = input("Enter a string: ")
        
        if choice == 1:
            print("Uppercase:", string.upper())
        elif choice == 2:
            print("Lowercase:", string.lower())
        elif choice == 3:
            if string == string[::-1]:
                print("The string is a palindrome.")
            else:
                print("The string is not a palindrome.")
        elif choice == 4:
            vowels = "aeiou"
            count = sum(1 for char in string.lower() if char in vowels)
            print("Vowels:", count)
        elif choice == 5:
            consonants = "bcdfghjklmnpqrstvwxyz"
            count = sum(1 for char in string.lower() if char in consonants)
            print("Consonants:", count)
        elif choice == 6:
            print("Reversed:", string[::-1])
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
