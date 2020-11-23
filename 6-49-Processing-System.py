'''
6-49 Processing System
'''
def welcomeMsg(): #() -> ()
    print(" Welcome to Travis's 6-49 Processing system!")
    print(" ===============================================")
    print()
    print("You first need to provide the input file name")
    print("You will be asked to provide the output file name later")
    print()
    print("The input file should be in this folder")
    print("The output file will be created in this folder")
    print()
    print("You will be able to provide new names for the files")
    print("or accept the default names. Both files should have the extension  .csv")
    print()
    return

def read_csv_into_list_of_lists(IN_file): #(string) -> (list)
    import csv

    lall = []

    print("\n.... TRACE - data read from the file\n")
    with open(IN_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for inrow in csv_reader:
            print(".......",inrow)
            lall.append(inrow)
    return lall

def convert_lall_to_separate_lists(lall): #(list) -> (list1, list2, list3, list4)
    dateLs = []
    numLs = []
    jackpotLs = []
    winLs = []
    for ls in lall:
        dateLs += [ls[0]]
        numLs += [ls[1:8]]
        jackpotLs += [ls[8]]
        winLs += [ls[9]]
            
    return dateLs, numLs, jackpotLs, winLs

def chooseMsg(): #() -> ()
    print()
    print("Please choose one of three options:")
    print()
    print("Type ALL to process all the data")
    print("Type SEL to process selected draws")
    print("Type END to end this program")
    print()
    return

def chooseValidate(cV): #(st) -> (st)
    cV = cV.upper()
    while cV != "ALL" and cV != "SEL" and cV != "END":
        print("That was not an option. Please retype")
        cV = input("Type ALL, SEL or END (not case sensitive) ==> ")
        cV = cV.upper()
    return cV

def processedMsg(chooseV): #(st) -> ()
    print()
    if chooseV == "ALL":
        print("============= ALL the data will be processed ============")
    elif chooseV == "SEL":
        print("============= SELECTED data will be processed ============")
    print()
    print()
    print()
    return

def morWeekValidate(morW): #(st) -> (st)
    print()
    morW = morW.upper()

    while morW != "M" and morW != "D":
        print("That was not an option. Please retype")
        morW = input("Want to select by month (M) or day of week (D)? ==> ")
        morW = morW.upper()
    return morW

def morWeekMsg(morW): #(st) -> ()
    if morW == "M":
        print()
        print("Please select a month")
        print("Only the draws associated to this month will be processed")
    elif morW == "D":
        print()
        print("Please select a day of the week")
        print("Only the draws associated to this day of the week will be processed")
    return

def mValidate(mNumber): # (st) -> (int)
    while not(mNumber.isdigit()) or int(mNumber) < 1 or int(mNumber) > 12:
        if not(mNumber.isdigit()):
            print("That was not an integer. Please retype")
        elif int(mNumber) < 1 or int(mNumber) > 12:
            print("The month number is out of range. Please retype")
        mNumber = input("Please type a month number (1 to 12)==> ")
    mNumber = int(mNumber)
    return mNumber

def dValidate(dNumber): # (st) -> (int)
    while not(dNumber.isdigit()) or int(dNumber) < 1 or int(dNumber) > 7:
        if not(dNumber.isdigit()):
            print("That was not an integer. Please retype")
        elif int(dNumber) < 1 or int(dNumber) > 7:
            print("The day of the week number is out of range. Please retype")
        dNumber = input("Please type a day of the week number (1 to 7) (Mon = 1, Sun = 7) ==> ")
    dNumber = int(dNumber)
    return dNumber

def countM(dateLs, mNumber): #(List, int) -> (List)
    numLs = []
    monthLs = ["aaa", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    month = monthLs[mNumber]

    for i in range(len(dateLs)):
        if month in dateLs[i]:
            numLs += [i]
    if len(numLs) == 0:
        print("The file does not have any draws in", month)
    else:
        print(len(numLs), "draws were found in the data for", month)
    return numLs

def countD(dateLs, dNumber): #(List, int) -> (List)
    from datetime import date
    numLs = []
    weekLs = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    monthLs = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    numDateLs = []

    for i in range(len(dateLs)):
        firstDash = dateLs[i].index("-")
        secondDash = firstDash+4
        d=int(dateLs[i][ :firstDash])
        mName = dateLs[i][firstDash+1 : secondDash]
        m = monthLs.index(mName)+1
        y = int(dateLs[i][secondDash+1: ]) + 2000
        numDateLs += [[y, m, d]]

    for pos in range(len(numDateLs)):
        if date(numDateLs[pos][0],numDateLs[pos][1],numDateLs[pos][2]).weekday() == (dNumber - 1):
            numLs += [pos]
    week = weekLs[dNumber-1]

    if len(numLs) == 0:
        print("The file does not have any draws in", week)
    else:
        print(len(numLs), "draws were found in the data for", week)
    return numLs

def countAll(lst): #(List) -> (List)
    numLs = []
    for i in range(len(lst)):
        numLs += [i]
    return numLs

def outputMsg(): # () -> ()
    print()
    print("Please confirm the output file name for your selected data")
    print("    (if there is a file with this name in the folder")
    print("     this new file will substitute the previous one)")
    print()
    return

def eachTrace(dateLs, numLs, jackpotLs, winLs, countLs): #(list1, list2, list3, list4, list5) -> ()
    for pos in countLs:
        print()
        print(" JUST TO TRACE, the draw being processed is:")
        print()
        print(" index#", pos)
        print(" date", dateLs[pos])
        print(" numbers drawn", numLs[pos])
        print(" jackpot", jackpotLs[pos])
        print(" num winners", winLs[pos])
    return
        
def distribute(numLs, countLs): #(list, list2) -> (list)
    dLs = []
    for pos in countLs:
        lin = [0]*5
        for num in numLs[pos]:
                for i in range(0, 5):
                    if int(num) > i*10 and int(num) <= (i*10)+10:
                        lin[i] += 1
        dLs += [lin]
    return dLs

def average(jackpotLs, winLs, countLs): #(list, list2) -> (list)
    aLs = []
    for pos in countLs:
        if winLs[pos] == "0":
            aLs += [0]
        else:
            aLs += [int(jackpotLs[pos])/int(winLs[pos])]
    return aLs

def date(dateLs, countLs): # (list, list2) -> (list)
    daLs = []
    for pos in countLs:
        daLs += [dateLs[pos]]
    return daLs

def outputTraceMsg(): #() -> ()
    print()
    print()
    print("TRACING: Here is the output saved to the file! ")
    print()
    return
        
def append_1_draw_to_output_list(lout,date,lfreq_ran,avg_paid): #(list, st, list, int) -> ()    
    lout.append(date + ",") #Remove the "'" as it added extra quotes
    for freq in lfreq_ran:
        lout.append(str(freq) + ",")
    lout.append(str(avg_paid) + "\n")
    return

def write_list_of_output_lines_to_file(lout,file_name): #(list, st) -> ()
    fileRef = open(file_name,"w") # opening file to be written
    for line in lout:
        fileRef.write(line)
                                    
    fileRef.close()  
    return

def statStart(countLs): #(list) -> ()
    print()
    print("=========== STATS: ===========")
    print()
    print("draws processed", len(countLs))
    print()
    return

def statJackpot(jackpotLs, dateLs, countLs): #(list, list2, list3) -> ()
    maxJack = 0
    maxPos = 0
    for pos in countLs:
        if maxJack < int(jackpotLs[pos]):
            maxJack = int(jackpotLs[pos])
            maxPos = int(pos)
    print("max jackpot", maxJack)
    print("date max jackpot", dateLs[maxPos])
    print()
    return

def statAverage(avgLs, dateLs): #(list, list2) -> ()
    maxAvg = 0
    maxDate = 0
    for i in range(len(avgLs)):
        if maxAvg < int(avgLs[i]):
            maxAvg = avgLs[i]
            maxDate = dateLs[i]
    print("max average won", maxAvg)
    print("date max average won", maxDate)
    print()
    return

def statNum(numLs, countLs, disLs): #(list, list2, list3) -> (list)
    numBigLs = [0]*50
    for pos in countLs:
        for num in numLs[pos]:
            numBigLs[int(num)] += 1
    print("number of times each number was drawn")
    print(numBigLs)
    print()
    disBigLs = [0]*5
    for dis in disLs:
        for i in range(5):
            disBigLs[i] += int(dis[i])
    print("number of numbers in each range - all selected draws considered")
    print("ranges: (0,10], (10,20], (20,30], (30,40], (40,50)")
    print(disBigLs)
    print()
    print("Six most frequently drawn numbers")
    maxNum = max(numBigLs)
    count = 0
    pos = 0
    while count != 6:
        
        if pos == 50:
            pos = 0
            maxNum -= 1
        if maxNum == numBigLs[pos]:
            print("number", pos, "was drawn", maxNum, "times")
            count += 1
        pos += 1
    print()
    return disBigLs
            
def graphValidate(gC): #(st) -> (st)
    gC = gC.upper()
    while gC != "Y" and gC != "N":
        print("That was not an option. Please retype")
        gC = input("Would you like to graph the ranges distribution? (Y/N): ")
        gC = gC.upper()
    return gC

def graph(disLs): #(list) -> ()
    import turtle as t
    t.reset()
    t.speed(0)
    t.width(1)
    t.fillcolor("blue")
    t.bk(80)
    t.lt(90)
    for i in range(5):
        t.begin_fill()
        t.fd(disLs[i]*5)
        t.rt(90)
        t.fd(20)
        t.rt(90)
        t.fd(disLs[i]*5)
        t.lt(90)
        t.end_fill()
        t.fd(20)
        t.lt(90)
    #t.done()
    return    

####Top Level####
welcomeMsg()

inputFileName = input("Type x for INPUT file name 'IN_data_draws3.csv', or a new file name ==> ")
if inputFileName.lower() == "x":
    inputFileName = "IN_data_draws3.csv"

allLst = read_csv_into_list_of_lists(inputFileName)
dateAllLst, numAllLst, jackpotAllLst, winAllLst = convert_lall_to_separate_lists(allLst)

chooseMsg()
choose = input("Type ALL, SEL or END (not case sensitive) ==> ")
choose = chooseValidate(choose)

while choose != "END":
    processedMsg(choose)
    if choose == "SEL":
        morWeek = input("Want to select by month (M) or day of week (D)? ==> ")
        morWeek = morWeekValidate(morWeek)
        morWeekMsg(morWeek)
        if morWeek == "M":
            mNum = input("Please type a month number (1 to 12)==> ")
            mNum = mValidate(mNum)
            countLst = countM(dateAllLst,mNum)
        elif morWeek == "D":
            dNum = input("Please type a day of the week number (1 to 7) (Mon = 1, Sun = 7) ==> ")
            dNum = dValidate(dNum)
            countLst = countD(dateAllLst,dNum)
    else:
        countLst = countAll(dateAllLst)

    if len(countLst) == 0:
        print("Nothing will be processed, you can try another option")
    else:
        outputMsg()
    
        outputFileName = input("Type x for OUTPUT file name 'OUT_results3.csv', or a new file name ==> ")
    
        if outputFileName.lower() == "x":
            outputFileName = "OUT_results3.csv"
        
        eachTrace(dateAllLst, numAllLst, jackpotAllLst, winAllLst, countLst)
        outputTraceMsg()
        
        disLst = distribute(numAllLst, countLst)
        avgLst = average(jackpotAllLst, winAllLst, countLst)
        dateLst = date(dateAllLst, countLst)
        outLst = []
        
        for i in range(len(dateLst)):
            append_1_draw_to_output_list(outLst, dateLst[i], disLst[i], avgLst[i])
            print(dateLst[i], disLst[i], avgLst[i])
        
        write_list_of_output_lines_to_file(outLst,outputFileName)
        
        statStart(countLst)
        statJackpot(jackpotAllLst, dateAllLst, countLst)
        statAverage(avgLst, dateLst)
        disAllLst = statNum(numAllLst, countLst, disLst)

        graphChoose = input("Would you like to graph the ranges distribution? (Y/N): ")
        graphChoose = graphValidate(graphChoose)

        if graphChoose == "Y":
            graph(disAllLst)
    
    chooseMsg()
    choose = input("Type ALL, SEL or END (not case sensitive) ==> ")
    choose = chooseValidate(choose)

print("BYE .... no more stats for you!!")
