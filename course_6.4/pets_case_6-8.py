# 创建多个字典，对于每个字典都用一个宠物的名称来给它命名
huangshang = {
    'type': 'cat',
    'master_name': 'maomaojie',
    }

ahuang = {
    'type': 'dog',
    'master_name': 'kaige',
    }

wujiu = {
    'type': 'cat',
    'master_name': 'chuangjiang',
    }

qiuqiu = {
    'type': 'cat',
    'master_name': 'yunjiao',
    }

pets = [huangshang, ahuang, wujiu, qiuqiu]

for pet in pets:
    print(pet)