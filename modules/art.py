from pyfiglet import figlet_format

def art(msg):
    ascii_art = figlet_format(msg)
    print(ascii_art)

art(input())