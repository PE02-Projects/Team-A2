![header](https://capsule-render.vercel.app/api?type=waving&color=gradient&height=300&section=header&text=Programming%20for%20Engineers2&fontSize=50&&fontColor=000000&animation=fadeIn&fontAlignY=38&desc=Team%20A2%20Project&descAlignY=51&descAlign=80)
## **Index**

1. [Overview](#overview)  
2. [Installation](#installation)  
3. [Environment](#environment)  
4. [Usage instructions](#usage-instructions)  
5. [Collaborators and contact info](#collaborators)  


***

## Overview

This python project is a tool to analyze measured data of wafers.  
It can plot and save graphs for any data you want, and also save xlsx files.  
  
***

## Installation
To install all the required modules just use the following command: 

```
pip install -r requirements.txt
```

***

## Environment
  - Windows 10
  - Python 3.8

***

## Usage Instructions
1. Execute run.py
2. Insert the desired device type.  
   Ex. `LMZC` or `LMZO` or `LMZ` (`LMZ` means both)
3. Insert the desired wafer number in the form of "D00".  
   Ex. `D07` or `D07 D08 ...` or `all`
4. Insert the desired coordinates in form of "row,column".  
   Ex. `0,0` or `-1,0/1,1/...` or `all`
5. Insert "y" or "n" whether to float the data as png files or not.  
   Ex. `y` or `n`  
6. Insert "y" or "n" whether to save the data as png files or not.  
   Ex. `y` or `n`
7. Insert "y" or "n" whether to save the data as xlsx files or not.  
   Ex. `y` or `n`

The files are saved in the `res` folder.


***

  ## **Collaborators** 

  * Seo Jinchan : sjhmp21@hanyang.ac.kr

  * Kim Chanyoung : belljy@hanyang.ac.kr
  
  * Jose Alan Barraza Villaverde : al167694@alumnos.uacj.mx

