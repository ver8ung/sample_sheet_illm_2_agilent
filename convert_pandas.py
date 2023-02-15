import pandas as pd

dict1 = {"a" : {"A701" : {"Agilent_Primer_Pair_1_I7"}},
        {"a" : {"A702" : {"Agilent_Primer_Pair_2_I7"}},
        {"a" : {"A703" : "Agilent_Primer_Pair_3_I7"}},
        {"a" : {"A704" : "Agilent_Primer_Pair_4_I7"}},
        {"a" : {"A705" : "Agilent_Primer_Pair_5_I7"}},
        {"a" : {"A706" : "Agilent_Primer_Pair_6_I7"}},
        {"a" : {"A707" : "Agilent_Primer_Pair_7_I7"}},
        {"a" : {"A708" : "Agilent_Primer_Pair_8_I7"}},
        {"a" : {"A709" : "Agilent_Primer_Pair_9_I7"}}               
}

input = pd.read_excel("test_sample_sheet.xlsx")
input.replace(to_replace(dict1))
