# <About>
#____________________________________________________________________________________________________________________________________________________________
# Copyright © 2018 SANSA. All rights reserved.
# 
# DESCRIPTION:    
# 	This script contains functions that return data regarding the status of a systems HDDs.
#
# NOTES:
# 	-Add notes here- 
# 
# REQUIREMENTS
#	-See import list below
#
# VERSION HISTORY
#	2017/06/08 17h02	:	Andre Odendaal 	: 	Created to read values from Windows PC.
#    
# TO DO:
# 	-Add functions for Linux PCs
#   -Add functions for Multiple Drives on Windows and Linux
# 
#____________________________________________________________________________________________________________________________________________________________
# </About>

from os import path
from shutil import disk_usage

#____________________________________________________________________________________________________________________________________________________________
def WindowsDiskUsePercent():
    total_bytes, used_bytes, free_bytes = disk_usage(path.realpath('C:\\'))
    myDiscPercentage = int(free_bytes/total_bytes*100)
    return(myDiscPercentage)

#____________________________________________________________________________________________________________________________________________________________
def WindowsDiskUsePrint():
    total_bytes, used_bytes, free_bytes = disk_usage(path.realpath('C:\\'))
    myDiscPercentage = int(free_bytes/total_bytes*100)
    if myDiscPercentage <= 70:
        return("0-70% Good")
    elif 70 < myDiscPercentage < 80:
        return("70-80% Low")
    elif 80 < myDiscPercentage < 90:
        return("80-90% Very Low")
    elif 90 < myDiscPercentage:
        return("90-100% Full")

#____________________________________________________________________________________________________________________________________________________________
def WindowsDiskUseBits():
    total_bytes, used_bytes, free_bytes = disk_usage(path.realpath('C:\\'))
    myDiscPercentage = int(free_bytes/total_bytes*100)

    if myDiscPercentage <= 70:
        return('00')    
    elif 70 < myDiscPercentage < 80:
        return('01') 
    elif 80 < myDiscPercentage < 90:
        return('10')
    elif 90 < myDiscPercentage:
        return('11')


def main():
    print(WindowsDiskUsePercent())
    print(WindowsDiskUsePrint())
    print(WindowsDiskUseBits())

if __name__ == "__main__":
	main()