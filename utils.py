import os
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_resume_text(data):
    """
    Flattens structured resume JSON into a single string.
    """
    text_parts = []

    # Personal Info
    text_parts.append(data.get("name", ""))
    text_parts.append(data.get("location", ""))

    # Summary
    text_parts.append(data.get("professional_summary", ""))

    # Work Experience
    work = data.get("work_experience", [])
    for job in work:
        text_parts.append(job.get("job_title", ""))
        text_parts.append(job.get("company", ""))
        text_parts.append(job.get("location", ""))
        text_parts.append(job.get("dates", ""))
        responsibilities = job.get("key_responsibilities", [])
        text_parts.extend(responsibilities)

    # Education
    education = data.get("education", [])
    for edu in education:
        text_parts.append(edu.get("degree", ""))
        text_parts.append(edu.get("institution", ""))
        text_parts.append(str(edu.get("year_of_completion", "")))

    # Skills
    text_parts.extend(data.get("technical_skills", []))
    text_parts.extend(data.get("tools_and_software", []))

    # Extras
    text_parts.extend(data.get("certifications", []))
    text_parts.extend(data.get("languages", []))
    text_parts.extend(data.get("achievements", []))

    return " ".join([str(part) for part in text_parts if part])
    

def load_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def load_json_text(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
        return extract_resume_text(data)


def load_texts(jd_path, resume_folder, max_files=None):
    jd_text = load_text(jd_path)
    resumes = {}
    for i, file in enumerate(os.listdir(resume_folder)):
        if file.endswith(".json"):
            resumes[file] = load_json_text(os.path.join(resume_folder, file))
        if max_files and i >= max_files - 1:
            break
    return jd_text, resumes


def score_resumes(jd_text, resumes):
    texts = [jd_text] + list(resumes.values())
    tfidf = TfidfVectorizer(stop_words="english")
    vecs = tfidf.fit_transform(texts)
    jd_vec = vecs[0:1]
    resume_vecs = vecs[1:]
    sims = cosine_similarity(jd_vec, resume_vecs).flatten()
    return dict(zip(resumes.keys(), sims))


def show_ranked(scores, top_n=10):
    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    print("\nTop Matching Resumes:\n")
    for i, (fname, score) in enumerate(ranked[:top_n]):
        print(f"{i+1}. {fname:20s} - {score*100:.2f}% match")
