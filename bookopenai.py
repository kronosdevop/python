import openai


openai.api_key = "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"



def get_best_books(genre, book_count=5):
    return {
        "genre": genre,
        "books": ["Book 1", "Book 2", "Book 3"][:book_count],
    }


def run_conversation():
    messages = [
        {"role": "system", "content": "You are my assistant."},
        {"role": "user", "content": input("Recommend me a few books in the genre of: ")}
    ]
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt='\n'.join([f"{msg['role']}: {msg['content']}" for msg in messages]) + "\n"
                f"function: get_best_books\n"
                f"genre: [fantasy, horror, romance, thriller, film-noir, literature, fiction, science-fiction, \
                    Social science, Dystopian Fiction, Political fiction, narrative, novel]\n",
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
        frequency_penalty=0,
        presence_penalty=0
    )
    generated_text = response["choices"][0]["text"]
    messages.append({"role": "assistant", "content": generated_text})
    return messages


print(run_conversation())
