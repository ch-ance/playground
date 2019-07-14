f = open('made_up_sentences.txt', 'r')

content = f.read()

sentences = []

content = content.split('. ')

class Node:
    def __init__(self):
        self.value = None
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
    
model = LinkedList()

for sentence in content:
    if model.value == None:
        model.value = sentence
    current = model.next
    while current != None:
        current = current.next

print(model.value)


f.close()