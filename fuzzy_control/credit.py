import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
import pdb

credit = ctrl.Antecedent(np.arange(300, 850, 1), 'credit')
credit['low'] = fuzz.trapmf(credit.universe, [300, 300, 550, 650])
credit['medium'] = fuzz.trapmf(credit.universe, [550, 650, 650, 750])
credit['high'] = fuzz.trapmf(credit.universe, [650, 750, 850, 850])
credit.view()

risk = ctrl.Consequent(np.arange(0, 1, 0.01), 'risk')
risk['low'] = fuzz.trapmf(risk.universe, [0, 0, 0.25, 0.3])
risk['medium'] = fuzz.trapmf(risk.universe, [0.25, 0.5, 0.5, 0.75])
risk['high'] = fuzz.trapmf(risk.universe, [0.5, 0.75, 1, 1])
risk.view()

rule1 = ctrl.Rule(credit['low'] ,risk['high'])
rule2 = ctrl.Rule(credit['medium'], risk['medium'])
rule3 = ctrl.Rule(credit['high'] , risk['low'])

risk_assessment_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
risk_assessment = ctrl.ControlSystemSimulation(risk_assessment_ctrl)

risk_assessment.input['credit'] = 600
risk_assessment.compute()
print(risk_assessment.output['risk'])
risk.view(sim=risk_assessment)
plt.show()