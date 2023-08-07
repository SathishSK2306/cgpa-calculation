import streamlit as st

APlus = 9
A = 8
BPlus = 7
B = 6
C = 5
RA = 0
gradeList = ['O', 'A+', 'A', 'B+', 'B', 'C', 'RA']

def overall(v1,v2,v3,v4,v5,v6):
    return (v1+v2+v3+v4+v5+v6)/14


def gradeValue(grade):
    if grade == 'O':
        return 10
    if grade == 'A+':
        return 9
    if grade == 'A':
        return 8
    if grade == 'B+':
        return 7
    if grade == 'B':
        return 6
    if grade == 'C':
        return 5
    if grade == 'RA':
        return 0


st.set_page_config(layout='wide')

lay1, lay2 = st.columns([1, 1])

with lay1:
    s1 = st.selectbox('Whats your Grade Sub1', gradeList)
    s2 = st.selectbox('Whats your Grade Sub2', gradeList)
    s3 = st.selectbox('Whats your Grade Sub3', gradeList)
    s4 = st.selectbox('Whats your Grade Sub4', gradeList)
    s5 = st.selectbox('Whats your Grade Sub5', gradeList)
    s6 = st.selectbox('Whats your Grade Sub6', gradeList)

with lay2:
    col0, col1, col2 = st.columns([0.5, 2, 1])
    with col0:
        st.write("")
    with col1:
        st.write("Transform and Partial Differential Equation")
        st.write("Digital Signal Processing")
        st.write("Java Script")
        st.write("Carrer English")
        st.write("Machine Learning")
        st.write("PHP full stack")
        st.write(" # result")


    with col2:
        st.write(2 * gradeValue(s1))
        st.write(3 * gradeValue(s2))
        st.write(2 * gradeValue(s3))
        st.write(2 * gradeValue(s4))
        st.write(3 * gradeValue(s5))
        st.write(2 * gradeValue(s6))
        sub1 = 2 * gradeValue(s1)
        sub2 = 3 * gradeValue(s2)
        sub3 = 2 * gradeValue(s3)
        sub4 = 2 * gradeValue(s4)
        sub5 = 3 * gradeValue(s5)
        sub6 = 2 * gradeValue(s6)
        total = (sub1 + sub2 + sub3 + sub4 + sub5 + sub6) / 14
        rounded_total=round(total,2)
        st.write(f"# {rounded_total}")
        


def cal():
    sub1 = 2 * gradeValue(s1)
    sub2 = 3 * gradeValue(s2)
    sub3 = 2 * gradeValue(s3)
    sub4 = 2 * gradeValue(s4)
    sub5 = 3 * gradeValue(s5)
    sub6 = 2 * gradeValue(s6)
    total = (sub1 + sub2 + sub3 + sub4 + sub5 + sub6) / 14
    print(total)


if __name__ == '__main__':
    cal()
