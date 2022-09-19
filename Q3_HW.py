#list1 = []
#for i in range (1 , 6 ):
#    ele = float(input("Enter elements : "))
#    list1. append(ele)
#print (" Largest element is : " , max(list1))
#print (" Smallest element is : " , min(list1))

words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]
past_tense = []
for ch in words:
    if ch[-1] == "e":
        ch = ch + "d"
        past_tense.append(ch)
    else:
        ch = ch + "ed"
        past_tense.append(ch)
print(past_tense)




