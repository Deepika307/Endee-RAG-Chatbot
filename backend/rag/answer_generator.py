def generate_answer(query, results):
    if not results:
        return "No relevant information found in the document."

    combined_context = ""

    for item in results:
        combined_context += item["text"] + " "

    answer = summarize_context(query, combined_context)

    return answer


def summarize_context(query, context):
    sentences = context.replace("\n", " ").split(".")

    keywords = set(query.lower().split())

    scored = []

    for sentence in sentences:
        words = set(sentence.lower().split())
        score = len(words.intersection(keywords))

        if score > 0:
            scored.append((score, sentence.strip()))

    if not scored:
        return "Relevant information was found but could not be summarized clearly."

    scored.sort(key=lambda x: x[0], reverse=True)

    top_sentences = [s[1] for s in scored[:2]]

    final_answer = ". ".join(top_sentences)

    return final_answer.strip() + "."
