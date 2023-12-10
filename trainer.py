from faker import Faker
import random

def generate_insert_query(trainer_id, entry):
    email_part = f"'{entry[7]}'" if len(entry) > 7 and random.choice([True, False]) else "''"
    return f"INSERT INTO trainer VALUES ({trainer_id}, {random.randint(1, 20)}, '{entry[0]}', '{entry[1]}', '{entry[2]}', '{entry[3]}', '{entry[4]}', '{entry[5]}', '{entry[6]}', {email_part});\n"

def generate_random_trainer(trainer_id):
    fake = Faker('en_CA')

    first_name = fake.first_name()
    last_name = fake.last_name()
    street = fake.street_address()
    city = fake.city()
    province = fake.province()
    postal_code = fake.postcode()
    phone = fake.numerify('###-###-####')
    email = fake.email() if random.choice([True, False]) else ''

    return trainer_id, [first_name, last_name, street, city, province, postal_code, phone, email]

def main():
    try:
        num_entries = int(input("Enter the number of trainer entries to generate: "))
        starting_id = int(input("Enter the starting ID for trainers: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    if num_entries <= 0 or starting_id < 0:
        print("Number of trainer entries must be greater than 0, and starting ID must be a non-negative integer.")
        return

    queries = []

    for i in range(starting_id, starting_id + num_entries):
        trainer_id, entry = generate_random_trainer(i)
        query = generate_insert_query(trainer_id, entry)
        queries.append(query)

    sql_filename = "trainer.sql"
    with open(sql_filename, mode='w') as sql_file:
        sql_file.writelines(queries)

    print(f"{num_entries} SQL queries have been generated and saved to {sql_filename}.")

if __name__ == "__main__":
    main()
