# Aerospace 1B
---

### 👥 **Team Members**


| Name             | GitHub Handle | Contribution                                                             |
|------------------|---------------|--------------------------------------------------------------------------|
| Sonya Popov      | @sophie2126   | Data exploration, visualization, overall project coordination            |
| Victor Silva     | @jramirez     | Data collection, exploratory data analysis (EDA), dataset documentation  |
| Nima Sherpa      | @aminahassan  | Data preprocessing, feature engineering, data validation                 |
| Erick Jacomes    | @pmehta       | Model selection, hyperparameter tuning, model training and optimization  |
| Max Hu           | @chrispark    | Model evaluation, performance analysis, results interpretation           |
| Lauren Nunez     | @chrispark    | Model evaluation, performance analysis, results interpretation           |

---

## 🎯 **Project Highlights**

**Example:**

- AI-Powered Compliance Auditing: Automates first-pass review of software requirements against NASA engineering standards.
- Progressive AI Architecture: Evolves from a traditional rule/keyword-based baseline → deterministic RAG pipeline → tool-calling LLM agent.
- Grounded Decisions: Every compliance verdict is tied to a specific NASA NPR 7150.2 clause to reduce unsupported or hallucinated judgments.
- Structured Compliance Classification: Categorizes requirements as Meets, Partial, or Gap and produces machine-readable results.
- Agentic Workflow: Uses specialized tools such as retrieve_clause, check_requirement, and log_gap to orchestrate the auditing process.
- Automated Audit Reports: Generates structured JSON and Markdown gap reports identifying potential compliance issues.
- Benchmark-Driven Evaluation: Measures precision, recall, and citation groundedness against a human-labeled ground-truth dataset.
- Real-World Applicability: Designed around aerospace compliance, with an architecture that could potentially generalize to other regulated domains such as MedTech and FinTech GRC.

---

## 👩🏽‍💻 **Setup and Installation**

**Provide step-by-step instructions so someone else can run your code and reproduce your results. Depending on your setup, include:**

* How to clone the repository
* How to install dependencies
* How to set up the environment
* How to access the dataset(s)
* How to run the notebook or scripts

---

## 🏗️ **Project Overview**

**Description:**

- How this project is connected to the Break Through Tech AI Program
- Your AI Studio host company and the project objective and scope
- The real-world significance of the problem and the potential impact of your work

This project is part of the **Break Through Tech AI Program's AI Studio**, where student teams apply machine learning and AI techniques to real-world industry problems. Our project focuses on developing an AI-powered **Compliance Copilot** for software engineering requirements.

The objective of the project is to create a system that can evaluate software requirements against established engineering compliance standards. We are using **NASA NPR 7150.2**, a software engineering requirements standard, as the primary compliance standard. The project will progress from an initial non-LLM baseline to a Retrieval-Augmented Generation (RAG) system and eventually a tool-calling LLM agent capable of retrieving relevant clauses, checking individual requirements, identifying compliance gaps, and generating structured audit reports.

Compliance review is especially important in safety-critical and highly regulated industries such as aerospace, medical technology, and financial infrastructure. Requirements may need to be manually reviewed against extensive engineering standards, making the process time-consuming and dependent on domain experts. The Compliance Copilot aims to support this process by providing a faster and more structured first-pass review while grounding its conclusions in specific clauses from the relevant standard. This could help engineers identify potential compliance gaps earlier and make the review process more efficient and transparent.


---

## 📊 **Data Exploration**

**You might consider describing the following (as applicable):**

* The dataset(s) used: origin, format, size, type of data
* Data exploration and preprocessing approaches
* Insights from your Exploratory Data Analysis (EDA)
* Challenges and assumptions when working with the dataset(s)

### Datasets

The project uses several sources related to NASA software engineering requirements:

* **NASA NPR 7150.2D – Software Engineering Requirements:** The primary compliance standard used by the project. It contains numbered and structured software engineering requirements that serve as the reference for evaluating software requirements.
* **NASA Software Engineering and Assurance Handbook:** Provides additional guidance and context for interpreting software engineering requirements.
* **Synthetic Software Requirements (SRS) Dataset:** A collection of software requirements used as inputs for the compliance auditing system. The dataset includes examples designed to represent both compliant requirements and requirements containing potential compliance gaps.

The project data is primarily text-based and is stored or processed in formats including **PDF, plain text, CSV, and JSON**. The overall dataset is relatively small and can be processed using standard Python tools and Google Colab.


**Potential visualizations to include:**

* Plots, charts, heatmaps, feature visualizations, sample dataset images

---

## 🧠 **Model Development**

**You might consider describing the following (as applicable):**

* Model(s) used (e.g., CNN with transfer learning, regression models)
* Feature selection and Hyperparameter tuning strategies
* Training setup (e.g., % of data for training/validation, evaluation metric, baseline performance)


---

## 📈 **Results & Key Findings**

**You might consider describing the following (as applicable):**

* Performance metrics (e.g., Accuracy, F1 score, RMSE)
* How your model performed
* Insights from evaluating model fairness

**Potential visualizations to include:**

* Confusion matrix, precision-recall curve, feature importance plot, prediction distribution, outputs from fairness or explainability tools

---

## 🚀 **Next Steps**

**You might consider addressing the following (as applicable):**

* What are some of the limitations of your model?
* What would you do differently with more time/resources?
* What additional datasets or techniques would you explore?

---

## 📝 **License**

Specify how your project can be used by others. Choose an appropriate license and link it here (e.g., MIT, Apache 2.0). Make sure your Challenge Advisor approves of the selected license type. 

**Example:**
This project is licensed under the MIT License.

---

## 📄 **References** (Optional but encouraged)

Cite relevant papers, articles, or resources that supported your project.

---

## 🙏 **Acknowledgements** (Optional but encouraged)

Thank your Challenge Advisor, host company representatives, TA, and others who supported your project.
