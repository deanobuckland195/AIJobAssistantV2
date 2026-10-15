from ai_engine import analyse_job

job_description = "We are looking for a Junior Python Developer with experience in Python, SQL, Git and APIs."

result = analyse_job(job_description)
print("Job Description:", job_description)
print(result)
