from IPython.display import display, Latex
print("If the rate of mRNA production reaches a plateau, we have reached a steady state where k_elong*Pe (the rate of mRNA production) does not depend on time anymore. ")
print(" Using the steady state solution of the model, we can see that the two variables Y that we measure, i.e. Y=dmRNA/dt and the number of nucleoplasmic polymerases Y=Pc both depend on all model parameters. As such, for both these variables, dY/dk_i is not 0 so they are sensitive to these model parameters.")
print(" However, for instance if k_p is multiplied by 3, ans simultaneously k_q is also multiplied by 3, both dmRNA/dt and P_c don't change: hence, those measurable quantities do not depend independently on the different parameters (in fact, they just depend on a huge function of all parameters): in this case, the parameters are also non-iodentifiable, individually. But we can remark that they are related by:")
display(Latex('$ dmRNA/dt=Pc*[(k_{elong}*k_{on})/(k_{off}+k_{elong})]$'))
print(" Hence, combining these two measurements yields the ratio")
display(Latex('$ [(k_{elong}*k_{on})/(k_{off}+k_{elong})]$'))
print(" Individually, the parameters are non-identifiable, but collectively they are constrained by the measurements. If k_on and k_off are known from previous studies in the same context, k_elong becomes identifiable")
print("In the regime where k_elong is very fast compare to the on and off dynamics (which is not realistic - just to make the point), the later ratio becomes approximately k_on. In this regime of very fast transcription, measuring the ratio of the rate of mRNA production to the mobile, nucleoplasmic pool of polymerase complexes is a direct readout for k_on, that becomes identifiable. This is an important notion to have in mind: with a given set of available data, and a given model for interpretation, the identifiability of certain parameters from the data might depend on the parameters themselves. Hence, a first estimation of the parameters with a global fitting might indicate in which parameter regime the model has to be considered, and then the identifiability of all parameters has to be studied in this regime.")