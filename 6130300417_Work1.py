# -*- coding: utf-8 -*-
import os, shutil
input = open("AllScore.txt", encoding="utf-8")

try:
    os.chdir('D:')
    os.mkdir('6130300417')
except:
    shutil.rmtree('D:\\6130300417')
    os.mkdir('6130300417')

numberStudent = 0
A = 0
Bplus = 0
B = 0
Cplus = 0
C = 0 

for line in input:
    No, ID, Midterm_Score, Other_Score, Final_Score = line.split()
    sum_score = int(Midterm_Score) + int(Other_Score) + int(Final_Score)
    numberStudent += 1
    
    if sum_score >= 80:
        A+=1
    if sum_score >= 75 and sum_score <= 79:
        Bplus+=1
    if sum_score >= 70 and sum_score <= 74:
        B+=1
    if sum_score >= 60 and sum_score <= 69:
        Cplus+=1
    if sum_score < 60:
        C+=1
    
print("จำนวนนักศึกษาทั้งหมด = ", numberStudent, "คน")
print("จำนวนคนได้ A = ", A, "คน")
print("จำนวนคนได้ B+ = ", Bplus, "คน")
print("จำนวนคนได้ B = ", B, "คน")
print("จำนวนคนได้ C+ = ", Cplus, "คน")
print("จำนวนคนได้ C = ", C, "คน")

os.chdir("6130300417")
input2 = open("ReportGrade.txt", "w", encoding="utf-8")

input2 .write("จำนวนนักศึกษาทั้งหมด = " + str(numberStudent) + " คน\n")
input2 .write("จำนวนคนได้ A = " + str(A) + " คน\n")
input2 .write("จำนวนคนได้ B+ = " + str(Bplus) + " คน\n")
input2 .write("จำนวนคนได้ B = " + str(B) + " คน\n")
input2 .write("จำนวนคนได้ C+ = " + str(Cplus) + " คน\n")
input2 .write("จำนวนคนได้ C = " + str(C) + " คน\n")

input.close()




