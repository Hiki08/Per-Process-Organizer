# %%
from Imports import *

# %%
class CsvReader():
    process1OrganizedCsv = ""
    process2OrganizedCsv = ""
    process3OrganizedCsv = ""
    process4OrganizedCsv = ""
    process5OrganizedCsv = ""
    process6OrganizedCsv = ""

    def __init__(self):
        pass

    def ReadProcess1Csv(self):
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

        self.process1OrganizedCsv = pd.concat(previousProcess1DataList, ignore_index=True)
        #_____________________________________________________________________________________________
    
    def ReadProcess2Csv(self):
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

        self.process2OrganizedCsv = pd.concat(previousProcess2DataList, ignore_index=True)
        #_____________________________________________________________________________________________

    def ReadProcess3Csv(self):
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

        self.process3OrganizedCsv = pd.concat(previousProcess3DataList, ignore_index=True)
        #_____________________________________________________________________________________________

    def ReadProcess4Csv(self):
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

        self.process4OrganizedCsv = pd.concat(previousProcess4DataList, ignore_index=True)
        #_____________________________________________________________________________________________

    def ReadProcess5Csv(self):
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

        self.process5OrganizedCsv = pd.concat(previousProcess5DataList, ignore_index=True)
        #_____________________________________________________________________________________________

    def ReadProcess6Csv(self):
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

        self.process6OrganizedCsv = pd.concat(previousProcess6DataList, ignore_index=True)
        #_____________________________________________________________________________________________

# %%
csvReader = CsvReader()

# %%
class CsvOrganizer():
    isProcess1Readed = ""
    isProcess2Readed = ""
    isProcess3Readed = ""
    isProcess4Readed = ""
    isProcess5Readed = ""
    isProcess6Readed = ""

    isProcess1Writed = ""
    isProcess2Writed = ""
    isProcess3Writed = ""
    isProcess4Writed = ""
    isProcess5Writed = ""
    isProcess6Writed = ""
    
    readCount = 0

    def __init__(self):
        pass
    def Process1Organizer(self):
        while not self.isProcess1Readed:
            try:
                process1OrigFile = os.path.getmtime(r"\\192.168.2.10\csv\csv\VT1\log000_1.csv")
                self.isProcess1Readed = True
            except:
                print("Failed Reading Of Process1 Trying Again In 1 Seconds")
                pass
        self.isProcess1Readed = False

        while True:
            #Checking Changes In PiCompiled Using Forced Reading Of Csv
            while not self.isProcess1Readed:
                try:
                    process1CurrentFile = os.path.getmtime(r"\\192.168.2.10\csv\csv\VT1\log000_1.csv")
                    self.isProcess1Readed = True
                except:
                    print("Failed Reading Of Process1 Trying Again In 1 Seconds")
                    pass
                
            self.isProcess1Readed = False

            if process1CurrentFile != process1OrigFile:
                print("Changes Detected")

                while not self.isProcess1Writed:
                    try:
                        csvReader.ReadProcess1Csv()
                        self.WriteCsv(csvReader.process1OrganizedCsv, "1")
                        self.isProcess1Writed = True
                    except:
                        pass
                self.isProcess1Writed = False

                #Setting The Original File Onto Current File
                process1OrigFile = process1CurrentFile

            print("Waiting For Changes In PiCompiled")
            time.sleep(1)
            
            self.readCount += 1
            if self.readCount >= 10:
                os.system('cls')
                self.readCount = 0

    def Process2Organizer(self):
        while not self.isProcess2Readed:
            try:
                process2OrigFile = os.path.getmtime(r"\\192.168.2.10\csv\csv\VT2\log000_2.csv")
                self.isProcess2Readed = True
            except:
                print("Failed Reading Of Process2 Trying Again In 1 Seconds")
                pass
        self.isProcess2Readed = False

        while True:
            #Checking Changes In PiCompiled Using Forced Reading Of Csv
            while not self.isProcess2Readed:
                try:
                    process2CurrentFile = os.path.getmtime(r"\\192.168.2.10\csv\csv\VT2\log000_2.csv")
                    self.isProcess2Readed = True
                except:
                    print("Failed Reading Of Process2 Trying Again In 1 Seconds")
                    pass
                
            self.isProcess2Readed = False

            if process2CurrentFile != process2OrigFile:
                print("Changes Detected")

                while not self.isProcess2Writed:
                    try:
                        csvReader.ReadProcess2Csv()
                        self.WriteCsv(csvReader.process2OrganizedCsv, "2")
                        self.isProcess2Writed = True
                    except:
                        pass
                self.isProcess2Writed = False

                #Setting The Original File Onto Current File
                process2OrigFile = process2CurrentFile

            print("Waiting For Changes In PiCompiled")
            time.sleep(1)
            
            self.readCount += 1
            if self.readCount >= 10:
                os.system('cls')
                self.readCount = 0


    def Process3Organizer(self):
        while not self.isProcess3Readed:
            try:
                process3OrigFile = os.path.getmtime(r"\\192.168.2.10\csv\csv\VT3\log000_3.csv")
                self.isProcess3Readed = True
            except:
                print("Failed Reading Of Process3 Trying Again In 1 Seconds")
                pass
        self.isProcess3Readed = False

        while True:
            #Checking Changes In PiCompiled Using Forced Reading Of Csv
            while not self.isProcess3Readed:
                try:
                    process3CurrentFile = os.path.getmtime(r"\\192.168.2.10\csv\csv\VT3\log000_3.csv")
                    self.isProcess3Readed = True
                except:
                    print("Failed Reading Of Process3 Trying Again In 1 Seconds")
                    pass
                
            self.isProcess3Readed = False

            if process3CurrentFile != process3OrigFile:
                print("Changes Detected")

                while not self.isProcess3Writed:
                    try:
                        csvReader.ReadProcess3Csv()
                        self.WriteCsv(csvReader.process3OrganizedCsv, "3")
                        self.isProcess3Writed = True
                    except:
                        pass
                self.isProcess3Writed = False

                #Setting The Original File Onto Current File
                process3OrigFile = process3CurrentFile

            print("Waiting For Changes In PiCompiled")
            time.sleep(1)
            
            self.readCount += 1
            if self.readCount >= 10:
                os.system('cls')
                self.readCount = 0

    def Process4Organizer(self):
        while not self.isProcess4Readed:
            try:
                process4OrigFile = os.path.getmtime(r"\\192.168.2.10\csv\csv\VT4\log000_4.csv")
                self.isProcess4Readed = True
            except:
                print("Failed Reading Of Process4 Trying Again In 1 Seconds")
                pass
        self.isProcess4Readed = False

        while True:
            #Checking Changes In PiCompiled Using Forced Reading Of Csv
            while not self.isProcess4Readed:
                try:
                    process4CurrentFile = os.path.getmtime(r"\\192.168.2.10\csv\csv\VT4\log000_4.csv")
                    self.isProcess4Readed = True
                except:
                    print("Failed Reading Of Process4 Trying Again In 1 Seconds")
                    pass
                
            self.isProcess4Readed = False

            if process4CurrentFile != process4OrigFile:
                print("Changes Detected")

                while not self.isProcess4Writed:
                    try:
                        csvReader.ReadProcess4Csv()
                        self.WriteCsv(csvReader.process4OrganizedCsv, "4")
                        self.isProcess4Writed = True
                    except:
                        pass
                self.isProcess4Writed = False

                #Setting The Original File Onto Current File
                process4OrigFile = process4CurrentFile

            print("Waiting For Changes In PiCompiled")
            time.sleep(1)
            
            self.readCount += 1
            if self.readCount >= 10:
                os.system('cls')
                self.readCount = 0

    def Process5Organizer(self):
        while not self.isProcess5Readed:
            try:
                process5OrigFile = os.path.getmtime(r"\\192.168.2.10\csv\csv\VT5\log000_5.csv")
                self.isProcess5Readed = True
            except:
                print("Failed Reading Of Process5 Trying Again In 1 Seconds")
                pass
        self.isProcess5Readed = False

        while True:
            #Checking Changes In PiCompiled Using Forced Reading Of Csv
            while not self.isProcess5Readed:
                try:
                    process5CurrentFile = os.path.getmtime(r"\\192.168.2.10\csv\csv\VT5\log000_5.csv")
                    self.isProcess5Readed = True
                except:
                    print("Failed Reading Of Process5 Trying Again In 1 Seconds")
                    pass
                
            self.isProcess5Readed = False

            if process5CurrentFile != process5OrigFile:
                print("Changes Detected")

                while not self.isProcess5Writed:
                    try:
                        csvReader.ReadProcess5Csv()
                        self.WriteCsv(csvReader.process5OrganizedCsv, "5")
                        self.isProcess5Writed = True
                    except:
                        pass
                self.isProcess5Writed = False

                #Setting The Original File Onto Current File
                process5OrigFile = process5CurrentFile

            print("Waiting For Changes In PiCompiled")
            time.sleep(1)
            
            self.readCount += 1
            if self.readCount >= 10:
                os.system('cls')
                self.readCount = 0

    def Process6Organizer(self):
        while not self.isProcess6Readed:
            try:
                process6OrigFile = os.path.getmtime(r"\\192.168.2.10\csv\csv\VT6\log000_6.csv")
                self.isProcess6Readed = True
            except:
                print("Failed Reading Of Process6 Trying Again In 1 Seconds")
                pass

        self.isProcess6Readed = False

        while True:
            #Checking Changes In PiCompiled Using Forced Reading Of Csv
            while not self.isProcess6Readed:
                try:
                    process6CurrentFile = os.path.getmtime(r"\\192.168.2.10\csv\csv\VT6\log000_6.csv")
                    self.isProcess6Readed = True
                except:
                    print("Failed Reading Of Process6 Trying Again In 1 Seconds")
                    pass
                
            self.isProcess6Readed = False

            if process6CurrentFile != process6OrigFile:
                print("Changes Detected")

                while not self.isProcess6Writed:
                    try:
                        csvReader.ReadProcess6Csv()
                        self.WriteCsv(csvReader.process6OrganizedCsv, "6")
                        self.isProcess6Writed = True
                    except:
                        pass
                self.isProcess6Writed = False

                #Setting The Original File Onto Current File
                process6OrigFile = process6CurrentFile

            print("Waiting For Changes In PiCompiled")
            time.sleep(1)
            
            self.readCount += 1
            if self.readCount >= 10:
                os.system('cls')
                self.readCount = 0
    
    def WriteCsv(self, excelData, processNumber):
        fileDirectory = (fr'\\192.168.2.10\csv\Ai Csv\Process\VT{processNumber}')

        os.chdir(fileDirectory)
        print(os.getcwd())
        
        print("Creating New File")
        #Create Excel File
        newValue = pd.concat([excelData], axis = 0, ignore_index = True)
        wireFrame = newValue
        wireFrame.to_csv(f"log000_{processNumber}.csv", index = False)

    def StartProcess1(self):
        threading.Thread(target=self.Process1Organizer).start()
    def StartProcess2(self):
        threading.Thread(target=self.Process2Organizer).start()
    def StartProcess3(self):
        threading.Thread(target=self.Process3Organizer).start()
    def StartProcess4(self):
        threading.Thread(target=self.Process4Organizer).start()
    def StartProcess5(self):
        threading.Thread(target=self.Process5Organizer).start()
    def StartProcess6(self):
        threading.Thread(target=self.Process6Organizer).start()

# %%
organizer = CsvOrganizer()
organizer.StartProcess1()
organizer.StartProcess2()
organizer.StartProcess3()
organizer.StartProcess4()
organizer.StartProcess5()
organizer.StartProcess6()


