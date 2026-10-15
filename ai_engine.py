from openai import OpenAI, APIConnectionError

client = OpenAI()

def analyse_job(job_description):
    try:
        response = client.responses.create(
        model="gpt-4.1-mini",
        input=f"List only the required technical skills from this job description, separated by commas. Do not add explanations or numbering:\n\n{job_description}"
    )
    except APIConnectionError:
        print("Unable to connect to OpenAI. Please check your internet connection.")
        raise

    skills = [skill.strip().lower() for skill in response.output_text.split(",")]
    return skills

def generate_learning_plan(skill):
    try:
        response = client.responses.create(
        model="gpt-4.1-mini",
        input=f"Create a beginner-friendly, 5-step learning plan for {skill}. Keep each step short and practical."
    )
    except APIConnectionError:
        print("Unable to connect to OpenAI while generating the learning plan.")
        raise
    learning_plan = response.output_text.replace("**", "")
    return learning_plan