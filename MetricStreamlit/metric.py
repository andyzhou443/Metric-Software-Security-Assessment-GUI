import numpy as np
import streamlit as st
import streamlit.components.v1 as components
import codecs
import base64
import pandas as pd  #pip install pandas openpyxl
import plotly.express as px
import re           #regex matching
import comparison

st.title("Metric-based Software Security Assessment Model")
file_ = open("light-mono@2x-8-1.jpg", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

st.markdown(
    f'<img src="data:image/jpg;base64,{data_url}" alt="cat jpg" style="margin-left:auto;margin-right:auto;" width="470" height="300">',
    unsafe_allow_html=True,
)

st.markdown("")
st.markdown("")
st.markdown("The goal of this research is to make the current software metrics more security-centric by identifying threshold values for the metrics based on which a file can be interpreted as a vulnerable file. This research will assist the developers in secure software development through the security assessment of their code using the values of the metrics.") 
st.markdown("")
st.markdown("To accomplish our goal, we will characterize the software metrics so that they can capture security specific properties of code. For this, we will identify the threshold limits for existing software metrics beyond which a code acts vulnerable.")
st.markdown("")
st.markdown("")

st.set_page_config(page_title = "Metric Dataset",
					page_icon = ":bar_chart:",
					layour = "wide")

df = pd.read_excel(
	io='Data.xlsx',
	engine='openpyxl',
	sheet_name='Sheet1',
	skiprows=1,
	usecols='D:CE',
	nrows=128,
)

st.dataframe(df)


st.markdown("Upload JAVA source code for code metric analysis")
st.markdown(f'<b>Upload JAVA source code for code metric analysis</b>', unsafe_allow_html=True)
file1= st.file_uploader("Choose a file...", type="java")
submit = st.button('Upload')
# st.write("Upload",submit)
if submit:
    if file1 is not None:
        filename = file1.name
        st.write("Filename",filename)
        Counter = 0
        commentSymbol = "*"
        totalBlankLineCount = 0
        totalCommentLineCount = 0
        totalClasses=0
        totalMethods=0
        Content = str(file1.read(),"utf-8")
        CoList = Content.split("\n")
        for line in CoList:
            #Check line
            if line:
                Counter+= 1
            lineWithoutWhitespace = line.strip()
            #check if blank line
            if not lineWithoutWhitespace:
                totalBlankLineCount += 1
            #check if line is comment
            elif lineWithoutWhitespace.startswith(commentSymbol):
                totalCommentLineCount += 1
            #check for class declaration
            classMatch = re.compile(r'^(?:public|private|protected) class')
            if classMatch.match(line):
                totalClasses += 1
            methodMatch = re.compile(r'^(?:public|private|protected)*[(]*[)]$')
            if methodMatch.match(line):
                totalMethods += 1
        totalCodeLine = Counter - totalBlankLineCount - totalCommentLineCount
        st.write("CountLine : ",Counter)
        st.write("CountLineBlank : ",totalBlankLineCount)
        st.write("CountLineComment : ",totalCommentLineCount)
        st.write("CountLineCode : ",totalCodeLine)
        st.write("CountClass : ",totalClasses)
        st.write("CountMethods:", totalMethods)
        st.write("RatioCommentToCode  : ",totalCommentLineCount/totalCodeLine)
        st.markdown("")
        st.markdown("")

        
        percentMatchCounter = comparison.percentMatch(Counter,"CountLine", Counter)
        if (percentMatchCounter > 100):
            st.write("User has " + str(round(percentMatchCounter - 100)) + " more lines of code than the average file.")
        else:
            st.write("User has " + str(round(100 - percentMatchCounter)) + " more lines of code than the average file.",)
        
        percentMatchLineBlank = comparison.percentMatch(totalBlankLineCount,"CountLineBlank", Counter)
        if (percentMatchLineBlank > 100):
            st.write("User has " + str(round(percentMatchLineBlank - 100)) + " more blank lines than the average file.")
        else:
            st.write("User has " + str(round(100 - percentMatchLineBlank)) + " more blank lines than the average file.",)
        
        
        st.markdown("Made with ❤️ and ☕")