# Agent-as-Coder
Project Overview

This project implements a coding agent that automatically generates custom parsers for bank statement PDFs. The agent uses Google Gemini AI to write Python parsers that extract data from PDFs and return a structured pandas DataFrame.

Goal:

Develop an AI-driven parser generator for bank statements.

Support automated testing and self-fixing of generated parsers.

Features

AI-Generated Parsers: Automatically creates a parser for a specified bank.

Self-Fixing Loop: Re-generates parser code if initial tests fail.

Automated Testing: Uses pytest to validate parser correctness.

CSV Output: Converts PDFs to pandas DataFrames matching bank-specific schema.

Folder Structure

project-root/
│
├─ custom_parsers/        # Generated parser files
│   └─ icici_parser.py
├─ data/                  # Sample CSV files for testing
│   └─ icici/
│       └─ sample_icici.csv
├─ test_icici_parser.py   # Pytest test cases
├─ agent.py               # Main agent script
├─ apikey.txt             # Your Google Gemini API key
├─ .env                   # Environment variables (GOOGLE_API_KEY)
└─ README.md


Installation

Clone the repository:

git clone <repository-link>
cd <project-folder>


Create a virtual environment (optional but recommended):

python -m venv aiagent
aiagent\Scripts\activate   # Windows


Install dependencies:

pip install -r requirements.txt
(Dependencies include: pandas, pytest, python-dotenv, google-generativeai, pdfplumber or PyPDF2)

Setup

Add your Google Gemini API key:

Create apikey.txt  file in the root directory:

add and save api key in apikey.txt (agent.py reads it automatically).

Place sample bank statement CSVs in the data/<bank_name>/ folder.

Usage

Run the agent to generate a parser:

python agent.py --target icici


This will create custom_parsers/icici_parser.py.

The agent will attempt up to 3 self-fix iterations if tests fail.

Run tests to validate parser functionality:

pytest

Testing

test_icici_parser.py contains 3 main tests:

Parser returns a pandas DataFrame.

DataFrame is not empty.

DataFrame contains expected columns.

Notes

The agent can be extended to other banks by adding the respective sample CSVs.

Ensure your API key has access to Google Gemini.

Place test CSVs in the correct data/<bank_name>/ folder before running tests.
