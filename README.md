# HR Candidate Search Assistant

## Project Overview

This project is a small GenAI style web app designed for a narrow HR workflow: first round candidate screening.

The user is an HR recruiter or hiring manager. In a normal recruiting process, HR often needs to open many resumes, read each one manually, identify the candidate's education, skills, experience, and then decide whether the candidate should move forward. This process takes time and can be inconsistent, especially when different candidates use different resume formats.

My app helps the recruiter search a candidate by name and quickly see a structured candidate profile. The app also generates a screening summary, role fit explanation, key strengths, potential concerns, and suggested interview questions.

The goal is to save HR time, reduce repeated resume reading, and help recruiters prepare better first round interviews.

## Context, User, and Problem

The main user is an HR recruiter who needs to review candidates during the first screening stage.

The workflow I am improving is candidate profile review. In the current workflow, the recruiter usually opens a resume, reads the full document, highlights important information, and writes notes about whether the candidate fits the role. This can be slow because resume information is often unstructured.

For example, one resume may emphasize education, another may emphasize projects, and another may emphasize work experience. Even when candidates have similar skills, the recruiter still needs to manually compare them.

This problem matters because first round screening affects both the company and the candidate. For the company, slow screening can delay hiring. For the candidate, slow screening can delay feedback. A structured assistant can help HR understand each candidate faster and more consistently.

This project focuses on one specific task: helping HR search one candidate by name and review that candidate's profile for a selected target role.

## Solution and Design

I built a simple HTML web app called HR Candidate Search Assistant.

The app allows the user to enter a candidate name and select a target role. After clicking the search button, the app searches a small built in candidate dataset. If the candidate is found, the app displays the candidate profile and generates a structured screening summary.

The app output includes the following sections:

Candidate profile

Education

Target career area

Experience summary

Projects

Key skills

Candidate overview

Role fit

Key strengths

Potential concerns

Suggested interview questions

Human review reminder

The app is intentionally simple. It is designed to show the business workflow clearly instead of building a large recruiting system.

## App Logic

The app follows a clear step by step workflow.

Step 1: The user enters a candidate name

The recruiter types a candidate name into the search box. For example, the recruiter can type Mingyu Wang.

Step 2: The user selects a target role

The recruiter selects a role from the dropdown menu. Example roles include Business Analyst Intern, Data Analyst Intern, Marketing Analyst Intern, AI Strategy Analyst Intern, and Operations Analyst Intern.

Step 3: The app searches the candidate dataset

The candidate dataset is stored inside the JavaScript code as structured objects. Each candidate record includes name, education, skills, experience, projects, target career area, and resume style text.

The search function converts the user input to lowercase and compares it with the candidate names in the dataset. This allows partial name search. For example, typing Mingyu can still find Mingyu Wang.

Step 4: The app checks whether a match exists

If the app finds a matching candidate, it continues to the summary generation step.

If the app does not find a matching candidate, it shows a message saying that no matching candidate was found. This helps the user check spelling or try another name.

Step 5: The app displays the candidate profile

After finding the candidate, the app shows a structured profile card. This card includes the candidate's education, experience, projects, target career area, and key skills.

This profile section works as the baseline information view. It gives the recruiter the original structured information before reading the AI style summary.

Step 6: The app generates an AI style screening summary

The app uses a function called generateAISummary. This function takes two inputs: the selected candidate and the target role.

The function reads the candidate's skills, experience, and target career area. Then it creates a structured screening summary with candidate overview, role fit, strengths, concerns, and interview questions.

The current version uses rule based logic to simulate a GenAI workflow. It demonstrates how a real LLM based version would organize resume information into a recruiter friendly summary. In a production version, this summary generation step could be connected to an LLM API through a secure backend.

Step 7: The app reminds the recruiter to keep human review

The final output includes a human review reminder. This is important because the app should support HR screening, while the final hiring decision should still be made by a human recruiter.

## Key Design Choices

The first design choice is to keep the workflow narrow. This app only focuses on searching and summarizing one candidate profile. It does not try to manage the full hiring process.

The second design choice is to use structured output. Instead of giving one long paragraph, the app separates the result into profile, role fit, strengths, concerns, and interview questions. This makes the result easier for HR to use.

The third design choice is to include a baseline comparison. The candidate profile card represents the simpler baseline because it only displays the candidate information. The AI style summary adds interpretation and interview support.

The fourth design choice is to include human review. Since hiring decisions can affect people's careers, the app should not be used as a final decision maker. It is a screening assistant that helps HR prepare.

## Why GenAI Is Useful

This task is useful for GenAI because resume screening is more than keyword search. HR needs to understand a candidate's overall background, connect skills to a target role, summarize project experience, and prepare interview questions.

A simple keyword search can show whether a candidate has Python, SQL, or Excel. However, it does not explain how those skills relate to a role. It also does not help the recruiter ask better follow up questions.

A GenAI workflow can turn unstructured candidate information into a consistent summary. It can also help HR identify strengths, possible concerns, and useful interview questions.

## Evaluation and Results

I evaluated the project by comparing two approaches.

The baseline approach is simple candidate search and raw profile display. In this approach, the recruiter can find the candidate and read the profile, but the recruiter still needs to interpret the information manually.

The GenAI style approach searches the candidate and generates a structured screening summary. This helps the recruiter understand the candidate faster and prepare for the interview.

I tested the app with five synthetic candidate profiles:

Mingyu Wang, a candidate with analytics and business analysis experience

Alex Chen, a candidate with software engineering experience

Maria Lopez, a candidate with marketing analytics experience

David Kim, a candidate with operations and supply chain experience

Priya Patel, a candidate with information systems and product analysis experience

I used the following rubric to judge the output:

Accuracy: whether the summary matches the candidate profile

Completeness: whether the output includes education, skills, experience, projects, and role fit

Usefulness: whether the recruiter can quickly understand the candidate

Interview support: whether the generated questions are useful for a first round interview

Human review risk: whether the output could miss details or overstate the candidate's fit

The GenAI style version was more useful than the baseline because it created a consistent screening format. The recruiter did not need to read the entire profile first to understand the candidate's background. The app also helped generate interview questions, which the baseline did not provide.

The main limitation is that the current version uses rule based logic instead of a live LLM API. This makes the app easier to run and safer for a class demo, but the summary is less flexible than a true LLM generated output. Another limitation is that the tool can miss details or make the candidate sound stronger than the original profile. Because of this, HR should always review the original resume before making a final decision.

## What Worked

The app successfully allows a recruiter to search a candidate by name.

The app shows a structured candidate profile.

The app generates a readable screening summary.

The app provides role fit explanation, strengths, concerns, and interview questions.

The app clearly shows how the workflow can save time during first round resume screening.

## What Failed or Needs Improvement

The app currently uses a small synthetic dataset. A real HR system would need a larger and more secure data source.

The summary generation is rule based in this prototype. A stronger version would connect to an LLM through a backend.

The app does not upload or parse real PDF resumes yet.

The app does not rank multiple candidates for one role.

The app should not be used for final hiring decisions without human review.

## Artifact Snapshot

The project artifact is an HTML web app.

The user opens the app, enters a candidate name, selects a target role, and clicks Search Candidate.

Example input:

Candidate Name: Mingyu Wang

Target Role: Business Analyst Intern

Example output:

The app displays Mingyu Wang's candidate profile, including education, skills, experience, projects, and target career area. It then generates an AI style screening summary with candidate overview, role fit, key strengths, potential concerns, suggested interview questions, and a human review reminder.

Screenshots can be added in the repository under a screenshots folder.

Suggested screenshots:

Homepage with search box

Search result for Mingyu Wang

AI Screening Summary output

## Setup and Usage Instructions

This project runs as a simple HTML app.

To use the app:

Download or clone this repository.

Open the project folder.

Find the file named index.html.

Double click index.html to open it in a browser.

Enter a candidate name, such as Mingyu Wang.

Select a target role.

Click Search Candidate.

The app will show the candidate profile and screening summary.

No API key is required for the current prototype.

## Repository Contents

index.html contains the full web app, including HTML, CSS, JavaScript, candidate data, search logic, and summary logic.

README.md explains the project context, design, evaluation, results, and usage instructions.

screenshots can contain screenshots of the app interface and sample output.

## Data and Privacy

This project uses synthetic candidate data for demonstration.

The repository should not include real private resumes, real phone numbers, real addresses, API keys, or sensitive personal information.

If this app is expanded in the future, candidate data should be stored securely and handled according to privacy and hiring compliance requirements.

## Future Improvements

A future version could connect the app to a secure backend and an LLM API.

A future version could allow HR to upload PDF resumes.

A future version could compare multiple candidates for the same target role.

A future version could include a stronger evaluation dataset and human recruiter feedback.

A future version could export the screening summary as a PDF or interview note.

## Conclusion

This project shows how a small GenAI workflow can support a real HR task. The app helps recruiters search a candidate by name, view a structured profile, and generate a first round screening summary. Compared with a simple profile display baseline, the GenAI style workflow gives the recruiter more organized and useful information. However, the tool should remain a decision support assistant, and human recruiters should review the original resume before making final hiring decisions.
