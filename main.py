import sqlite3

from sqlFunc import insert_record, get_exercise_by_name, display_records, create_record 
from interface import displayMenu, processChoice

database = 'fitness.db'

conn = sqlite3.connect(database)
c = conn.cursor()

# c.execute('''
#         CREATE TABLE fitness(
#           exercise text,
#           reps integer,
#           caloriesPerRep integer
#           )
#         ''')

displayMenu()
processChoice(database)

conn.commit()

conn.close()

