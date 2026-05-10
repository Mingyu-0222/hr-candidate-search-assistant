# server.py

import os
import json
import requests
from flask import Flask, request, jsonify, send_from_directory
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

app = Flask(__name__, static_folder=".", static_url_path="")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-5.2")

client = OpenAI(api_key=OPENAI_API_KEY)


@app.route("/")
def home():
    return send_from_directory(".", "index.html")


@app.route("/api/research", methods=["POST"])
def research_candidate():
    data = request.get_json() or {}

    candidate_name = data.get("candidate_name", "").strip()
    context = data.get("context", "").strip()
    target_role = data.get("target_role", "").strip()

    if not candidate_name:
        return jsonify({
            "error": "Candidate name is required."
        }), 400

    if not OPENAI_API_KEY:
        return jsonify({
            "error": "OPENAI_API_KEY is missing. Please add it to your .env file."
        }), 500

    if not SERPAPI_API_KEY:
        return jsonify({
            "error": "SERPAPI_API_KEY is missing. Please add it to your .env file."
        }), 500

    try:
        search_results = search_public_web(candidate_name, context)
        summary = summarize_with_llm(candidate_name, context, target_role, search_results)

        return jsonify({
            "candidate_name": candidate_name,
            "context": context,
            "target_role": target_role,
            "search_results": search_results,
            "summary": summary
        })

    except Exception as error:
        return jsonify({
            "error": str(error)
        }), 500


def search_public_web(candidate_name, context):
    query_parts = [candidate_name]

    if context:
        query_parts.append(context)

    query_parts.append("professional background LinkedIn GitHub portfolio university company")

    query = " ".join(query_parts)

    url = "https://serpapi.com/search"

    params = {
        "engine": "google",
        "q": query,
        "api_key": SERPAPI_API_KEY,
        "hl": "en",
        "gl": "us",
        "num": 8
    }

    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()

    data = response.json()
    organic_results = data.get("organic_results", [])

    cleaned_results = []

    for item in organic_results[:8]:
        title = item.get("title", "")
        link = item.get("link", "")
        snippet = item.get("snippet", "")

        if not title and not snippet:
            continue

        cleaned_results.append({
            "title": title,
            "link": link,
            "snippet": snippet
        })

    return cleaned_results


def summarize_with_llm(candidate_name, context, target_role, search_results):
    search_text = json.dumps(search_results, indent=2, ensure_ascii=False)

    prompt = f"""
You are helping an HR recruiter research publicly available professional information about a candidate.

Candidate name:
{candidate_name}

Optional context:
{context if context else "No extra context provided"}

Target role:
{target_role if target_role else "No target role provided"}

Public search results:
{search_text}

Your task:
Create a structured HR friendly candidate research profile based only on the provided search results.

Important rules:
1. Use only the information in the search results.
2. Do not invent facts.
3. If information is uncertain, clearly label it as uncertain.
4. If the search results may refer to multiple people with the same name, clearly warn the recruiter.
5. Focus on public professional information only.
6. Do not include private information, sensitive personal information, home address, private phone number, or private email.
7. Do not make a final hiring decision.
8. Include source links for verification.

Return the answer using this exact structure:

Candidate Overview
Possible Education
Possible Work Experience
Public Skills and Strengths
Public Projects or Portfolio Evidence
Role Fit Notes
Uncertainty and Verification Notes
Suggested Interview Questions
Source Links
Human Review Reminder
"""

    response = client.responses.create(
        model=OPENAI_MODEL,
        input=prompt
    )

    return response.output_text


if __name__ == "__main__":
    app.run(debug=True, port=5000)
