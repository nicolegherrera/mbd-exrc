# U is tracked 
# A is not tracked

def P_disease_given_A(P_disease, P_A_given_disease, P_A_given_no_disease):
    P_A = P_A_given_disease * P_disease + P_A_given_no_disease * (1 - P_disease)
    return (P_A_given_disease * P_disease) / P_A

def P_disease_given_A(P_disease, P_A_given_disease, P_A_given_no_disease):
    P_A = P_A_given_disease * P_disease + P_A_given_no_disease * (1 - P_disease)
    return (P_A_given_disease * P_disease) / P_A
