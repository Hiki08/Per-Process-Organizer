# %%
from Imports import *

# %%
process1OrganizedCsv = ""
process2OrganizedCsv = ""
process3OrganizedCsv = ""
process4OrganizedCsv = ""
process5OrganizedCsv = ""
process6OrganizedCsv = ""

isProcess1Readed = False
isProcess2Readed = False
isProcess3Readed = False
isProcess4Readed = False
isProcess5Readed = False
isProcess6Readed = False

isProcess1Writed = False
isProcess2Writed = False
isProcess3Writed = False
isProcess4Writed = False
isProcess5Writed = False
isProcess6Writed = False

isDuplicated = False

readCount = 0

# %%
def ReadProcess1Csv():
    global process1OrganizedCsv

    #VT1____________________________________________________________________________________
    previousProcess1Directory = (r'\\192.168.2.10\csv\Ai Csv\Previous file')
    os.chdir(previousProcess1Directory)
    #Reading All FC1 Previous Data
    previousProcess1Data = glob.glob('*log000_1*')
    previousProcess1DataList = []

    #Appending All Previous Data Into List
    for f in previousProcess1Data:
        a = pd.read_csv(f, encoding='latin1')
        previousProcess1DataList.append(a)

    currentProcess1Directory = (r'\\192.168.2.10\csv\csv\VT1')
    os.chdir(currentProcess1Directory)

    #Appending Latest Data Into List
    currentProcess1Data = pd.read_csv('log000_1.csv', encoding='latin1')
    previousProcess1DataList.append(currentProcess1Data)

    process1OrganizedCsv = pd.concat(previousProcess1DataList, ignore_index=True)
    #_____________________________________________________________________________________________

# %%
def ReadProcess2Csv():
    global process2OrganizedCsv

    #VT2____________________________________________________________________________________
    previousProcess2Directory = (r'\\192.168.2.10\csv\Ai Csv\Previous file')
    os.chdir(previousProcess2Directory)
    #Reading All FC1 Previous Data
    previousProcess2Data = glob.glob('*log000_2*')
    previousProcess2DataList = []

    #Appending All Previous Data Into List
    for f in previousProcess2Data:
        a = pd.read_csv(f, encoding='latin1')
        previousProcess2DataList.append(a)

    currentProcess2Directory = (r'\\192.168.2.10\csv\csv\VT2')
    os.chdir(currentProcess2Directory)

    #Appending Latest Data Into List
    currentProcess2Data = pd.read_csv('log000_2.csv', encoding='latin1')
    previousProcess2DataList.append(currentProcess2Data)

    process2OrganizedCsv = pd.concat(previousProcess2DataList, ignore_index=True)
    #_____________________________________________________________________________________________

# %%
def ReadProcess3Csv():
    global process3OrganizedCsv

    #VT3____________________________________________________________________________________
    previousProcess3Directory = (r'\\192.168.2.10\csv\Ai Csv\Previous file')
    os.chdir(previousProcess3Directory)
    #Reading All FC1 Previous Data
    previousProcess3Data = glob.glob('*log000_3*')
    previousProcess3DataList = []

    #Appending All Previous Data Into List
    for f in previousProcess3Data:
        a = pd.read_csv(f, encoding='latin1')
        previousProcess3DataList.append(a)

    currentProcess3Directory = (r'\\192.168.2.10\csv\csv\VT3')
    os.chdir(currentProcess3Directory)

    #Appending Latest Data Into List
    currentProcess3Data = pd.read_csv('log000_3.csv', encoding='latin1')
    previousProcess3DataList.append(currentProcess3Data)

    process3OrganizedCsv = pd.concat(previousProcess3DataList, ignore_index=True)
    #_____________________________________________________________________________________________

# %%
def ReadProcess4Csv():
    global process4OrganizedCsv

    #VT4____________________________________________________________________________________
    previousProcess4Directory = (r'\\192.168.2.10\csv\Ai Csv\Previous file')
    os.chdir(previousProcess4Directory)
    #Reading All FC1 Previous Data
    previousProcess4Data = glob.glob('*log000_4*')
    previousProcess4DataList = []

    #Appending All Previous Data Into List
    for f in previousProcess4Data:
        a = pd.read_csv(f, encoding='latin1')
        previousProcess4DataList.append(a)

    currentProcess4Directory = (r'\\192.168.2.10\csv\csv\VT4')
    os.chdir(currentProcess4Directory)

    #Appending Latest Data Into List
    currentProcess4Data = pd.read_csv('log000_4.csv', encoding='latin1')
    previousProcess4DataList.append(currentProcess4Data)

    process4OrganizedCsv = pd.concat(previousProcess4DataList, ignore_index=True)
    #_____________________________________________________________________________________________

# %%
def ReadProcess5Csv():
    global process5OrganizedCsv

    #VT5____________________________________________________________________________________
    previousProcess5Directory = (r'\\192.168.2.10\csv\Ai Csv\Previous file')
    os.chdir(previousProcess5Directory)
    #Reading All FC1 Previous Data
    previousProcess5Data = glob.glob('*log000_5*')
    previousProcess5DataList = []

    #Appending All Previous Data Into List
    for f in previousProcess5Data:
        a = pd.read_csv(f, encoding='latin1')
        previousProcess5DataList.append(a)

    currentProcess5Directory = (r'\\192.168.2.10\csv\csv\VT5')
    os.chdir(currentProcess5Directory)

    #Appending Latest Data Into List
    currentProcess5Data = pd.read_csv('log000_5.csv', encoding='latin1')
    previousProcess5DataList.append(currentProcess5Data)

    process5OrganizedCsv = pd.concat(previousProcess5DataList, ignore_index=True)
    #_____________________________________________________________________________________________

# %%
def ReadProcess6Csv():
    global process6OrganizedCsv

    #VT6____________________________________________________________________________________
    previousProcess6Directory = (r'\\192.168.2.10\csv\Ai Csv\Previous file')
    os.chdir(previousProcess6Directory)
    #Reading All FC1 Previous Data
    previousProcess6Data = glob.glob('*log000_6*')
    previousProcess6DataList = []

    #Appending All Previous Data Into List
    for f in previousProcess6Data:
        a = pd.read_csv(f, encoding='latin1')
        previousProcess6DataList.append(a)

    currentProcess6Directory = (r'\\192.168.2.10\csv\csv\VT6')
    os.chdir(currentProcess6Directory)

    #Appending Latest Data Into List
    currentProcess6Data = pd.read_csv('log000_6.csv', encoding='latin1')
    previousProcess6DataList.append(currentProcess6Data)

    process6OrganizedCsv = pd.concat(previousProcess6DataList, ignore_index=True)
    #_____________________________________________________________________________________________

# %%
def WriteCsv(excelData, processNumber):
    fileDirectory = (fr'\\192.168.2.10\csv\Ai Csv\Process\VT{processNumber}')

    os.chdir(fileDirectory)
    print(os.getcwd())
    
    print("Creating New File")
    #Create Excel File
    newValue = pd.concat([excelData], axis = 0, ignore_index = True)
    wireFrame = newValue
    wireFrame.to_csv(f"log000_{processNumber}.csv", index = False)

# %%
def Process1Organizer():
    global isProcess1Readed
    global isProcess1Writed
    global readCount

    while not isProcess1Readed:
        try:
            process1OrigFile = os.path.getmtime(r"\\192.168.2.10\csv\csv\VT1\log000_1.csv")
            isProcess1Readed = True
        except:
            print("Failed Reading Of Process1 Trying Again In 1 Seconds")
            pass
    isProcess1Readed = False

    while True:
        #Checking Changes In PiCompiled Using Forced Reading Of Csv
        while not isProcess1Readed:
            try:
                process1CurrentFile = os.path.getmtime(r"\\192.168.2.10\csv\csv\VT1\log000_1.csv")
                isProcess1Readed = True
            except:
                print("Failed Reading Of Process1 Trying Again In 1 Seconds")
                pass
            
        isProcess1Readed = False

        if process1CurrentFile != process1OrigFile:
            print("Changes Detected")

            while not isProcess1Writed:
                try:
                    ReadProcess1Csv()
                    WriteCsv(process1OrganizedCsv, "1")
                    isProcess1Writed = True
                except:
                    pass
            isProcess1Writed = False

            #Setting The Original File Onto Current File
            process1OrigFile = process1CurrentFile

        print("Waiting For Changes In PiCompiled")
        time.sleep(1)
        
        readCount += 1
        if readCount >= 10:
            os.system('cls')
            readCount = 0

# %%
def Process2Organizer():
    global isProcess2Readed
    global isProcess2Writed
    global readCount

    while not isProcess2Readed:
        try:
            process2OrigFile = os.path.getmtime(r"\\192.168.2.10\csv\csv\VT2\log000_2.csv")
            isProcess2Readed = True
        except:
            print("Failed Reading Of Process2 Trying Again In 1 Seconds")
            pass
    isProcess2Readed = False

    while True:
        #Checking Changes In PiCompiled Using Forced Reading Of Csv
        while not isProcess2Readed:
            try:
                process2CurrentFile = os.path.getmtime(r"\\192.168.2.10\csv\csv\VT2\log000_2.csv")
                isProcess2Readed = True
            except:
                print("Failed Reading Of Process2 Trying Again In 1 Seconds")
                pass
            
        isProcess2Readed = False

        if process2CurrentFile != process2OrigFile:
            print("Changes Detected")

            while not isProcess2Writed:
                try:
                    ReadProcess2Csv()
                    WriteCsv(process2OrganizedCsv, "2")
                    isProcess2Writed = True
                except:
                    pass
            isProcess2Writed = False

            #Setting The Original File Onto Current File
            process2OrigFile = process2CurrentFile

        print("Waiting For Changes In PiCompiled")
        time.sleep(1)
        
        readCount += 1
        if readCount >= 10:
            os.system('cls')
            readCount = 0

# %%
def Process3Organizer():
    global isProcess3Readed
    global isProcess3Writed
    global readCount

    while not isProcess3Readed:
        try:
            process3OrigFile = os.path.getmtime(r"\\192.168.2.10\csv\csv\VT3\log000_3.csv")
            isProcess3Readed = True
        except:
            print("Failed Reading Of Process3 Trying Again In 1 Seconds")
            pass
    isProcess3Readed = False

    while True:
        #Checking Changes In PiCompiled Using Forced Reading Of Csv
        while not isProcess3Readed:
            try:
                process3CurrentFile = os.path.getmtime(r"\\192.168.2.10\csv\csv\VT3\log000_3.csv")
                isProcess3Readed = True
            except:
                print("Failed Reading Of Process3 Trying Again In 1 Seconds")
                pass
            
        isProcess3Readed = False

        if process3CurrentFile != process3OrigFile:
            print("Changes Detected")

            while not isProcess3Writed:
                try:
                    ReadProcess3Csv()
                    WriteCsv(process3OrganizedCsv, "3")
                    isProcess3Writed = True
                except:
                    pass
            isProcess3Writed = False

            #Setting The Original File Onto Current File
            process3OrigFile = process3CurrentFile

        print("Waiting For Changes In PiCompiled")
        time.sleep(1)
        
        readCount += 1
        if readCount >= 10:
            os.system('cls')
            readCount = 0

# %%
def Process4Organizer():
    global isProcess4Readed
    global isProcess4Writed
    global readCount

    while not isProcess4Readed:
        try:
            process4OrigFile = os.path.getmtime(r"\\192.168.2.10\csv\csv\VT4\log000_4.csv")
            isProcess4Readed = True
        except:
            print("Failed Reading Of Process4 Trying Again In 1 Seconds")
            pass
    isProcess4Readed = False

    while True:
        #Checking Changes In PiCompiled Using Forced Reading Of Csv
        while not isProcess4Readed:
            try:
                process4CurrentFile = os.path.getmtime(r"\\192.168.2.10\csv\csv\VT4\log000_4.csv")
                isProcess4Readed = True
            except:
                print("Failed Reading Of Process4 Trying Again In 1 Seconds")
                pass
            
        isProcess4Readed = False

        if process4CurrentFile != process4OrigFile:
            print("Changes Detected")

            while not isProcess4Writed:
                try:
                    ReadProcess4Csv()
                    WriteCsv(process4OrganizedCsv, "4")
                    isProcess4Writed = True
                except:
                    pass
            isProcess4Writed = False

            #Setting The Original File Onto Current File
            process4OrigFile = process4CurrentFile

        print("Waiting For Changes In PiCompiled")
        time.sleep(1)
        
        readCount += 1
        if readCount >= 10:
            os.system('cls')
            readCount = 0

# %%
def Process5Organizer():
    global isProcess5Readed
    global isProcess5Writed
    global readCount

    while not isProcess5Readed:
        try:
            process5OrigFile = os.path.getmtime(r"\\192.168.2.10\csv\csv\VT5\log000_5.csv")
            isProcess5Readed = True
        except:
            print("Failed Reading Of Process5 Trying Again In 1 Seconds")
            pass
    isProcess5Readed = False

    while True:
        #Checking Changes In PiCompiled Using Forced Reading Of Csv
        while not isProcess5Readed:
            try:
                process5CurrentFile = os.path.getmtime(r"\\192.168.2.10\csv\csv\VT5\log000_5.csv")
                isProcess5Readed = True
            except:
                print("Failed Reading Of Process5 Trying Again In 1 Seconds")
                pass
            
        isProcess5Readed = False

        if process5CurrentFile != process5OrigFile:
            print("Changes Detected")

            while not isProcess5Writed:
                try:
                    ReadProcess5Csv()
                    WriteCsv(process5OrganizedCsv, "5")
                    isProcess5Writed = True
                except:
                    pass
            isProcess5Writed = False

            #Setting The Original File Onto Current File
            process5OrigFile = process5CurrentFile

        print("Waiting For Changes In PiCompiled")
        time.sleep(1)
        
        readCount += 1
        if readCount >= 10:
            os.system('cls')
            readCount = 0

# %%
def Process6Organizer():
    global isProcess6Readed
    global isProcess6Writed
    global readCount

    while not isProcess6Readed:
        try:
            process6OrigFile = os.path.getmtime(r"\\192.168.2.10\csv\csv\VT6\log000_6.csv")
            isProcess6Readed = True
        except:
            print("Failed Reading Of Process6 Trying Again In 1 Seconds")
            pass

    isProcess6Readed = False

    while True:
        #Checking Changes In PiCompiled Using Forced Reading Of Csv
        while not isProcess6Readed:
            try:
                process6CurrentFile = os.path.getmtime(r"\\192.168.2.10\csv\csv\VT6\log000_6.csv")
                isProcess6Readed = True
            except:
                print("Failed Reading Of Process6 Trying Again In 1 Seconds")
                pass
            
        isProcess6Readed = False

        if process6CurrentFile != process6OrigFile:
            print("Changes Detected")

            while not isProcess6Writed:
                try:
                    ReadProcess6Csv()
                    WriteCsv(process6OrganizedCsv, "6")
                    isProcess6Writed = True
                except:
                    pass
            isProcess6Writed = False

            #Setting The Original File Onto Current File
            process6OrigFile = process6CurrentFile

        print("Waiting For Changes In PiCompiled")
        time.sleep(1)
        
        readCount += 1
        if readCount >= 10:
            os.system('cls')
            readCount = 0

# %%
os.system('echo -ne "\033]0;Per Process Organizer\007"')

threading.Thread(target=Process1Organizer).start()
threading.Thread(target=Process2Organizer).start()
threading.Thread(target=Process3Organizer).start()
threading.Thread(target=Process4Organizer).start()
threading.Thread(target=Process5Organizer).start()
threading.Thread(target=Process6Organizer).start()

# %%
# ReadProcessCsv()
# WriteCsv(process1OrganizedCsv, "1")
# WriteCsv(process2OrganizedCsv, "2")
# WriteCsv(process3OrganizedCsv, "3")
# WriteCsv(process4OrganizedCsv, "4")
# WriteCsv(process5OrganizedCsv, "5")
# WriteCsv(process6OrganizedCsv, "6")


# %%
# ReadProcess1Csv()
# WriteCsv(process1OrganizedCsv, "1")

# ReadProcess2Csv()
# WriteCsv(process2OrganizedCsv, "2")

# ReadProcess3Csv()
# WriteCsv(process3OrganizedCsv, "3")

# ReadProcess4Csv()
# WriteCsv(process4OrganizedCsv, "4")

# ReadProcess5Csv()
# WriteCsv(process5OrganizedCsv, "5")

# ReadProcess6Csv()
# WriteCsv(process6OrganizedCsv, "6")


