import requests
import os
from prompts import BULLET_OPTIMIZER_PROMPT, COVER_LETTER_PROMPT
from prompts import MATCH_SCORE_PROMPT, FEEDBACK_PROMPT


from dotenv import load_dotenv

load_dotenv()
PPLX_API_KEY = os.getenv("PPLX_API_KEY")
PPLX_API_URL = "https://api.perplexity.ai/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {PPLX_API_KEY}",
    "Content-Type": "application/json"
}

MODEL = "sonar-pro"  # Make sure this matches your API access

def query_perplexity(prompt):
    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
        "top_p": 1,
    }

    response = requests.post(PPLX_API_URL, headers=HEADERS, json=payload)
    response.raise_for_status()

    return response.json()['choices'][0]['message']['content']


def generate_resume_bullets(resume_text, job_description):
    prompt = BULLET_OPTIMIZER_PROMPT.format(
        job_description=job_description,
        resume_text=resume_text
    )
    return query_perplexity(prompt)


def generate_cover_letter(resume_text, job_description):
    prompt = COVER_LETTER_PROMPT.format(
        job_description=job_description,
        resume_text=resume_text
    )
    return query_perplexity(prompt)

def generate_match_score(resume_text, job_description):
    prompt = MATCH_SCORE_PROMPT.format(
        job_description=job_description,
        resume_text=resume_text
    )
    return query_perplexity(prompt)

def get_feedback_prompt(resume_text):
    return FEEDBACK_PROMPT.format(resume_text=resume_text)
