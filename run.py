import xml.etree.ElementTree as ET
import glob
#Specify which file is going to be analyzed
lot = str(input("Please insert the wafer number: "))
row = str(int(input("Please insert the row: ")))
column = str(int(input("Please insert the column: ")))

#Obtain the path we want to analyse
if lot == "D06":
    P1 = r"C:\Users\Alan_\PycharmProjects\Team_A2_project\Team-A2\dat\D07\20190715_190855\HY202103_D07_(ROW,COLUMN)_LION1_DCM_LMZC.xml"
    P2 = P1.replace("ROW",row)
    P2 = P2.replace("COLUMN",column)
    tree = ET.parse(P1)
    root = tree.getroot()
elif lot == "D07":
    P1 = r"C:\Users\Alan_\PycharmProjects\Team_A2_project\Team-A2\dat\D08\20190712_113254\HY202103_D08_(ROW,COLUMN)_LION1_DCM_LMZC.xml"
    P2 = P1.replace("ROW", row)
    P2 = P2.replace("COLUMN", column)
    tree = ET.parse(P1)
    root = tree.getroot()
elif lot == "D22":
    P1 = r"C:\Users\Alan_\PycharmProjects\Team_A2_project\Team-A2\dat\D23\20190603_204847\HY202103_D23_(ROW,COLUMN)_LION1_DCM_LMZO.xml"
    P2 = P1.replace("ROW", row)
    P2 = P2.replace("COLUMN", column)
    tree = ET.parse(P1)
    root = tree.getroot()
elif lot == "D23":
    P1 = r"C:\Users\Alan_\PycharmProjects\Team_A2_project\Team-A2\dat\D24\20190603_225101\HY202103_D24_(ROW,COLUMN)_LION1_DCM_LMZO.xml"
    P2 = P1.replace("ROW", row)
    P2 = P2.replace("COLUMN", column)
    tree = ET.parse(P1)
    root = tree.getroot()