#!/usr/bin/env python3

from datetime import datetime

def main():
    now = datetime.now()
    print(f"Seconds since January 1, 1970: {now.timestamp():,.4f} or {now.timestamp():.2e} in scientific notation")
    print(now.strftime("%b %d %Y"))

if __name__ == "__main__":
    main()

