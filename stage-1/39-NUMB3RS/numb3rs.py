import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # You’re welcome, but not required, to use re and/or sys.

    if "." not in ip: return False

    ipv4 = ip.split(".")

    if len(ipv4) < 4: return False

    for num in ipv4:
        if int(num) > 255 or int(num) < 0:
            return False

    return True

if __name__ == "__main__":
    main()