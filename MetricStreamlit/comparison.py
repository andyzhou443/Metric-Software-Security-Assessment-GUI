
# Hard coded constants that represent the mean of each metric in the spreadsheet
COUNTER_MEAN = 1008.96            # "CountLine"
TOTALBLANKLINECOUNT_MEAN = 172.24 # "CountLineBlank"
TOTALCOMMENTLINECOUNT_MEAN = 248  # "CountLineComment"
TOTALCODELINE_MEAN = 592.232      # "CountLineCode"
TOTALCLASSES_MEAN = 2.288         # "CountClass"
TOTALMETHODS_MEAN = 42.88         # "CountMethods"
RATIOCOMMENTTOCODE_MEAN = 0.56208 # "RatioCommentToCode"

# Param: Number userMetric, String METRIC_CODE
# (UserMetric/DatabaseMetricMean) x 100
# USE ONE OF CODES ABOVE TO TELL WHICH METRIC TO USE
def percentMatch(userMetric, METRIC_CODE) {
    if METRIC_CODE == "CountLine":
    
    elif METRIC_CODE == "CountLineBlank":
    
    elif METRIC_CODE == "CountLineComment":
    
    elif METRIC_CODE == "CountLineCode":
    
    elif METRIC_CODE == "CountClass":
    
    elif METRIC_CODE == "CountMethods":
    
    elif METRIC_CODE == "RatioCommentToCode":
}