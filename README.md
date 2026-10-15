# AI Job Assistant V2

An AI-powered Python application that helps job seekers compare their skills against job descriptions, identify missing skills, and create personalised learning plans.

Built as a portfolio project while learning Python, AI integration, and software engineering.

## Features

- **AI Job Analysis:** Uses OpenAI to identify technical skills mentioned in job descriptions.
- **Skill Matching:** Compares the job seeker's skills against the detected requirements.
- **Weighted Match Score:** Calculates a percentage based on the importance of different skills.
- **Skill Standardisation:** Recognises alternative skill names such as `api`, `rest api`, and `apis`.
- **Personalised Learning Plans:** Uses AI to generate practical learning steps for missing skills.
- **Saved Reports:** Saves job analysis results and learning plans to a text file.
- **Error Handling:** Handles OpenAI connection problems and report-saving failures.
- **Automated Testing:** Includes seven pytest tests.

## Technologies Used

- Python
- OpenAI API
- Pytest
- Git and GitHub
- PyCharm

## How It Works

1. The user enters their name and existing skills.
2. The application displays an initial AI Developer skill assessment.
3. The user copies a job description from a job advertisement.
4. OpenAI identifies the technical skills mentioned in the description.
5. The application compares those skills against the user's existing skills.
6. A weighted job-match percentage is calculated.
7. If skills are missing, OpenAI generates personalised learning plans.
8. The results are saved to `job_analysis.txt`.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/AIJobAssistantV2.git
cd AIJobAssistantV2
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

Activate it on macOS or Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your OpenAI API key

Create an environment variable named `OPENAI_API_KEY`.

For example, on macOS or Linux:

```bash
export OPENAI_API_KEY="your-api-key-here"
```

Never share or commit your actual API key.

### 5. Run the application

```bash
python main.py
```

## Running Automated Tests

Run the tests using:

```bash
python -m pytest tests/
```

The automated tests use simulated API responses, so they do not require real OpenAI requests.

## Current Limitations

- Job descriptions must be pasted manually.
- The application runs in the terminal rather than a graphical interface.
- Skill matching uses predefined weights and skill aliases.
- AI-generated results may occasionally miss or misinterpret requirements.
- The match score is an estimate, not a guarantee of employment suitability.

## Future Improvements

Ideas for a future V3 include:

- Analyse CVs uploaded as PDF files.
- Retrieve real job vacancies from external job feeds.
- Add a graphical user interface.
- Improve skill matching and recommendations.
- Allow users to compare multiple job opportunities.

## Project Purpose

I built AI Job Assistant V2 to develop my Python and AI software engineering skills through a practical project.

The project demonstrates API integration, problem-solving, modular programming, error handling, automated testing, and working with AI-generated information.