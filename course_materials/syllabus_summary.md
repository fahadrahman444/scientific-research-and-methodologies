# CSE 418: Scientific Research and Methodologies Lab — Course Synthesis

**Institution:** University of Information Technology and Sciences (UITS)  
**Program:** B.Sc in Computer Science & Engineering (Year 4, Semester 1)  
**Course Code:** CSE 418 | **Credit:** 1.00 (2.00 Hours/Week)  
**Instructor:** Tahmina Islam (Lecturer, Department of CSE; Specialization: Machine Learning, Deep Learning, Computer Vision, Healthcare AI)  
**Core Reference Text:** Creswell, J. W., & Creswell, J. D. (2018). *Research Design: Qualitative, Quantitative, and Mixed Methods Approaches* (5th ed.). SAGE Publications.

---

## 1. Course Outcomes (COs) & Program Outcomes (POs)

| CO Code | Course Outcome Description | Bloom's Level | Assessment Strategy |
| :--- | :--- | :--- | :--- |
| **CO1** | Investigate a research proposal by formulating research questions, objectives, hypotheses, methodology, and experimental plan using appropriate scientific methods. | L6 (Create) | Proposal, Presentation, Related Work |
| **CO2** | Formulate fundamental concepts of scientific research, research paradigms, and research problem identification. | L4 (Analyze) | Proposal, Discussion, Case Study |
| **CO3** | Select and apply appropriate research methodologies, data collection techniques, experimental procedures, and analytical tools for scientific investigation. | L3 (Apply) | Lab Test, Methodology, Result Report |
| **CO4** | Demonstrate research findings, prepare scientific reports, and communicate research outcomes through technical writing and presentations. | L5 (Evaluate) | Project Presentation, Viva, Final Manuscript |

---

## 2. Assessment & Marks Distribution (100% Continuous Evaluation)

According to the official CSE 418 syllabus:

| Assessment Component | Weightage | Sub-Components |
| :--- | :--- | :--- |
| **Class Attendance & Participation** | 10% | Weekly regular attendance and active engagement |
| **Topic Selection & Concept Formulation** | 10% | Problem clarity, novelty, and feasibility |
| **Lab Performance & Deliverables** | 30% | • Abstract Submission (10%)<br>• Related Work / Introduction (20%) |
| **Research Execution & Technical Report** | 30% | • Methodology & Experimental Results (20%)<br>• Research Report / Draft Paper (10%) |
| **Final Project Presentation & Defense** | 10% | Professional slide deck, methodology defense, visual demonstration |
| **Viva Voce** | 10% | Individual theoretical and empirical defense |
| **Total** | **100%** | |

---

## 3. 14-Week Course Roadmap & Project Alignment

| Week | Official Syllabus Topic | Project Milestone & Deliverables | Deliverable File Location |
| :---: | :--- | :--- | :--- |
| **W01** | Introduction to Research Methodologies: Qualitative vs. Quantitative | Quantitative, empirical, postpositivist paradigm chosen for 15-year weather-crop study | `docs/creswell_methodology_guide.md` |
| **W02** | Research Problem Statement, Identification, Literature Search | Formalized problem statement on Bangladesh climate variability & agriculture | `docs/research_proposal.md` |
| **W03** | Literature Review Writing, Citation Styles, Reference Management | BibTeX reference library (IEEE format) & systematic literature review | `literature_review/references.bib`, `literature_survey.md` |
| **W04** | Research Proposal Writing, Questions (RQs), Objectives, Hypotheses | Complete Proposal with 4 Objectives, 4 Research Questions, and 4 Hypotheses | `docs/research_proposal.md` |
| **W05** | Research Design, Experimental Planning, Variables, Sampling | Definition of independent, dependent, and moderating variables across 8 divisions | `docs/methodology_framework.md` |
| **W06** | Data Collection Methods: Primary vs. Secondary Datasets | Data collection schema from Bangladesh Meteorological Dept (BMD) & BBS | `data/data_dictionary.md`, `data/raw/README.md` |
| **W07** | Experimental Methods, Data Analysis Techniques, Statistical Analysis | Mann-Kendall Trend Test, Sen's Slope, SPI calculation in Google Colab | `colab_notebooks/01_Bangladesh_Weather_Crop_EDA_and_Preprocessing.ipynb` |
| **W08** | **Mid-Term Research Progress Presentation & Feedback** | **Progress Slide Deck covering Introduction, Related Work, and Preliminary EDA** | `presentation/Week08_Progress_Presentation.md` |
| **W09** | Data Interpretation, Tables, Charts, Graphs, Equations, Algorithms | Feature engineering (GDD, Anomaly scores), correlation matrices, ML pipeline | `colab_notebooks/02_Feature_Engineering_and_Statistical_Analysis.ipynb` |
| **W10** | Scientific Report Writing (IMRaD Structure) & Ethics | Drafting IEEE/Springer Manuscript (Introduction, Methodology, Results) | `paper/main.tex` |
| **W11** | Scientific Writing Tools, Plagiarism Checking, Overleaf/LaTeX, AI Tools | LaTeX formatting, reproducible Google Colab execution, zero plagiarism compliance | `paper/main.tex`, `colab_notebooks/` |
| **W12** | Journal/Conference Selection, Peer Review Process, Ethics | Identifying target IEEE/Elsevier conferences and open-access climate-agri journals | `paper/publication_targets.md` |
| **W13** | Final Research Paper Preparation & Manuscript Polishing | Complete IEEE Transactions-style scientific paper with experimental tables & figures | `paper/main.tex` |
| **W14** | **Final Project Presentation and Comprehensive Viva Voce** | **Final Presentation Slide Deck and Defense Viva Question Bank** | `presentation/Week14_Final_Defense_Viva.md` |

---

## 4. Methodological Alignment with Lecturer Tahmina Islam's Guidelines

From the Google Classroom postings and slides:
1. **Methodology Block Diagram:** A rigorous block diagram is mandatory (referencing the Classroom examples: Data Acquisition $\rightarrow$ Preprocessing $\rightarrow$ Feature Engineering $\rightarrow$ ML/DL Training $\rightarrow$ Performance Evaluation $\rightarrow$ Interpretation & Deployment).
2. **Reproducibility & Cloud Execution:** Machine learning training is to be executed in **Google Colab** (with GPU acceleration and automated cloud pipelining) rather than taxing local development environments.
3. **Novelty Statement (from Week 01 slide):**
   * *Domain Application:* Applying advanced non-linear ensemble models (XGBoost, CatBoost, LightGBM) and deep temporal architectures (LSTM) across all 8 administrative divisions of Bangladesh over an explicit 15-year historical continuum (2009–2024).
   * *Explainability:* Incorporating SHapley Additive exPlanations (SHAP) to unpack the "black box" and quantify exact physiological impacts of temperature and rainfall anomalies on staple rice varieties (Aus, Aman, Boro) and cash crops.
