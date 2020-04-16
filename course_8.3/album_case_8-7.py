# 编写一个名为make_album()的函数，接受歌手名字和专辑，返回包含两项信息的字典
def make_album(singer_name, album, number=''):
    singer = {singer_name: album}

    if number:
       singer['number'] = number

    return singer


singer_0 = make_album('liuhuan', 'dahexiangdongliu')
print(singer_0)
singer_1 = make_album('zhoujielun', 'yehuimei', number=12)
print(singer_1)
singer_2 = make_album('zhangjie', 'boluomi', number=10)
print(singer_2)