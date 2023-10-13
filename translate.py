import gtts

def read_from_file():
    global words_bank

    f = open("assignment8/translate.txt", "r")
    f.close()

def show_menu():
    print ("Welcome to my translate")
    print ("1: translate english to persian")
    print ("2: translate persian to english")
    print ("3: add a new word to database")
    print ("exit")

def translate_english_to_persian ():
        user_text = input("please enter your english text: ")
        user_words =user_text.split(" ")
        output = ""

        for user_word in user_words:
            for word in words_bank:
                if user_word == word["en"]:
                    output = output + word["fa"] + " "
                    break
            else:
                output = output + user_word +" "
        print(output)

def translate_persian_to_english():
    user_text = input("please enter your persian text: ")
    user_words = user_text.split(".")
    output = ""

    for user_word in user_words:
        for word in words_bank:
            if user_word == word["fa"]:
                output = output + word["en"] + " "
                break
            else:
                output = output + user_word +" "
        print(output)
    x = gtts.GTTS(output , lang = "en" , slow = false)  
    x.save("assignment8/voice.mp3")  

def add_words():
    user_text_english = input("please enter your english word: ")
    user_text_persian = input("please enter your persian word: ")
    new_word = {'en' :user_text_english , 'fa' :user_text_persian }
    words_bank.append(new_word)

    
while True:    
    read_from_file()
    show_menu()

    choice = int (input("enter your choice : "))

    if choice == 1:
        translate_english_to_persian()
    elif choice == 2:
        translate_persian_to_english()
    elif choice == 3:
        add_words()
    elif choice == 4:    
        exit(0)