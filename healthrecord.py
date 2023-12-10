from faker import Faker
import random
from datetime import datetime, timedelta

def generate_insert_query_healthrecord(entry):
    return f"INSERT INTO healthrecord VALUES ('{entry[0]}', {entry[1]}, {entry[2]}, {entry[3]}, '{entry[4]}', {entry[5]});\n"

def generate_random_healthrecord():
    fake = Faker()

    # Generate a random datetime after the year 2020
    datetime_entry = fake.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S')

    # Generate a reasonable weight for an average adult in lb
    weight_entry = round(random.uniform(120, 180), 2)

    # Generate a BMI between 18.5 and 24.9
    bmi_entry = round(random.uniform(18.5, 24.9), 2)

    # Generate muscle mass between 0.62 and 0.89
    muscle_mass_entry = round(random.uniform(0.62, 0.89), 2)

    # Generate a random note (may be empty)
    note_entry = fake.text() if random.choice([True, False]) else ''
    note_entry = note_entry.replace('\n', ' ')

    # Generate a member ID between 1 and 5000
    member_id_entry = random.randint(1, 5000)

    return [datetime_entry, weight_entry, bmi_entry, muscle_mass_entry, note_entry, member_id_entry]

def main():
    try:
        num_entries = int(input("Enter the number of health record entries to generate: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if num_entries <= 0:
        print("Number of health record entries must be greater than 0.")
        return

    queries = []

    for _ in range(num_entries):
        entry = generate_random_healthrecord()
        query = generate_insert_query_healthrecord(entry)
        queries.append(query)

    sql_filename = "healthrecord.sql"
    with open(sql_filename, mode='w') as sql_file:
        sql_file.writelines(queries)

    print(f"{num_entries} SQL queries for health records have been generated and saved to {sql_filename}.")

if __name__ == "__main__":
    main()
