# 6-49 Processing System
Lottery processing system that analyzes data from past Lotto 6-49 draw results.
The program will input and output CSV with lottery data.
Max, averages, number of times, number in range, most frequently drawn, and a distribution graph will be given.

## Installation
1. Clone the repository
```bash
git clone https://github.com/Toooo123/6-49-Processing-System.git
```
2. Run the program with Python 3
```bash
python 6-49-Processing-System.py
```

## Sample Run
In this sample run, the program will input 3 draws from the file [In_data_draws3.csv.](/IN_data_draws3.csv)
Three options will be chosen:
1. [All](#option-1-all)
2. [Tuesday](#option-2-tuesday)
3. [August](#option-3-august)

### Option 1: All
```
 Welcome to the Travis's 6-49 Processing system!
 ===============================================
You first need to provide the input file name
You will be asked to provide the output file name later

The input file should be in this folder
The output file will be created in this folder

You will be able to provide new names for the files
or accept the default names. Both files should have the extension  .csv

Type x for INPUT file name 'IN_data_draws3.csv', or a new file name ==>
```
Input: ```x```
```
.... TRACE - data read from the file

....... ['25-Nov-15', '1', '2', '3', '4', '29', '48', '21', '1500', '2']
....... ['1-Apr-17', '27', '40', '41', '42', '45', '46', '20', '2500', '0']
....... ['17-Apr-18', '16', '17', '35', '43', '44', '46', '49', '55500', '3']

Please choose one of three options:

Type ALL to process all the data
Type SEL to process selected draws
Type END to end this program

Type ALL, SEL or END (not case sensitive) ==>
```
Input: ```all```
```
============= ALL the data will be processed ============
Please confirm the output file name for your selected data
    (if there is a file with this name in the folder
     this new file will substitute the previous one)

Type x for OUTPUT file name 'OUT_results3.csv', or a new file name ==>
```
Input: ```x``` 

Output File: [OUT_results3.csv](/OUT_results3.csv)

```
 JUST TO TRACE, the draw being processed is:

 index# 0
 date 25-Nov-15
 numbers drawn ['1', '2', '3', '4', '29', '48', '21']
 jackpot 1500
 num winners 2

 JUST TO TRACE, the draw being processed is:

 index# 1
 date 1-Apr-17
 numbers drawn ['27', '40', '41', '42', '45', '46', '20']
 jackpot 2500
 num winners 0

 JUST TO TRACE, the draw being processed is:

 index# 2
 date 17-Apr-18
 numbers drawn ['16', '17', '35', '43', '44', '46', '49']
 jackpot 55500
 num winners 3

TRACING: Here is the output saved to the file! 

25-Nov-15 [4, 0, 2, 0, 1] 750.0
1-Apr-17 [0, 1, 1, 1, 4] 0
17-Apr-18 [0, 2, 0, 1, 4] 18500.0

=========== STATS: ===========

draws processed 3

max jackpot 55500
date max jackpot 17-Apr-18

max average won 18500.0
date max average won 17-Apr-18

number of times each number was drawn
[0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 0, 1, 1]

number of numbers in each range - all selected draws considered
ranges: (0,10], (10,20], (20,30], (30,40], (40,50)
[4, 3, 3, 2, 9]

Six most frequently drawn numbers
number 46 was drawn 2 times
number 1 was drawn 1 times
number 2 was drawn 1 times
number 3 was drawn 1 times
number 4 was drawn 1 times
number 16 was drawn 1 times

Would you like to graph the ranges distribution? (Y/N):
```
Input: ```y```
#### Distribution Graph
![Graph1](/Images/Graph1.PNG)

### Option 2: Tuesday
```
Please choose one of three options:

Type ALL to process all the data
Type SEL to process selected draws
Type END to end this program

Type ALL, SEL or END (not case sensitive) ==> 
```
Input: ```sel```
```
============= SELECTED data will be processed ============
Want to select by month (M) or day of week (D)? ==>
```
Input: ```d```
```
Please select a day of the week
Only the draws associated to this day of the week will be processed
Please type a day of the week number (1 to 7) (Mon = 1, Sun = 7) ==>
```
Input: 2
```
1 draws were found in the data for Tuesday

Please confirm the output file name for your selected data
    (if there is a file with this name in the folder
     this new file will substitute the previous one)

Type x for OUTPUT file name 'OUT_results3.csv', or a new file name ==>
```
Input ```OUT_result3_Tues.csv```

Output File: [OUT_results3_Tues.csv](/OUT_results3_Tues.csv)
```
JUST TO TRACE, the draw being processed is:

 index# 2
 date 17-Apr-18
 numbers drawn ['16', '17', '35', '43', '44', '46', '49']
 jackpot 55500
 num winners 3


TRACING: Here is the output saved to the file! 

17-Apr-18 [0, 2, 0, 1, 4] 18500.0

=========== STATS: ===========

draws processed 1

max jackpot 55500
date max jackpot 17-Apr-18

max average won 18500.0
date max average won 17-Apr-18

number of times each number was drawn
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1]

number of numbers in each range - all selected draws considered
ranges: (0,10], (10,20], (20,30], (30,40], (40,50)
[0, 2, 0, 1, 4]

Six most frequently drawn numbers
number 16 was drawn 1 times
number 17 was drawn 1 times
number 35 was drawn 1 times
number 43 was drawn 1 times
number 44 was drawn 1 times
number 46 was drawn 1 times

Would you like to graph the ranges distribution? (Y/N):
```
Input: ```y```
#### Distribution Graph
![Graph2](/Images/Graph2.PNG)

### Option 3: August
```
Please choose one of three options:

Type ALL to process all the data
Type SEL to process selected draws
Type END to end this program

Type ALL, SEL or END (not case sensitive) ==>
```
Input: ```sel```
```
============= SELECTED data will be processed ============
Want to select by month (M) or day of week (D)? ==>
```
Input: ```m```
```
Please select a month
Only the draws associated to this month will be processed
Please type a month number (1 to 12)==>
```
Input: ```8```
```
The file does not have any draws in Aug
Nothing will be processed, you can try another option

Please choose one of three options:

Type ALL to process all the data
Type SEL to process selected draws
Type END to end this program

Type ALL, SEL or END (not case sensitive) ==>
```
Input: ```end```
```
BYE .... no more stats for you!!
```
## Flow Chart
![Flow Chart](/Images/FlowChart.png)
