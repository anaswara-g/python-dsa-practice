text=input("enter a letter:")
count=0
vowels="aeiou"
for letters in text:
    if letters in vowels:
        count+=1
if count>0:
    print("vowel",count)
else:
       print("not vowel")