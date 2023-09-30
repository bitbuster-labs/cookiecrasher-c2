import sys
import select
from machine import UART, soft_reset
from utime import sleep_ms

line0 = UART(0, 115200)
line0.init(115200, bits=8, parity=None, stop=1)

def read_lines(prompt):
    # for each line
    while True:
        write(prompt.encode())
        buffer = b""

        # for each character
        while True:
            char = read()
            # TODO: handle all tty control characters
            # or not, i'm too lazy

            if char == b"\r":
                # newline
                write(b"\r\n")
                yield buffer + b"\n"
                break
            elif char == b"\n":
                # newline handling *****, please PLEASE don't ask
                pass
            elif char == b"\x7f" or char == b"\x08":
                # backspace
                buffer = buffer[:-1]
                write(b"\x08 \x08")
            elif char == b"\x1b":
                # escape sequences
                # I don't want to implement a cursor..... so let's just ignore the control character and print the rest to the screen
                pass
            elif char == b"\x03":
                # CTRL+C
                write(b"^C\r\n")
                break
            elif char == b"\x04":
                # CTRL+D -> reboot
                soft_reset()
            else:
                buffer += char
                write(char)

def read():
    while True:
        if select.select([sys.stdin],[],[],0)[0]:
            return sys.stdin.buffer.read(1)
        if line0.any():
            return line0.read(1)

def write_line(string):
    for i in string.encode() + b"\r\n":
        write(bytes([i]))
        sleep_ms(10)
    sleep_ms(500)

def write(char):
    sys.stdout.buffer.write(char)
    line0.write(char)
