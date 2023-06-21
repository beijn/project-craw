

from langchain.output_parsers import PydanticOutputParser
from langchain import PromptTemplate


def Chain(tag, instructions, Output):
    parser = PydanticOutputParser(pydantic_object=Output)

    prompt = PromptTemplate(
        template="{instructions}\n{format_instructions}\nQuery:\n{query}\n",
        input_variables=["query"],
        partial_variables={"format_instructions": parser.get_format_instructions(), 'instructions':instructions},
    )

    return lambda llm: lambda q: parser.parse(llm(tag)(prompt.format_prompt(query=q).to_string()))
