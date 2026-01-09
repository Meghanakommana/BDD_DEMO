# generate.py using Groq (Free + Updated!)
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
print("GROQ KEY LOADED:", os.getenv("GROQ_API_KEY"))

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_scenarios(requirement: str):
    prompt = f"""
    Convert the following requirement into exactly two BDD scenarios:
    1. One happy path
    2. One negative path
    Format strictly in Given/When/Then.
    Requirement: {requirement}
    """

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    content = (completion.choices[0].message.content or "").strip()
    blocks = [b for b in content.split("```") if "Given" in b]
    return blocks[:2]

if __name__ == "__main__":
    req = "A registered user should be able to log in with valid credentials and view their dashboard."
    scenarios = generate_scenarios(req)
    for s in scenarios:
        print(s)
        print("-----")
