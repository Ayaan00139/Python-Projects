import argparse

parser=argparse.ArgumentParser(description="Meow Like A Cat"); """ making a object called parser to use argparse """
parser.add_argument("-n" ,default=1, help="number of times to meow",type=int)

args=parser.parse_args(); """ will automatically look in in sys.argv for us we dont specify"""
""" inside of this args have all the command line arguments after "-n" parsed by the parser"""


for _ in range(args.n):
    print("meow")