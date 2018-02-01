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
import requests
import time
import sys
import os

# Making a log file.
logs = open('logs.txt','w')
logs.write("The following errors were encountered during scraping ->\n\n")

# Creating Output folder.
if (os.path.exists("Academic_Transcript")):
    delete = str('rm -r Academic_Transcript')
    os.system(delete)
    os.makedirs("Academic_Transcript")
else:
    os.makedirs("Academic_Transcript")

# Printing unecessary information for 'wanna be cool' people.
# Comment all for minimal script.
os.system('cls' if os.name == 'nt' else 'clear')
banner = Figlet(font='slant')
print("\n")
print (banner.renderText('CGPA CALC'))
print ("\t  >>>>>>> VIT CGPA Calculator <<<<<<<")
print ("\t  >>>>>>  Author : ConanKapoor <<<<<<\n")
print (">>> Login into your account and run this script coz I'm <<<\n>>> not gonna do image processing shit to fill captcha  <<<\n>>> for your sorry ass.\t\t\t\t\t<<<\n")
print(">>> Go to Academic History and save the webpage into\t<<<\n>>> this project folder.\t\t\t\t<<<")
print ("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print ("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n")

# try:
fileName = input(">>> Please enter the name of file without .html : ")
fileName = fileName + '.html'


# except Exception:
#     print("    >!>!> Exceptioncaught - skipping to next grade.")
#     print("          Most Probably Network error.")
#     print("          GPA will suffer\n")
#     logs.write(" Outer Exception error.\n\n")
#     pass
#
# except KeyboardInterrupt:
#     print("\n\n>>> Interrupt received! Exiting cleanly...")
#     logs.write("End of logs - Abruptly Ended")
#     logs.close()
#     sys.exit()

logs.close()
############################### END OF SCRIPT :) ##############################
