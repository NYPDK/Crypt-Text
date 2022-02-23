import os, random, string, customkey, time, pyperclip

defaultKey = {"a": "00-", "A": "00+", "b": "01-", "B": "01+", "c": "02-", "C": "02+", "d": "03-", "D": "03+", "e": "04-", "E": "04+", "f": "05-", "F": "05+", "g": "06-", "G": "06+", "h": "07-", "H": "07+", "i": "08-", "I": "08+", "j": "09-", "J": "09+", "k": "10-", "K": "10+", "l": "11-", "L": "11+", "m": "12-", "M": "12+", "n": "13-", "N": "13+", "o": "14-", "O": "14+", "p": "15-", "P": "15+", "q": "16-", "Q": "16+", "r": "17-", "R": "17+", "s": "18-", "S": "18+", "t": "19-", "T": "19+", "u": "20-", "U": "20+", "v": "21-", "V": "21+", "w": "22-", "W": "22+", "x": "23-", "X": "23+", "y": "24-", "Y": "24+", "z": "25-", "Z": "25+", "1": "26$", "2": "27$", "3": "28$", "4": "29$", "5": "30$", "6": "31$", "7": "32$", "8": "33$", "9": "34$", "0": "35$", "`": "36%", "~": "37%", "!": "38%", "@": "^v^", "#": "39%", "$": "40%", "%": "41%", "^": "42%", "&": "43%", "*": "44%", "(": "45%", ")": "46%", "-": "47%", "_": "48%", "=": "49%", "+": "50%", "[": "51%", "{": "52%", "]": "53%", "}": "54%", "\\": "55%", "|": "56%", ";": "57%", ":": "58%", "'": "59%", "\"": "60%", ",": "61%", "<": "62%", ".": "63%", ">": "64%", "/": "65%", "?": "66%", " ": "+=+", "\n": "<->"}
header = " ██████╗██████╗ ██╗   ██╗██████╗ ████████╗    ████████╗██╗  ██╗████████╗\n██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝    ╚══██╔══╝╚██╗██╔╝╚══██╔══╝\n██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║          ██║    ╚███╔╝    ██║   \n██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║          ██║    ██╔██╗    ██║   \n╚██████╗██║  ██║   ██║   ██║        ██║          ██║   ██╔╝ ██╗   ██║   \n ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝          ╚═╝   ╚═╝  ╚═╝   ╚═╝   \n                                                                        "

def keygen():
    keys = list(defaultKey.keys())
    chars = (string.ascii_letters + string.digits + "!#$%&()*+,-./:;<=>?@[]^_`~")
    gen = {}
    for key in keys:
        val = ""
        for i in range(0, 8):
            val += random.choice(chars) 
        gen[key] = val
    os.system("cls")
    print(header)
    print("Key generated, restart to apply!")
    with open("customkey.py", "w") as w:
        w.write(f"customKey = {gen}")
    
def encode(customMessage, key):
    chars = []
    encodedString = ""
    if not customMessage:
        with open("input.txt") as f:
            for line in f:
                chars += line
    else:
        for chr in customMessage:
            chars += chr
    for char in chars:
        encodedString += f"|{key[char]}"
    os.system("cls")
    print(header)
    print("Encrypted text output to encrypted.txt!")
    with open("encrypted.txt", "w") as w:
        w.write(encodedString[1:])

def decode(customMessage, key):
    decodedString = ""
    keys = list(key.keys())
    vals = list(key.values())
    if not customMessage:
        try:
            with open("encrypted.txt") as f:
                for line in f:
                    split = line.split("|")
        except Exception as e:
            os.system("cls")
            print(header)
            print(f"Error: {e}")
            return
    else:
        split = customMessage.split("|")
    os.system("cls")
    print(header)
    try:
        for code in split:
            position = vals.index(f"{code}")
            decodedString += keys[position]
    except Exception as e:
        print(f"Key Error!\nError: {e}")
    print(decodedString)
    with open("decrypted.txt", "w") as w:
        w.write(decodedString)

def menu():
    print(header)
    print("If you want to encrypt from a text file, name it \"input\" with file type txt.")
    while True:
        choice = input("\n[1] Encrypt a message\n[2] Decrypt a message\n[3] Generate custom key\n[4] Copy custom key\n[5] Input custom key\n[6] Quit\nChoice: ")
        if choice == "1":
            customMessage = input("Input message to encrypt (leave blank to encrypt from input.txt): ")
            key = input("Do you want to use your custom key? If N then default key is used. (y/N): ")
            if key == "y" or key == "Y":
                encode(customMessage, customkey.customKey)
            elif key == "" or key == "n" or key == "N":
                encode(customMessage, defaultKey)
            else:
                pass
        elif choice == "2":
            customMessage = input("Input message to decrypt (leave blank to decode from encrypted.txt): ")
            key = input("Do you want to use your custom key? (y/N): ")
            if key == "y" or key == "Y":
                decode(customMessage, customkey.customKey)
            elif key == "" or key == "n" or key == "N":
                decode(customMessage, defaultKey)
            else:
                pass
        elif choice == "3":
            confirm = input("Are you sure you want to generate a new key? (y/N): ")
            if confirm == "y" or confirm == "Y":
                keygen()
            elif confirm == "" or confirm == "n" or confirm == "N":
                print("OK! Not generating a new key. :)")
                time.sleep(1)
                os.system("cls")
                print(header)
            else:
                print("Why did you even input that? Not generating a new key.")
                time.sleep(2)
                os.system("cls")
                print(header)
        elif choice == "4":
            with open("customkey.py") as f:
                for line in f:
                    message = line.split("= ")
            pyperclip.copy(message[1])
            os.system("cls")
            print(header)
            print("Copied custom key to clipboard.")
        elif choice == "5":
            keyInput = input("Paste key: ")
            with open("customkey.py", "w") as w:
                if keyInput != "":
                    w.write(f"customKey = {keyInput}")
                    os.system("cls")
                    print(header)
                    print("Key appplied, restart to apply!")
                else:
                    os.system("cls")
                    print(header)
                    print("No key given! Please try again!")
        elif choice == "6":
            quit()
        else:
            # cry about it
            os.system("cls")
            print(header)

if __name__ == "__main__":
    menu()