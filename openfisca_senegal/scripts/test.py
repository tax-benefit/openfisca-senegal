from openfisca_senegal import CountryTaxBenefitSystem as SenegalTBS
from openfisca_senegal.scenarios import init_single_entity

tax_benefit_system = SenegalTBS()

scenario = tax_benefit_system.new_scenario()

init_single_entity(
    scenario,
    parent1 = {
        'salaire_imposable': 1800000,
        'est_marie': True,
        'conjoint_a_des_revenus': False,
        'nombre_enfants': 2,
        },
    period='2015',
    )

simulation = scenario.new_simulation()
assert all(simulation.calculate("salaire_imposable", period = 2015) == 1800000)
# print('Salaire retenu :')
# print(simulation.individu('salaire_imposable', period='2015'))
# print('Impot avant réduction famille :')
# print(simulation.individu('droit_progressif', period='2015'))
# print('Réduction pour charge famille :')
# print(simulation.individu('reduction_impots_pour_charge_famille', period='2015'))
# print('Impot pour la famille :')
# print(simulation.individu('impot_revenus', period='2015'))
