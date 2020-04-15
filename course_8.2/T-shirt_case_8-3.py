# 修改函数make_shirt()，使其在默认情况下制作意见印有"I love python"字样的大号T恤
def make_shirt(word='I love python', size='large'):
    print("\nThis shirt size is " + size + ".")
    print("Words on T-shirt are: " + word)

# 一件有默认字样的大号T恤
make_shirt()
# 一件因为有默认字样的中号T恤
make_shirt(size='medium')
# 一件有其他字样的t恤
make_shirt('I love China!')
make_shirt('I love China!', 'small')
