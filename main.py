# main.py
from utils import load_texts, score_resumes, show_ranked

if __name__ == "__main__":
    jd_path = "job_description.txt"
    folder = "sample resumes"
    jd_text, resumes = load_texts(jd_path, folder)
    scores = score_resumes(jd_text, resumes)
    show_ranked(scores)
