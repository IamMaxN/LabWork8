import itertools

def taxi_min_costs(N, distances, tariffs):
    # Генерируем все возможные перестановки сотрудников и машин
    permutations = list(itertools.permutations(range(N)))

    # Инициализируем минимальную стоимость и номера такси для каждой перестановки
    min_cost = float('inf')
    best_assignment = None

    for perm in permutations:
        cost = 0
        for i in range(N):
            cost += distances[i] * tariffs[perm[i]]
        if cost < min_cost:
            min_cost = cost
            best_assignment = perm

    return [taxi + 1 for taxi in best_assignment], min_cost  # Добавляем 1, чтобы индексация начиналась с 1


# Ввод данных от пользователя
N = int(input("Введите количество сотрудников (натуральное число от 1 до 1000): "))
print("Введите расстояния в километрах для каждого сотрудника через пробел (положительные целые числа):")
distances = list(map(int, input().split()))
print("Введите тарифы в рублях за проезд одного километра для каждой машины через пробел (положительные целые числа):")
tariffs = list(map(int, input().split()))

# Вызов функции и вывод результата
taxi_numbers, total_cost = taxi_min_costs(N, distances, tariffs)
print("Номера такси для каждого сотрудника:", taxi_numbers)
print("Общая стоимость всех поездок:", total_cost, "руб.")





def sklonenierubley(num):
    if num % 10 == 1 and num % 100 != 11:
        return "рубль"
    elif num % 10 in [2, 3, 4] and num % 100 not in [12, 13, 14]:
        return "рубля"
    else:
        return "рублей"

def okonchanie (num):
    kos = num % 10000
    if kos == 0:
        return "тысяч "
    if kos >= 1000 and kos < 2000:
        return "тысяча "
    elif kos >= 2000 and kos < 5000:
        return "тысячи "
    elif kos >= 5000 and kos < 100001:
        return "тысяч "
    
def numbertowords(num):
    units = ["", "один ", "два ", "три ", "четыре ", "пять ", "шесть ", "семь ", "восемь ", "девять "]
    tens = ["", "десять ", "двадцать ", "тридцать ", "сорок ", "пятьдесят ", "шестьдесят ", "семьдесят ", "восемьдесят ", "девяносто "]
    hundreds = ["", "сто ", "двести ", "триста ", "четыреста ", "пятьсот ", "шестьсот ", "семьсот ", "восемьсот ", "девятьсот "]
    iskl = ["","одна ","две "]
    
    words = ""
    if num // 1000 > 0:
        thousands = num // 1000
        words += numbertowords(thousands) + okonchanie (num)
        num %= 1000
    
    if num // 100 > 0:
        words += hundreds[num // 100]
        num %= 100
    
    if num // 10 > 1:
        words += tens[num // 10]
        num %= 10
        
    elif num // 10 == 1:
        if num == 10:
            words += "десять "
        elif num == 11:
            words += "одиннадцать "
        elif num == 12:
            words += "двенадцать "
        elif num == 13:
            words += "тринадцать "
        elif num == 14:
            words += "четырнадцать "
        elif num == 15:
            words += "пятнадцать "
        elif num == 16:
            words += "шестнадцать "
        elif num == 17:
            words += "семнадцать "
        elif num == 18:
            words += "восемнадцать "
        elif num == 19:           
            words += "девятнадцать "
        return words
         
    if num > 0:
        words += units[num]
    return words



num = total_cost
ch = ""
if num > 999 and num < 3000:   
    if num >= 1000 and num < 2000:
        num = num%1000
        ch = "одна тыcяча "
    if num >= 2000 and num < 3000:
        num = num%1000
        ch = "две тысячи "

words = numbertowords(num)
rubles = sklonenierubley(num)
print(f"({ch}{words}{rubles})")

    
