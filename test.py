#!/usr/bin/python

import sys
import time
import math
from hp8350b import *

def main():
	gen = HP8350B('PROLOGIX::/dev/ttyUSB0::GPIB::19')
#	print gen.cmd("++spoll;");
#	print gen.cmd("++loc;");
	gen.frq_start("3GZ");
	print gen.cmd("FA 1GZ FB 2GZ");

if __name__ == "__main__":
    main()
