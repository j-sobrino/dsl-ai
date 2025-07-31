import pdfplumber
import openai
import os
import json
import re

from dotenv import load_dotenv

load_dotenv()  # This loads variables from .env into environment



# 🔐 Set your OpenAI API key here
openai.api_key = os.environ["OPENAI_API_KEY"]

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        return "\n".join(
            page.extract_text() for page in pdf.pages if page.extract_text()
        )

def query_openai_with_contract_text(contract_text):
    prompt = f"""
You are a loan agreement analyzer. Extract the following fields from this contract:
- loan_amount
- monthly_payment
- term_months
- total_payable
- interest_rate
- APR

Return only the result as valid JSON.

Contract text:
{contract_text}
"""
    client = openai.OpenAI(
        api_key=os.getenv("OPENAI_API_KEY")
    )

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role": "system", "content": "You extract structured loan values from UK credit contracts."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=200
    )

    # Parse the response to extract JSON
    response_text = response.choices[0].message.content
    return extract_json_from_gpt_response(response_text)

def extract_json_from_gpt_response(response_text):
    # Use regex to find the JSON block
    match = re.search(r"\{[\s\S]*\}", response_text)
    if match:
        json_str = match.group(0)
        try:
            return json.loads(json_str)
        except json.JSONDecodeError:
            return None
    return None

def main():
    pdf_path = "RELLENO-personal-loans-sample-agreement.pdf"
    contract_text = extract_text_from_pdf(pdf_path)
    result = query_openai_with_contract_text(contract_text)
    parsed_result = extract_json_from_gpt_response(result)
    print(parsed_result)

if __name__ == "__main__":
    main()