import numpy as np
import streamlit as st
import streamlit.components.v1 as components
import codecs
import base64
import re           #regex matching

st.title("Metric Software Security Assessment")
file_ = open("pic.jpg", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

st.markdown(
    f'<img src="data:image/jpg;base64,{data_url}" alt="cat jpg" style="margin-left:auto;margin-right:auto;" width="800" height="300">',
    unsafe_allow_html=True,
)


st.markdown("Upload JAVA source code to analyze")
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
        st.write("RatioCommentToCode  : ",totalCommentLineCount/totalCodeLine)