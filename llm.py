from litellm import completion

def completion_prompt(prompt):
    response = completion(
        model="ollama/llama3.2:3b", 
        messages=[{
                    "content":"""
            you are a helpful assistant that can answer questions about the context provided and summarize it
            """,
            "role":"system"
        },
        {
            "content":prompt,
            "role":"user"
        }],
        api_base="http://localhost:11434",
        stream=False
    )
    # For non-streaming, the content is in response.choices[0].message.content
    print(response.choices[0].message.content, end="", flush=True)
