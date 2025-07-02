# Resume Ranker AI

A smart resume-matching tool that reads a **job description** and compares it with a directory of **JSON-formatted resumes**, ranking each resume by its relevance using **TF-IDF** and **cosine similarity**.

---

##  Folder Structure

resume-ranker-ai/
├── main.py
├── utils.py
├── job_description.txt
├── requirements.txt
├── README.md
└── sample_resumes/
├── resume_1.json
├── resume_2.json
└── ...

yaml
Copy
Edit

---

##  What This Project Does

- Parses **structured JSON resumes** with fields like:
 - `professional_summary`, `technical_skills`, `achievements`, etc.
- Flattens each resume into a single string
- Compares each to the job description using **TF-IDF**
- Ranks resumes based on **cosine similarity**
- Displays top matching resumes

---

##  How to Run

### 1. Clone the repo & navigate into it
```bash
git clone https://github.com/yourusername/resume-ranker-ai.git
cd resume-ranker-ai
```
### 2. Install requirements
```bash

pip install -r requirements.txt
```
### 3. Add your files
 Add your job description inside job_description.txt

 Put all resume .json files in the sample_resumes/ folder

### 4. Run the program
```bash

python main.py
```
## Sample Job Description `job_description.txt`

Looking for a Python developer experienced in machine learning, NLP, and deep learning frameworks like TensorFlow or PyTorch. Knowledge of pandas, scikit-learn, and cloud platforms is a plus.
## Sample Output

Top Matching Resumes:

1. resume_203.json       → 84.23% match
2. resume_519.json       → 80.67% match
3. resume_031.json       → 76.52% match
...
## Requirements
Python 3.7+

scikit-learn

## Install using:

```
pip install -r requirements.txt
```


### Built By
Vaidehi Hattikar
Data Science undergrad | Python + ML Enthusiast

Give it a star if you like it!
Let me know if you'd like me to:
- Generate a professional logo/banner for the GitHub repo
- Help write the `.gitignore` file to avoid pushing large datasets
- Write a professional LinkedIn post or résumé line for this project

You're just a commit away from a killer portfolio project. 🚀
