# name, class, subj_marks[100,100,100], percentage, grade
#input- name, class, subj_marks
#output- result- report card
name: str =""
clas: str =""
subj_marks: float = []
percentage: float =0.0
grade: str = ""
results= []
report= []
count:int =2
while (count):
    results=[]
    name= input("Enter your name:")
    clas=input("Enter your class:")
    count2:int=0
    gained_marks:float =0.0
    while(count2<3):
        m= input(f"Enter {count2+1} subj marks:")
        m= int(m)
        gained_marks= m+gained_marks
        subj_marks.append(m)
        count2=count2+1
    percentage= (gained_marks/300)*100
    results.append(name)
    results.append(clas)
    results.append(subj_marks)
    results.append(percentage)
    count=count-1
    if gained_marks >= 90:
        grade = "A+"
        results.append(grade)
    elif gained_marks >=80:
        grade= "A"
        results.append(grade)
    elif gained_marks >=70:
        grade= "B"
        results.append(grade)
    elif gained_marks >=60:
        grade= "C"
        results.append(grade)
    elif gained_marks >=50:
        grade= "D"
        results.append(grade)
    else:
        grade= "F"
        results.append(grade)
    report.append(results)
print(f"Name {report[0][0]}, Class {report[0][1]}, Percentage {report[0][3]}, Grade {report[0][4]}")
print(f"Name {report[1][0]}, Class {report[1][1]}, Percentage {report[1][3]}, Grade {report[1][4]}")

