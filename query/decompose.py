from lib.Chain import Chain

from pydantic import BaseModel, Field


### Your task is first to sanitize and input query into a most likely intended properly specific and well formed question (called 'parent question').
instructions = """Your task is to decide whether the parent question is atomic, if the parent question is not atomic decompose the parent question into a list of non-overlapping and independent subquestions, explain for each of those how they contribute to the question.
Decide whether the parent question is an atomic question or a compound question. An atomic question is a question for a fact that  most likely is written plainly in Wikipedia and can be looked up by a simple fact checker. Examples of atomic questions include "What is the birthday of the musician Micheal Jackson?", "Who is the current president of the United States?" or "What is the spin of an electron". A compound question is a question that most likely cannot be found by a simple fact checker on Wikipedia, but one that can only be answered using reasoning and answers for subquestions. For example the question "Which is heavier: Saturn or Jupiter?" most likely is not answered explicitely in Wikipedia, but can be decomposed into the subquestions "What is the weight of Saturn?" and "What is the weight of Jupiter?". Subquestions might in turn be compound as well. Judge if the parent question is an atomic question or a compound question.
If you decided the question is compound, find the set of obvious non-overlapping, independent, disjoint subquestions, which if answered each independently are sufficient to answer the parent question using only reasoning and no additional fact knowledge.
Give a list of those subquestions (they can be atomic or compound). Focus on a meaningful flat decomposition of the parent question. The subqestions must not overlap and must be independently answerable and must contribute to answering the parent question. If you decide the question is atomic, simply give the empty list.
Give an exact explanation of the reasoning steps that are to take to combine the answers to the subquestions into an answer of the parent question (without using additional knowledge besides answers to the subquestions and very basic illiterate common sense knowledge).
Separate the subquestions and the explanations of reasoning very well. Dont every repeat the subquestions in the reasoning.
"""

class Output(BaseModel):
    question          :      str  = Field(description='A sanitized most likely intended question equivalent of the query. Corrected for typos, grammar, punctuation, etc. Expand abbreviations with their most likely interpretation given the context of the rest of the question. Too unspecific terms get replaced by their most likely specific term depending on the the context.')
    subquestions      : list[str] = Field(description='A list of subquestions that will help answering the question. In case the question is already atomic and cannot be decomposed into meaningful subquestions, give the empty list!')
    reasoning         :      str  = Field(description='If the parent question is atomic only give \'atomic\'. If the question is compound give a detailed explanation of in which way exactly answering the subquestions will help answering the parent question. Explain exactly what reasoning steps are to take to combine the answers to the subquestion into an answer of the parent question. Do not use any additional knowledge besides answers to the subquestions and very basic common sense. Your are not required to form valid sentences in order be as short as possible.')



chain = Chain('decompose', instructions, Output)


def test(llm):
    query = chain(llm)

    query('waht is mas of triton ')
    query('who is larger, saturn or uranus?? ')
    query('Which planet is heavier: Jupiter or Saturn?')
    query('what has lower albedo, obama or donald ?')
    query('evaluate (812*319)+(123*64) ')
    query('the complete recursive definution of the fibonacci sequence (base case + recursive case) ')