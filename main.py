

def inputData():
    rank = dict()
    while True:
        key = input('|NB|: Enter "Done" if you done!! Enter Student Name >  ')
        
        if key == 'done' or key == 'Done':
            break
        
        value = input('Enter Marks > ')
        value = int(value)
        
        rank[key] = value
        
    test = sorted([(v,k) for k,v in rank.items()],reverse=True)
    
    for v,k in test:
        f = open('./views/NewFile.docx', 'a')
        f.write(f'\n{k} - {v}')
        f.close()
        

inputData()
        
     
        