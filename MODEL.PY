# REPLICATE_API_TOKEN= "r8_VAAq0KeuMARpcmK2Zun1uzohwdK0tFD1Lp2Yd"
import os
from llama_index.llms import Replicate
from llama_index.llms import ChatMessage

os.environ["REPLICATE_API_TOKEN"] = "r8_VAAq0KeuMARpcmK2Zun1uzohwdK0tFD1Lp2Yd"

llm = Replicate(
    model="a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5"
)

messages = [
    ChatMessage(role="user", content="What is your name"),
]
resp = llm.chat(messages)
print(resp)


# import replicate
# output = replicate.run(
#     "replicate/llama-2-70b-chat:2c1608e18606fad2812020dc541930f2d0495ce32eee50074220b87300bc16e1",
#     input={"prompt": input}
# )
# # The replicate/llama-2-70b-chat model can stream output as it's running.
# # The predict method returns an iterator, and you can iterate over that output.
# for item in output:
#     # https://replicate.com/replicate/llama-2-70b-chat/versions/2c1608e18606fad2812020dc541930f2d0495ce32eee50074220b87300bc16e1/api#output-schema
#     print(item)


