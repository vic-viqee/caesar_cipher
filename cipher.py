def caesar(text, shift, encrypt=True):
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'
    
    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    if not encrypt:
        shift = -shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    result_text = text.translate(translation_table)
    return result_text

def encrypt(text, shift):
    return caesar(text, shift)

def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)

def get_valid_shift():
    """Get and validate shift input from user."""
    while True:
        try:
            shift = int(input("Enter the shift value (1-25): "))
            if 1 <= shift <= 25:
                return shift
            else:
                print("Shift must be between 1 and 25. Please try again.")
        except ValueError:
            print("Invalid input! Shift must be an integer between 1 and 25. Please try again.")

def main():
    print("=== Caesar Cipher Program ===")
    
    # Get user input
    text = input("Enter the text: ")
    
    # Get and validate shift (now with try-except)
    shift = get_valid_shift()
    
    # Get encryption/decryption choice
    while True:
        choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").upper()
        if choice in ['E', 'ENCRYPT']:
            result = encrypt(text, shift)
            print(f"\nOriginal text: {text}")
            print(f"Encrypted text: {result}")
            break
        elif choice in ['D', 'DECRYPT']:
            result = decrypt(text, shift)
            print(f"\nEncrypted text: {text}")
            print(f"Decrypted text: {result}")
            break
        else:
            print("Please enter 'E' for encrypt or 'D' for decrypt.")

if __name__ == "__main__":
    main()