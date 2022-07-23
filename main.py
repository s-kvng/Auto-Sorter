import re

def inputData():
    rank = dict()
    while True:
        key = input('|NB|: Enter "Done" if you done!! Enter Student Name >  ')
        
        if key == 'done' or key == 'Done':
            break
        
        try:
            value = input('Enter Marks > ')
            value = int(value)
        except:
            continue
            
        
        rank[key] = value
        
    test = sorted([(v,k) for k,v in rank.items()],reverse=True)
    
    new_file = input("Name the new file > ")
    
    for v,k in test:
        f = open(f'./views/{new_file}.docx', 'a')
        f.write(f'\n{k} - {v}')
        f.close()
        


def readFile():
    
    count = dict()
    file = input("Enter the file name : ")
    
    fhand = open(f"./views/{file}")
        
       # if fhand < 1 :
          #  fhand = "TestFile.txt"
    
    for lines in fhand:
        kline = re.findall('(\S+\s.+)\s[-:]\s[0-9]+',lines) #find and extract only the names within the file(comes in list form) 
        vline = re.findall('\S+\s.+\s[-:]\s([0-9]+)',lines)#find and extract only the numbers within the file (comes in list form)
        
        for text in kline:
            for val in vline:
                val = int(val) #change the numbers which is in string form to int
                count[text] = val # creating the dictionary
                
                
    test2 = sorted([(v,k) for k,v in count.items()], reverse=True)
    
    save_file = input("Enter new file name to save : ")
    #if save_file < 1:
            #save_file = "TestFile2.txt" 
    
    for v,k in test2:
        fh = open(f"./views/{save_file}.docx", "a")  
        fh.write(f"\n{k} - {v}")
        fh.close()
        

readFile()
        