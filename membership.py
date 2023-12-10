from faker import Faker

def generate_insert_query(member_id, entry):
    return f"INSERT INTO member VALUES ({member_id}, '{entry[0]}', '{entry[1]}', '{entry[2]}', '{entry[3]}', '{entry[4]}', '{entry[5]}', '{entry[6]}', '{entry[7]}', '{entry[8]}');\n"

def generate_random_member(member_id):
    fake = Faker('en_CA')

    first_name = fake.first_name()
    last_name = fake.last_name()
    date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=80).strftime('%Y-%m-%d')
    street = fake.street_address()
    city = fake.city()
    province = fake.province()
    postal_code = fake.postcode()
    phone = fake.numerify('###-###-####')
    email = fake.email()

    return member_id, [first_name, last_name, date_of_birth, street, city, province, postal_code, phone, email]

def main():
    try:
        num_entries = int(input("Enter the number of entries to generate: "))
        starting_id = int(input("Enter the starting ID for members: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    if num_entries <= 0 or starting_id < 0:
        print("Number of entries must be greater than 0, and starting ID must be a non-negative integer.")
        return

    queries = []

    for i in range(starting_id, starting_id + num_entries):
        member_id, entry = generate_random_member(i)
        query = generate_insert_query(member_id, entry)
        queries.append(query)

    sql_filename = "membership.sql"
    with open(sql_filename, mode='w') as sql_file:
        sql_file.writelines(queries)

    print(f"{num_entries} SQL queries have been generated and saved to {sql_filename}.")

if __name__ == "__main__":
    main()
