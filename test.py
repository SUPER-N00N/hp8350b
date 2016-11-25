#!/usr/bin/python

import sys
import time
import math
from hp8350b import *

def main():
	gen = HP8350B('PROLOGIX::/dev/ttyUSB0::GPIB::19')
#	print gen.cmd("++spoll;");
#	print gen.cmd("++loc;");
	gen.frq_stop("7.2371GZ");
	gen.frq_start("3.1415GZ");
	gen.setSweepTime("53");
	gen.dBm("19");
#	gen.cmd("END");
#	gen.cmd("ST42MS");
#	gen.cmd("PL13DM");

if __name__ == "__main__":
    main()
