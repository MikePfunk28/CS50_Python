from datetime import datetime

odds = [ 1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
	21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
	41, 43, 45, 47, 49, 51, 53, 55, 57, 59 ]

right_this_minute = datetime.today().minute

if right_this_minute in odds:
	print("This minute seems a little odd.")
else:
	print("Not an odd minute.")

# Examples using if, else, elif, and using commas to seperate Suites,
# like {} are used to seperate Bloacks of code in other languages.
# if today == 'Saturday':
#        print("Party")
# elif today == 'Sunday':
#        print("Recover")
# else:
#        print("Rest")
#
# if today == 'Saturday':
#        print('Party!')
# elif today == 'Sunday':
#        if condition == 'Headache':
#                print('Recover, then rest.')
#        else:
#                print('Rest.')
# else:
#        print('Work, work, work.')
#
#
#
