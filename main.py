
def inputData():
    rank = dict()
    while True:
        key = input('|NB|: Enter "Done" if you done!! Enter Student Name >  ')
        
        if key == 'done' or key == 'Done':
            break
        
        value = input('Enter Marks > ')
        value = int(value)
        
        rank[key] = value
        
    
    return rank

print(inputData())
        
        
        