# def format_less_than_10(day):
#     if day < 10:
#         return "0" + str(day)
#     else:
#         return day
#
# def show_month(name, days):
#     print(name)
#     print()
#     for day in days:
#         day += 1
#         if day % 7 == 0:
#             print(format_less_than_10(day)) #dodoanie formatowanie jesli liczba jest od 1 do 9
#         else:
#             print(format_less_than_10(day), end=" \t")
#     print()
#     print()

from calendar import show_month


list_elem = [
    ['happy', range(20)],
    ['sad', range(30)],
    ['angry', range(10)]
]

data = dict(list_elem)

for name, days_range in data.items():
    show_month(name, days_range)

