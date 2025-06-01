import docx2txt
import PyPDF2
import os   
from django.conf import settings

def extract_text(file_path):
    if file_path.endswith(".pdf"):
        with open (file_path,"rb") as file:
            pdf = PyPDF2.PdfReader(file)
            texts = []
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    texts.append(text)
                else:
                    texts.append("")
            text_extracted = " ".join(texts)
        return text_extracted
    elif file_path.endswith(".docx"):
        return docx2txt.process(file_path)
    return ""

def score_resume(resume_path,job_description):
    resume_text = extract_text(resume_path).lower()
    jd_text = job_description.lower()

    jd_words = set(jd_text.split())
    resume_words = set(resume_text.split())

    matched = jd_words.intersection(resume_words)

    return round((len(matched))/(len(jd_words)) * 100 ,2)