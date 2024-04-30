import openai

# optional; defaults to `os.environ['OPENAI_API_KEY']`
openai.api_key = 'sk-lIr8I173VkdOHtW7fzTkmZeMJbpBMuy8AED6CUJugd2ZkcsF'

# all client options can be configured just like the `OpenAI` instantiation counterpart
openai.base_url = "https://api.chatanywhere.tech"
openai.default_headers = {"x-foo": "true"}


def translate_text(text):

    # 调用openai的API进行翻译
    # completion = openai.chat.completions.create(
    #     model="gpt-4",
    #     messages=[
    #         {
    #             "role": "user",
    #             "content": "How do I output all files in a directory using Python?",
    #         },
    #     ],
    # )
    completion = openai.chat.completions.create(model="gpt-3.5-turbo-16k",
            messages=[
                                                    {
                                                        "role": "user",
                                                        "content": "translate the following text into simple Chinese",
                                                    },
                                                    {
                                                        "role": "user",
                                                        "content": text,
                                                    }
                                                ],
                                                )
    # completion = openai.chat.completions.create(prompt, text)
    t_text = (
        # completion["choices"][0]
        # .get("message")
        # .get("content")
        # .encode("utf8")
        # .decode()
        completion.choices[0].message.content.encode("utf8").decode()
    )
    print(completion)
    print(completion.usage.total_tokens)
    # Get the token usage from the API response
    # cost_tokens += completion["usage"]["total_tokens"]
    return t_text


# completion = openai.chat.completions.create(
#     model="gpt-3.5-turbo-16k",
#     messages=[
#         {
#             "role": "user",
#             "content": "请将接下来英语翻译成中文",
#         },
#         {
#             "role": "user",
#             "content": "hello everybody",
#         }
#     ],
# )
# print(completion)
# print(completion.choices[0].message.content)
翻译后的文字 = translate_text('a every nice day')
print(翻译后的文字)
