def my_roman_numerals_converter(son):
    eng_numb = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    rom_numb = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'LC', 'C', 'CD', 'D', 'DM', 'M']
    javob = ""
    a = 12
    while son != 0:
        if eng_numb[a] <= son:
            javob += rom_numb[a]
            son = son - eng_numb[a]
        else:
            a -= 1

    return javob

(my_roman_numerals_converter(19))
(my_roman_numerals_converter(59))
(my_roman_numerals_converter(794))
(my_roman_numerals_converter(2024))
