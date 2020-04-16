# 了不起的魔术师，编写一个名为make_great()的函数，对魔术师列表进行修改
def make_great(magicians_names, magician_great):

    while magicians_names:
        current_magician = magicians_names.pop()

        name = current_magician + " the Great"
        magician_great.append(name)


def show_magicians(magician_great):
    for great in magician_great:
        print(great)


list_0 = ['kaige', 'shanjie', 'nange']
list_1 = []

make_great(list_0[:], list_1)
show_magicians(list_1)