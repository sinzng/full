from langchain.prompts import PromptTemplate
from langchain.prompts import FewShotPromptTemplate
from langchain.prompts.example_selector import LengthBasedExampleSelector

examples =[
    {"input": "밝은", "output":"어두운"},
    {"input": "재미있는", "output":"지루한"},
    {"input": "활기찬", "output":"무기력한"},
    {"input": "높은", "output":"낮은"},
    {"input": "빠른", "output":"느린"},
]

example_prompt = PromptTemplate(
    input_variables= ["input","output"],
    template = "입력 : {input}\n출력 : {output}",
)

example_selector = LengthBasedExampleSelector(
    examples=examples, # 답변 예시
    example_prompt=example_prompt, #프롬프트 템플릿
    max_length= 10, #문자열 최대 길이 
)

prompt_from_string_examples = FewShotPromptTemplate(
    example_selector = example_selector,
    example_prompt = example_prompt,
    prefix ="모든 입력에 대한 반의어를 입력하세요.", 
    suffix = "입력: {adjective}\n출력: ",
    input_variables=["adjective"],
    example_separator="\n\n"
    
)

print(prompt_from_string_examples.format(adjective="큰"))