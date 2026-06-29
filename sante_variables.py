# =============================================================
# MODULE FONDATEUR – Projet Sante Publique / Akieni Academy
# Ce fichier centralise toutes les constantes et variables metier
# Il sera enrichi chaque semaine jusqu'a S24
# =============================================================

# === SECTION A : CONSTANTES NATIONALES ET NORMES OMS ===
TAUX_EUR_FCFA = 655.957
TAUX_USD_FCFA = 600.0
SEUIL_OMS_DENSITE_MEDICALE = 2.3  # medecins pour 1000 habitants
SEUIL_OMS_COUVERTURE_VACCIN = 95.0  # pourcentage minimum OMS
SEUIL_MORTALITE_ALERTE = 2.0  # % deces / hospitalisations
SEUIL_RUPTURE_STOCK_JOURS = 30  # jours minimum de stock

DEPARTEMENTS_CONGO = [
    'Brazzaville', 'Pointe-Noire', 'Bouenza', 'Cuvette',
    'Cuvette-Ouest', 'Kouilou', 'Lekoumou', 'Likouala',
    'Niari', 'Plateaux', 'Pool', 'Sangha'
]

# === SECTION B : VARIABLES DES 5 HOPITAUX ===
h1_nom = 'CHU de Brazzaville'
h1_ville = 'Brazzaville'
h1_departement = 'Brazzaville'
h1_type = 'CHU'
h1_nb_lits = 320
h1_nb_lits_occupes = 284
h1_nb_medecins = 47
h1_nb_infirmiers = 123
h1_population_zone = 1_800_000

h2_nom = 'Hopital General de Pointe-Noire'
h2_ville = 'Pointe-Noire'
h2_departement = 'Pointe-Noire'
h2_type = 'Hopital General'
h2_nb_lits = 250
h2_nb_lits_occupes = 218
h2_nb_medecins = 32
h2_nb_infirmiers = 95
h2_population_zone = 1_200_000

h3_nom = 'Hopital de Dolisie'
h3_ville = 'Dolisie'
h3_departement = 'Niari'
h3_type = 'Hopital de district'
h3_nb_lits = 120
h3_nb_lits_occupes = 92
h3_nb_medecins = 12
h3_nb_infirmiers = 45
h3_population_zone = 350_000

h4_nom = 'Hopital de district Owando'
h4_ville = 'Owando'
h4_departement = 'Cuvette'
h4_type = 'Hopital de district'
h4_nb_lits = 80
h4_nb_lits_occupes = 63
h4_nb_medecins = 8
h4_nb_infirmiers = 30
h4_population_zone = 180_000

h5_nom = 'Centre de sante de Impfondo'
h5_ville = 'Impfondo'
h5_departement = 'Likouala'
h5_type = 'Centre de sante'
h5_nb_lits = 40
h5_nb_lits_occupes = 28
h5_nb_medecins = 3
h5_nb_infirmiers = 18
h5_population_zone = 75_000

# === SECTION C : VARIABLES DES 5 MEDICAMENTS ===
m1_nom = 'Artemether-Lumefantrine'
m1_categorie = 'Antipaludeen'
m1_quantite_disponible = 8450
m1_seuil_rupture = 2000
m1_cout_unitaire = 3500.0

m2_nom = 'Amoxicilline 500mg'
m2_categorie = 'Antibiotique'
m2_quantite_disponible = 3200
m2_seuil_rupture = 800
m2_cout_unitaire = 850.0

m3_nom = 'Paracetamol 500mg'
m3_categorie = 'Antalgique'
m3_quantite_disponible = 12000
m3_seuil_rupture = 3000
m3_cout_unitaire = 250.0

m4_nom = 'Sels de rehydratation orale'
m4_categorie = 'Rehydratation'
m4_quantite_disponible = 15600
m4_seuil_rupture = 5000
m4_cout_unitaire = 125.0

m5_nom = 'Vaccin antiplaudeen'
m5_categorie = 'Vaccin'
m5_quantite_disponible = 2300
m5_seuil_rupture = 500
m5_cout_unitaire = 8500.0

# === SECTION D : CALCULS D'INITIALISATION (S2) ===
# KPIs globaux
total_medecins = h1_nb_medecins + h2_nb_medecins + h3_nb_medecins + h4_nb_medecins + h5_nb_medecins
total_population = h1_population_zone + h2_population_zone + h3_population_zone + h4_population_zone + h5_population_zone
densite_nationale = (total_medecins / total_population) * 1000

total_lits = h1_nb_lits + h2_nb_lits + h3_nb_lits + h4_nb_lits + h5_nb_lits
total_lits_occupes = h1_nb_lits_occupes + h2_nb_lits_occupes + h3_nb_lits_occupes + h4_nb_lits_occupes + h5_nb_lits_occupes
taux_occupation_moyen = (total_lits_occupes / total_lits) * 100

# Calcul des taux d'occupation individuels (pour S3 Section G)
taux_occupation_h1 = (h1_nb_lits_occupes / h1_nb_lits) * 100
taux_occupation_h2 = (h2_nb_lits_occupes / h2_nb_lits) * 100
taux_occupation_h3 = (h3_nb_lits_occupes / h3_nb_lits) * 100
taux_occupation_h4 = (h4_nb_lits_occupes / h4_nb_lits) * 100
taux_occupation_h5 = (h5_nb_lits_occupes / h5_nb_lits) * 100

# Valeur du stock
valeur_stock_m1 = m1_quantite_disponible * m1_cout_unitaire
valeur_stock_m2 = m2_quantite_disponible * m2_cout_unitaire
valeur_stock_m3 = m3_quantite_disponible * m3_cout_unitaire
valeur_stock_m4 = m4_quantite_disponible * m4_cout_unitaire
valeur_stock_m5 = m5_quantite_disponible * m5_cout_unitaire
valeur_totale_stock = valeur_stock_m1 + valeur_stock_m2 + valeur_stock_m3 + valeur_stock_m4 + valeur_stock_m5

# === SECTION E : RAPPORT INITIAL (S2) ===
print('=' * 70)
print(' RAPPORT INITIAL DU SYSTEME DE SANTE CONGOLAIS (S2)')
print('=' * 70)
print()
print('--- CONSTANTES NATIONALES ---')
print(f'Taux de change EUR/FCFA : {TAUX_EUR_FCFA}')
print(f'Taux de change USD/FCFA : {TAUX_USD_FCFA}')
print(f'Seuil OMS densite medicale : {SEUIL_OMS_DENSITE_MEDICALE} medecins/1000 hab')
print(f'Seuil OMS couverture vaccinale : {SEUIL_OMS_COUVERTURE_VACCIN}%')
print(f'Seuil alerte mortalite : {SEUIL_MORTALITE_ALERTE}%')
print(f'Seuil rupture stock (jours) : {SEUIL_RUPTURE_STOCK_JOURS}')
print(f'Nombre de departements : {len(DEPARTEMENTS_CONGO)}')
print()
print('--- HOPITAUX ENREGISTRES ---')
print(f"1. {h1_nom} - {h1_ville} ({h1_departement}) - {h1_type} - Lits: {h1_nb_lits_occupes}/{h1_nb_lits} - Medecins: {h1_nb_medecins}")
print(f"2. {h2_nom} - {h2_ville} ({h2_departement}) - {h2_type} - Lits: {h2_nb_lits_occupes}/{h2_nb_lits} - Medecins: {h2_nb_medecins}")
print(f"3. {h3_nom} - {h3_ville} ({h3_departement}) - {h3_type} - Lits: {h3_nb_lits_occupes}/{h3_nb_lits} - Medecins: {h3_nb_medecins}")
print(f"4. {h4_nom} - {h4_ville} ({h4_departement}) - {h4_type} - Lits: {h4_nb_lits_occupes}/{h4_nb_lits} - Medecins: {h4_nb_medecins}")
print(f"5. {h5_nom} - {h5_ville} ({h5_departement}) - {h5_type} - Lits: {h5_nb_lits_occupes}/{h5_nb_lits} - Medecins: {h5_nb_medecins}")
print()
print('--- MEDICAMENTS ESSENTIELS ---')
print(f"1. {m1_nom} - Stock: {m1_quantite_disponible} unites (Seuil: {m1_seuil_rupture}) - Prix: {m1_cout_unitaire:.0f} FCFA")
print(f"2. {m2_nom} - Stock: {m2_quantite_disponible} unites (Seuil: {m2_seuil_rupture}) - Prix: {m2_cout_unitaire:.0f} FCFA")
print(f"3. {m3_nom} - Stock: {m3_quantite_disponible} unites (Seuil: {m3_seuil_rupture}) - Prix: {m3_cout_unitaire:.0f} FCFA")
print(f"4. {m4_nom} - Stock: {m4_quantite_disponible} unites (Seuil: {m4_seuil_rupture}) - Prix: {m4_cout_unitaire:.0f} FCFA")
print(f"5. {m5_nom} - Stock: {m5_quantite_disponible} unites (Seuil: {m5_seuil_rupture}) - Prix: {m5_cout_unitaire:.0f} FCFA")
print()
print('--- INDICATEURS GLOBAUX ---')
print(f"Densite medicale nationale : {densite_nationale:.2f} medecins/1000 hab (Objectif OMS: >= {SEUIL_OMS_DENSITE_MEDICALE})")
print(f"Taux d'occupation moyen des lits : {taux_occupation_moyen:.1f}% (Optimal: 70-85%)")
print(f"Valeur totale du stock de medicaments : {valeur_totale_stock:,.0f} FCFA")
print()
print('--- ALERTES (si applicable) ---')
if densite_nationale < SEUIL_OMS_DENSITE_MEDICALE:
    print("ALERTE : Densite medicale nationale inferieure au seuil OMS !")
if not (70 <= taux_occupation_moyen <= 85):
    print("ALERTE : Taux d'occupation moyen en dehors de la plage optimale (70-85%)")
print()
print('=' * 70)
print(' FIN DU RAPPORT INITIAL')
print('=' * 70)
print('\n\n')

# =============================================================
# === NOUVEAUTES SEMAINE 3 - SECTIONS F, G, H, I ===
# =============================================================

# === SECTION F : CLASSIFICATION AUTOMATIQUE DES STOCKS ===
# (if/elif/else pour chaque medicament)
if m1_quantite_disponible <= m1_seuil_rupture:
    m1_statut = 'RUPTURE CRITIQUE'
    m1_couleur = '[ROUGE]'
    m1_action = 'Alerte immediate PNA - commande express sous 24h'
elif m1_quantite_disponible <= m1_seuil_rupture * 1.5:
    m1_statut = 'ALERTE STOCK'
    m1_couleur = '[ORANGE]'
    m1_action = 'Commande urgente a declencher sous 72h'
elif m1_quantite_disponible <= m1_seuil_rupture * 2.0:
    m1_statut = 'STOCK LIMITE'
    m1_couleur = '[JAUNE]'
    m1_action = 'Surveillance renforcee - planifier commande'
else:
    m1_statut = 'STOCK NORMAL'
    m1_couleur = '[VERT]'
    m1_action = 'Situation normale - suivi standard'

if m2_quantite_disponible <= m2_seuil_rupture:
    m2_statut = 'RUPTURE CRITIQUE'
    m2_couleur = '[ROUGE]'
    m2_action = 'Alerte immediate PNA - commande express sous 24h'
elif m2_quantite_disponible <= m2_seuil_rupture * 1.5:
    m2_statut = 'ALERTE STOCK'
    m2_couleur = '[ORANGE]'
    m2_action = 'Commande urgente a declencher sous 72h'
elif m2_quantite_disponible <= m2_seuil_rupture * 2.0:
    m2_statut = 'STOCK LIMITE'
    m2_couleur = '[JAUNE]'
    m2_action = 'Surveillance renforcee - planifier commande'
else:
    m2_statut = 'STOCK NORMAL'
    m2_couleur = '[VERT]'
    m2_action = 'Situation normale - suivi standard'

if m3_quantite_disponible <= m3_seuil_rupture:
    m3_statut = 'RUPTURE CRITIQUE'
    m3_couleur = '[ROUGE]'
    m3_action = 'Alerte immediate PNA - commande express sous 24h'
elif m3_quantite_disponible <= m3_seuil_rupture * 1.5:
    m3_statut = 'ALERTE STOCK'
    m3_couleur = '[ORANGE]'
    m3_action = 'Commande urgente a declencher sous 72h'
elif m3_quantite_disponible <= m3_seuil_rupture * 2.0:
    m3_statut = 'STOCK LIMITE'
    m3_couleur = '[JAUNE]'
    m3_action = 'Surveillance renforcee - planifier commande'
else:
    m3_statut = 'STOCK NORMAL'
    m3_couleur = '[VERT]'
    m3_action = 'Situation normale - suivi standard'

if m4_quantite_disponible <= m4_seuil_rupture:
    m4_statut = 'RUPTURE CRITIQUE'
    m4_couleur = '[ROUGE]'
    m4_action = 'Alerte immediate PNA - commande express sous 24h'
elif m4_quantite_disponible <= m4_seuil_rupture * 1.5:
    m4_statut = 'ALERTE STOCK'
    m4_couleur = '[ORANGE]'
    m4_action = 'Commande urgente a declencher sous 72h'
elif m4_quantite_disponible <= m4_seuil_rupture * 2.0:
    m4_statut = 'STOCK LIMITE'
    m4_couleur = '[JAUNE]'
    m4_action = 'Surveillance renforcee - planifier commande'
else:
    m4_statut = 'STOCK NORMAL'
    m4_couleur = '[VERT]'
    m4_action = 'Situation normale - suivi standard'

if m5_quantite_disponible <= m5_seuil_rupture:
    m5_statut = 'RUPTURE CRITIQUE'
    m5_couleur = '[ROUGE]'
    m5_action = 'Alerte immediate PNA - commande express sous 24h'
elif m5_quantite_disponible <= m5_seuil_rupture * 1.5:
    m5_statut = 'ALERTE STOCK'
    m5_couleur = '[ORANGE]'
    m5_action = 'Commande urgente a declencher sous 72h'
elif m5_quantite_disponible <= m5_seuil_rupture * 2.0:
    m5_statut = 'STOCK LIMITE'
    m5_couleur = '[JAUNE]'
    m5_action = 'Surveillance renforcee - planifier commande'
else:
    m5_statut = 'STOCK NORMAL'
    m5_couleur = '[VERT]'
    m5_action = 'Situation normale - suivi standard'

# === SECTION G : CLASSIFICATION OCCUPATION DES 5 HOPITAUX ===
# (if/elif/else)
if taux_occupation_h1 > 95:
    occ1 = 'OCCUPATION CRITIQUE'
    occ1_couleur = '[ROUGE]'
    occ1_action = 'Transferts a organiser d\'urgence'
elif taux_occupation_h1 > 85:
    occ1 = 'OCCUPATION ELEVEE'
    occ1_couleur = '[ORANGE]'
    occ1_action = 'Renforcement prevu - capacite limite'
elif taux_occupation_h1 > 70:
    occ1 = 'OCCUPATION OPTIMALE'
    occ1_couleur = '[VERT]'
    occ1_action = 'Situation normale'
else:
    occ1 = 'SOUS-UTILISATION'
    occ1_couleur = '[JAUNE]'
    occ1_action = 'Ressources sous-exploitees'

if taux_occupation_h2 > 95:
    occ2 = 'OCCUPATION CRITIQUE'
    occ2_couleur = '[ROUGE]'
    occ2_action = 'Transferts a organiser d\'urgence'
elif taux_occupation_h2 > 85:
    occ2 = 'OCCUPATION ELEVEE'
    occ2_couleur = '[ORANGE]'
    occ2_action = 'Renforcement prevu - capacite limite'
elif taux_occupation_h2 > 70:
    occ2 = 'OCCUPATION OPTIMALE'
    occ2_couleur = '[VERT]'
    occ2_action = 'Situation normale'
else:
    occ2 = 'SOUS-UTILISATION'
    occ2_couleur = '[JAUNE]'
    occ2_action = 'Ressources sous-exploitees'

if taux_occupation_h3 > 95:
    occ3 = 'OCCUPATION CRITIQUE'
    occ3_couleur = '[ROUGE]'
    occ3_action = 'Transferts a organiser d\'urgence'
elif taux_occupation_h3 > 85:
    occ3 = 'OCCUPATION ELEVEE'
    occ3_couleur = '[ORANGE]'
    occ3_action = 'Renforcement prevu - capacite limite'
elif taux_occupation_h3 > 70:
    occ3 = 'OCCUPATION OPTIMALE'
    occ3_couleur = '[VERT]'
    occ3_action = 'Situation normale'
else:
    occ3 = 'SOUS-UTILISATION'
    occ3_couleur = '[JAUNE]'
    occ3_action = 'Ressources sous-exploitees'

if taux_occupation_h4 > 95:
    occ4 = 'OCCUPATION CRITIQUE'
    occ4_couleur = '[ROUGE]'
    occ4_action = 'Transferts a organiser d\'urgence'
elif taux_occupation_h4 > 85:
    occ4 = 'OCCUPATION ELEVEE'
    occ4_couleur = '[ORANGE]'
    occ4_action = 'Renforcement prevu - capacite limite'
elif taux_occupation_h4 > 70:
    occ4 = 'OCCUPATION OPTIMALE'
    occ4_couleur = '[VERT]'
    occ4_action = 'Situation normale'
else:
    occ4 = 'SOUS-UTILISATION'
    occ4_couleur = '[JAUNE]'
    occ4_action = 'Ressources sous-exploitees'

if taux_occupation_h5 > 95:
    occ5 = 'OCCUPATION CRITIQUE'
    occ5_couleur = '[ROUGE]'
    occ5_action = 'Transferts a organiser d\'urgence'
elif taux_occupation_h5 > 85:
    occ5 = 'OCCUPATION ELEVEE'
    occ5_couleur = '[ORANGE]'
    occ5_action = 'Renforcement prevu - capacite limite'
elif taux_occupation_h5 > 70:
    occ5 = 'OCCUPATION OPTIMALE'
    occ5_couleur = '[VERT]'
    occ5_action = 'Situation normale'
else:
    occ5 = 'SOUS-UTILISATION'
    occ5_couleur = '[JAUNE]'
    occ5_action = 'Ressources sous-exploitees'

# === SECTION H : CLASSIFICATION DE LA COUVERTURE VACCINALE ===
# (if/elif/else avec constantes OMS)
# Donnees : Brazzaville, Pointe-Noire, Pool, Sangha
taux_brazzaville = (418500 / 450000) * 100
taux_pointe_noire = (229600 / 280000) * 100
taux_pool = (54000 / 120000) * 100
taux_sangha = (35700 / 85000) * 100

if taux_brazzaville < 50:
    statut_brazzaville = 'ZONE CRITIQUE'
    couleur_brazzaville = '[ROUGE]'
    action_brazzaville = 'Campagne d\'urgence obligatoire'
elif taux_brazzaville < 80:
    statut_brazzaville = 'ZONE A RISQUE'
    couleur_brazzaville = '[ORANGE]'
    action_brazzaville = 'Campagne renforcee requise'
elif taux_brazzaville < SEUIL_OMS_COUVERTURE_VACCIN:
    statut_brazzaville = 'ZONE INSUFFISANTE'
    couleur_brazzaville = '[JAUNE]'
    action_brazzaville = 'Objectif OMS non atteint'
else:
    statut_brazzaville = 'ZONE OMS CONFORME'
    couleur_brazzaville = '[VERT]'
    action_brazzaville = 'Objectif OMS atteint'

if taux_pointe_noire < 50:
    statut_pointe_noire = 'ZONE CRITIQUE'
    couleur_pointe_noire = '[ROUGE]'
    action_pointe_noire = 'Campagne d\'urgence obligatoire'
elif taux_pointe_noire < 80:
    statut_pointe_noire = 'ZONE A RISQUE'
    couleur_pointe_noire = '[ORANGE]'
    action_pointe_noire = 'Campagne renforcee requise'
elif taux_pointe_noire < SEUIL_OMS_COUVERTURE_VACCIN:
    statut_pointe_noire = 'ZONE INSUFFISANTE'
    couleur_pointe_noire = '[JAUNE]'
    action_pointe_noire = 'Objectif OMS non atteint'
else:
    statut_pointe_noire = 'ZONE OMS CONFORME'
    couleur_pointe_noire = '[VERT]'
    action_pointe_noire = 'Objectif OMS atteint'

if taux_pool < 50:
    statut_pool = 'ZONE CRITIQUE'
    couleur_pool = '[ROUGE]'
    action_pool = 'Campagne d\'urgence obligatoire'
elif taux_pool < 80:
    statut_pool = 'ZONE A RISQUE'
    couleur_pool = '[ORANGE]'
    action_pool = 'Campagne renforcee requise'
elif taux_pool < SEUIL_OMS_COUVERTURE_VACCIN:
    statut_pool = 'ZONE INSUFFISANTE'
    couleur_pool = '[JAUNE]'
    action_pool = 'Objectif OMS non atteint'
else:
    statut_pool = 'ZONE OMS CONFORME'
    couleur_pool = '[VERT]'
    action_pool = 'Objectif OMS atteint'

if taux_sangha < 50:
    statut_sangha = 'ZONE CRITIQUE'
    couleur_sangha = '[ROUGE]'
    action_sangha = 'Campagne d\'urgence obligatoire'
elif taux_sangha < 80:
    statut_sangha = 'ZONE A RISQUE'
    couleur_sangha = '[ORANGE]'
    action_sangha = 'Campagne renforcee requise'
elif taux_sangha < SEUIL_OMS_COUVERTURE_VACCIN:
    statut_sangha = 'ZONE INSUFFISANTE'
    couleur_sangha = '[JAUNE]'
    action_sangha = 'Objectif OMS non atteint'
else:
    statut_sangha = 'ZONE OMS CONFORME'
    couleur_sangha = '[VERT]'
    action_sangha = 'Objectif OMS atteint'

# === SECTION I : RAPPORT D'ETAT GLOBAL AVEC COMPTEURS ===
# Compteurs pour les médicaments
nb_ruptures = 0
nb_alertes = 0
nb_normaux = 0

if m1_statut == 'RUPTURE CRITIQUE':
    nb_ruptures += 1
elif m1_statut == 'ALERTE STOCK':
    nb_alertes += 1
else:
    nb_normaux += 1

if m2_statut == 'RUPTURE CRITIQUE':
    nb_ruptures += 1
elif m2_statut == 'ALERTE STOCK':
    nb_alertes += 1
else:
    nb_normaux += 1

if m3_statut == 'RUPTURE CRITIQUE':
    nb_ruptures += 1
elif m3_statut == 'ALERTE STOCK':
    nb_alertes += 1
else:
    nb_normaux += 1

if m4_statut == 'RUPTURE CRITIQUE':
    nb_ruptures += 1
elif m4_statut == 'ALERTE STOCK':
    nb_alertes += 1
else:
    nb_normaux += 1

if m5_statut == 'RUPTURE CRITIQUE':
    nb_ruptures += 1
elif m5_statut == 'ALERTE STOCK':
    nb_alertes += 1
else:
    nb_normaux += 1

# Compteurs pour les occupations
nb_occup_critique = 0
nb_occup_elevee = 0
nb_occup_optimale = 0
nb_occup_sous = 0

if occ1 == 'OCCUPATION CRITIQUE':
    nb_occup_critique += 1
elif occ1 == 'OCCUPATION ELEVEE':
    nb_occup_elevee += 1
elif occ1 == 'OCCUPATION OPTIMALE':
    nb_occup_optimale += 1
else:
    nb_occup_sous += 1

if occ2 == 'OCCUPATION CRITIQUE':
    nb_occup_critique += 1
elif occ2 == 'OCCUPATION ELEVEE':
    nb_occup_elevee += 1
elif occ2 == 'OCCUPATION OPTIMALE':
    nb_occup_optimale += 1
else:
    nb_occup_sous += 1

if occ3 == 'OCCUPATION CRITIQUE':
    nb_occup_critique += 1
elif occ3 == 'OCCUPATION ELEVEE':
    nb_occup_elevee += 1
elif occ3 == 'OCCUPATION OPTIMALE':
    nb_occup_optimale += 1
else:
    nb_occup_sous += 1

if occ4 == 'OCCUPATION CRITIQUE':
    nb_occup_critique += 1
elif occ4 == 'OCCUPATION ELEVEE':
    nb_occup_elevee += 1
elif occ4 == 'OCCUPATION OPTIMALE':
    nb_occup_optimale += 1
else:
    nb_occup_sous += 1

if occ5 == 'OCCUPATION CRITIQUE':
    nb_occup_critique += 1
elif occ5 == 'OCCUPATION ELEVEE':
    nb_occup_elevee += 1
elif occ5 == 'OCCUPATION OPTIMALE':
    nb_occup_optimale += 1
else:
    nb_occup_sous += 1

# Compteurs pour les vaccinations
nb_vacc_critique = 0
nb_vacc_risque = 0
nb_vacc_insuffisant = 0
nb_vacc_conforme = 0

if statut_brazzaville == 'ZONE CRITIQUE':
    nb_vacc_critique += 1
elif statut_brazzaville == 'ZONE A RISQUE':
    nb_vacc_risque += 1
elif statut_brazzaville == 'ZONE INSUFFISANTE':
    nb_vacc_insuffisant += 1
else:
    nb_vacc_conforme += 1

if statut_pointe_noire == 'ZONE CRITIQUE':
    nb_vacc_critique += 1
elif statut_pointe_noire == 'ZONE A RISQUE':
    nb_vacc_risque += 1
elif statut_pointe_noire == 'ZONE INSUFFISANTE':
    nb_vacc_insuffisant += 1
else:
    nb_vacc_conforme += 1

if statut_pool == 'ZONE CRITIQUE':
    nb_vacc_critique += 1
elif statut_pool == 'ZONE A RISQUE':
    nb_vacc_risque += 1
elif statut_pool == 'ZONE INSUFFISANTE':
    nb_vacc_insuffisant += 1
else:
    nb_vacc_conforme += 1

if statut_sangha == 'ZONE CRITIQUE':
    nb_vacc_critique += 1
elif statut_sangha == 'ZONE A RISQUE':
    nb_vacc_risque += 1
elif statut_sangha == 'ZONE INSUFFISANTE':
    nb_vacc_insuffisant += 1
else:
    nb_vacc_conforme += 1

# --- AFFICHAGE DU RAPPORT GLOBAL (S3) ---
print('=' * 70)
print(' RAPPORT D\'ETAT GLOBAL - SYSTEME DE SANTE CONGOLAIS (S3)')
print('=' * 70)
print()

print('--- CLASSIFICATION DES STOCKS MEDICAMENTS ---')
print(f'{m1_couleur} {m1_nom} : {m1_statut} (Stock: {m1_quantite_disponible}, Seuil: {m1_seuil_rupture})')
print(f'{m2_couleur} {m2_nom} : {m2_statut} (Stock: {m2_quantite_disponible}, Seuil: {m2_seuil_rupture})')
print(f'{m3_couleur} {m3_nom} : {m3_statut} (Stock: {m3_quantite_disponible}, Seuil: {m3_seuil_rupture})')
print(f'{m4_couleur} {m4_nom} : {m4_statut} (Stock: {m4_quantite_disponible}, Seuil: {m4_seuil_rupture})')
print(f'{m5_couleur} {m5_nom} : {m5_statut} (Stock: {m5_quantite_disponible}, Seuil: {m5_seuil_rupture})')
print()

print('--- CLASSIFICATION OCCUPATION DES HOPITAUX ---')
print(f'{occ1_couleur} {h1_nom} : {occ1} ({taux_occupation_h1:.1f}%) - {occ1_action}')
print(f'{occ2_couleur} {h2_nom} : {occ2} ({taux_occupation_h2:.1f}%) - {occ2_action}')
print(f'{occ3_couleur} {h3_nom} : {occ3} ({taux_occupation_h3:.1f}%) - {occ3_action}')
print(f'{occ4_couleur} {h4_nom} : {occ4} ({taux_occupation_h4:.1f}%) - {occ4_action}')
print(f'{occ5_couleur} {h5_nom} : {occ5} ({taux_occupation_h5:.1f}%) - {occ5_action}')
print()

print('--- CLASSIFICATION COUVERTURE VACCINALE ---')
print(f'{couleur_brazzaville} Brazzaville : {statut_brazzaville} ({taux_brazzaville:.1f}%) - {action_brazzaville}')
print(f'{couleur_pointe_noire} Pointe-Noire : {statut_pointe_noire} ({taux_pointe_noire:.1f}%) - {action_pointe_noire}')
print(f'{couleur_pool} Pool : {statut_pool} ({taux_pool:.1f}%) - {action_pool}')
print(f'{couleur_sangha} Sangha : {statut_sangha} ({taux_sangha:.1f}%) - {action_sangha}')
print()

print('--- BILAN DES ALERTES ---')
print(f'Medicaments : {nb_ruptures} ruptures critiques, {nb_alertes} alertes stock, {nb_normaux} normaux')
print(f'Occupation : {nb_occup_critique} critiques, {nb_occup_elevee} elevees, {nb_occup_optimale} optimales, {nb_occup_sous} sous-utilises')
print(f'Vaccination : {nb_vacc_critique} zones critiques, {nb_vacc_risque} a risque, {nb_vacc_insuffisant} insuffisantes, {nb_vacc_conforme} conformes')
print()

print('--- RECOMMANDATIONS PRIORITAIRES ---')
if nb_ruptures > 0:
    print('  - Alerte PNA : commandes express pour les medicaments en rupture')
if nb_occup_critique > 0:
    print('  - Alerte saturation : transferts a organiser dans les hopitaux critiques')
if nb_vacc_critique > 0:
    print('  - Alerte vaccination : campagnes d\'urgence dans les zones critiques')
if nb_ruptures == 0 and nb_occup_critique == 0 and nb_vacc_critique == 0:
    print('  - Aucune alerte critique. Situation globalement satisfaisante.')

print('=' * 70)
print(' FIN DU RAPPORT GLOBAL (S3)')
print('=' * 70)