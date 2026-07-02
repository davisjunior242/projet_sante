# =========================================
# AKIENI ACADEMY - Projet Sante Publique
# Semaine 2 - Exercice 1 : Fiche Patient CHU Brazzaville
# Apprenant : M'BIELO-LIBEAU Davis Junior
# Date : 25/06/2026
# =========================================

# --- SECTION 1 : VARIABLES PATIENT (FIXES) ---
nom_patient = 'MAVOUNGOU Celestine'
sexe_patient = 'F'
departement_patient = 'Brazzaville'
couverture_sociale = 'CNSS'

# --- SECTION 2 : SAISIE UTILISATEUR AVEC GESTION D'ERREURS ---
print("=== SAISIE DES INFORMATIONS DE CONSULTATION ===")

# Boucle pour l'âge avec gestion d'erreur
while True:
    age_input = input("Entrez l'âge du patient (en années entières) : ")
    try:
        age_patient = int(age_input)
        break  # Sortie de la boucle si la conversion réussit
    except ValueError:
        print("ERREUR : Veuillez entrer un nombre entier valide pour l'âge.")
        # Le programme continue la boucle, redemandant la saisie

# Boucle pour le coût de la consultation avec gestion d'erreur
while True:
    cout_input = input("Entrez le coût unitaire de la consultation (en FCFA) : ")
    try:
        cout_consultation_fcfa = float(cout_input)
        break  # Sortie de la boucle si la conversion réussit
    except ValueError:
        print("ERREUR : Veuillez entrer un nombre valide (ex: 15000 ou 15000.50).")
        # Le programme continue la boucle, redemandant la saisie

# Boucle pour le nombre de consultations avec gestion d'erreur
while True:
    nb_input = input("Entrez le nombre de consultations réalisées : ")
    try:
        nb_consultations = int(nb_input)
        break  # Sortie de la boucle si la conversion réussit
    except ValueError:
        print("ERREUR : Veuillez entrer un nombre entier valide.")
        # Le programme continue la boucle, redemandant la saisie

# --- VARIABLES FIXES POUR LA CONSULTATION ET L'HOPITAL ---
type_consultation = 'Urgences'
remise_cnss_pct = 30.0
diagnostic_principal = 'Paludisme grave'
nom_hopital = 'CHU de Brazzaville'
ville_hopital = 'Brazzaville'
nb_lits_total = 320
nb_lits_occupes = 284
nb_medecins_actifs = 47

# --- SECTION 4 : CALCULS ---
# Calcul du coût total après remise CNSS
cout_total_fcfa = cout_consultation_fcfa * nb_consultations * (1 - remise_cnss_pct / 100)

# Calcul du taux d'occupation (en pourcentage, arrondi à 1 décimale)
taux_occupation_pct = round(nb_lits_occupes / nb_lits_total * 100, 1)

# Calcul du ratio consultations par médecin (ce jour)
# Hypothèse : 120 consultations ont eu lieu ce matin dans tout l'hôpital
nb_consultations_hopital = 120
ratio_consultations_medecin = round(nb_consultations_hopital / nb_medecins_actifs, 1)

# --- SECTION 5 : AFFICHAGE ---
print('\n' + '=' * 60)
print(f' FICHE PATIENT - {nom_patient}')
print('=' * 60)
print(f'Âge : {age_patient} ans')
print(f'Sexe : {sexe_patient}')
print(f'Département : {departement_patient}')
print(f'Couverture : {couverture_sociale}')
print()
print('CONSULTATION')
print(f'Type : {type_consultation}')
print(f'Diagnostic : {diagnostic_principal}')
print(f'Coût unitaire : {cout_consultation_fcfa:,.0f} FCFA')
print(f'Remise CNSS : {remise_cnss_pct}%')
print(f'COUT TOTAL : {cout_total_fcfa:.1f} FCFA')
print()
print(f'HOPITAL : {nom_hopital}')
print(f'Ville : {ville_hopital}')
print(f'Lits occupés : {nb_lits_occupes} / {nb_lits_total} ({taux_occupation_pct}%)')
print(f'Médecins actifs : {nb_medecins_actifs}')
print()
print(f'Ratio consult. : {ratio_consultations_medecin} consultations / médecin ce matin')
print()
print('STATUT : Prise en charge validée')
print('=' * 60)