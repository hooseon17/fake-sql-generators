from faker import Faker

def generate_insert_query(store_id, entry):
    return f"INSERT INTO store VALUES ({store_id}, '{entry[0]}', '{entry[1]}', '{entry[2]}', '{entry[3]}', '{entry[4]}', '{entry[5]}');\n"

def generate_random_store(store_id):
    fake = Faker('en_CA')

    street = fake.street_address()
    city = fake.city()
    province = fake.province()
    postal_code = fake.postcode()
    phone = fake.numerify('###-###-####')
    email = fake.email()

    return store_id, [street, city, province, postal_code, phone, email]

def main():
    try:
        num_entries = int(input("Enter the number of store entries to generate: "))
        starting_id = int(input("Enter the starting ID for stores: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    if num_entries <= 0 or starting_id < 0:
        print("Number of store entries must be greater than 0, and starting ID must be a non-negative integer.")
        return

    queries = []

    for i in range(starting_id, starting_id + num_entries):
        store_id, entry = generate_random_store(i)
        query = generate_insert_query(store_id, entry)
        queries.append(query)

    sql_filename = "store.sql"
    with open(sql_filename, mode='w') as sql_file:
        sql_file.writelines(queries)

    print(f"{num_entries} SQL queries have been generated and saved to {sql_filename}.")

if __name__ == "__main__":
    main()
