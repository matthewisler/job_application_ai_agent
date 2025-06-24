import gradio as gr
import fitz

def extract_text_from_pdf(file):
    try:
        doc = fitz.open(stream=file_obj.read(), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        return text.strip()
    except Exception as e:
        return f"Error reading PDF: {str(e)}"

def process_inputs(resume_file, job_criteria):
    if resume_file is None:
        return "No file uploaded."

    try:
        filename = getattr(resume_file, "name", "")
        if filename.endswith(".pdf"):
            content = extract_text_from_pdf(resume_file)
        else:
            content = f"Unsupported file type: {filename.split('.')[-1]} (only .pdf supported)"
        
        return f"Job Criteria: {job_criteria}\n\n📄 Resume Preview:\n{content[:1000]}"
    
    except Exception as e:
        return f"Error while processing the file: {str(e)}"

# Build interface
gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.File(label="Upload Resume (.pdf only)", file_types=[".pdf"]),
        gr.Textbox(label="Job Search Criteria (e.g., 'AI Engineer, Remote')")
    ],
    outputs=gr.Textbox(label="Output"),
    title="Resume Analyzer",
    description="Upload your resume and enter job search criteria. Currently supports .pdf files only."
).launch(share=True)
