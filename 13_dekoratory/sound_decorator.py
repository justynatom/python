
def sound_decorator(func_as_param):
    def draw_pattern_nested():
        print("hau hau")
        func_as_param()

    return draw_pattern_nested

@sound_decorator
def get_dog_info():
    print("pies to najlepszy przyjaciel czlowieka")

@sound_decorator
def get_turtle_info():
    print("zółw to nudne zwierze")
get_dog_info()
print("*****")

# dog_info=sound_decorator(get_dog_info)
# dog_info()

get_turtle_info()