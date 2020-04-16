def make_album(singer_name, album, number=''):
    singer = {singer_name: album}
    if number:
       singer['number'] = number
    return singer

while True:
    print("Could you tell us something about singers?")
    print("\nenter 'q' to close this program.")

    name = input("Singer name:")
    if name == 'q':
        break

    song = input("Singer songs:")
    if song == 'q':
        break

    shuliaing = input("Songs number:")
    if shuliaing == 'q':
        break

    zhuanji = make_album(name, song, shuliaing)
    print(zhuanji)

