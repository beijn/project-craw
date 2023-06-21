from pprint import pprint



class Interface():

    def __init__(self):
        pass

    def log_llm_query(self, tag,  query, llm):
        print(f"QUERRIED {llm.model_name} at {tag} with {len(query)} characters.")

    def log_wikipedia(self, type, query): print(f"WIKI QUERRIED for a {type} for {query}.")


    def get_question(self):
        return input("Input question: ")


    def put_answer(self, answer):
        print('\n\n===== Final Answer Tree =====\n')
        pprint(answer.dict())



    def render_graph(self, obj):

        import streamlit as st
        from graphviz import Digraph

        #### generated by GPT-4 !!
        def obj_to_graph(obj, graph=None, parent=None):
            if graph is None:
                graph = Digraph()

            if isinstance(obj, dict):
                for key in obj:
                    child = f"{parent}_{key}" if parent else key
                    if parent:
                        graph.edge(parent, child, label=str(key))
                    obj_to_graph(obj[key], graph, child)
            elif isinstance(obj, list):
                for idx, item in enumerate(obj):
                    child = f"{parent}_{idx}" if parent else str(idx)
                    if parent:
                        graph.edge(parent, child, label=str(idx))
                    obj_to_graph(item, graph, child)
            else:
                leaf_node = f"{parent}_{obj}" if parent else str(obj)
                graph.node(leaf_node, label=str(obj))
                if parent:
                    graph.edge(parent, leaf_node)

            return graph

        dot = obj_to_graph(obj.__dict__)

        st.graphviz_chart(dot)

