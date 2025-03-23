def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    
    return result


mode = input("Enter mode (encrypt/decrypt): ").strip().lower()
text = input("Enter the text: ")
shift = int(input("Enter the shift value: "))


output = caesar_cipher(text, shift, mode)
print(f"Output: {output}")
