
# Hard coded constants that represent the mean of each metric in the spreadsheet
COUNTER_MEAN = 1008.96            # "CountLine"
TOTALBLANKLINECOUNT_MEAN = 172.24 # "CountLineBlank"
TOTALCOMMENTLINECOUNT_MEAN = 248  # "CountLineComment"
TOTALCODELINE_MEAN = 592.232      # "CountLineCode"
TOTALCLASSES_MEAN = 2.288         # "CountClass"
TOTALMETHODS_MEAN = 42.88         # "CountMethods"
RATIOCOMMENTTOCODE_MEAN = 0.56208 # "RatioCommentToCode"

# Param: Number userMetric 
# Param: int lineCount - CountLine
# Param: String METRIC_CODE - USE ONE OF CODES ABOVE TO TELL WHICH METRIC TO USE
# Return: Number (in percent)
# (UserMetric/DatabaseMetricMean) x 100 SCALED

def percentMatch(userMetric, METRIC_CODE, lineCount):
    scaleFactor = COUNTER_MEAN/lineCount # 1008/100 = 10 
    print(scaleFactor)
    #if METRIC_CODE == "CountLine":
    #    return (userMetric/COUNTER_MEAN) * 100
    if METRIC_CODE == "CountLineBlank":
        return (((userMetric * scaleFactor)/TOTALBLANKLINECOUNT_MEAN) * 100)
    elif METRIC_CODE == "CountLineComment":
        return (((userMetric * scaleFactor)/TOTALCOMMENTLINECOUNT_MEAN) * 100)
    elif METRIC_CODE == "CountLineCode":
        return (((userMetric * scaleFactor)/TOTALCODELINE_MEAN) * 100)
    elif METRIC_CODE == "CountClass":
        return (((userMetric * scaleFactor)/TOTALCLASSES_MEAN) * 100)
    elif METRIC_CODE == "CountMethods":
        return (((userMetric * scaleFactor)/TOTALMETHODS_MEAN) * 100)
    elif METRIC_CODE == "RatioCommentToCode":
        return (((userMetric * scaleFactor)/RATIOCOMMENTTOCODE_MEAN) * 100)

test = False
if test:
    print(percentMatch(111, "CountLine", 111))
    print(percentMatch(12, "CountLineBlank", 111))
    print(percentMatch(15, "CountLineComment", 111))
    print(percentMatch(84, "CountLineCode", 111))
    print(percentMatch(1, "CountClass", 111))
    print(percentMatch(4, "CountMethods", 111))
    print(percentMatch(0.17857142857142858, "RatioCommentToCode", 111))
    
    #CountBlankLine
    percentMatchLineBlank = percentMatch(15,"CountLineBlank", 111)
    print(percentMatchLineBlank)
    if (percentMatchLineBlank > 100):
       print("User has " + str(round(percentMatchLineBlank - 100)) + "% more blank lines than the average file.")
       
    else:
       print("User has " + str(round(100 - percentMatchLineBlank)) + "% less blank lines than the average file.",)