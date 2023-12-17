import random

def generate_update_query_trainer(trainer_id, tier):
    return f"UPDATE trainer SET tier = '{tier}' WHERE trainer.id = {trainer_id};\n"

def generate_random_tier():
    return random.randint(1, 3)

def main():
    try:
        starting_id = int(input("Enter the starting ID for trainers: "))
        ending_id = int(input("Enter the ending ID for trainers: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    if starting_id < 0 or ending_id < 0 or starting_id > ending_id:
        print("Starting ID must be a non-negative integer, and ending ID must be greater than or equal to starting ID.")
        return

    queries = []

    for trainer_id in range(starting_id, ending_id + 1):
        tier_value = generate_random_tier()
        query = generate_update_query_trainer(trainer_id, tier_value)
        queries.append(query)

    sql_filename = "update_trainer.sql"
    with open(sql_filename, mode='w') as sql_file:
        sql_file.writelines(queries)

    print(f"SQL queries for updating 'tier' in the 'trainer' table have been generated and saved to {sql_filename}.")

if __name__ == "__main__":
    main()
