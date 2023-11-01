import openai

def narrowCall(instructions, person, functions):
    textQuery = openai.ChatCompletion.create(
        model="gpt-4-0613",
        messages=[
            {"role" : "system", "content" : "Follow all instructions. Ensure you do a function call."},
            {"role" : "system", "content" : instructions},
            {"role": "user", "content": person}
        ],
        functions = functions,
    )
    if textQuery["choices"][0]["message"]["content"]:
        return narrowCall(instructions, person, functions)
    result = textQuery["choices"][0]["message"]["function_call"]["arguments"]
    return result