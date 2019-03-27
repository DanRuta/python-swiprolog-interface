
import os
import argparse
from pyswip import Prolog
prolog = Prolog()

def main(prologFile):

    print("Prolog file: {}".format(prologFile))

    while True:
        queryLine = input("\n> ")
        prolog.consult(prologFile)
        prologOutput = prolog.query(queryLine)

        for soln in prologOutput:
            if "X" in soln:
                print(soln["X"])


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--i", help="Input .pl file")
    args = parser.parse_args()

    prologFile = None

    if args.i is not None:
        prologFile = args.i
    else:
        files = os.listdir("./")
        for file in files:
            if file.endswith(".pl"):
                prologFile = file
                break

    main(prologFile)