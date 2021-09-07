import tkinter

#  Functions
def uppercase(word):
    counter = 0
    for all in word:
        if all.isupper() == True:
            counter += 1
    if counter > 0:
        word = word.lower()
        word = list(word)
        word[1] = word[1].upper()
        word = "".join(word)
    return word


def pig_latin(text):
    pig_text = text.split()
    new_string = ""
    for each in pig_text:
        if (each.isalpha() == True) and (len(each) > 1):
            each = uppercase(each)
            new_string += each[1:] + each[0] + "ay "

        elif (each.isalpha() == True) and (len(each) == 1):
            new_string += each + "ay "

        elif each.isdigit() == True:
            new_string += each + "ay "

        elif (each.isalpha() == False) and (each.isdigit() == False) and ("." not in each) and ("," not in each) and ("!" not in each) and ("?" not in each) and (len(each) > 2):
            each = uppercase(each)
            new_string += each[1:] + each[0] + "ay "

        elif (each.isalpha() == False) and (each.isdigit() == False) and ("." in each) and (len(each) > 2):
            each = each.replace(".", "")
            each = uppercase(each)
            new_string += each[1:] + each[0] + "ay. "

        elif (each.isalpha() == False) and (each.isdigit() == False) and ("," in each) and (len(each) > 2):
            each = each.replace(",", "")
            each = uppercase(each)
            new_string += each[1:] + each[0] + "ay, "

        elif (each.isalpha() == False) and (each.isdigit() == False) and ("!" in each) and (len(each) > 2):
            each = each.replace("!", "")
            each = uppercase(each)
            new_string += each[1:] + each[0] + "ay! "

        elif (each.isalpha() == False) and (each.isdigit() == False) and ("?" in each) and (len(each) > 2):
            each = each.replace("?", "")
            each = uppercase(each)
            new_string += each[1:] + each[0] + "ay? "

        elif (each.isalpha() == False) and (each.isdigit() == False) and ("." in each) and (len(each) == 1):
            new_string += each + "ay. "

        elif (each.isalpha() == False) and (each.isdigit() == False) and ("," in each) and (len(each) == 1):
            new_string += each + "ay, "

        elif (each.isalpha() == False) and (each.isdigit() == False) and ("!" in each) and (len(each) == 1):
            new_string += each + "ay! "

#        elif (each.isalpha() == False) and (each.isdigit() == False) and ("?" in each) and (len(each) == 1):
        else:
            new_string += each + "ay? "
    text_box_2.insert(0, new_string)
#    print("Old:{}\nNew:{}".format(text, new_string))


def copy_to_clipboard():
    window.clipboard_clear()
    window.clipboard_append(text_box_2.get())


def erase():
    text_box_1.delete(0, "end")
    text_box_2.delete(0, "end")


"""
Variables
"""
window = tkinter.Tk()
instruction_1 = tkinter.Label(window, text="Type text into this box", bg="#ffcccc", fg="#000000")
text_box_1 = tkinter.Entry(window, width=35)
text_box_2 = tkinter.Entry(window, width=35)
copy_button = tkinter.Button(window, text="Copy", command=copy_to_clipboard, padx="20", bg="#ff8080", fg="#ffffff")
convert_button = tkinter.Button(window, text="Convert", command= lambda : pig_latin(text_box_1.get()), padx="20", bg="#ff8080", fg="#ffffff")
erase_button = tkinter.Button(window, text="Delete Text", command=erase, padx="20", bg="#ff8080", fg="#ffffff")
#pig_latin("I will destroy you, son. It won't be instantaneous, but it will happen!")

"""
Display
"""
instruction_1.grid(row=0, column=0, columnspan=3)
text_box_1.grid(row=1, column=0, columnspan=3, padx=5, pady=5)
text_box_2.grid(row=2, column=0, columnspan=3, padx=5, pady=5)
copy_button.grid(row=3, column=0)
convert_button.grid(row=3, column=1)
erase_button.grid(row=3, column=2)
window.configure(background="#ffcccc")
window.title("Pig Latin Converter!")
window.mainloop()