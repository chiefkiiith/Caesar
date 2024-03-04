
def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            if mode == 'encrypt':
                result += chr((ord(char) - offset + shift) % 26 + offset)
            elif mode == 'decrypt':
                result += chr((ord(char) - offset - shift) % 26 + offset)
        else:
            result += char
    return result

def main():
    print("Welcome to the Caesar Cipher Interaction Tool!")

    while True:
        try:
            shift = int(input("Enter the shift value (an integer): "))
            break
        except ValueError:
            print("Please enter a valid integer for the shift.")
            continue

    text = input("Enter the text to encrypt/decrypt: ").strip()

    while True:
        mode = input("Enter 'encrypt' or 'decrypt': ").lower()
        if mode in ['encrypt', 'decrypt']:
            break
        else:
            print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")

    result_text = caesar_cipher(text, shift, mode)

    print("\nResults:")
    print(f"Original Text: {text}")
    print(f"{mode.capitalize()}ed Text (Shift={shift}): {result_text}")

if __name__ == "__main__":
    main()