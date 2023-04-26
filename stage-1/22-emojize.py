emojis = {
    ":thumbs_up:" : "👍",
    ":1st_place_medal:" : "🥇",
    ":money_bag:" : "💰",
    ":smile_cat:" : "😸"
}

text = input("Input: ").split(" ")

for word in text:
    if word in emojis:
        print(emojis[word], end=" ")
    else:
        print(word, end=" ")
        
print("")