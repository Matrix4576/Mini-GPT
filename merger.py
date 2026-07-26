import os
def count_files(directory):
    count = 0
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_file():
                count += 1
    return count
count1 = count_files("Projects//Mini-GPT//sample-texts//b1")
count2 = count_files("Projects//Mini-GPT//sample-texts//b2")
file1 = open('Projects//Mini-GPT//sample-texts//mergedB1.txt', 'w')
file2 = open('Projects//Mini-GPT//sample-texts//mergedB2.txt', 'w')
for i in range(1, count1 + 1):
    file = open(f"Projects//Mini-GPT//sample-texts//b1//pg{i}.txt", 'r')
    l = file.readlines()
    if len(l) == 0:
        continue
    else:
        for sentences in l:
            for words in sentences.split(" "):
                s = ""
                if words.isalnum() == False and words.isspace() == False:
                    continue
                else:
                    s += words + " "
                file1.write(s)
                print(s, "appended b1")
        file.close()
file1.close()
for i in range(1, count2 + 1):
    file = open(f"Projects//Mini-GPT//sample-texts//b2//pg{i}.txt", 'r')
    l = file.readlines()
    if len(l) == 0:
        continue
    else:
        for sentences in l:
            for words in sentences.split(" "):
                s = ""
                if words.isalnum() == False and words.isspace() == False:
                    continue
                else:
                    s += words + " "
                file2.write(s)
                print(s, "appended b2")
    file.close()
file2.close()
