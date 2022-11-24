from owlready2 import *

def model_1():
    onto = get_ontology("https://github.com/xiao-gao-gao/model_Test/blob/cbb4afd86bb01f774ff9b59f4cbe035804c26117/model_2.owl")
    onto.load()

    onto.m.input_value = (float(onto.WICQst_st.param_value) + float(onto.WICQst_nd.param_value)) / 2
    value = (float(onto.mu.input_value) * float(onto.M_ZnO.input_value) * float(onto.Ch.input_value)) / (
                1000 * float(onto.alpha.input_value) * float(onto.M_H.input_value) * float(onto.m.input_value))
    print(value)
    onto.beta.output_value = value

model_1()