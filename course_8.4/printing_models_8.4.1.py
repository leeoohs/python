# 在函数中修改列表
"""将列表传递给函数后，函数就可对其进行修改。
在函数中对这个列表所做的任何修改都是永久性的，这让你能够高效地处理大量的数据。"""

# 首先创建一个列表，其中包含一些要打印的设计
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# 模拟打印每个设计，直到没有未打印的设计为止
# 打印每个设计后，都将其移动到列表completed_models中
while unprinted_designs:
    current_design = unprinted_designs.pop()

    # 模拟根据设计制作3D打印模型的过程
    print("Printing model: " + current_design)
    completed_models.append(current_design)


# 显示打印好的所有模型
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)


"""为重新组织这些代码，我们可编写两个函数，每个都做一件具体的工作。
第一个函数将负责处理打印设计的工作
第二个函数将概述打印了哪些设计"""
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

print_models(unprinted_designs, completed_models)
show_comleted_models(completed_models)
