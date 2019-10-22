
string = 'aabbccccddd'

def count_segment(string):
    list = []
    segment = string[0]
    for letter in string[1:]:
        if letter in segment:
            segment += letter
            continue
        list.append(segment)
        segment = letter
    list.append(segment)
    for i in list:
        print(i, end=' ')
    print(f'\nNumber of segments is: {len(list)}')
    

count_segment('aaddccrrrreeeeeeaffffww')