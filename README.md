ko# Resume Match System

NLP-based resume and job description matching system built during the Bano Qabil Agentic AI program.

## Overview

This project takes a resume (PDF or DOCX) and a job description, then:

- Extracts text from the resume
- Cleans and vectorizes the combined text using TF-IDF
- Predicts a match score
- Lists matched and missing skills
- Generates a short recommendation report

A simple frontend is included so the full flow can be tested end-to-end.

## Project Structure

```text
resumedetector/
├── .devcontainer/
│   └── devcontainer.json
├── Resume_detector/
│   ├── app.py
│   ├── requirements.txt
│   ├── resume_match_system.ipynb
│   ├── models/
│   │   ├── resume_match_model.pkl
│   │   └── tfidf.pkl
│   └── utils/
│       ├── __init__.py
│       ├── jobs.py
│       ├── parser.py
│       ├── predictor.py
│       ├── preprocessing.py
│       └── test_predictor.py
└── README.md

## How it works

1. Resume text is extracted from PDF or DOCX  
2. Text is cleaned and combined with the job description  
3. TF-IDF vectorization is applied  
4. A trained model returns a match score (0–1)  
5. Simple skill overlap is calculated  
6. A short report is generated  

## Notes

- Skill extraction is basic (token-level matching) and can flag generic words  
- The focus of this project was building a complete pipeline (parsing → scoring → interface), not production-level ATS accuracy  

## Tech Stack

- Python  
- scikit-learn (TF-IDF + model)  
- pdfplumber / python-docx  
- Streamlit (frontend)  

## Live Demo

[Add your deployed frontend link here]

## Author

Saad Maqbool  
Bano Qabil — Agentic AI Program