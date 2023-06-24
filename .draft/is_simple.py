from lib.Chain import Chain

from pydantic import BaseModel, Field

instructions="""Please asses whether the following query is an atomic or a compound question. A atomic question is a question for a fact most likely is written plainly Wikipedia and can be looked up by a atomic fact checker. Examples of atomic questions include "What is the birthday of the musician Micheal Jackson?", "Who is the current president of the United States?" or "What is the spin of an electron". A compound question is a question that most likely cannot be found by a atomic fact checker on Wikipedia, but one that can only be answered using reasoning and answers for subquestions. For example the question "Which is heavier: Saturn or Jupiter?" most likely is not answered explicitely in Wikipedia but can be decomposed into the subquestions "What is the weight of Saturn?" and "What is the weight of Jupiter?". Subquestions might in turn be compound as well. Your job is to judge if the given question is a atomic question or a compound question."""


class Output(BaseModel):
    is_atomic : bool  = Field(description='Whether the query is an atomic question or not.')


chain = Chain(instructions, Output)