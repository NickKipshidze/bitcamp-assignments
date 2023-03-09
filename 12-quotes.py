quote = input("What is the quote?") 
author = input("Who said it?")
print(f"{author} says, \"{quote}\"")

# BONUS:

quotes = {
  "elon musk" : "AI is the most dangerous thing ever created.",
  "bill gates" : "I use windows every day. I have at least 4 windows in my room.",
  "steve jobs" : "My favorite kind of apple is mac book.",
  "შოტა რუსთაველი" : "ლეკვი ლომისა სწორია, ძუ იყოს, თუმდა ხვადია.",
  "oto zakalashvili" : "სწავლა და ბრძოლა!", 
}

try:
    print(f"{author} says, \"{quotes[author]}\"")
except KeyError:
    pass
