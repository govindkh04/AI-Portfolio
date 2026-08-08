from groq import Groq

from config import GROQ_API_KEY, MODEL_NAME


# Create the Groq client once when the application starts
client = Groq(api_key=GROQ_API_KEY)


def get_llm_response(messages):
    """
    Sends the conversation messages to the LLM
    and returns the generated text.
    """

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            temperature=0.3
        )

        return response.choices[0].message.content

    except Exception as e:
        print(f"LLM Error: {e}")
        return "I'm sorry, I couldn't generate a response right now."
    