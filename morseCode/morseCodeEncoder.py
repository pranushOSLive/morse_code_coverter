def definitions() -> []:
    arr1 = [".---","---...","---.---.","---..",".","..---.","------.","....","..",".---------","---.---",".---..","------","---.","---------",".------.","------.---",".---.","...","---","..---","...---",".------","---..---","---.------","------..","....."]
    arr2 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
    return arr1,arr2

def split(data):
    temp = []
    for val in data:
        temp.append(val)
    return temp
     

def encode(data="".lower()):
    definition = definitions()
    morse_def = definition[0]
    char_def = definition[1]
    temp_arr = split(data.lower())
    temp = []
    result = ""
    for val in temp_arr:
        try:
            temp.append(morse_def[char_def.index(val)])
            temp.append(" ")
        except:
            pass
    for val in temp:
        result += val
    return result

if __name__ == "__main__":
    print(encode(input("Enter text to encode into morse:")))
    