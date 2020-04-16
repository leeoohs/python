# 导入特定的函数
# 通过逗号分隔函数名，可根据需要从模块中导入任意数量的函数
from pizza import make_pizza

"""若使用这种语法，调用函数时就无需使用句点。
由于我们在import语句中显式地导入了函数make_pizza()，
因此调用它时只需要指定其名称"""
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

