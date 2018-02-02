#########################################
# Author - Shivam Kapoor (mailme@shivamkapoor.me)
#
# A small python script written for personal convineance to calculate
# CGPA by scraping academic history webpage.
#
# Github : https://github.com/ConanKapoor/VIT-CGPA-Scrapy-Calculator
#########################################

# Importing Essesnsials.
from bs4 import BeautifulSoup
from pyfiglet import Figlet
import urllib.request
import xlsxwriter
import getpass
import time
import math
import sys
import os

# Creating Output folder.
if (os.path.exists("Academic_Transcript")):
    delete = str('rm -r Academic_Transcript')
    os.system(delete)
    os.makedirs("Academic_Transcript")
else:
    os.makedirs("Academic_Transcript")

def display(quote):
    # Printing unecessary information for 'wanna be cool' people.
    # Comment all for minimal script.
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = Figlet(font='slant')
    print("\n")
    print (banner.renderText('CGPA CALC'))
    print ("\t  >>>>>>> VIT CGPA Calculator <<<<<<<")
    print ("\t  >>>>>>  Author : ConanKapoor <<<<<<")
    print ("\t  >>>>>> API by : sridharswain <<<<<<\n")

    # Printing unecessary information for 'wanna be cool' people #2
    if (quote == 1):
        print (">>> Now I have to do image processing shit to fill  <<<\n>>> captcha so your sorry ass don't have to log in. <<<\n>>>\t\t\t\t    - Sridhar Swain <<<")
    if (quote == 2):
        print (">>> I did this for showing off and because i'd rather do <<<\n>>> this than studying. #PEACE #YOLO \t\t\t <<<\n>>>\t\t\t\t         - Shivam Kapoor <<<")

    # Printing unecessary information for 'wanna be cool' people #3
    print ("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print ("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n")

def gpaCalc(credits,grades,CSEcredits,CSEgrades):
    totalCredits = sum(credits)
    totalCSECredits = sum(CSEcredits)
    totalPoints, totalCSEPoints = 0,0
    for subject in range(len(credits)):
        totalPoints = totalPoints + (credits[subject]*grades[subject])
    for subject in range(len(CSEcredits)):
        totalCSEPoints = totalCSEPoints + (CSEcredits[subject]*CSEgrades[subject])
    GPA = round((math.floor((totalPoints/totalCredits)*1000))/1000,2)
    MajorGPA = round((math.floor((totalCSEPoints/totalCSECredits)*1000))/1000,2)
    time.sleep(2)
    return totalCredits, GPA, totalCSECredits, MajorGPA

# try:
# Making a log file.
logs = open('logs.txt','w')
logs.write("The following errors were encountered during scraping ->\n\n")

flag = 1
while(flag):
    display(1)
    Username = input(">>> Please feed your Registration No. : ")
    Password = getpass.getpass(">>> Please feed your Password(hidden) : ")
    url ="https://vitgrades.herokuapp.com/grades?userName=" + Username + "&password=" + Password

    # Printing unecessary information for 'wanna be cool' people #4
    print ("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print ("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n")

    # Printing unecessary information for 'wanna be cool' people #5
    print(">>> Request sent to server.")
    time.sleep(1)
    print(">>> Done!!!\n")
    print(">>> Cracking Captcha.")
    time.sleep(1)
    print(">>> Done!!!\n")
    print(">>> Receiving data from server. This will take time.")

    # Collecting html content.
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)

    # Using BeautifulSoup to parse Students data.
    soup = BeautifulSoup(response.read(),"lxml")

    if "Bad Credentials" in soup.text:
        print("!>!>!> Credentials provided are wrong. Try the fuck again dyslexic turd.")
        print("!>!>!> Wasted 1 API call for fucks sake - Sridhar Swain")
        time.sleep(3)
        display(1)

    else:
        print(">>> Data Received. Parsing!!!\n")
        time.sleep(3)
        infoTable = soup.find("table",{"height": "58"})
        infoStudent = infoTable.find_all("td",{"bgcolor":"#EDEADE"})

        # Scraping Student data
        Regno = infoStudent[0].text
        Name = infoStudent[1].text
        Branch = (infoStudent[2].text).replace('B.Tech. ','')
        School = infoStudent[3].text

        # Showing Student details
        display(2)
        time.sleep(1)
        print(">>> Student Details - ")
        print("\t>>> Reg. No. : %s" %(Regno))
        print("\t>>> Name     : %s" %(Name))
        print("\t>>> Branch   : %s" %(Branch))
        print("\t>>> School   : %s" %(School))

        # Using BeautifulSoup to parse Grades data.
        gradesTable = soup.find("table",{"id":"hist"})
        infoGrades = gradesTable.find_all("tr",{"bgcolor":"#EDEADE"})

        # Initiating XLSX file
        filepath = 'Academic_Transcript/Grades-'+ Regno +'.xlsx'
        workbook = xlsxwriter.Workbook(filepath)
        worksheet = workbook.add_worksheet()

        bold = workbook.add_format({'bold': True})

        worksheet.write('A1', 'S.No.', bold)
        worksheet.write('B1', 'Course Code', bold)
        worksheet.write('C1', 'Course Title', bold)
        worksheet.write('D1', 'Course Type', bold)
        worksheet.write('E1', 'Credits', bold)
        worksheet.write('F1', 'Grade', bold)
        worksheet.write('G1', 'Exam Held', bold)
        worksheet.write('H1', 'Result Date', bold)

        rows,extra = 1,0
        credits, grades, CSEcredits, CSEgrades = [],[],[],[]
        useless = ['S','A','B','C','D','E','F','N']
        gradeKey = {'S':10,'A':9,'B':8,'C':7,'D':6,'E':5,'F':0,'N':0}
        for subject in range(len(infoGrades)):
            gradeRow = infoGrades[subject]
            gradeData = gradeRow.find_all("td")

            # Putting data in Worksheet.
            if((gradeData[5].text) == 'P'):
                extra = extra + int(gradeData[4].text)

            if((gradeData[5].text) in useless):
                if ('CSE' in gradeData[1].text):
                    CSEcredits.append(int(gradeData[4].text))
                    CSEgrades.append(gradeKey[gradeData[5].text])
                credits.append(int(gradeData[4].text))
                grades.append(gradeKey[gradeData[5].text])
                # Writing to worksheet
                worksheet.write(rows, 0, rows)
                for i in range(1,8):
                    worksheet.write(rows, i, gradeData[i].text)
                rows = rows +1
            else:
                continue;
        flag = 0
        workbook.close()
        time.sleep(1)
        print("\n>>> Academic Transcript stored in folder as xlsx file.")

        temp = 1
        while(temp):
            time.sleep(1)
            choice = input("\n>>> Do you want to add more courses and grades for speculation? (Y or N) : ")
            if (choice == 'Y' or choice == 'y'):
                display(2)
                Addition = int(input("\n>>>How many courses you want to input? : "))
                print(">>> \nPlease enter data in following form - (credits grade subject)")
                print(">>> For example - (4 S CSE)\n")
                print(">>> Start - ")

                for new in range(Addition):
                    tempCredits,tempGrade,Subject = map(str,sys.stdin.readline().split())
                    if (Subject == 'CSE'):
                        CSEcredits.append(int(tempCredits))
                        CSEgrades.append(gradeKey[tempGrade])

                    credits.append(int(tempCredits))
                    grades.append(gradeKey[tempGrade])
                    totalCredits, GPA, totalCSECredits, MajorGPA = gpaCalc(credits,grades,CSEcredits,CSEgrades)
                    display(2)
                    print("\n\t>>> Total (Speculated) Credits Completed - %s" %(totalCredits))
                    print("\t>>> Cumulative (Speculated) GPA - %s\n" %(GPA))
                    print("\t>>> Total (Speculated) CSE Credits Completed - %s" %(totalCSECredits + extra))
                    print("\t>>> Major (Speculated) GPA - %s\n" %(MajorGPA))
                    time.sleep(5)
                    temp = 0

            elif (choice == 'N' or choice == 'n'):
                totalCredits, GPA, totalCSECredits, MajorGPA = gpaCalc(credits,grades,CSEcredits,CSEgrades)
                print("\n\t>>> Total Credits Completed - %s" %(totalCredits))
                print("\t>>> Cumulative GPA - %s\n" %(GPA))
                print("\t>>> Total CSE Credits Completed - %s" %(totalCSECredits))
                print("\t>>> Major GPA - %s\n" %(MajorGPA))
                time.sleep(5)
                temp = 0

            else:
                print("!>!>!> Please select a valid input (Y or N). Try Again - ")
                time.sleep(3)
                display(2)
                time.sleep(1)
                print(">>> Student Details - ")
                print("\t>>> Reg. No. : %s" %(Regno))
                print("\t>>> Name     : %s" %(Name))
                print("\t>>> Branch   : %s" %(Branch))
                print("\t>>> School   : %s" %(School))

logs.close()

# except Exception:
#     print("    >!>!> Exceptioncaught - Most Probably Network error.")
#     print("          Try Again\n")
#     logs.write(" Outer Exception error.\n\n")
#     workbook.close()
#     logs.close()
#     pass
#
# except KeyboardInterrupt:
#     print("\n\n>>> Interrupt received! Exiting cleanly...")
#     logs.write("End of logs - Abruptly Ended")
#     logs.close()
#     sys.exit()
############################### END OF SCRIPT :) ##############################
