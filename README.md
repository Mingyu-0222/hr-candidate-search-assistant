Context, User, and Problem

This project is designed for HR recruiters who need to quickly review candidate resumes during the first screening stage. Recruiters often spend a large amount of time opening different resumes, reading unstructured experience descriptions, and manually deciding whether a candidate is worth moving forward. This process is repetitive, time consuming, and inconsistent.

The workflow I improve is candidate profile review. Instead of reading the entire resume first, the recruiter can search a candidate name and receive a structured candidate summary, role fit analysis, and suggested interview questions.

Solution and Design

I built a small Streamlit app. The user enters a candidate name and selects a target role. The app searches a small synthetic candidate dataset and retrieves the matching candidate profile. Then it sends the candidate profile and target role to a GenAI model. The model returns a structured HR screening summary.

The output includes candidate background, key skills, experience summary, role fit, potential concerns, interview questions, and a human review reminder.

The main GenAI design choice is to use the model for summarization and judgment support, not final hiring decisions. The app is designed to assist HR with first pass screening while keeping the final decision with a human reviewer.

Evaluation and Results

I tested the app on five synthetic candidate profiles. I compared the GenAI version against a simpler baseline that only searches for the candidate and displays the raw resume text.

Good output was defined as a response that accurately summarized the candidate, included the most important skills and experiences, gave a reasonable role fit explanation, and generated useful interview questions.

The GenAI version performed better than the baseline because it gave HR a faster and more consistent way to understand each candidate. The baseline still required the recruiter to read the full resume manually. The GenAI version reduced this effort by turning the resume into a standard screening format.

The main failure risk is that the model may miss details, overstate a candidate’s fit, or summarize vague experience too positively. Because of this, the tool should be used as a screening assistant, not as a final decision maker.

Artifact Snapshot

Include a screenshot of the app interface and one sample output.

Setup and Usage
1. Clone this repository.
2. Install dependencies with pip install -r requirements.txt.
3. Create a .env file and add your API key.
4. Run the app with streamlit run app.py.
5. Enter a candidate name and target role.
