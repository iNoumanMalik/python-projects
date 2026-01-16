def find_word_freq(data):
    words = data.split()
    # print(words)
    count = 0
    frequencyDict = {}
    for x in words:
        x = x.strip(".")
        for y in words:
            y = y.strip(".")
            if x == y:
                count += 1
                
                
        frequencyDict[x] = count
        count = 0
        
    return frequencyDict


with open("demotext.txt","w") as f:
    f.write("I am Nouman. I am from Islamabad. Islamabad is a beautiful city.")
    
with open("data/demotext.txt") as f: #rt is default that's why we don't usually write
    data = f.read()
    # print(data)

print(find_word_freq(data))

