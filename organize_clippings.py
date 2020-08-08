from collections import defaultdict
import os

filepath = 'My Clippings.txt'
notes = defaultdict(list)
cur_book = ''

with open(filepath) as clippings:
    first_line = clippings.readline().rstrip('\n')
cur_book = first_line

with open(filepath) as clippings:
    for line in clippings:
        line = line.rstrip('\n')
        if line == '==========':
            cur_book = clippings.readline().rstrip('\n')
            if cur_book != '':
                metadata = clippings.readline().rstrip('\n')
                newline = clippings.readline().rstrip('\n')
                note = clippings.readline().rstrip('\n')
                notes[cur_book].append(note)
                
# MAKE A FILE FOR EACH BOOK'S NOTES IN A NEW DIRECTORY

newdir = 'organized_kindle_notes'
os.mkdir(newdir)

for book in notes:
    newbookpath = os.path.join(newdir, book) 
    newbookpath = newbookpath + '.txt'  # make plain text
    with open(newbookpath, 'w') as organizedbooknotes:
        print('==========', file=organizedbooknotes)
        print(book, file=organizedbooknotes) 
        print('==========', file=organizedbooknotes)
        print('', file=organizedbooknotes)
        for note in notes[book]:
            print(note, file=organizedbooknotes)
            print('', file=organizedbooknotes)                
           
           
           
# PRINT ALL BOOKS' NOTES IN ONE FILE

# with open('organizedkindlenotes.txt', 'w') as organizednotes:
#     for book in notes:
#         print(book, file=organizednotes) 
#         print('', file=organizednotes)
#         for note in notes[book]:
#             print(note, file=organizednotes)
#             print('', file=organizednotes)
#         print('==========', file=organizednotes)
#         print('', file=organizednotes) 


# TEST PRINT

# print('LIBRARY:')
# for book in notes:
#     print('  ' + book)
    
# for note in notes[book]:
#     print(note)
#     print()
