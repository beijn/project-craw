from lib.Chain import Chain

from pydantic import BaseModel, Field


instructions = """Your task is to transform a given question into a list of three wikipedia search terms. The search terms need to be optimized to likely yield an article that likely contains the information that can answer the question. The first term should be very specific but still likely to occur in an article that contains information that can answer the question. The last term should be related to question, but highly likely to exist in a relevant wikipedia article in case the first and second term don't. The second term should strike a balance between these two. Add a specific word that narrows down the possible results in case ob ambiguity. For example given the question "What is the mother of Obama?"
return ["mother president Barack Obama", "family president Barack Obama", "president Barack Obama"]
or for "What are all the fruits of taiwan?"
return ["fruits taiwan", "taiwan flora", "taiwan agriculture"]
"""

class Output(BaseModel):
    searches : list[str] = Field(description='List of three search terms for wikipedia')

chain = Chain('wiki_queries', instructions, Output)


