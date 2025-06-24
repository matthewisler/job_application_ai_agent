# SmartApply Agent – Job Application AI Assistant

An autonomous AI agent that helps job seekers match, optimize, and apply to job listings—powered by NLP, LLMs, and automation.

## Features

- Upload your resume (PDF or DOCX)
- Automatically scrape job postings from online job boards
- Score how well your resume matches each job
- Extract critical keywords and required qualifications
- Tailor your resume to each job with ATS-friendly formatting
- Download the optimized resume for instant use

## Demo

TO DO: [Insert link to GIF or screenshot]

## How It Works

1. Upload Resume – Extract and clean content using `pdfminer` or `python-docx`
2. Scrape Jobs – Use Selenium or APIs to collect job descriptions
3. Analyze Match – Use embeddings + cosine similarity to score fit
4. Extract Keywords – Pull out key skills, tools, verbs from the JD
5. Generate Resume – Update resume with relevant terms using GPT or Jinja2 templates

## Tech Stack

- Python 3.11
- Streamlit or Gradio
- SentenceTransformers
- LangChain
- OpenAI
- `pdfminer.six`, `python-docx`, `spacy`, `jinja2`
- Selenium for scraping
- Optional: FAISS for job vector retrieval, MLflow or Weights & Biases for tracking

## Getting Started

1. Clone the repo

```bash
git clone https://github.com/yourusername/job-application-ai-agent.git
cd job-application-ai-agent
```

2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run the app

```bash
streamlit run app/ui.py
```

## Project Structure

| Folder      | Purpose                                           |
|-------------|---------------------------------------------------|
| `src/`      | Core logic: scraping, NLP, scoring, generation    |
| `app/`      | App entry point and agent orchestration           |
| `templates/`| Resume templates for generation                   |
| `data/`     | Sample resumes and job descriptions               |
| `notebooks/`| Experiments and testing code                      |

## Sample Use Case

Upload your resume, search for "AI Engineer, New York", and let the agent:
- Score jobs for fit
- Extract keywords like “PyTorch”, “LLMs”, “Vector DBs”
- Rewrite your resume to emphasize those terms
- Export the final version for direct application

## Ideas for Future Features

- Cover letter generator
- Batch resume tailoring
- Auto-fill application forms
- Interview question prep agent

## Author

- Matthew Isler – [LinkedIn]https://www.linkedin.com/in/matthew-isler/

Questions or feedback? Open an issue or send a message.
