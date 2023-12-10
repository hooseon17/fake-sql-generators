from faker import Faker
import random

def generate_insert_query_inquiry(inquiry_id, entry):
    return f"INSERT INTO new_customer_inquiry VALUES({inquiry_id}, '{entry[0]}', '{entry[1]}', '{entry[2]}', '{entry[3]}', {entry[4]}, '{entry[5]}');\n"

def generate_random_inquiry(inquiry_id):
    fake = Faker()

    # Generate a member ID between 1 and 5000
    member_id_entry = random.randint(1, 5000)

    # Generate a text for inquiry message without new lines
    inquiry_message_entry = fake.text().replace('\n', ' ')

    # Generate other random fields
    first_name_entry = fake.first_name()
    last_name_entry = fake.last_name()
    email_entry = fake.email()
    phone_entry = fake.numerify('###-###-####')

    return [first_name_entry, last_name_entry, email_entry, phone_entry, member_id_entry, inquiry_message_entry]

def main():
    try:
        num_entries = int(input("Enter the number of new customer inquiry entries to generate: "))
        starting_inquiry_id = int(input("Enter the starting ID for inquiries: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    if num_entries <= 0 or starting_inquiry_id < 0:
        print("Number of inquiry entries must be greater than 0, and starting ID must be a non-negative integer.")
        return

    queries = []

    for i in range(starting_inquiry_id, starting_inquiry_id + num_entries):
        inquiry_id = i
        entry = generate_random_inquiry(inquiry_id)
        query = generate_insert_query_inquiry(inquiry_id, entry)
        queries.append(query)

    sql_filename = "new_customer_inquiry.sql"
    with open(sql_filename, mode='w') as sql_file:
        sql_file.writelines(queries)

    print(f"{num_entries} SQL queries for new customer inquiries have been generated and saved to {sql_filename}.")

if __name__ == "__main__":
    main()
