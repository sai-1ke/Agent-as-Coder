import argparse
import subprocess
from pathlib import Path
import google.generativeai as genai # type: ignore
from dotenv import load_dotenv # type: ignore
import os

# Load API key
load_dotenv() 

with open("apikey.txt", "r") as f:
    api_key = f.read().strip()

# Configure API key
genai.configure(api_key=api_key)

def run_tests():
    """Run pytest and capture results"""
    result = subprocess.run(["pytest"], capture_output=True, text=True)
    return result.returncode, result.stdout

def ask_gemini(prompt: str) -> str:
    """Send prompt to Gemini and return response"""
    model = genai.GenerativeModel("gemini-2.5-flash-lite")
    response = model.generate_content(prompt)
    return response.text

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", required=True, help="Bank name, e.g., icici")
    args = parser.parse_args()

    target = args.target.lower()
    output_file = Path(f"custom_parsers/{target}_parser.py")
    output_file.parent.mkdir(parents=True, exist_ok=True)  # create folder if missing

    # Initial parser code prompt
    prompt = f"""
You are an AI agent. Write Python code for a parser:
Function: parse(pdf_path: str) -> pd.DataFrame
Bank: {target}
Input: bank statement PDF
Output: DataFrame matching schema of provided CSV (in data/{target}/)
Use PyPDF2 or pdfplumber to extract text.
"""
    # Generate initial parser
    parser_code = ask_gemini(prompt)
    output_file.write_text(parser_code, encoding="utf-8")

    # Try up to 3 attempts with self-fix loop
    for attempt in range(3):
        code, logs = run_tests()
        if code == 0:
            print("✅ Parser works!")
            break
        else:
            print(f"❌ Attempt {attempt+1} failed, retrying...")
            # Use only last 10 lines of logs
            log_summary = "\n".join(logs.splitlines()[-10:])
            fix_prompt = f"""
The parser failed with pytest. Here are the last 10 lines of logs:
{log_summary}

Please fix the code. Current code:
{output_file.read_text(encoding="utf-8")}
"""
            fixed_code = ask_gemini(fix_prompt)
            output_file.write_text(fixed_code, encoding="utf-8")

if __name__ == "__main__":
    main()
