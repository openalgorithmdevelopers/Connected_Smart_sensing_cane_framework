"""
Created on Wed Feb  5 22:31:27 2022

@author: bhupendra.singh
"""
import constants

def findNearestClass(detectedHt):
    NO_DistanceFound = abs(detectedHt - constants.HEIGHT_NO)
    SM_DistanceFound = abs(detectedHt - constants.HEIGHT_SM)
    MD_DistanceFound = abs(detectedHt - constants.HEIGHT_MD)
    LG_DistanceFound = abs(detectedHt - constants.HEIGHT_LG)

    #print("NO = " + str(NO_DistanceFound))
    #print("SM = " + str(SM_DistanceFound))
    #print("MD = " + str(MD_DistanceFound))
    #print("LG = " + str(LG_DistanceFound))
    ### finding the class according to lesser distance logic is
    # simpler but not optimal for the sake of readability
    if(NO_DistanceFound < SM_DistanceFound):
        if(NO_DistanceFound < MD_DistanceFound):
            if(NO_DistanceFound < LG_DistanceFound):
                return constants.CLASS_NO
    if(SM_DistanceFound < NO_DistanceFound):
        if(SM_DistanceFound < MD_DistanceFound):
            if(SM_DistanceFound < LG_DistanceFound):
                return constants.CLASS_SM
    if(MD_DistanceFound < NO_DistanceFound):
        if(MD_DistanceFound < SM_DistanceFound):
            if(MD_DistanceFound < LG_DistanceFound):
                return constants.CLASS_MD
    return constants.CLASS_LG