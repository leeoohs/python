# 编写一个名为make_shirt()的函数，接受一个尺码以及要印在T恤上的字样
def make_shirt(size, word):
    print("This shirt size is " + str(size) + ".")
    print("\nWords on T-shirt are: " + word)

make_shirt(28,'Hello world!')
make_shirt(size=28, word='Hello world!')