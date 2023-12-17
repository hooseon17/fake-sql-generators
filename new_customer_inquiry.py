import random
from faker import Faker

# List of sample inquiries
sample_inquiries = [
    "How much does a monthly membership cost?",
    "Do you offer a family membership option?",
    "Can I freeze my membership if I go on vacation?",
    "What types of memberships do you offer?",
    "Is there a trial period for memberships?",
    "Can I upgrade my membership at any time?",
    "Are there any discounts for long-term commitments?",
    "What is included in a standard membership?",
    "Do you have student or senior discounts?",
    "Are there any additional fees beyond the membership cost?",
    "Can I cancel my membership at any time?",
    "Do you offer corporate membership plans?",
    "What are the benefits of a premium membership?",
    "Is there a sign-up fee for new members?",
    "Do you have special rates for off-peak hours?",
    "Can I transfer my membership to another location?",
    "What facilities are included in the membership?",
    "Are there locker facilities available for members?",
    "Can I bring a guest to the gym with my membership?",
    "What is the process for renewing a membership?",
    "Do you provide personalized membership consultations?",
    "What are the payment options for memberships?",
    "Are there any restrictions on using certain equipment?",
    "Do you offer a money-back guarantee for memberships?",
    "Can I suspend my membership temporarily?",
    "What is the policy for upgrading or downgrading memberships?",
    "Are there any incentives for referring new members?",
    "What group fitness classes are included in the membership?",
    "Is personal training included in certain memberships?",
    "Can I use the facilities at any time of day with my membership?",
    "Do you have partnerships with local businesses for member discounts?",
    "What amenities are available in the members-only area?",
    "Can I track my fitness progress through the membership?",
    "Are there any limitations on the number of visits per week?",
    "Do you have events or social activities for members?",
    "Is there a minimum age requirement for membership?",
    "What are the cancellation policies for classes?",
    "Can I book private lessons with a trainer?",
    "How do I sign up for a specific class or lesson?",
    "What qualifications do your trainers have?",
    "Are there any assessments before starting a training program?",
    "Can I choose the trainer for my sessions?",
    "Do you offer nutrition guidance with training programs?",
    "Are there group lessons available for beginners?",
    "Can I book lessons on a flexible schedule?",
    "Are there age-specific classes for children or seniors?",
    "What types of equipment are used in lessons?",
    "Do you offer virtual lessons or training sessions?",
    "What is the duration of a typical training session?",
    "Can I request a trial lesson before committing?",
    "Are there any prerequisites for joining advanced lessons?",
    "Do you provide training programs for specific sports?",
    "How often are lesson schedules updated?",
    "Is there a dress code for lessons?",
    "Can I track my progress and goals with lessons?",
    "What safety measures are in place during lessons?",
    "Do you offer specialized lessons for weight loss?",
    "Can I switch between different lessons or programs?",
    "Are there any additional costs for lesson materials?",
    "What is your policy on missed lessons?",
    "Do you provide training for specific fitness goals (e.g., muscle gain, endurance)?",
    "How do I cancel or reschedule a lesson?",
    "What types of lessons are suitable for beginners?",
    "Are there any assessments before starting a training program?",
    "Can I choose the lesson for my sessions?",
    "Do you offer nutrition guidance with training programs?",
    "Are there group lessons available for beginners?",
    "Can I book lessons on a flexible schedule?",
    "Are there age-specific classes for children or seniors?",
    "What types of equipment are used in lessons?",
    "Do you offer virtual lessons or training sessions?",
    "What is the duration of a typical training session?",
    "Can I request a trial lesson before committing?",
    "Are there any prerequisites for joining advanced lessons?",
    "Do you provide training programs for specific sports?",
    "How often are lesson schedules updated?",
    "Is there a dress code for lessons?",
    "Can I track my progress and goals with lessons?",
    "What safety measures are in place during lessons?",
    "Do you offer specialized lessons for weight loss?",
    "Can I switch between different lessons or programs?",
    "Are there any additional costs for lesson materials?",
    "What is your policy on missed lessons?",
    "Do you provide training for specific fitness goals (e.g., muscle gain, endurance)?",
    "How do I cancel or reschedule a lesson?",
    "What types of lessons are suitable for beginners?",
    "Do you have certified nutritionists on staff?",
    "Can I get a personalized nutrition plan with my membership?",
    "Are there cooking classes or workshops on nutrition?",
    "Do you provide guidance on dietary supplements?",
    "Is nutritional counseling included in personal training packages?",
    "Can I schedule a consultation with a nutrition expert?",
    "Do you offer meal planning services?",
    "Are there any discounts on nutrition services for members?",
    "Can I attend workshops on healthy eating habits?",
    "Is there a separate fee for nutritional consultations?",
    "Can I get assistance with dietary restrictions or allergies?",
    "Are nutrition seminars included in the membership?",
    "Do you offer guidance on post-workout nutrition?",
    "Can I request a personalized diet analysis?",
    "Are there special programs for weight management?",
    "Can I get recipes or meal ideas from your nutrition experts?",
    "Do you provide guidance on maintaining a balanced diet?",
    "Are there resources available for vegetarian or vegan diets?",
    "Can I get assistance with creating a grocery shopping list?",
    "Is there a helpline or support for nutritional queries?",
    "Do you organize events or challenges related to nutrition?",
    "Can I access nutritional resources online?",
    "Are there any restrictions on using certain equipment?",
    "Do you offer a money-back guarantee for memberships?",
    "Can I suspend my membership temporarily?",
    "What is the policy for upgrading or downgrading memberships?",
    "Are there any incentives for referring new members?",
    "What group fitness classes are included in the membership?",
    "Is personal training included in certain memberships?",
    "Can I use the facilities at any time of day with my membership?",
    "Do you have partnerships with local businesses for member discounts?",
    "What amenities are available in the members-only area?",
    "Can I track my fitness progress through the membership?",
    "Are there any limitations on the number of visits per week?",
    "Do you have events or social activities for members?",
    "Is there a minimum age requirement for membership?",
    "What are the cancellation policies for classes?",
    "Can I book private lessons with a trainer?",
    "How do I sign up for a specific class or lesson?",
    "What qualifications do your trainers have?",
    "Are there any assessments before starting a training program?",
    "Can I choose the trainer for my sessions?",
    "Do you offer nutrition guidance with training programs?",
    "Are there group lessons available for beginners?",
    "Can I book lessons on a flexible schedule?",
    "Are there age-specific classes for children or seniors?",
    "What types of equipment are used in lessons?",
    "Do you offer virtual lessons or training sessions?",
    "What is the duration of a typical training session?",
    "Can I request a trial lesson before committing?",
    "Are there any prerequisites for joining advanced lessons?",
    "Do you provide training programs for specific sports?",
    "How often are lesson schedules updated?",
    "Is there a dress code for lessons?",
    "Can I track my progress and goals with lessons?",
    "What safety measures are in place during lessons?",
    "Do you offer specialized lessons for weight loss?",
    "Can I switch between different lessons or programs?",
    "Are there any additional costs for lesson materials?",
    "What is your policy on missed lessons?",
    "Do you provide training for specific fitness goals (e.g., muscle gain, endurance)?",
    "How do I cancel or reschedule a lesson?",
    "What types of lessons are suitable for beginners?",
    "Do you have certified nutritionists on staff?",
    "Can I get a personalized nutrition plan with my membership?",
    "Are there cooking classes or workshops on nutrition?",
    "Do you provide guidance on dietary supplements?",
    "Is nutritional counseling included in personal training packages?",
    "Can I schedule a consultation with a nutrition expert?",
    "Do you offer meal planning services?",
    "Are there any discounts on nutrition services for members?",
    "Can I attend workshops on healthy eating habits?",
    "Is there a separate fee for nutritional consultations?",
    "Can I get assistance with dietary restrictions or allergies?",
    "Are nutrition seminars included in the membership?",
    "Do you offer guidance on post-workout nutrition?",
    "Can I request a personalized diet analysis?",
    "Are there special programs for weight management?",
    "Can I get recipes or meal ideas from your nutrition experts?",
    "Do you provide guidance on maintaining a balanced diet?",
    "Are there resources available for vegetarian or vegan diets?",
    "Can I get assistance with creating a grocery shopping list?",
    "Is there a helpline or support for nutritional queries?",
    "Do you organize events or challenges related to nutrition?",
    "Can I access nutritional resources online?",
    "How do I join your fitness community?",
    "Are there social events or meetups for members?",
    "Can I connect with other members through your platform?",
    "What online platforms do you use for member communication?",
    "Is there a members-only forum or community board?",
    "Do you have a mobile app for member interactions?",
    "Can I participate in challenges or competitions with other members?",
    "Are there networking opportunities within the fitness community?",
    "Do you organize group outings or activities for members?",
    "Is there a newsletter or email updates for members?",
    "Can I share my fitness achievements with the community?",
    "How do I access resources for members (e.g., guides, videos)?",
    "Are there recognition programs for member achievements?",
    "Can I contribute content or articles to the fitness community?",
    "What social media platforms does the gym use?",
    "Do you feature member success stories on your website?",
    "Are there any member-exclusive discounts with local businesses?",
    "Can I volunteer for community events organized by the gym?",
    "Is there a mentorship program for new members?",
    "Do you have a loyalty program for long-term members?",
    "Can I suggest new classes or programs to the fitness community?",
    "Are there any virtual events or webinars for members?",
    "How can I connect with trainers or instructors outside of lessons?",
    "Do you organize charity events or fundraisers for the community?",
    "Can I share my fitness journey on your social media channels?",
    "What initiatives do you have for a more sustainable fitness community?",
    "Are there any online challenges or contests for members?",
    "How do I provide feedback or suggestions to improve the fitness community?",
    "Can I participate in virtual group workouts with other members?",
    "Are there any themed events or parties for members?",
    "Do you have a buddy system for members to support each other?",
    "How do I access workout plans or routines shared by other members?",
    "Can I create or join fitness challenges with other members?",
    "Are there educational resources available for members (e.g., workshops)?",
    "Do you offer virtual workshops or seminars for members?",
    "Can I attend live Q&A sessions with fitness experts in the community?",
    "What resources are available for members seeking mental health support?",
    "Are there forums or groups for members with specific fitness goals?",
    "How do I share my fitness journey with the larger fitness community?",
    "Can I participate in virtual wellness events with other members?",
    "Do you organize online team-building activities for members?"
]

def generate_insert_query_inquiry(inquiry_id, entry):
    # Replace single quotes with two single quotes in each entry
    entry = [value.replace("'", "''") if isinstance(value, str) else value for value in entry]
    return f"INSERT INTO new_customer_inquiry VALUES({inquiry_id}, '{entry[0]}', '{entry[1]}', '{entry[2]}', '{entry[3]}', {entry[4] if entry[4] is not None else ''}, '{entry[5]}');\n"

def generate_random_inquiry(inquiry_id):
    # Randomly select an inquiry message from the sample list
    inquiry_message_entry = random.choice(sample_inquiries)

    # Generate other random fields
    first_name_entry = Faker().first_name()
    last_name_entry = Faker().last_name()
    email_entry = Faker().email()
    phone_entry = Faker().numerify('###-###-####')

    # Generate a member ID between 1 and 5000
    include_member_id = random.choice([True, False])
    member_id_entry = random.randint(1, 5000) if include_member_id else None

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
