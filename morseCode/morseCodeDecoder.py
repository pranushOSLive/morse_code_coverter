def definitions() -> []:
    arr1 = [".---","---...","---.---.","---..",".","..---.","------.","....","..",".---------","---.---",".---..","------","---.","---------",".------.","------.---",".---.","...","---","..---","...---",".------","---..---","---.------","------..","....."]
    arr2 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
    return arr1,arr2

def split(data):
    temp = []
    for val in data:
        temp.append(val)
    return temp

     
def decode(data):
    definition = definitions()
    morse_def = definition[0]
    char_def = definition[1]
    temp_arr = []
    temp = ""
    arr = data.split(" ")
    for i in arr:
        try:
            temp_arr.append(char_def[morse_def.index(i)])
        except:
            pass
    for i in temp_arr:
        temp+=i
    return temp


if __name__ == "__main__":
    print(decode(input("Enter text to decode into morse:")))
