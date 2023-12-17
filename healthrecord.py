from faker import Faker
import random
from datetime import datetime, timedelta

def generate_insert_query_healthrecord(entry):
    return f"INSERT INTO healthrecord VALUES ('{entry[0]}', {entry[1]}, {entry[2]}, {entry[3]}, {entry[4]}, {entry[5]}, {entry[6]}, '{entry[7]}', {entry[8]});\n"

def generate_random_healthrecord():
    fake = Faker()

    # Generate a random datetime after the year 2020
    datetime_entry = fake.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S')

    # Generate a reasonable weight for an average adult in lb
    weight_entry = round(random.uniform(120, 180), 2)

    # Generate body fat percentage between 8 and 33
    bodyfat_entry = round(random.uniform(8, 33), 2)

    # Generate waist, hip, arm, and thigh measurements for an adult in inches
    waist_entry = round(random.uniform(28, 40), 2)
    hip_entry = round(random.uniform(32, 45), 2)
    arm_entry = round(random.uniform(10, 20), 2)
    thigh_entry = round(random.uniform(18, 30), 2)

    # List of predefined short notes
    short_notes = [
        "No significant health issues.",
        "Mild allergy symptoms.",
        "Experiencing occasional headaches.",
        "Recent increase in physical activity.",
        "Good overall health.",
        "Recovering from a minor injury.",
        "Maintaining a balanced diet.",
        "Getting regular exercise.",
        "Managing stress levels.",
        "Adequate sleep and rest.",
        "Taking vitamin supplements.",
        "Routine health check scheduled.",
        "Moderate caffeine intake.",
        "Occasional back pain.",
        "Practicing mindfulness.",
        "Enjoying outdoor activities.",
        "Limiting processed food consumption.",
        "Attending fitness classes.",
        "Annual flu vaccination received.",
        "Minor digestive issues.",
        "Positive mental health practices.",
        "Avoiding excessive sugar intake.",
        "Regular dental checkups.",
        "Participating in team sports.",
        "Engaging in creative hobbies.",
        "Socializing with friends regularly.",
        "Tracking nutrition intake.",
        "Maintaining a healthy work-life balance.",
        "No current medication.",
        "Routine blood pressure monitoring.",
        "Daily meditation practice.",
        "Limited alcohol consumption.",
        "Participating in community events.",
        "Maintaining a positive outlook.",
        "Practicing good hygiene habits.",
        "No recent illness.",
        "Regular vision checkups.",
        "Active involvement in volunteer work.",
        "Exploring new fitness activities.",
        "Mindful eating practices.",
        "Monitoring cholesterol levels.",
        "Prioritizing self-care.",
        "Consistent hydration habits.",
        "Participating in charity runs.",
        "Incorporating fruits and vegetables into diet."
    ]

    # Randomly decide whether to have an empty note or not
    if random.choice([True, False]):
        note_entry = random.choice(short_notes)
    else:
        note_entry = ''

    # Generate a member ID between 1 and 5000
    member_id_entry = random.randint(1, 5000)

    return [datetime_entry, weight_entry, bodyfat_entry, waist_entry, hip_entry, arm_entry, thigh_entry, note_entry, member_id_entry]

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
