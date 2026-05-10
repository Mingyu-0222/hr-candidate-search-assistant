# AI Candidate Web Research Assistant

## Project Overview

This project is a small GenAI app designed for an HR recruiting workflow.

The app helps an HR recruiter search public professional information about a candidate and turn scattered web results into a structured candidate research profile.

The user enters a candidate name, such as Mingyu Wang. In the demo version, the app shows a sample workflow and sample output. In the backend connected version, the app sends the candidate name to a Flask backend. The backend performs public web search, sends the search results to an LLM, and returns a structured HR research summary.

The goal of this project is to show how GenAI can help recruiters save time during early candidate research while still keeping human review involved.

## Context, User, and Problem

The target user is an HR recruiter or hiring manager.

Before a first round interview, recruiters often search a candidate online to understand their public professional background. They may look at public LinkedIn pages, GitHub pages, school pages, company pages, personal websites, portfolio pages, or public project pages.

The current workflow is manual. The recruiter searches the candidate name, opens multiple links, reads scattered information, and writes notes by hand. This takes time and can be inconsistent because different recruiters may focus on different details.

This project improves one narrow workflow:

An HR recruiter enters a candidate name and receives a structured candidate research profile based on public professional information.

This matters because faster candidate research can help companies move qualified candidates forward sooner. It can also help candidates receive faster responses during the hiring process.

## Solution and Design

This repository includes two versions of the app.

## Version 1: index.html

`index.html` is the static demo version.

It does not connect to a backend.

It does not perform live web search.

It is used to demonstrate the intended user experience, interface design, and output structure.

This version is useful for presentation because it clearly shows how the HR workflow should look. The recruiter enters a candidate name, and the page displays a structured candidate research profile.

## Version 2: index1.html

`index1.html` is the backend connected version.

This version is designed to work with `serve.py`.

The user enters a candidate name, optional context, and target role. The page sends this information to the Flask backend. The backend searches the public web and uses an LLM to generate a structured HR research summary.

This version shows the real GenAI workflow.

## Backend: serve.py

`serve.py` is the Flask backend.

The backend receives the candidate name from `index1.html`.

Then it performs three main steps.

Step 1: It receives candidate information from the frontend.

Step 2: It uses a public search API to search for public professional information.

Step 3: It sends the search results to an LLM and asks the LLM to organize the information into an HR friendly candidate research profile.

The backend returns the result to the frontend, and the frontend displays the summary and source links.

## App Logic

The full workflow has six main steps.

## Step 1: HR enters candidate information

The recruiter enters a candidate name, such as Mingyu Wang.

The recruiter can also enter optional context, such as school, company, location, or target role.

This optional context is important because many people can share the same name. Extra context helps the system search more accurately.

## Step 2: Frontend sends request to backend

In `index1.html`, the page sends the candidate name, context, and target role to the backend route in `serve.py`.

The static demo file `index.html` does not do this step. It only shows the workflow visually.

## Step 3: Backend searches public web results

The backend uses a search API to collect public web results.

The system focuses on public professional information, such as public profile pages, GitHub pages, university pages, company pages, portfolio pages, and public project pages.

The backend collects information such as page title, link, and snippet.

The app should not collect private information, hidden information, or information behind login pages.

## Step 4: Backend sends search results to LLM

After collecting search results, the backend sends them to an LLM.

The LLM is instructed to summarize only the information found in the search results.

The LLM is also instructed to avoid inventing facts.

If something is uncertain, the LLM should clearly mark it as uncertain.

## Step 5: LLM creates structured HR profile

The LLM returns a structured candidate research summary.

The output includes:

Candidate overview

Possible education background

Possible work experience

Public skills and strengths

Public projects or portfolio evidence

Role fit notes

Uncertainty and verification notes

Suggested interview questions

Source links

Human review reminder

## Step 6: Human recruiter verifies the result

The app is designed to support HR research. It is not designed to make final hiring decisions.

The recruiter should review the source links manually.

This is important because public search results may be incomplete, outdated, or about a different person with the same name.

## Why GenAI Is Useful

This task is useful for GenAI because candidate research is more than keyword search.

A search engine can return links, but the recruiter still needs to open pages, compare information, identify what is relevant, and write notes.

GenAI can help synthesize scattered public information into a consistent profile. It can also generate interview questions and highlight uncertainty.

The value of GenAI in this workflow is not replacing the recruiter. The value is helping the recruiter prepare faster and more consistently.

## Baseline Comparison

The baseline workflow is manual public web search.

In the baseline workflow, the recruiter searches the candidate name manually, opens multiple pages, reads each result, and writes notes by hand.

The GenAI workflow is faster because the recruiter enters the candidate name once and receives a structured first draft of the candidate research profile.

The baseline gives raw search results.

The GenAI version gives an organized summary with source links and verification notes.

## Evaluation and Results

I evaluated the project by comparing the app workflow with the manual search baseline.

The baseline approach was manual web search and manual note taking.

The app approach was candidate name input, public web search, LLM summary, and structured HR output.

I used the following evaluation criteria.

## Relevance

The output should focus on professional information that is useful for HR screening.

Examples include education, work experience, skills, projects, public profile pages, and portfolio evidence.

## Completeness

The output should include the main sections that a recruiter needs during first round candidate research.

These sections include candidate overview, possible education, possible work experience, skills, projects, source links, uncertainty notes, and interview questions.

## Usefulness

The output should help the recruiter understand the candidate faster than manual search.

The structure should make the candidate easier to review.

## Source Transparency

The output should include links so the recruiter can verify the information.

This is important because HR should not rely only on an AI summary.

## Risk Control

The output should clearly mention uncertainty.

If the search results may refer to multiple people with the same name, the system should warn the recruiter.

## Evaluation Findings

The demo version shows that the workflow is easy to understand and useful for presentation.

The backend connected version shows how the app could perform a real public web search and LLM summary process.

Compared with manual search, the GenAI workflow provides a clearer output format. It helps the recruiter review public candidate information faster and prepare interview questions more easily.

The main limitation is that the quality of the output depends on the search results. If the candidate has limited public information, the summary may be incomplete. If the candidate has a common name, the search results may include information about the wrong person.

Because of this, the app should always be used as a research assistant, not as a final decision tool.

## What Worked

The app clearly demonstrates a real HR research workflow.

The static demo version is easy to open and present.

The backend connected version shows a realistic technical design.

The output structure is useful for HR screening.

The app includes uncertainty notes and a human review reminder.

## What Needs Improvement

The backend version depends on external APIs.

The result quality depends on the search API results.

The app may confuse people with the same name.

The app needs stronger source filtering in a production version.

The app should eventually support better context input, such as school, company, target role, and location.

The app should not be used for final hiring decisions without human verification.

## Artifact Snapshot

The repository includes two HTML files.

`index.html` is the static demo. It shows the interface and sample output.

`index1.html` is the backend connected version. It sends the candidate search request to `serve.py`.

The app output includes a structured candidate research profile with overview, possible education, possible experience, skills, public project evidence, source links, uncertainty notes, and interview questions.

Suggested screenshots for the repository:

Homepage of `index.html`

Example output from `index.html`

Homepage of `index1.html`

Backend connected search result from `index1.html`

## Repository Contents

`README.md`

Explains the project context, solution design, app logic, evaluation, setup, and usage.

`index.html`

Static demo version of the app. This version is for showing the user interface and sample workflow.

`index1.html`

Backend connected version of the app. This version sends candidate information to the Flask backend.

`serve.py`

Flask backend. It handles the API request, calls the search API, calls the LLM API, and returns the candidate research summary.

`requirements.txt`

Python dependencies needed to run the backend.

`.env`

Local environment file for API keys. This file should not be uploaded to GitHub.

## Setup and Usage

## Option 1: Run the static demo

This is the easiest way to view the project.

1. Open the project folder.

2. Open `index.html` in a browser.

3. Enter a candidate name.

4. Review the sample candidate research output.

This version does not require an API key.

## Option 2: Run the Backend Connected Version

This version uses `index1.html` and `serve.py`.

### 1. Install dependencies

```text
pip install -r requirements.txt
2. Create a .env file

Create a file named .env in the project folder.

The .env file should include the required API keys:

OPENAI_API_KEY=your_openai_api_key_here
SERPAPI_API_KEY=your_serpapi_api_key_here
OPENAI_MODEL=gpt-5.2
3. Run the backend
python serve.py
4. Open the backend connected app

Open this link in your browser:

http://127.0.0.1:5000/index1.html
5. Use the app

Enter a candidate name, optional context, and target role.

Click the search button.

Review the AI generated candidate research summary and source links.

Important Security Note

The .env file should not be committed to GitHub.

API keys should be stored locally only.

For submission, the repository should include an example environment file, such as .env.example, instead of the real .env file.

If a real .env file was uploaded by mistake, it should be removed from the repository and the API keys should be rotated.

Data and Privacy

This project is designed to use public professional information only.

The app should not collect private phone numbers, home addresses, private emails, sensitive personal information, or information from private accounts.

The app should only summarize public professional information and should provide source links for human verification.

Responsible Use

This app is a research assistant for HR recruiters.

It should not make final hiring decisions.

It should not be used to automatically reject or accept candidates.

The recruiter should verify all source links manually.

The recruiter should be careful when the candidate has a common name.

The recruiter should use the output as a first draft, not as a final truth.

Future Improvements

A future version could improve source filtering.

A future version could allow users to add more search context.

A future version could separate results by source type.

A future version could detect possible same name confusion more clearly.

A future version could export the research summary as a PDF.

A future version could compare the app output with human recruiter notes.

A future version could include a stronger evaluation dataset.

Conclusion

This project demonstrates how a small GenAI workflow can support HR candidate research.

The static demo version shows the user experience and output design.

The backend connected version shows how the app can connect public web search with LLM summarization.

Compared with manual web search, this workflow can help recruiters save time, create more consistent research notes, and prepare better interview questions.

However, the tool should remain a human support tool. Recruiters should verify the source links and make final decisions themselves.
