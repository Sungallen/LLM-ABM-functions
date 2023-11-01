import openai

def broadCall(instructions, person, functions):
    textQuery = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=[
            {"role" : "system", "content" : "Follow all instructions. Don't deviate from the format or mess up the JSON"},
            {"role" : "system", "content" : instructions},
            {"role": "user", "content": person}
        ],
        functions = functions,
    )
    if textQuery["choices"][0]["message"]["content"]:
        return broadCall(instructions, person, functions)
    result = textQuery["choices"][0]["message"]["function_call"]["arguments"]
    return result