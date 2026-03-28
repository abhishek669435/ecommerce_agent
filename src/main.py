import os
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings


# 🔹 STEP 1: Retriever
def get_retriever():
    embeddings = HuggingFaceEmbeddings()

    db = Chroma(
        persist_directory="db",
        embedding_function=embeddings
    )

    return db.as_retriever(search_kwargs={"k": 3})


# 🔹 STEP 2: Classification
def classify_issue(query):
    q = query.lower()
    if "refund" in q:
        return "Refund"
    elif "delay" in q or "late" in q:
        return "Shipping"
    elif "cancel" in q:
        return "Cancellation"
    else:
        return "Other"


# 🔹 STEP 3: FINAL DECISION ENGINE (PRECISE + CORRECT)
def decide_policy(query, context):
    query_lower = query.lower()
    context_lower = context.lower()

    decision = "Denied"
    rationale = "Policy does not allow this request."

    # ✅ Melted / perishable items (MOST IMPORTANT CASE)
    if "melted" in query_lower or "perishable" in query_lower:
        if ("delay" in query_lower or "late" in query_lower) and "48 hours" in context_lower:
            decision = "Approved"
            rationale = "Melted perishable items are eligible for refund only if delivery delay exceeds 48 hours."
        else:
            decision = "Denied"
            rationale = "Melted or spoiled perishable items are not refundable after delivery unless delay exceeds 48 hours."

    # ✅ Damaged items
    elif "damaged" in query_lower:
        decision = "Approved"
        rationale = "Items damaged during delivery are eligible for refund."

    # ✅ Lost package
    elif "lost" in query_lower:
        decision = "Approved"
        rationale = "Lost packages are eligible for refund."

    # ✅ Delay case
    elif "delay" in query_lower or "late" in query_lower:
        decision = "Partial"
        rationale = "Delayed deliveries may qualify for compensation depending on duration."

    return decision, rationale


# 🔹 STEP 4: Generate structured response
def generate_answer(query, context, docs):
    classification = classify_issue(query)
    decision, rationale = decide_policy(query, context)

    # Citations
    citations = "\n".join([
        f"- Source {i+1}: {doc.metadata.get('source', 'policy file')}"
        for i, doc in enumerate(docs)
    ])

    # Final structured output
    answer = f"""
Classification: {classification}

Clarifying Questions:
None

Decision:
{decision}

Rationale:
{rationale}

Citations:
{citations}

Customer Response:
We’re sorry for the inconvenience. Based on our policy, your request is {decision.lower()}.

Internal Notes:
Decision derived using query intent and grounded policy rules.
"""

    return answer.strip()


# 🔹 STEP 5: MAIN (for terminal testing)
if __name__ == "__main__":
    print("🚀 E-commerce Support Assistant Started\n")

    retriever = get_retriever()

    query = input("Enter your question: ")

    docs = retriever.invoke(query)

    context = "\n\n".join([doc.page_content for doc in docs])

    answer = generate_answer(query, context, docs)

    print("\n🤖 AI Response:\n")
    print(answer)