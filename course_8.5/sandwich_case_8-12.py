# 三明治：写一个函数接受顾客要在三明治中添加的一些列食材，这个函数只有一个形参
def make_sanfwich(*foods):
    print(foods)

make_sanfwich('egg')
make_sanfwich('egg', 'apple')
make_sanfwich('egg', 'apple', 'meat')