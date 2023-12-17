from faker import Faker
import random

def generate_insert_query_invoice_line(entry):
    return f"INSERT INTO invoice_line VALUES({entry[0]}, {entry[1]}, {entry[2]}, {entry[3]}, {entry[4]}, {entry[5]});\n"

def generate_random_invoice_line(line_numbers_dict):
    fake = Faker()

    # Generate a random invoice ID
    invoice_id = random.randint(1, 1000)

    # Initialize line number to 1 if the invoice_id is not in the dictionary
    line_no = line_numbers_dict.get(invoice_id, 1)

    # Increment the line number in the dictionary
    line_numbers_dict[invoice_id] = line_no + 1

    # Generate a random quantity between 1 and 20
    quantity_entry = random.randint(1, 20)

    # Generate a price less than 200 with two decimals
    price_entry = round(random.uniform(0.01, 199.99), 2)

    # Generate a discount less than the price with two decimals
    discount_entry = random.choice([0, round(random.uniform(0.01, price_entry), 2)])

    # Generate a product ID between 1 and 23
    product_id_entry = random.randint(1, 23)

    return [line_no, quantity_entry, price_entry, discount_entry, invoice_id, product_id_entry]

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
    line_numbers_dict = {}

    for _ in range(num_entries):
        entry = generate_random_invoice_line(line_numbers_dict)
        queries.append(generate_insert_query_invoice_line(entry))

    sql_filename = "invoice_line.sql"
    with open(sql_filename, mode='w') as sql_file:
        sql_file.writelines(queries)

    print(f"{num_entries} SQL queries for invoice lines have been generated and saved to {sql_filename}.")

if __name__ == "__main__":
    main()
