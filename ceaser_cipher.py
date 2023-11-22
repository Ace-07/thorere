def encrypted(letter, secret_key):
    list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
    word_list = list(letter)
    store = []
    for i in word_list:
        if i == " ":
            store.append(" ")
        else:
            for j in range(26):
                if list1[j] == i:
                    add_up = (j + secret_key) % 26
                    store.append(list1[add_up])
    store2 = ''.join(map(str, store))
    print(store2)
def decrypted(letter, secret_key):
    list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']

    word_list = list(letter)
    store = []
    total = 0
    for i in word_list:
        if i == " ":
            store.append(" ")
        else:
            for j in range(26):
                if list1[j] == i:
                    add_up = (j - secret_key)
                    if add_up < 0:
                        total = (add_up + 26) % 26
                        store.append(list1[total])
                    else:
                        total = add_up % 26
                        store.append(list1[add_up])
    store2 = ''.join(map(str, store))
    print(store2)


word = "welcome"
print(word)
letter = word
while letter != "not":
    word = input('enter the word ur want to type or type "not" to escape the world: ')
    if word == "not":
        letter = word
    else:
        key = int(input("choose ur key: "))
        choose = input("select encrypted or decrypted: ")
        taken = choose
        if taken == "encrypt":
            print("we will encrypt it for you: ")
            encrypted(letter=word, secret_key=key)
        elif taken == "decrypt":
            print("we will decrypt it for you: ")
            decrypted(letter=word,secret_key=key)
print("thank you")