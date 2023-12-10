from faker import Faker
import random
from datetime import datetime, timedelta

def generate_insert_query_lesson(lesson_id, entry):
    return f"INSERT INTO lesson VALUES({lesson_id}, '{entry[0]}', {entry[1]}, {entry[2]}, {entry[3]}, {entry[4]});\n"

def generate_random_lesson(lesson_id):
    fake = Faker()

    # Generate a random date and time between today and 1 year ago, with whole hours between 9:00 and 17:00
    start_date = datetime.now() - timedelta(days=random.randint(1, 365))
    start_time = random.choice([9, 10, 11, 12, 13, 14, 15, 16, 17])
    datetime_entry = fake.date_time_between_dates(datetime_start=start_date, datetime_end=start_date + timedelta(hours=start_time)).strftime('%Y-%m-%d %H:%M:%S')

    # Generate a member ID between 1 and 5000
    member_id_entry = random.randint(1, 5000)

    # Generate an equipment ID between 1 and 10
    equipment_id_entry = random.randint(1, 10)

    # Generate a room ID between 1 and 10
    room_id_entry = random.randint(1, 10)

    # Generate a store ID between 1 and 20
    store_id_entry = random.randint(1, 20)

    return [datetime_entry, member_id_entry, equipment_id_entry, room_id_entry, store_id_entry]

def main():
    try:
        num_entries = int(input("Enter the number of lesson entries to generate: "))
        starting_lesson_id = int(input("Enter the starting ID for lessons: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    if num_entries <= 0 or starting_lesson_id < 0:
        print("Number of lesson entries must be greater than 0, and starting ID must be a non-negative integer.")
        return

    queries = []

    for i in range(starting_lesson_id, starting_lesson_id + num_entries):
        lesson_id = i
        entry = generate_random_lesson(lesson_id)
        query = generate_insert_query_lesson(lesson_id, entry)
        queries.append(query)

    sql_filename = "lesson.sql"
    with open(sql_filename, mode='w') as sql_file:
        sql_file.writelines(queries)

    print(f"{num_entries} SQL queries for lessons have been generated and saved to {sql_filename}.")

if __name__ == "__main__":
    main()
