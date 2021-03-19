ENGLISH = ['hello', 'friend', 'hey', 'awful', 'wow','reward', 'song', 'money',
           'board', 'cocktail', 'bathroom', 'friends', 'cheat', 'flag','boy',
           'girl', 'my', 'take', 'sink', 'telescope', 'clean', 'you']
PIRATE = ['ahoy', 'matey', 'avast', 'bilge-sucking', 'blimey', 'booty', 'chanty',
          'dubloon', 'plank', 'grogg', 'head', 'hearties', 'hornswaggle',
          'jack', 'lad', 'lass', 'me', 'plunder', 'scuttle', 'spyglass', 'swob','ye']

res = {}
for key in ENGLISH:
    for value in PIRATE:
        res[key] = value
        PIRATE.remove(value)
        break

def toPirate(sentence):
    pirateDic = res
    pirateSentence=''
    wordList=sentence.split()
    for i in wordList:
        if i in pirateDic:
            i=pirateDic[i]
        pirateSentence=pirateSentence+' '+i
    return pirateSentence

while(True):
    print("Arrrr welcome to my pirate dictionary!")
    print("Type some stuff then hit enter with yer sword.")
    print("Or just say 'arr' to be done, ya scalliwag.",)
    sentence=input()
    if(sentence != 'arr'):
        print(toPirate(sentence),"\n")
    else:
        break;


