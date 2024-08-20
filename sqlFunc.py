import sqlite3
from records import Records

def insert_record(record, database):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    with conn:
        c.execute('''
                INSERT INTO fitness VALUES(
                  :exercise, :reps, :calories
                  )
                ''', {'exercise':record.exercise, \
                    'reps': record.reps, \
                    'calories': record.caloriesPerRep})

def get_exercise_by_name(database):
    while True:
        userExercise = ""
        userExercise = input("Please enter in an exercise to search: ")
        if(not userExercise.isalpha):
            print("Sorry, that is not a valid input.")
        else:
            break
    print("")
    
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute('''
            SELECT * FROM fitness WHERE exercise = :exercise
            ''', {'exercise': userExercise})
    totalRecords = c.fetchall()
    
    print("Here are the results for " + userExercise + "\n")
    print('{0:15} | {1:4} | {2:4}'.format('Exercise', 'Reps', \
                                         'Calories Burned Per Rep'))
    line = "-" * 50
    print(line)
    for record in totalRecords:
        print('{0:15} | {1:4} | {2:4}'.format(record[0], \
                                             record[1], \
                                             record[2]))      
    print("")

def display_records(database):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute("SELECT * FROM fitness")
    totalRecords = c.fetchall()
    print('{0:15} | {1:4} | {2:4}'.format('Exercise', 'Reps', \
                                         'Calories Burned Per Rep'))
    line = "-" * 50
    print(line)
    for record in totalRecords:
        print('{0:15} | {1:4} | {2:4}'.format(record[0], \
                                             record[1], \
                                             record[2]))      
    print("")

def create_record():
    while True:
        userExercise = ""
        userExercise = input("Please enter in an exercise: ")
        if(not userExercise.isalpha):
            print("Sorry, that is not a valid input.")
        else:
            break

    while True:
        userReps = ""
        userReps = input("Please input number of reps: ")
        if(not userReps.isdigit()):
            print("Sorry, that is not a number.")
        elif(int(userReps) < 0):
            print("Please input a number of reps greater than 0.")
        else:
            break
    
    while True:
        userCPR = ""
        userCPR = input("Please input calories burned per rep: ")
        if(not userCPR.isdigit()):
            print("Sorry, that is not a number.")
        elif(int(userCPR) < 0):
            print("Please input a number greater than 0.")
        else:
            break
    print("")
    
    newRecord = Records(userExercise, userReps, userCPR)
    return newRecord

