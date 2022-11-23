def uppercase_decorator(func_param):
    def make_big():
        text = func_param()
        return text.upper()

    return make_big


@uppercase_decorator
def show_string():
    return "Hakuna Matata"


print(show_string())

# def uppercase_decorator(text):
#     def get_text(text):
#         return text
#
# @uppercase_decorator
# def upper_text(text):
#     return text.upper
#     print(text.upper)
#
#
#
#
# uppercase_decorator("hello")