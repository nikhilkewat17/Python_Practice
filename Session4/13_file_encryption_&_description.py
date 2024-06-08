def encrypt(text):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted_char = chr(((ord(char) - 97  + 3 ) % 26) + 97 ) if char.islower() else chr(((ord(char)-65 + 3) % 26) + 65)
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text


file_name="Nikhil"

with open(file_name,"r") as file:
    content = file.read()
    encryypted_content = encrypt(content)

print(encryypted_content)