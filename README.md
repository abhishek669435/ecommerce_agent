# 🛒 E-commerce Support Resolution Agent

## 📌 Overview
This project implements a **Retrieval-Augmented Generation (RAG)** based AI system that resolves e-commerce customer support tickets using policy documents.

The system ensures **accurate, policy-grounded, and structured responses** without hallucination.

---

## 🚀 Features

- 🔍 Retrieval-Augmented Generation (RAG)
- 📄 Policy-based decision making (no guessing)
- 🧠 Rule-based reasoning for correctness
- 📊 Structured output format (as per requirements)
- 📚 Citation-backed responses
- 🌐 Streamlit UI for interaction
- 📈 Evaluation system with test cases

---

## 🏗️ Architecture


User Query
↓
Retriever (Chroma Vector DB)
↓
Relevant Policy Documents
↓
Decision Engine (Rule-Based Logic)
↓
Structured Response Generator


---

## 🛠️ Tech Stack

- Python
- LangChain
- ChromaDB (Vector Database)
- HuggingFace Embeddings
- Streamlit (UI)
- JSON (Test Cases)

---

## 📂 Project Structure

ecommerce-agent/
│
├── app.py # Streamlit UI
├── README.md
├── requirements.txt
│
├── data/
│ └── policies/ # Policy documents
│
├── db/ # Vector database
│
├── src/
│ ├── main.py # Core logic
│ ├── ingestion.py # Data ingestion
│ ├── retriever.py # Retrieval logic
│ ├── evaluation.py # Evaluation script
│
├── tests/
│ └── test_cases.json # Test dataset


---

## ⚙️ Setup Instructions

### 1. Clone the repository

### 2. Install dependencies

### 3. Build vector database

### 4. Run the application (UI)

### 5. Run evaluation

---

## 🧪 Example Query

**Input:**
**Output:**

---

## 📊 Evaluation

The system is evaluated using predefined test cases covering:

- ✔ Refund eligibility
- ✔ Shipping and delay scenarios
- ✔ Exception handling
- ✔ Policy conflicts
- ✔ Edge cases

Metrics:
- Decision Accuracy
- Citation Coverage
- Handling of “not in policy” cases

---

## ⚠️ Limitations

- Uses rule-based decision logic instead of full LLM reasoning
- Limited dataset (synthetic policy documents)
- No real-time order integration

---

## 🔮 Future Improvements

- Integrate advanced LLM (GPT-4 / Llama)
- Add multi-agent architecture (Triage, Resolver, Compliance)
- Expand policy dataset
- Improve UI/UX
- Add real-time order data integration

---

## 🙌 Conclusion

This project demonstrates a **production-style AI system** combining:
- Retrieval-based grounding
- Deterministic decision logic
- Structured outputs
- Evaluation-driven development

---

## 📬 Author

**Abhishek Sahay**  
AI/ML Engineer Intern 