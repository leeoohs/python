# 将5个简单食品存储在一个元组中
buffets = ('egg', 'corn', 'carrot', 'beef', 'ice cream')

# 使用一个for循环将该餐馆提供的五种食品都打印出来
for buffet in buffets:
    print(buffet)

# 尝试修改其中一个元素，核实python会拒绝你这样做
# buffets[0] = "eggs"

# 执行结果如下：
'''File "/Users/huangdaxianer./Downloads/subline/project/course_4.5/buffet_case_4-13.py", line 9, in <module>
    buffets[0] = "eggs"
corn
TypeError: 'tuple' object does not support item assignment'''

# 给元组变量赋值，并使用for循环将新元组的每个元素都打印出来
buffets = ('milk', 'corn', 'apple', 'beef', 'ice cream')
for buffet in buffets:
    print(buffet)