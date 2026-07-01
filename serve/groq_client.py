from groq import Groq
from config import GROQ_API_KEY, MODEL_NAME

# Create Groq client
client = Groq(api_key=GROQ_API_KEY)
def get_llm_response(prompt):
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
        {
            "role": "system",
            "content": (
                "You are an API that returns ONLY valid JSON. "
                "Never explain anything. "
                "Never use markdown. "
                "Never use ```json. "
                "Return only the JSON object."
            )
        },
        {
            "role": "user",
            "content": prompt
        }
        # messages=[
        #     {
        #         "role": "user",
        #         "content": prompt
        #     }
        ]
    )

    return response.choices[0].message.content