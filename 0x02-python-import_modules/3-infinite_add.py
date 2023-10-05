#!/usr/bin/python3
import sys

if __name__ == "__main__":
    def main():
        list_arg = sys.argv
        sum = 0
        for count in range(1, len(list_arg)):
            sum += int(list_arg[count])
        print("{}".format(sum))
