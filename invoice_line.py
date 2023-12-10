from faker import Faker
import random

def generate_insert_query_invoice_line(entry):
    return f"INSERT INTO invoice_line VALUES({entry[0]}, {entry[1]}, {entry[2]}, {entry[3]}, {entry[4]});\n"

def generate_random_invoice_line():
    fake = Faker()

    # Generate a random line number between 1 and 50
    line_no = random.randint(1, 50)

    # Generate a random quantity between 1 and 20
    quantity_entry = random.randint(1, 20)

    # Generate a price less than 200 with two decimals
    price_entry = round(random.uniform(0.01, 199.99), 2)

    # Generate a discount less than the price with two decimals
    discount_entry = round(random.uniform(0.01, price_entry), 2)

    # Generate an invoice ID between 1 and 1000
    invoice_id_entry = random.randint(1, 1000)

    # Generate a product ID between 1 and 23
    product_id_entry = random.randint(1, 23)

    return [line_no, quantity_entry, price_entry, discount_entry, invoice_id_entry, product_id_entry]

def main():
    try:
        num_entries = int(input("Enter the number of invoice line entries to generate: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if num_entries <= 0:
        print("Number of invoice line entries must be greater than 0.")
        return

    queries = []

    for _ in range(num_entries):
        entry = generate_random_invoice_line()
        query = generate_insert_query_invoice_line(entry)
        queries.append(query)

    sql_filename = "invoice_line.sql"
    with open(sql_filename, mode='w') as sql_file:
        sql_file.writelines(queries)

    print(f"{num_entries} SQL queries for invoice lines have been generated and saved to {sql_filename}.")

if __name__ == "__main__":
    main()
