#6511171_Wai_Yan_Paing_class10_section542
def DistanceConversion(word):
    if 'mi' or 'MI' in word:
        if int(word[:-2]) >= 0:
            return (f'{word} is equal to {int(word[:-2])*1.6}km.')
        else:
            return (f'The distance should not be negative value.' )
    elif 'km' or 'KM' in word:
        if int(word[:-2]) >= 0:
            return (f'{word} is equal to {int(word[:-2])/1.6}mi.')
        else:
            return (f'The distance should not be negative value.' )
word = input('Enter a distance (in km or mi): ')
print(DistanceConversion(word))