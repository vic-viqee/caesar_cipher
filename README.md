Caesar Cipher Encoder/Decoder

A simple Python program that implements the classic Caesar cipher encryption and decryption algorithm. This program allows users to easily encrypt and decrypt messages using a shift cipher method.

📋 Features

•
Encrypt text: Convert plain text into cipher text using a custom shift value

•
Decrypt text: Convert cipher text back to plain text using the same shift value

•
Input validation: Handles invalid inputs gracefully without crashing

•
Case preservation: Maintains original letter case (uppercase/lowercase)

•
Non-alphabet character handling: Leaves numbers, symbols, and spaces unchanged

🔧 Requirements

•
Python 3.x (no additional packages required)

🚀 How to Use

Running the Program

1.
Save the script as caesar_cipher.py

2.
Open a terminal/command prompt

3.
Run the program:

Bash


python caesar_cipher.py


Program Flow

1.
Start the program: You'll see the welcome message

2.
Enter your text: Type the message you want to encrypt or decrypt

3.
Enter shift value: Choose a number between 1 and 25

•
This is the number of positions each letter will be shifted

•
The same shift must be used for both encryption and decryption



4.
Choose operation:

•
Type E or ENCRYPT to encrypt your text

•
Type D or DECRYPT to decrypt your text



5.
View results: The program displays both original and processed text

Example Usage

Encryption Example:

Plain Text


=== Caesar Cipher Program ===
Enter the text: Hello World
Enter the shift value (1-25): 13
Do you want to (E)ncrypt or (D)ecrypt? E

Original text: Hello World
Encrypted text: Uryyb Jbeyq


Decryption Example:

Plain Text


=== Caesar Cipher Program ===
Enter the text: Uryyb Jbeyq
Enter the shift value (1-25): 13
Do you want to (E)ncrypt or (D)ecrypt? D

Encrypted text: Uryyb Jbeyq
Decrypted text: Hello World


📝 How the Caesar Cipher Works

The Caesar cipher is one of the simplest encryption techniques. It works by shifting each letter in the plaintext by a fixed number of positions down or up the alphabet.

Example with shift 3:

•
A → D

•
B → E

•
C → F

•
...

•
X → A

•
Y → B

•
Z → C

Formula:

•
Encryption: $E(x) = (x + shift) \pmod{26}$

•
Decryption: $D(x) = (x - shift) \pmod{26}$

Where $x$ is the position of the letter in the alphabet (0-25).

⚠️ Limitations

•
Shift range: Only supports shift values from 1 to 25

•
Alphabet: Only works with English alphabet characters (A-Z, a-z)

•
Security: NOT secure for real encryption - easy to crack

•
Special characters: Non-alphabet characters remain unchanged

🛠️ Code Structure

The program consists of several functions:

•
caesar(): Core encryption/decryption logic

•
encrypt(): Wrapper function for encryption

•
decrypt(): Wrapper function for decryption

•
get_valid_shift(): Validates user input for shift value

•
main(): Main program flow and user interaction

🔒 Security Note

This is an educational tool only! The Caesar cipher is extremely weak and should never be used for actual secure communication. It can be easily broken by:

•
Brute force (only 25 possible keys)

•
Frequency analysis

•
Known plaintext attacks

🤝 Contributing

Feel free to fork this repository and enhance the program! Some ideas for improvements:

•
Add support for different alphabets

•
Implement file encryption/decryption

•
Add a brute-force decryption option

•
Create a graphical user interface (GUI)

Created as a Python programming exercise to demonstrate:

•
String manipulation

•
User input validation

•
Function organization

•
Basic cryptography concepts

