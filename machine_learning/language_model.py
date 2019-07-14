f = open('made_up_sentences.txt', 'r')

content = f.read()

sentences = []

content = content.split('. ')

class LinkedList:
    def __init__(self):
        self.value = None
        self.next = None
    

for sentence in content:
    print(sentence)


f.close()