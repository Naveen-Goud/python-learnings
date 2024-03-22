#open the file
text_file = open('/home/naveen.sunkari/Desktop/python-learnings/python-learnings/learnings/example.txt','r')

line_list = text_file.readlines()

for line in line_list:
    print(line)

#writing into the file
text_file = open('/home/naveen.sunkari/Desktop/python-learnings/python-learnings/learnings/example2.txt','w')
word_list= []
for i in range (1, 5):
    print("Please enter data: ")
    line = input()
    word_list.append(line)


text_file.writelines(word_list)

text_file.close()



text_file.close()