sentence = input()
index_from_start = sentence.find('old')
index_from_end = sentence.rfind('old')

if index_from_end > index_from_start:
    print(index_from_end)
elif index_from_start > index_from_end:
    print(index_from_start)

