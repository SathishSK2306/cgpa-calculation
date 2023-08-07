import streamlit as st

APlus = 9
A = 8
BPlus = 7
B = 6
C = 5
RA = 0
gradeList = ['O', 'A+', 'A', 'B+', 'B', 'C', 'RA']

def overall(v1,v2,v3,v4,v5,v6,v7,v8,v9):
    return (v1+v2+v3+v4+v5+v6+v7+v8+v9)/22


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
    s1 = st.selectbox('Edge Computing', gradeList)
    s2 = st.selectbox('Java Script', gradeList)
    s3 = st.selectbox('Wireless Communication', gradeList)
    s4 = st.selectbox('Machine Learning', gradeList)
    s5 = st.selectbox('Data Communication', gradeList)
    s6 = st.selectbox('VLSI', gradeList)
    s7 = st.selectbox('Machine Learning Laboratory', gradeList)
    s8 = st.selectbox('Networks Laboratory', gradeList )
    s9 = st.selectbox('Mini Project', gradeList )


with lay2:
    col0, col1, col2 = st.columns([0.5, 2, 1])
    with col0:
        st.write("")
    with col1:
        st.write("Edge Computing")
        st.write("Java Script")
        st.write("Wireless Communication")
        st.write("Machine Learning")
        st.write("Data Communication")
        st.write("VLSI")
        st.write("Machine Learning Laboratory")
        st.write("Networks Laboratory")
        st.write("Mini Project")
        st.write(" # result")


    with col2:
        st.write(3 * gradeValue(s1))
        st.write(3 * gradeValue(s2))
        st.write(3 * gradeValue(s3))
        st.write(3 * gradeValue(s4))
        st.write(3 * gradeValue(s5))
        st.write(4 * gradeValue(s6))
        st.write(1 * gradeValue(s7))
        st.write(1 * gradeValue(s8))
        st.write(1 * gradeValue(s9))
        sub1 = 3 * gradeValue(s1)
        sub2 = 3 * gradeValue(s2)
        sub3 = 3 * gradeValue(s3)
        sub4 = 3 * gradeValue(s4)
        sub5 = 3 * gradeValue(s5)
        sub6 = 4 * gradeValue(s6)
        sub7 = 1 * gradeValue(s7)
        sub8 = 1 * gradeValue(s8)
        sub9 = 1 * gradeValue(s9)
        total = (sub1 + sub2 + sub3 + sub4 + sub5 + sub6 + sub7 + sub8 + sub9) / 22
        rounded_total=round(total,2)
        st.write(f"# {rounded_total}")
        


def cal():
    sub1 = 3 * gradeValue(s1)
    sub2 = 3 * gradeValue(s2)
    sub3 = 3 * gradeValue(s3)
    sub4 = 3 * gradeValue(s4)
    sub5 = 3 * gradeValue(s5)
    sub6 = 4 * gradeValue(s6)
    sub7 = 1 * gradeValue(s7)
    sub8 = 1 * gradeValue(s8)
    sub9 = 1 * gradeValue(s9)
    total = (sub1 + sub2 + sub3 + sub4 + sub5 + sub6 + sub7 + sub8 + sub9) / 22
    print(total)


if __name__ == '__main__':
    cal()
