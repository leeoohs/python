# 禁止函数修改列表，可向函数传递列表的副本而不是原件
def print_models(unprinted_designs, completed_models):

    while unprinted_designs:
        current_design = unprinted_designs.pop()

        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_comleted_models(complete_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# 切片表示法[:]创建表的副本：function_name(list_name[:])
print_models(unprinted_designs[:], completed_models)
show_comleted_models(completed_models)