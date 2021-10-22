def one_digit(num, new_num):
   if int(num[-1]) in (1, 2, 3):
       new_num = new_num + "I" * int(num[-1])
       print(new_num)
   elif int(num[-1]) == 4:
       new_num = new_num + "IV"
       print(new_num)
   elif (int(num[-1]) > 4) and (int(num[-1]) < 9):
       new_num = new_num + "V" + "I" * (int(num[-1]) - 5)
       print(new_num)
   else:
       new_num = new_num + "IX"
       print(new_num)


def two_digit(num, new_num):
   if int(num[-2]) < 4:
       new_num += "X"*(int(num[-2]))
       return new_num
   elif int(num[-2]) == 4:
       new_num += "XL"
       return new_num
   elif (int(num[-2]) > 4) and (int(num[-2]) < 9):
       new_num += "L" + "X"*(int(num[-2])-5)
       return new_num
   else:
       new_num += "XC"
       return new_num


def to_roman_numerals():
   while True:
       try:
           number = int(input("Type the number you want to convert to roman numerals: "))
           number, numeral = str(number), ""
           if len(number) == 1:
               one_digit(number, numeral)
           elif len(number) == 2:
               two_digit(number, numeral)
               one_digit(number, two_digit(number, numeral))
           else:
               print("lolk")
       except ValueError:
           print("You cannot spell out a number.")

to_roman_numerals()
