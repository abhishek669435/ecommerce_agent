import json
from main import get_retriever, generate_answer

def evaluate():
    with open("tests/test_cases.json") as f:
        test_cases = json.load(f)

    retriever = get_retriever()

    total = len(test_cases)
    correct = 0

    for test in test_cases:
        query = test["ticket"]
        expected = test["expected"]

        docs = retriever.invoke(query)
        context = "\n\n".join([doc.page_content for doc in docs])

        answer = generate_answer(query, context, docs)

        print("\n==============================")
        print("Query:", query)
        print("Expected:", expected)
        print("Output:", answer)

        if expected.lower() in answer.lower():
            correct += 1

    print("\n==============================")
    print(f"Accuracy: {correct}/{total} = {round((correct/total)*100, 2)}%")

if __name__ == "__main__":
    evaluate()