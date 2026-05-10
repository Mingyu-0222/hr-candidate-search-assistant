# AI Candidate Web Research Assistant

## Project Overview

This project is a small front end demo of a GenAI powered candidate web research assistant for HR recruiters.

The intended user is an HR recruiter or hiring manager who wants to quickly understand a candidate before a first round screening conversation. In a normal hiring workflow, recruiters often search a candidate name online, open several public pages, read LinkedIn profiles, GitHub pages, school pages, company pages, personal websites, or portfolio pages, and then write notes by hand.

This process can take time because public information is scattered across many sources. It can also be inconsistent because different recruiters may focus on different details.

This project demonstrates a more structured workflow. The recruiter enters a candidate name, such as Mingyu Wang, and the app shows what an AI generated candidate research profile could look like after collecting and summarizing public professional information.

The current version is an HTML demo. It does not perform live web search. It shows the intended user experience, interface design, output format, and business logic. A full version would connect the HTML interface to a secure backend, a public web search API, and an LLM API.

## Context, User, and Problem

The user for this project is an HR recruiter who needs to research candidates during the early screening stage.

The workflow I am improving is public candidate research. Before interviewing a candidate, recruiters often want to understand the candidate's public professional background. They may search the candidate's name online, check public profiles, review project pages, and look for evidence of skills or experience.

The problem is that this research process is repetitive and time consuming. A recruiter may need to open multiple pages, compare information, decide what is relevant, and write a short candidate summary manually.

This matters because early candidate research affects both the company and the candidate. For the company, faster research can help recruiters move qualified candidates forward sooner. For the candidate, faster research can improve response time and reduce delays in the hiring process.

This project focuses on one narrow use case:

An HR recruiter enters a candidate name and receives a structured research summary based on publicly available professional information.

## Solution and Design

I built a simple HTML based demo app called AI Candidate Web Research Assistant.

The app allows the user to enter a candidate name and optional context. The optional context can include school, company, target role, or location. This helps reduce confusion when different people have the same name.

The current HTML demo simulates the output of a GenAI powered web research workflow. It shows how the final system would organize candidate information after public web search and LLM summarization.

The output includes:

Candidate overview

Possible education background

Possible work experience

Publicly visible skills

Public projects or portfolio evidence

Source links or source placeholders

Uncertainty notes

Suggested interview questions

Human review reminder

The main design choice is to focus on public professional information. The app is not designed to collect private information, hidden information, or information from accounts that require login access.

The second design choice is to show uncertainty clearly. Public web search results can be incomplete, outdated, or about the wrong person with the same name. Because of this, the app reminds HR to verify the sources manually.

The third design choice is to keep the app simple. This project is focused on one business workflow instead of trying to build a complete recruiting platform.

## App Logic

The app follows this workflow.

## Step 1: User enters candidate information

The recruiter enters a candidate name, such as Mingyu Wang.

The recruiter can also enter optional context, such as Johns Hopkins Carey Business School, Business Analyst, or New York. This optional context helps the system focus the search and reduce same name confusion.

## Step 2: The app simulates public web research

Since the current version is an HTML demo, it does not call a live search API from the browser.

Instead, it uses sample research content to show what the output would look like after a full system collects public search results.

In the full version, the frontend would send the candidate name and optional context to a backend server.

## Step 3: The full version backend would search the public web

In the full version, the backend would use a search API such as SerpAPI, Bing Search API, Google Custom Search API, or Tavily.

The backend would search public professional sources, such as:

LinkedIn public profile pages

GitHub pages

University pages

Company profile pages

Personal portfolio websites

Public project pages

Public articles or publications

The system would collect only public information, including page titles, URLs, and snippets.

## Step 4: The LLM would summarize the results

After collecting the public search results, the backend would send the result snippets and links to an LLM.

The LLM would organize the information into a structured HR research profile.

The prompt would ask the LLM to separate facts from assumptions and clearly mark uncertain information.

The LLM would also be asked to avoid making final hiring decisions.

## Step 5: The app displays a structured candidate profile

The frontend displays the result in a clean format.

The output includes a candidate overview, possible education, possible experience, skills, projects, links, uncertainty notes, and interview questions.

This structure helps HR understand the candidate faster than reading multiple web pages manually.

## Step 6: Human review stays required

The app includes a human review reminder.

This is important because public search results may be incomplete or incorrect. A person with the same name may appear in the results. The recruiter must verify the source links before using the information in a real hiring process.

## Why GenAI Is Useful

This task is useful for GenAI because candidate research involves more than simple keyword search.

A search engine can find pages related to a candidate name, but it does not automatically organize the results into an HR friendly profile. The recruiter still needs to read several pages, identify relevant career information, and write notes.

GenAI is useful because it can synthesize scattered public information into a consistent summary. It can help explain possible education, work experience, skills, projects, and interview topics.

The LLM also helps turn unstructured web snippets into a readable format that supports recruiter decision making.

## Baseline Comparison

The baseline workflow is manual public web search.

In the baseline workflow, a recruiter searches the candidate name manually, opens several pages, reads the results, and writes notes by hand.

The GenAI workflow is different because the recruiter enters the candidate name once and receives a structured research profile.

The baseline gives the recruiter raw search results.

The GenAI workflow gives the recruiter an organized first draft of candidate research.

This saves time because the recruiter does not need to start from a blank page.

## Evaluation and Results

For this prototype, I evaluated the app as a workflow demo.

I compared two approaches:

Baseline approach: manual web search and manual note taking

Prototype approach: candidate name input and structured AI style research summary

I used several sample candidate names and sample output scenarios to evaluate whether the workflow would be useful for an HR recruiter.

The evaluation rubric included five criteria.

## Relevance

The output should focus on professional information that is useful for HR screening. This includes education, work experience, skills, projects, and public professional links.

## Completeness

The output should include the main sections that an HR recruiter needs during first round research.

These sections include candidate overview, possible education, possible experience, skills, projects, source links, uncertainty notes, and interview questions.

## Usefulness

The output should help the recruiter understand the candidate faster than manual search.

The summary should be easy to read and should support interview preparation.

## Source Transparency

The output should include links or source placeholders so the recruiter can verify the information.

This is important because HR should not rely only on an AI summary.

## Risk Control

The output should clearly mention uncertainty.

For example, if the candidate has a common name, the app should remind the recruiter that some information may belong to another person with the same name.

## Evaluation Findings

The prototype shows that a structured GenAI workflow can make candidate research easier for recruiters.

Compared with manual search, the app provides a clearer output format. It helps the recruiter quickly review possible education, experience, skills, and interview questions.

The app also improves consistency because every candidate profile follows the same structure.

However, the current HTML version does not perform live web search. Because of this, the evaluation focuses on workflow design, output structure, and business usefulness.

A full implementation would need to be tested with real search results. The full version should be evaluated for accuracy, relevance, source quality, same name confusion, and hallucination risk.

## What Worked

The app clearly demonstrates the HR research workflow.

The interface is simple and easy to understand.

The output format is useful for first round candidate research.

The app includes uncertainty notes and a human review reminder.

The project shows how GenAI can support recruiter productivity without replacing human judgment.

## What Needs Improvement

The current version is a demo and does not perform live web search.

The current version does not connect to a real LLM API.

The current version uses sample output to represent what the full system would generate.

A future version should use a secure backend to protect API keys.

A future version should include live search results and real source links.

A future version should allow the recruiter to add more context, such as school, company, location, or target role.

A future version should include stronger checks for people with the same name.

## Artifact Snapshot

The artifact is an HTML demo app.

The user opens the HTML file in a browser.

The user enters a candidate name such as Mingyu Wang.

The app shows a structured candidate research profile.

The output includes candidate overview, possible education, possible work experience, skills, project evidence, source links or source placeholders, uncertainty notes, and interview questions.

Suggested screenshots for this repository:

Homepage with candidate name input

Example search result for Mingyu Wang

Candidate profile output

Uncertainty notes and human review reminder

## Setup and Usage Instructions

This project runs as a simple HTML demo.

To use the app:

1. Download or clone this repository.

2. Open the project folder.

3. Find the file named index.html.

4. Double click index.html to open it in a browser.

5. Enter a candidate name, such as Mingyu Wang.

6. Click the search button.

7. Review the structured candidate research profile.

No API key is required for the current demo.

## Repository Contents

index.html contains the full HTML demo app, including the page layout, style, interaction logic, and sample output.

README.md explains the project context, solution design, app logic, evaluation, results, and usage instructions.

screenshots contains screenshots of the app interface and sample output.

## Data and Privacy

This project is designed to use public professional information only.

The current demo does not collect real private data.

The repository should not include API keys, private resumes, real phone numbers, home addresses, private emails, or sensitive personal information.

If this app is expanded into a full system, candidate data should be handled carefully and securely.

The app should only summarize publicly available professional information and should always provide sources for human verification.

## Human Review and Responsible Use

This app is designed to assist HR research. It should not make hiring decisions.

The recruiter should verify the source links manually.

The recruiter should be careful with candidates who have common names.

The recruiter should avoid using private, sensitive, or irrelevant personal information.

The recruiter should use this tool as a first draft research assistant.

Final hiring decisions should remain with human reviewers.

## Future Improvements

A future version could connect the HTML frontend to a Flask or Node backend.

A future version could use a search API to retrieve live public web results.

A future version could use an LLM API to generate the candidate summary.

A future version could include source ranking and duplicate result removal.

A future version could allow the recruiter to enter candidate name, school, company, role, and location.

A future version could export the summary as a PDF or interview note.

A future version could evaluate results with more test cases and human recruiter feedback.

## Conclusion

This project demonstrates a focused GenAI workflow for HR candidate research.

The app helps recruiters move from manual web search to a more structured research process. The recruiter enters a candidate name and receives an organized profile that includes possible background, skills, projects, source links, uncertainty notes, and interview questions.

Compared with manual search, the workflow can save time and create more consistent candidate research notes.

The current version is an HTML demo that shows the intended workflow and output format. A full version would connect to a secure backend, public web search API, and LLM API.

The tool should support HR work, and human recruiters should always verify the information before using it in real hiring decisions.
