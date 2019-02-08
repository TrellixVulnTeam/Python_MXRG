

# fhand = open('mbox.txt')
#
# for line in fhand:
#
#     line = line.rstrip()
#
#     if not line.startswith('From:'):
#         continue
#
#     print(line)
#

# fhand = open('mbox.txt')
#
# for line in fhand:
#
#     line = line.rstrip()
#
#     if not '@uct.ac.za' in line:
#
#         continue
#
#     print(line)
#


# fname = input('Enter the file name: ')
#
# fw= input('Enter the word: ')
#
# fhand = open(fname)
#
# count =0
#
# for line in fhand:
#
#     if line.startswith(fw):
#
#         count = count +1
#
# print('There were', count,' ' , fw, ' lines in', fname)

fname = input('Enter the file name: ')

try :
    fhand = open(fname)

except:
    print('File cannot be opened:', fname)
    quit()

count = 0

for line in fhand :
    if line.startswith('Subject'):
        count = count+1

print('There were', count, 'subject lines in', fname)

