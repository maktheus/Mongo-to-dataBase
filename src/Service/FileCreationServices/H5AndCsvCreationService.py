from Controllers.PayloadControllers.payloadHex import payloadHexParser
from Controllers.PayloadControllers.payloadWise import payloadWiseParser
from Controllers.PayloadControllers.payloadKs import payloadKSParser

import pandas as pd
from datetime import datetime


def DataFromTheDatabaseToH5AndCsv():
    WiseToCsv()
    HexToCsv()
    KSToCsv()
    WiseToH5()
    HexToH5()
    KSToH5()


def main():
    KSToCsv()


if __name__ == "__main__":
    main()
