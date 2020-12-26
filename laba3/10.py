count=0
anagram=['топор', "гор", "рог", "ропот", "учись", "молись", "работай", "женись, "воспитай", "умри"]
for i in anagram:
    for j in anagram:
        if i==j[::-1]:
            print("Anagram: ",i)
