# ============================================================
# AKIENI ACADEMY - Projet Sante Publique
# Semaine 2 - CHALLENGE ENTREPRISE : Rapport comparatif
# 3 hopitaux du departement du Pool
# Apprenant: M'BIELO-LIBEAU Davis Junior
# Date : 25/06/2026
# ============================================================

# --- DONNEES DES 3 HOPITAUX ---
# Hopital de Kinkala
h1_nom = 'Hopital District Kinkala'
h1_budget = 12_500_000
h1_consultations = 1847
h1_hospitalisations = 312
h1_deces = 8
h1_lits_total = 45
h1_lits_occupes = 41
h1_medecins = 3
h1_population = 85_000

# CMS de Vindza
h2_nom = 'CMS de Vindza'
h2_budget = 6_800_000
h2_consultations = 923
h2_hospitalisations = 87
h2_deces = 2
h2_lits_total = 20
h2_lits_occupes = 14
h2_medecins = 1
h2_population = 42_000

# Hopital de Kindamba
h3_nom = 'Hopital de Kindamba'
h3_budget = 9_200_000
h3_consultations = 1234
h3_hospitalisations = 201
h3_deces = 11
h3_lits_total = 35
h3_lits_occupes = 33
h3_medecins = 2
h3_population = 67_000

# --- CALCULS POUR CHAQUE HOPITAL ---
# Fonction pour arrondir à 2 décimales (sauf densité qu'on arrondit à 2 aussi)
# On va faire les calculs directement

# Hopital 1
h1_cout_moyen = h1_budget / h1_consultations
h1_taux_occupation = (h1_lits_occupes / h1_lits_total) * 100
h1_densite = (h1_medecins / h1_population) * 1000
h1_taux_mortalite = (h1_deces / h1_hospitalisations) * 100

# Hopital 2
h2_cout_moyen = h2_budget / h2_consultations
h2_taux_occupation = (h2_lits_occupes / h2_lits_total) * 100
h2_densite = (h2_medecins / h2_population) * 1000
h2_taux_mortalite = (h2_deces / h2_hospitalisations) * 100

# Hopital 3
h3_cout_moyen = h3_budget / h3_consultations
h3_taux_occupation = (h3_lits_occupes / h3_lits_total) * 100
h3_densite = (h3_medecins / h3_population) * 1000
h3_taux_mortalite = (h3_deces / h3_hospitalisations) * 100

# --- IDENTIFICATION DE L'HOPITAL CRITIQUE ---
# Critère : taux_mortalite > 2% OU densite < 0.05
critique_h1 = (h1_taux_mortalite > 2.0) or (h1_densite < 0.05)
critique_h2 = (h2_taux_mortalite > 2.0) or (h2_densite < 0.05)
critique_h3 = (h3_taux_mortalite > 2.0) or (h3_densite < 0.05)

# BONUS : budget total pour passer à 5 médecins chacun
# Coût d'un médecin par trimestre = 1 200 000 FCFA
cout_medecin_trimestre = 1_200_000
budget_total = h1_budget + h2_budget + h3_budget
besoin_total = (5 - h1_medecins + 5 - h2_medecins + 5 - h3_medecins) * cout_medecin_trimestre
# Calcul du nombre de médecins supplémentaires nécessaires :
# Pour h1: 5-3=2, h2:5-1=4, h3:5-2=3, total 9 médecins
# besoin_total = 9 * 1_200_000 = 10_800_000
# On peut aussi le calculer dynamiquement :

medecins_manquants = (5 - h1_medecins) + (5 - h2_medecins) + (5 - h3_medecins)
cout_ajout_medecins = medecins_manquants * cout_medecin_trimestre
budget_suffisant = budget_total >= cout_ajout_medecins

# --- AFFICHAGE RAPPORT CONSOLIDE ---
print('=' * 80)
print(' RAPPORT COMPARATIF DES 3 HOPITAUX DU DEPARTEMENT DU POOL')
print('=' * 80)
print()

# En-tête du tableau
print(f"{'Hopital':<25} {'Budget':>15} {'Cons.':>8} {'Cout moy.':>12} {'Taux occ.':>12} {'Densité':>12} {'Mortalité':>12} {'Critique'}")
print('-' * 100)

# Ligne 1
statut_h1 = 'OUI' if critique_h1 else 'NON'
print(f"{h1_nom:<25} {h1_budget:>15,} {h1_consultations:>8} {h1_cout_moyen:>12.0f} {h1_taux_occupation:>11.1f}% {h1_densite:>11.2f} {h1_taux_mortalite:>11.1f}% {statut_h1:>8}")

# Ligne 2
statut_h2 = 'OUI' if critique_h2 else 'NON'
print(f"{h2_nom:<25} {h2_budget:>15,} {h2_consultations:>8} {h2_cout_moyen:>12.0f} {h2_taux_occupation:>11.1f}% {h2_densite:>11.2f} {h2_taux_mortalite:>11.1f}% {statut_h2:>8}")

# Ligne 3
statut_h3 = 'OUI' if critique_h3 else 'NON'
print(f"{h3_nom:<25} {h3_budget:>15,} {h3_consultations:>8} {h3_cout_moyen:>12.0f} {h3_taux_occupation:>11.1f}% {h3_densite:>11.2f} {h3_taux_mortalite:>11.1f}% {statut_h3:>8}")

print('-' * 100)
print()

# --- DETAILS SUR L'HOPITAL CRITIQUE ---
if critique_h1:
    print(f"!!! ALERTE : {h1_nom} est en situation critique !!!")
    if h1_taux_mortalite > 2.0:
        print(f"   - Taux de mortalité = {h1_taux_mortalite:.1f}% (seuil > 2%)")
    if h1_densite < 0.05:
        print(f"   - Densité médicale = {h1_densite:.2f} pour 1000 hab (seuil < 0.05)")

if critique_h2:
    print(f"!!! ALERTE : {h2_nom} est en situation critique !!!")
    if h2_taux_mortalite > 2.0:
        print(f"   - Taux de mortalité = {h2_taux_mortalite:.1f}% (seuil > 2%)")
    if h2_densite < 0.05:
        print(f"   - Densité médicale = {h2_densite:.2f} pour 1000 hab (seuil < 0.05)")

if critique_h3:
    print(f"!!! ALERTE : {h3_nom} est en situation critique !!!")
    if h3_taux_mortalite > 2.0:
        print(f"   - Taux de mortalité = {h3_taux_mortalite:.1f}% (seuil > 2%)")
    if h3_densite < 0.05:
        print(f"   - Densité médicale = {h3_densite:.2f} pour 1000 hab (seuil < 0.05)")

# BONUS : budget suffisant ?
print()
print('=== BONUS : Budget pour 5 médecins par hopital ===')
print(f"Budget total des 3 hopitaux : {budget_total:,.0f} FCFA")
print(f"Nombre de médecins manquants : {medecins_manquants}")
print(f"Coût pour les recruter : {cout_ajout_medecins:,.0f} FCFA")
if budget_suffisant:
    print("STATUT : Le budget total SUFFIT pour recruter les médecins manquants.")
else:
    print("STATUT : Le budget total NE SUFFIT PAS (déficit de {:,.0f} FCFA)".format(cout_ajout_medecins - budget_total))