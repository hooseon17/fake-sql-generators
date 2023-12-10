from faker import Faker
import random
from datetime import date, time, datetime, timedelta

def generate_insert_query_invoice(invoice_id, entry):
    return f"INSERT INTO invoice VALUES('{invoice_id}', '{entry[0]}', {entry[1]});\n"

def generate_random_invoice(invoice_id):
    fake = Faker()

    # Generate a random date after the year 2020
    date_entry = fake.date_between(start_date=date(2020, 1, 1), end_date=date.today()).strftime('%Y-%m-%d')

    # Generate a random time between 9:00 and 17:00
    time_entry = time(hour=random.randint(9, 17), minute=random.randint(0, 59), second=random.randint(0, 59))

    # Combine date and time
    datetime_entry = f"{date_entry} {time_entry}"

    # Generate a store ID between 1 and 20
    store_id_entry = random.randint(1, 20)

    return [datetime_entry, store_id_entry]

def main():
    try:
        num_entries = int(input("Enter the number of invoice entries to generate: "))
        starting_id = int(input("Enter the starting ID for invoices: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    if num_entries <= 0 or starting_id < 0:
        print("Number of invoice entries must be greater than 0, and starting ID must be a non-negative integer.")
        return

    queries = []

    for i in range(starting_id, starting_id + num_entries):
        invoice_id = i
        entry = generate_random_invoice(invoice_id)
        query = generate_insert_query_invoice(invoice_id, entry)
        queries.append(query)

    sql_filename = "invoice.sql"
    with open(sql_filename, mode='w') as sql_file:
        sql_file.writelines(queries)

    print(f"{num_entries} SQL queries for invoices have been generated and saved to {sql_filename}.")

if __name__ == "__main__":
    main()
