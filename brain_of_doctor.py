import os
import base64
from groq import Groq
import base64

def encode_images(image_path):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"File not found: {image_path}")
    print("IMAGE paTH",image_path)

    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
    
    return encoded_string  # Make sure this is properly returned    

def analyze_img_with_query(query, model, encode_image, GROQ_API_KEY):
    client = Groq(api_key=GROQ_API_KEY)
    # Messages
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": query
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encode_image}"
                    }
                }
            ]
        }
    ]

    # Chat Completion Request
    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model
    )

    # Print Response
    return chat_completion.choices[0].message.content



# Setup 1: Load GROQ API Key
# GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

# # Setup 2: Convert Image to Required Format
# image_path = "acne.png"

# with open(image_path, "rb") as image_file:
#     encode_image = base64.b64encode(image_file.read()).decode('utf-8')


# # Setup 3: Initialize Groq API Client
# client = Groq(api_key=GROQ_API_KEY)

# # Query
# query = "Is there something wrong with my face?"
# model="llama-3.2-90b-vision-preview"

# # Messages
# messages = [
#     {
#         "role": "user",
#         "content": [
#             {
#                 "type": "text",
#                 "text": query
#             },
#             {
#                 "type": "image_url",
#                 "image_url": {
#                     "url": f"data:image/jpeg;base64,{encode_image}"
#                 }
#             }
#         ]
#     }
# ]

# # Chat Completion Request
# chat_completion = client.chat.completions.create(
#     messages=messages,
#     model=model
# )

# # Print Response
# print(chat_completion.choices[0].message.content)


# query = "Is there something wrong with my face?"
# model="llama-3.2-90b-vision-preview"

# def analyze_img_with_query(query, model, encode_image, GROQ_API_KEY):
#     client = Groq(api_key=GROQ_API_KEY)
#     # Messages
#     messages = [
#         {
#             "role": "user",
#             "content": [
#                 {
#                     "type": "text",
#                     "text": query
#                 },
#                 {
#                     "type": "image_url",
#                     "image_url": {
#                         "url": f"data:image/jpeg;base64,{encode_image}"
#                     }
#                 }
#             ]
#         }
#     ]

#     # Chat Completion Request
#     chat_completion = client.chat.completions.create(
#         messages=messages,
#         model=model
#     )

#     # Print Response
#     return chat_completion.choices[0].message.content

