import pandas as pd
from datetime import datetime

keep_going = True
cmds = ['view','enter','quit']
diary = None
try:
    diary = pd.read_csv('./diary.csv')
except:
    columns = ['Date','Entries']
    diary = pd.DataFrame(columns=columns)
while keep_going:
    cmd = str(input('Enter Command: View, Enter, Quit: ')).lower().strip()
    if (cmd in cmds):
        if (cmd == 'quit'):
            keep_going = False
        elif (cmd == 'enter'):
            entry = str(input('What do you have to say?\n'))
            final_entry = pd.DataFrame({'Date': str(datetime.today().strftime('%Y-%m-%d')), 'Entries': entry }, index=[0])
            diary = diary.append(final_entry, ignore_index = True)
            f = open('./diary.csv','w+')
            f.write(diary.to_csv(index=False))
            f.close()
        elif (cmd == 'view'):
            search = str(input('Enter date (yyyy-mm-dd): ')).strip()
            results = diary[diary.Date == search]
            print('-'*86)
            print('Date: ' + search)
            print('-'*43)
            if  (len(results) > 0):
                for i in range(len(results)):
                    print(results['Entries'].iloc[i])
                    print('\n')
                    print('-'*43)
            else:
                print('No Results')
            print('-'*86)
    else:
        print("Command not found")


