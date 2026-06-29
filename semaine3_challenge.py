# ===========================================
# AKIENI ACADEMY - Projet Sante Publique
# Semaine 3 - CHALLENGE : Rapport d'etat sanitaire departemental
# S2 + S3 : variables, calculs, conditions, and/or
# ===========================================

# --- DONNEES DES 5 HOPITAUX ---
# CHU Brazzaville
h1_nom = 'CHU Brazzaville'
h1_lits_total = 320
h1_lits_occupes = 298
h1_nb_medecins = 47
h1_ruptures = 2  # SRO, Vaccin
h1_alertes = 2   # Artemether, Amoxi

# Hopital Pointe-Noire
h2_nom = 'Hopital Pointe-Noire'
h2_lits_total = 180
h2_lits_occupes = 143
h2_nb_medecins = 22
h2_ruptures = 0
h2_alertes = 1   # Amoxicilline

# Hopital Dolisie
h3_nom = 'Hopital Dolisie'
h3_lits_total = 95
h3_lits_occupes = 91
h3_nb_medecins = 8
h3_ruptures = 1   # SRO
h3_alertes = 2    # Artemether, Vaccin

# Hopital Owando
h4_nom = 'Hopital Owando'
h4_lits_total = 45
h4_lits_occupes = 32
h4_nb_medecins = 3
h4_ruptures = 3   # SRO, Vaccin, Artemether
h4_alertes = 0

# CMS Impfondo
h5_nom = 'CMS Impfondo'
h5_lits_total = 20
h5_lits_occupes = 19
h5_nb_medecins = 1
h5_ruptures = 2   # SRO, Amoxi
h5_alertes = 1    # Vaccin

# --- CALCULS POUR CHAQUE HOPITAL ---
# Taux d'occupation (S2)
taux1 = (h1_lits_occupes / h1_lits_total) * 100
taux2 = (h2_lits_occupes / h2_lits_total) * 100
taux3 = (h3_lits_occupes / h3_lits_total) * 100
taux4 = (h4_lits_occupes / h4_lits_total) * 100
taux5 = (h5_lits_occupes / h5_lits_total) * 100

# Classification du niveau d'alerte global (S3)
# Regles : CRITIQUE si ruptures >= 2 OU taux > 95%
# PREOCCUPANT si ruptures >= 1 OU taux > 85% OU (alertes >= 2 ET medecins < 5)
# SATISFAISANT sinon

if h1_ruptures >= 2 or taux1 > 95:
    niv1 = 'CRITIQUE'
elif h1_ruptures >= 1 or taux1 > 85 or (h1_alertes >= 2 and h1_nb_medecins < 5):
    niv1 = 'PREOCCUPANT'
else:
    niv1 = 'SATISFAISANT'

if h2_ruptures >= 2 or taux2 > 95:
    niv2 = 'CRITIQUE'
elif h2_ruptures >= 1 or taux2 > 85 or (h2_alertes >= 2 and h2_nb_medecins < 5):
    niv2 = 'PREOCCUPANT'
else:
    niv2 = 'SATISFAISANT'

if h3_ruptures >= 2 or taux3 > 95:
    niv3 = 'CRITIQUE'
elif h3_ruptures >= 1 or taux3 > 85 or (h3_alertes >= 2 and h3_nb_medecins < 5):
    niv3 = 'PREOCCUPANT'
else:
    niv3 = 'SATISFAISANT'

if h4_ruptures >= 2 or taux4 > 95:
    niv4 = 'CRITIQUE'
elif h4_ruptures >= 1 or taux4 > 85 or (h4_alertes >= 2 and h4_nb_medecins < 5):
    niv4 = 'PREOCCUPANT'
else:
    niv4 = 'SATISFAISANT'

if h5_ruptures >= 2 or taux5 > 95:
    niv5 = 'CRITIQUE'
elif h5_ruptures >= 1 or taux5 > 85 or (h5_alertes >= 2 and h5_nb_medecins < 5):
    niv5 = 'PREOCCUPANT'
else:
    niv5 = 'SATISFAISANT'

# Classification du niveau d'occupation pour l'affichage
def classer_occupation(taux):
    if taux > 95:
        return 'CRI'
    elif taux > 85:
        return 'ALT'
    elif taux > 70:
        return 'OPT'
    else:
        return 'SOU'

occ1 = classer_occupation(taux1)
occ2 = classer_occupation(taux2)
occ3 = classer_occupation(taux3)
occ4 = classer_occupation(taux4)
occ5 = classer_occupation(taux5)

# --- BILAN NATIONAL (BONUS) ---
total_ruptures = h1_ruptures + h2_ruptures + h3_ruptures + h4_ruptures + h5_ruptures
total_alertes = h1_alertes + h2_alertes + h3_alertes + h4_alertes + h5_alertes

# Compter les niveaux globaux
nb_critique = 0
nb_preoccupant = 0
nb_satisfaisant = 0

if niv1 == 'CRITIQUE':
    nb_critique += 1
elif niv1 == 'PREOCCUPANT':
    nb_preoccupant += 1
else:
    nb_satisfaisant += 1

if niv2 == 'CRITIQUE':
    nb_critique += 1
elif niv2 == 'PREOCCUPANT':
    nb_preoccupant += 1
else:
    nb_satisfaisant += 1

if niv3 == 'CRITIQUE':
    nb_critique += 1
elif niv3 == 'PREOCCUPANT':
    nb_preoccupant += 1
else:
    nb_satisfaisant += 1

if niv4 == 'CRITIQUE':
    nb_critique += 1
elif niv4 == 'PREOCCUPANT':
    nb_preoccupant += 1
else:
    nb_satisfaisant += 1

if niv5 == 'CRITIQUE':
    nb_critique += 1
elif niv5 == 'PREOCCUPANT':
    nb_preoccupant += 1
else:
    nb_satisfaisant += 1

# BONUS : Coût des commandes urgentes
cout_express = 450_000  # FCFA
cout_total_urgent = total_ruptures * cout_express

# --- AFFICHAGE TABLEAU DE BORD ---
print('=' * 80)
print(' TABLEAU DE BORD SANITAIRE - MINISTERE DE LA SANTE')
print(' Date : 16 janvier 2026 | Pour le Conseil des Ministres')
print('=' * 80)
print(f"{'HOPITAL':<20} {'OCCUPATION':>12} {'ALERTES':>12} {'NIVEAU GLOBAL':>20}")
print('-' * 80)

print(f"{h1_nom:<20} {taux1:>6.1f}% [{occ1}] {h1_ruptures}R+{h1_alertes}A {niv1:>20}")
print(f"{h2_nom:<20} {taux2:>6.1f}% [{occ2}] {h2_ruptures}R+{h2_alertes}A {niv2:>20}")
print(f"{h3_nom:<20} {taux3:>6.1f}% [{occ3}] {h3_ruptures}R+{h3_alertes}A {niv3:>20}")
print(f"{h4_nom:<20} {taux4:>6.1f}% [{occ4}] {h4_ruptures}R+{h4_alertes}A {niv4:>20}")
print(f"{h5_nom:<20} {taux5:>6.1f}% [{occ5}] {h5_ruptures}R+{h5_alertes}A {niv5:>20}")

print('-' * 80)
print(f'{nb_critique} hopitaux sur 5 en situation CRITIQUE')
print(f'{total_ruptures} ruptures de stock identifiees a l\'echelle nationale')
print(f'Coût estime des commandes urgentes : {cout_total_urgent:,.0f} FCFA')
print()
if nb_critique > 0:
    print('RECOMMANDATION PRIORITAIRE : Mobiliser la reserve nationale PNA')