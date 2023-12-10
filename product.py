from faker import Faker
import random

def generate_insert_query_product(product_id, entry):
    return f"INSERT INTO product VALUES({product_id}, '{entry[0]}', '{entry[1]}', '{entry[2]}');\n"

def generate_random_product(product_id, name):
    fake = Faker()

    # Generate a name from the provided list
    name_entry = name

    # Generate a random description without new lines
    description_entry = fake.text().replace('\n', ' ') if random.choice([True, False]) else ''

    # Generate a random MSRP between 0 and 500 in 2 decimal format
    msrp_entry = round(random.uniform(0, 500), 2)

    return [name_entry, description_entry, msrp_entry]

def main():
    # Lists for generating product names
    lesson_list = [f"lesson {i}" for i in range(1, 11)]
    equipment_list = ['Dumbbells', 'Kettlebells', 'yoga mat', 'stability ball', 'Activewear', 'Resistance Bands', 'gym bag', 'Foam Rollers', 'Headphone', 'Workout Glove', 'footwear', 'waterbottle', 'weight scale']

    combined_list = lesson_list + equipment_list

    queries = []

    for i in range(len(combined_list)):
        product_id = i + 1
        entry = generate_random_product(product_id, combined_list[i])
        query = generate_insert_query_product(product_id, entry)
        queries.append(query)

    sql_filename = "product.sql"
    with open(sql_filename, mode='w') as sql_file:
        sql_file.writelines(queries)

    print(f"{len(combined_list)} SQL queries for products have been generated and saved to {sql_filename}.")

if __name__ == "__main__":
    main()
