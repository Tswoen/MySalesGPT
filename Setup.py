import os
from salesgpt.agents import SalesGPT
from langchain_community.chat_models import ChatLiteLLM

# from dotenv import load_dotenv

# load_dotenv()  # make sure you have .env file with your API keys, eg., OPENAI_API_KEY=sk-xxx, MINDWARE_API_KEY etc.

# select your model - we support 50+ LLMs via LiteLLM https://docs.litellm.ai/docs/providers
# llm = ChatLiteLLM(temperature=0.4, model_name="gpt-4-0125-preview")
os.environ["DASHSCOPE_API_KEY"] = 'sk-36c7f4e71d904a35afab94dc68747d48'
llm = ChatLiteLLM(model="openai/qwen-max",
                  api_base="https://dashscope.aliyuncs.com/compatible-mode/v1",
                  api_key=os.environ.get('DASHSCOPE_API_KEY'),
                  temperature=0.2)

# sales_agent = SalesGPT.from_llm(llm, use_tools=True, verbose=False,
#                                 product_catalog="examples/sample_product_catalog.txt",
#                                 salesperson_name="Ted Lasso",
#                                 salesperson_role="Sales Representative",
#                                 company_name="Sleep Haven",
#                                 company_business='''Sleep Haven
#                             is a premium mattress company that provides
#                             customers with the most comfortable and
#                             supportive sleeping experience possible.
#                             We offer a range of high-quality mattresses,
#                             pillows, and bedding accessories
#                             that are designed to meet the unique
#                             needs of our customers.'''
#                                 )
sales_agent = SalesGPT.from_llm(llm, use_tools=True, verbose=False,
                                product_catalog="examples/sample_product_catalog.txt",
                                salesperson_name="Ted Lasso",
                                salesperson_role="Sales Representative",
                                company_name="Sleep Haven",
                                company_business='''Sleep Haven 
                            is a premium mattress company that provides
                            customers with the most comfortable and
                            supportive sleeping experience possible. 
                            We offer a range of high-quality mattresses,
                            pillows, and bedding accessories 
                            that are designed to meet the unique 
                            needs of our customers.'''
                                )
sales_agent.seed_agent()  #初始化SalesGPT，清空SalesGPT的历史记录，并将stage设为1
sales_agent.determine_conversation_stage()  # optional for demonstration, built into the prompt #根据SalesGPT中的历史记录和stage来确定当前处于哪一个阶段
# agent
sales_agent.step()

# user
user_input = input('Your response: ')  # Yea, sure
sales_agent.human_step(user_input)

# agent
sales_agent.determine_conversation_stage()  # optional for demonstration, built into the prompt
sales_agent.step()

# user
user_input = input('Your response: ')  # What pricing do you have for your mattresses?
sales_agent.human_step(user_input)

# agent
sales_agent.determine_conversation_stage()  # optional for demonstration, built into the prompt
sales_agent.step()