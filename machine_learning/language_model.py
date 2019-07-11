f = open('made_up_sentences.txt', 'r')

content = f.read()

sentences = []

content = content.split('.')

for sentence in content:
    


print(content)

f.close()