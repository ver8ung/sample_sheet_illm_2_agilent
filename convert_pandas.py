import pandas as pd

dict1 = {"A701" : "Agilent_Primer_Pair_1_I7",
"A702" : "Agilent_Primer_Pair_2_I7",
"A703" : "Agilent_Primer_Pair_3_I7",
"A704" : "Agilent_Primer_Pair_4_I7",
"A705" : "Agilent_Primer_Pair_5_I7",
"A706" : "Agilent_Primer_Pair_6_I7",
"A707" : "Agilent_Primer_Pair_7_I7",
"A708" : "Agilent_Primer_Pair_8_I7",
"A709" : "Agilent_Primer_Pair_9_I7"
}

input = pd.read_excel("test_sample_sheet.xlsx")
input.replace(to_replace(dict1))
