from datetime import datetime
from ai_engine import analyse_job, generate_learning_plan
from openai import APIConnectionError
from skill_matching import calculate_weighted_match

def greet_user():
    print("Welcome to the AI Job Assistant!")
    name = input("What is your name? ")
    print(f"\nWelcome, {name}!")

greet_user()

def get_user_skills():
    skills = input("\nEnter your current skills, separated by commas: ")
    skill_list = skills.split(",")
    return skill_list

skill_list = get_user_skills()

def show_skills(skill_list):
    print("\nYour current skills are:")

    for skill in skill_list:
        print(f"- {skill.strip()}")

show_skills(skill_list)

print("=== AI Job & Apprenticeship Assistant ===")

print("Let's find out which skills you have.")

def check_skills(user_skills, required_skills):
    matching_skills = []
    missing_skills = []

    for skill in required_skills:
        if skill in user_skills:
            matching_skills.append(skill)
        else:
            missing_skills.append(skill)
    return matching_skills, missing_skills

required_skills = [
    "python",
    "git",
    "sql",
    "apis",
    "machine learning",
    "javascript",
    "html",
    "css",
    "excel",
    "data analysis",
    "communication",
    "customer service"
]

skill_aliases = {
    "ml": "machine learning",
    "rest api": "apis",
    "rest api development": "apis",
    "api": "apis",
    "postgresql": "sql",
    "js": "javascript",
    "ms excel": "excel",
    "spreadsheets": "excel",
    "data analytics": "data analysis",
    "customer support": "customer service",
    "customer care": "customer service"
}

skill_weights = {
    "python": 5,
    "machine learning": 5,
    "sql": 4,
    "apis": 4,
    "git": 3,
    "docker": 2
}

user_skills = []

for skill in skill_list:
    clean_skill = skill.strip().lower()
    standard_skill = skill_aliases.get(clean_skill, clean_skill)
    user_skills.append(standard_skill)

matching_skills, missing_skills = check_skills(user_skills, required_skills)

print("\n=== AI Developer Skill Check ===")

print("\nSkills you already have:")
for skill in matching_skills:
    print(f"✓ {skill}")

print("\nSkills you should learn:")
for skill in missing_skills:
    print(f"- {skill}")

def calculate_match(matching_skills, required_skills):
    match_percentage = (len(matching_skills) / len(required_skills)) * 100
    return match_percentage
match_percentage = calculate_match(matching_skills, required_skills)

print(f"\nAI Developer Match Score: {match_percentage:.0f}%")

if match_percentage >= 80:
    print("Excellent match! You are well prepared for this role.")
elif match_percentage >= 60:
    print("Good match! You have a strong foundation.")
elif match_percentage >= 40:
    print("You're making progress. Keep developing your missing skills.")
else:
    print("You're at the beginning. Focus on building the core skills first.")


def match_job_skills(user_skills, detected_skills):
    job_matching_skills = []
    job_missing_skills = []

    for skill in detected_skills:
        if skill in user_skills:
            job_matching_skills.append(skill)
        else:
            job_missing_skills.append(skill)
    return job_matching_skills, job_missing_skills


answer = "yes"

while answer == "yes":

    print("\n=== AI Job Description Analyser ===")

    job_description = input("\nPaste a job description here: ")

    if not job_description.strip():
        print("Please enter a job description before continuing.")
        continue

    print("\nJob description received:")
    print(job_description)
    print("\n=== AI Job Analysis ===")
    try:
        ai_skills = analyse_job(job_description)
    except APIConnectionError:
        print("Job analysis failed. Please try again.")
        continue

    detected_skills = []

    for skill in ai_skills:
        clean_skill = skill.strip().lower()
        standard_skill = skill_aliases.get(clean_skill, clean_skill)
        detected_skills.append(standard_skill)

    print("\n=== Skills Detected in Job Description ===")


    for skill in detected_skills:
        print(f"- {skill}")

    job_matching_skills, job_missing_skills = match_job_skills(user_skills, detected_skills)

    print("\n=== Your Match Against This Job ===")

    print("\nSkills you match:")
    for skill in job_matching_skills:
        print(f"✓ {skill}")

    print("\nSkills you're missing:")

    if len(job_missing_skills) > 0:
        for skill in job_missing_skills:
            print(f"- {skill}")
    else:
        print("No missing skills!")

    job_match_percentage = calculate_weighted_match(
        detected_skills,
        job_matching_skills,
        skill_weights
    )

    print(f"\nJob Match Score: {job_match_percentage:.0f}%")

    if job_match_percentage >= 80:
        print("Recommendation: Excellent match - you should apply!")
    elif job_match_percentage >= 60:
        print("Recommendation: Good match - definitely consider applying.")
    elif job_match_percentage >= 40:
        print("Recommendation: Possible match - work on the missing skills.")
    elif len(detected_skills) == 0:
        print("Recommendation: No technical skills detected - unable to calculate a meaningful match score.")
    else:
        print("Recommendation: Low match - build more of the required skills first.")

    print("\n=== Your Personalised Learning Roadmap ===")

    ai_learning_plans = {}

    if len(detected_skills) == 0:
        print("No recognised technical skills were found in this job description.")
    elif len(job_missing_skills) == 0:
        print("Congratulations! You already have all the detected skills for this job!")

    else:
        for skill in job_missing_skills:
            print(f"\n{skill.upper()} Learning Plan:")

            try:
                learning_plan = generate_learning_plan(skill)
            except APIConnectionError:
                learning_plan = "Learning plan unavailable. Please check your connection and try again."

            ai_learning_plans[skill] = learning_plan
            print(learning_plan)

    analysis_time = datetime.now()

    try:
        with open("job_analysis.txt", "r", encoding="utf-8") as file:
            report_count = file.read().count("AI Job Assistant - Job Analysis Report")
    except FileNotFoundError:
        report_count = 0

    report_number = report_count + 1

    try:
        with open("job_analysis.txt", "a", encoding="utf-8") as file:
            file.write("\n" + "=" * 50 + "\n")
            file.write(f"AI Job Assistant - Job Analysis Report #{report_number}\n")
            file.write(f"Date: {analysis_time.strftime('%d %B %Y')}\n")
            file.write(f"Time: {analysis_time.strftime('%H:%M')}\n")
            file.write(f"Job Match Score: {job_match_percentage:.0f}%\n")

            file.write("\nMatching Skills:\n")
            for skill in job_matching_skills:
                file.write(f"- {skill}\n")

            file.write("\nMissing Skills:\n")
            for skill in job_missing_skills:
                file.write(f"- {skill}\n")

            file.write("\n=== Personalised Learning Roadmap ===\n")

            if not detected_skills:
                file.write("No recognised technical skills were found in this job description.\n")

            elif not job_missing_skills:
                file.write("You already have all the detected skills!\n")

            else:
                for skill in job_missing_skills:
                    file.write(f"\n{skill.upper()} Learning Plan:\n")
                    file.write(ai_learning_plans[skill] + "\n")

    except OSError:
        print("Unable to save your job analysis. Please check the file location or permissions.")

    else:
        print("Your job analysis has been saved!")

    answer = input("\nWould you like to analyse another job? (yes/no): ").strip().lower()












