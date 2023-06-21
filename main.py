#!python

from lib.TreeTypes import Question, Answer, AnsweredQuestion, UnanswerableQuestion

import os

from langchain.llms import OpenAI as Provider

os.environ["OPENAI_API_KEY"] = open('secret/openai_api_key').read().strip()
llm = Provider()



def answer_question(question, depth, attempts=2):
    print('CURRENT QUESTION:',question.question)
    if attempts <= 0 or depth <= 0:
        return UnanswerableQuestion(question=question, answer='Recursion depth / number of attempts exhausted')

    tree = decompose(question.question)
    question.question = tree.question

    if not tree.subquestions:
        answer, source = answer_wikipedia(question.question)
        if answer: return AnsweredQuestion(question=question, answer=Answer(answer=answer, source=source))


    if tree.subquestions:
        sub_aqs = [answer_question(Question(question=subq, failed_alternatives=[]), depth-1) for subq in tree.subquestions]

        answer = answer_compound(question, tree.reasoning, [(aq.answer.answer if isinstance(aq, AnsweredQuestion) else aq.answer) for aq in sub_aqs])

        if answer.found: return AnsweredQuestion(question=question, answer=Answer(answer=answer.answer, source='Deduction: '+answer.explain), sub_aqs=sub_aqs)

    return UnanswerableQuestion(question=question, answer=answer)

    """
    failed_alternatives = question.failed_alternatives + [UnanswerableQuestion(question=question.question, answer=answer.answer)]

    altq = alternative(question.failed_alternatives)

    question = Question(question=altq.question, failed_alternatives = failed_alternatives)

    return answer_question(question, depth, attempts-1)
    """


from lib.Interface import Interface
interface = Interface()


def llm(tag, llm=llm):
    def ret(query):
        interface.log_llm_query(tag, query, llm)
        return llm(query)
    return ret




from query.decompose import chain
decompose = chain(llm)

from query.alternative import chain
alternative = chain(llm)

from query.answer_compound import chain
answer_compound = chain(llm)


from lib.Wikipedia import WikipediaAnswerer
answer_wikipedia = WikipediaAnswerer(llm, interface.log_wikipedia).answer





question = interface.get_question()
question = Question(question=question, failed_alternatives=[])



answer = answer_question(question, depth=2)

interface.put_answer(answer)


#interface.render_graph(answer)

