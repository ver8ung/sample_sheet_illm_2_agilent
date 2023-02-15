import pandas as pd

dict1 = {"E" : {"A701" : {"Agilent_Primer_Pair_1_I7"}},
        {"E" : {"A702" : {"Agilent_Primer_Pair_2_I7"}},
        {"E" : {"A703" : "Agilent_Primer_Pair_3_I7"}},
        {"E" : {"A704" : "Agilent_Primer_Pair_4_I7"}},
        {"E" : {"A705" : "Agilent_Primer_Pair_5_I7"}},
        {"E" : {"A706" : "Agilent_Primer_Pair_6_I7"}},
        {"E" : {"A707" : "Agilent_Primer_Pair_7_I7"}},
        {"E" : {"A708" : "Agilent_Primer_Pair_8_I7"}},
        {"E" : {"A709" : "Agilent_Primer_Pair_9_I7"}}  
         
        {"F" : {"ATCACGAC" : "CAAGGTGA"}},
ACAGTGGT
CAGATCCA
ACAAACGG
ACCCAGCA
AACCCCTC
CCCAACCT
CACCACAC
GAAACCCA
        {"H" : {"TGAACCTT" : "ATGGTTAG"}}, 
         

TGCTAAGT
TGTTCTCT
TAAGACAC
CTAATCGA
CTAGAACA
TAAGTTCC
TAGACCTA
TAGACCTA
         
        }

input = pd.read_excel("test_sample_sheet.xlsx")
input.replace(to_replace(dict1))
