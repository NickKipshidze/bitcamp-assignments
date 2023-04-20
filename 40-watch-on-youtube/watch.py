import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    regex_src = re.search('src="http[s]*://www.youtube.com/[^"]*', s)

    if regex_src == None:
        return None
    
    src = s[regex_src.start():regex_src.end()]
    youtube_id = src.split("/")[-1]

    return "https://youtu.be/"+youtube_id

if __name__ == "__main__":
    main()