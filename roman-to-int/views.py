from django.shortcuts import render


roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def is_valid(num):
    for letter in num:
        if letter in roman.keys():
            continue
        else:
            return False
    return True


def roman_to_int(s: str) -> int:
    num = 0
    for i in range(len(s) - 1):
        if roman[s[i]] < roman[s[i + 1]]:
            num += roman[s[i]] * (-1)
            continue
        num += roman[s[i]]
    num += roman[s[-1]]
    return num


def converter(request):
    if request.method == 'POST':
        roman_num = request.POST['roman_num']
        if is_valid(roman_num):
            roman_num = roman_num.upper()
            num = roman_to_int(roman_num)
        else:
            num = "Вы ввели некорректное значение!"
        return render(request, 'main_app/converter.html', {'roman_num': roman_num, 'num': num})
    return render(request, 'main_app/converter.html')
