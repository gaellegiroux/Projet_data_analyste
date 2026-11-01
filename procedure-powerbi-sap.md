# Procédure – Gestion de projet Data Analyst / BI (SAP + Power BI) – BIOLINE

Guide professionnel complet : cycle de vie de la donnée, de l’analyse SAP au dashboard Power BI.

**Sources** : SAP · Power BI · BIOLINE

---

**🏢 Présentation entreprise**

## 1. Présentation de l’entreprise

**Bioline AgroSciences** est une société française spécialisée dans le **biocontrol** : « L’allié de confiance des agriculteurs dans la lutte biologique. La nature. Les gens. La simplicité. »

« Aider les agriculteurs dans leur transition vers une agriculture durable. »

- Produits et domaines : biostimulants, contrôle des ravageurs, nutrition des auxiliaires / écosystèmes, phéromones, pièges, pollinisation, outils digitaux (Bioline App – the Biocontrol Advisor).
- Cultures et cibles : vigne, maïs, oléagineurs / céréales à paille, arboriculture, espaces verts… Ravageurs : Eulia, Cochylis, Tordeuses de la vigne, Mites alimentaires, Pyrale du buis, Mouches des terreaux, Noctuelles défoliatrices, Lépidoptères, Acariens…
- Contact : Passage des 4 saisons, 26250 Livron-sur-Drôme, France · +33 (0)4 75 60 09 31 · france@biolineagrosciences.com

## 2. Cartographie métier

Représentation du schéma du processus métier de BIOLINE :

```text
Demande / Besoin
↓
Cadrage & Compréhension
↓
Collecte & Préparation
↓
Modélisation
↓
Analyse & Gouvernance
↓
Reporting / KPI
↓
Recommandations business
```

---

## 3. Contexte

Ce document constitue la **procédure officielle** de gestion des projets Power BI de l’entreprise **BIOLINE** qui reposent sur des données **SAP**.

### Les 3 sources utilisées dans le cadre du projet

| Source | Type | Document / Lien |
|---|---|---|
| SAP | Documentation technique | [SAP – User Guide (SAP Fiori Client)](https://help.sap.com/doc/d55f83e12e4b40779158fbaf08fe0f14/1.11/fr-FR/index.html) |
| Power BI | Documentation produit | [Power BI – Documentation Microsoft Learn](https://learn.microsoft.com/fr-fr/power-bi/) |
| Bioline AgroSciences | Documentation société | [Bioline AgroSciences – Site officiel](https://www.biolineagrosciences.com/fr/) |

> **Point important :** la documentation SAP référencée porte sur le **SAP Fiori Client**. Quelle que soit la module SAP utilisée (SD, MM, PP, QM, FICO, BW, HANA…), la **procédure de connexion et de traitement des données reste la même**.

## 4. Cahier des charges

**Résumé :** Ce cahier des charges définit le contexte métier, les objectifs d’analyse (performance, écarts, décisions), les sources de données (SAP, Power BI, Bioline), les livrables attendus (procédure, modélisation, dashboard, synthèse), le planning des phases et les risques associés.

📎 Fichier lié : [cahier_des_charges.docx](cahier_des_charges.docx)



## 5. Prérequis

### 5.1. Environnement SAP

- Accès réseau SAP (firewall, proxy, VPN) autorisé entre Power BI Desktop / le service Power BI et le serveur SAP.
- Utilisateur SAP avec les autorisations nécessaires (Rôle SAP_BW, ou autorisations OData / Fiori selon le cas).
- Service OData (ou RFC / JDBC / ODBC / BW) **actif** côté SAP.
- URL du service OData SAP connue (ex. : `http://<serveur>:port/sap/opu/odata/sap/<NomService>`).

### 5.2. Environnement Power BI

- Power BI Desktop installé.
- Power BI Service (si publication) + **Passerelle de données** si les données SAP sont sur site (on-premise).
- DAC / credentials Power BI configurés pour le rafraîchissement.

## 6. Procédure – Étapes de gestion d'un projet Power BI / SAP

### Étape 0 – Créer / identifier le projet

1. Définir le périmètre métier du rapport (ex. ventes produits biocontrôle, commandes, interventions, stocks…).
2. Définir les indicateurs KPI attendus.
3. Créer le fichier `.pbix` dans Power BI Desktop.

### Étape 1 – Identifier le module SAP et la source de données

1. Connaître le module SAP utilisé (SD, MM, PP, QM, FICO, BW, HANA…). **La procédure reste identique.**
2. Identifier l'objet métier source : table SAP, service OData Fiori, InfoProvider BW, etc.
3. Sélectionner le connecteur Power BI adapté :
   - **SAP BW** → connecteur SAP BW (MDX).
   - **SAP HANA** → connecteur SAP HANA (SQL).
   - **SAP S/4HANA / ECC** → OData via SAP Gateway / SAP Fiori.

### Étape 2 – Tester la connexion SAP

1. Côté SAP : tester l'endpoint via transaction `/IWFND/GW_CLIENT` (OData) ou `SM59` (RFC).
2. Côté Power BI Desktop : `Obtenir des données → OData → SAP` et saisir l'URL.
3. Vérifier l'authentification (SSO, Active Directory, SAP).

### Étape 3 – Charger et transformer les données (Power Query)

1. Importer les tables / services dans Power Query.
2. Supprimer les doublons, filtrer les données, créer les dates.
3. Écrire les requêtes DAX si nécessaire.

### Étape 4 – Publier et planifier le rafraîchissement

1. Publier le modèle dans Power BI Service.
2. Configurer le gateway si SAP est on-premise.
3. Planifier / activer l'actualisation (scheduled refresh).

## 7. Modélisation recommandée

- Table de faits : mesures (montant, quantité, nombre d'interventions…).
- Dimensions : produit, culture, région, date, canal de vente…
- Relations 1..N entre fait et dimensions.

> **Conseil BIOLINE :** adopter un schéma en étoile (fait + dimensions) pour les rapports biocontrôle (produits, cultures, interventions, ventes, etc.).

## 8. Bonnes pratiques de gestion de projet

- Versionner les fichiers `.pbix` et les sources.
- Documentation des requêtes OData et des traitements Power Query.
- Séparer les environnements (dev / test / prod SAP).
- Contrôle des accès et sécurité des données.

## 9. Checklist de validation avant publication

- [ ] Source SAP de test validée (connexion + OData/RFC/BW OK).
- [ ] Qualité des données : doublons vérifiés, valeurs manquantes identifiées.
- [ ] Modèle validé : toutes les relations nécessaires existent.
- [ ] État du modèle Power BI : **« Valid »**.
- [ ] Refresh de test réussi dans Power BI Desktop.
- [ ] Refresh réussi sur le service Power BI après publication.
- [ ] Identités / permissions Power BI définies (workspaces, rôles).
- [ ] Documentation du modèle et des mesures mise à jour.

### Workflow de validation avant publication

1. Exécuter un **refresh de test** dans Power BI Desktop.
2. Vérifier les éventuelles erreurs de chargement dans la vue *Données* / *Modifier les requêtes*.
3. Publier le modèle dans Power BI Service.
4. Lancer un refresh sur le service.
5. Consulter les logs d’erreur du refresh si nécessaire.
6. Valider les KPI / rapports dans le service avant diffusion.

## 10. Modèle de questionnaire – Identifier le module SAP utilisé par BIOLINE

| Champ | Question / Réponse |
|---|---|
| Société | Bioline AgroSciences |
| Domaine | Agriculture / biocontrôle |
| Module SAP | ☐ SD ☐ MM ☐ PP ☐ QM ☐ FICO ☐ BW ☐ HANA ☐ Autre : ________ |
| Version du système | ☐ ECC ☐ S/4HANA ☐ BW ☐ HANA |
| Type de connexion SAP | ☐ OData ☐ RFC ☐ JDBC / ODBC ☐ MDX ☐ SQL |
| Fonction métier concernée | ____________________ |
| Interlocuteur SAP / expert | ____________________ |
| Période de référence des données | ____________________ |

> **Note :** une fois le module identifié, la procédure de connexion Power BI ↔ SAP reste la même ; seule l’URL du service et le connecteur changent.

## 11. Planning des tâches

Planification visuelle des tâches, de leurs durées et de leurs dépendances pour suivre l’avancement et respecter les délais.

| Étape | Semaines |
|---|---|
| Cadrage & Contexte / Sources | S0 |
| Prérequis & Environnement | S1–S2 |
| Connexion SAP & Test | S3 |
| Modélisation – Star schema | S4–S5 |
| Dépannage & Validation | S6 |
| Publication & Refresh | S7 |

**Fichier lié :** [Planning_stage_data_analyse.xlsx](Planning_stage_data_analyse.xlsx)

## 12. Données réelles – Planning_stage_data_analyse.xlsx

Données issues du fichier Excel **Planning_stage_data_analyse.xlsx** (onglet « PLANNING DES TÂCHES »), en lien avec le [diagramme de Gantt](#11-modèle-de-gestion-du-projet--diagramme-de-gantt) :

### Tâches du projet 


> **Note :** ces données sont extraites du planning de stage en analyse de données ; à confronter et mettre à jour avec les valeurs réelles du fichier Excel.

📄 Fichier source lié : [Planning_stage_data_analyse.xlsx](Planning_stage_data_analyse.xlsx)

### 📄 Aperçu des 5 premières lignes

```text
ID	Phase	Tâche	Responsable	Durée (jours)	Priorité	Statut	Dépend de	Livrable attendu	Notes
T01	Cadrage	Prendre connaissance du contexte, des objectifs et du processus métier	Stagiaire	2	Haute	En cours	Note de cadrage	–	–
T02	Cadrage	Clarifier la problématique et les questions d'analyse	Stagiaire	4	Haute	à faire	T01	Problématique validée	–
T03	Cadrage	Définir les indicateurs de réussite et le périmètre	Stagiaire	6	Haute	à faire	T02	Liste des indicateurs	–
T04	Cadrage	Établir le plan de travail avec le tuteur ou la tutrice	Stagiaire	2	Moyenne	à faire	T03	Planning validé	–
```

---

### 🔍 Compréhension des données

## 13. Architecture des données

```text
SAP
↓
Extraction SQL
↓
Python
↓
Data Warehouse
↓
Power BI
```

ou :

```text
SAP S/4
↓
SQL Server
↓
Power BI
```

## 14. Dictionnaire des acronymes

📄 Fichier lié : [dictionnaire_acronyme.xlsx](dictionnaire_acronyme.xlsx) — recense les acronymes.

## 15. Dictionnaire des données

📄 Fichier lié : [dictionnaire_donnees.xlsx](dictionnaire_donnees.xlsx) — contient les tables, colonnes, types et descriptions.

| Table | Colonne | Type | Description |
|---|---|---|---|
| – | – | – | Contenu à alimenter via le fichier. |

## 16. Schéma de l’étoile (schema_etoile.loo)

📎 Fichier lié : [schema_etoile.loo](schema_etoile.loo) — schéma du fichier.

## 17. Modèle de données biologique

Proposition de modélisation pour les données métier de biocontrôle : **produits biocontrôle, cultures, bioprédateurs, interventions**.

### 17.1. Tables / entités suggérées

- **Dim_Produit** : Code produit, Libellé, Famille (bioprédateur / substrat / phéromone / piège), DCI, Culture cible.
- **Dim_Culture** : Code culture, Libellé (vigne, maïs, orchard…), Type de culture.
- **Dim_Date** : Date, Année, Saison, Mois.
- **Fact_Intervention** : Date, Culture, Produit, Quantite, Dosage, Methode.
- **Fact_Vente** : Date, Produit, Culture, Quantite, Montant.

### 17.2. Exemples DAX – Modèle biologique

```dax
Quantite Biopreveur par Intervention = SUM ( 'Fact_Intervention'[Quantite] )

Nombre d'Interventions par Produit = CALCULATE (
    DISTINCTCOUNT ( 'Fact_Intervention'[Produit] ),
    'Fact_Intervention'[Produit]
)
```

```dax
Total Biopreveur par Culture = CALCULATE (
    SUM ( 'Fact_Intervention'[Quantite] ),
    ALLSELECTED ( 'Fact_Intervention'[Culture] )
)
```

## 18. Gouvernance des données

⚠️ Ce volet est issu d’un fichier à créer (vide pour l’instant) et sera alimenté ultérieurement.

- Principes de gouvernance : conformité, rôles, accès, documentation, qualité.

---

**✅ Qualité des analyses**

## 19. Analyse exploratoire (EDA)

Analyse exploratoire (EDA) : exploration des données pour dégager les tendances, comparer les performances et repérer les saisonnalités, à l’aide de visualisations.

- 📄 Fichier lié : [Analyse.pdf](Analyse.pdf)
- 📄 Données : [Data Quality Report.xlsx](Data%20Quality%20Report.xlsx) — recense toutes les métriques d’exploration.
- 📄 Journal : [Journal des décisions.xlsx](Journal%20des%20d%C3%A9cisions.xlsx)

## 20. Tests de validation

Tests de validation : vérifications menées pour s’assurer que les données et les résultats sont exacts, cohérents et conformes aux attentes avant leur mise en production.

- Objectifs : vérifier l’exactitude des données extraites depuis SAP ; vérifier la cohérence des données (jointures, référentiels, dates) ; vérifier la conformité des résultats par rapport aux attentes métier ; valider les KPI et les tableaux de bord avant publication.

📄 Fichier lié : [20_1_Tests_Validation.docx](20_1_Tests_Validation.docx)
📄 Rapport : [20_Tests_Validation.pdf](20_Tests_Validation.pdf)

---

## 21. Script / ETL

Automatisation de la collecte, du nettoyage et de la transformation des données pour alimenter les analyses de façon fiable et reproductible.

- Outils : Python, Power Query, SSIS, Talend, Airflow, dbt.
- Pipeline : Extraction → Nettoyage → Transformation → Chargement.

📄 Fichiers liés : [Scripts SQL.txt](Scripts%20SQL.txt) | [Scripts Python.py](Scripts%20Python.py) | [mesures_DAX.txt](mesures_DAX.txt)

---

**📊 Visualisation**

## 22. Catalogue des KPI

📄 Fichier lié : [Catalogue KPI.xlsx](Catalogue%20KPI.xlsx) — contient les KPI, leur formule et l’objectif.

| KPI | Formule | Objectif |
|---|---|---|
| – | – | Contenu à alimenter via le fichier. |

## 23. Power BI – Modélisation et reporting

Phase de modélisation et de mise en forme du modèle Power BI, juste avant l’analyse exploratoire : prise en main du fichier `.pbix`, chargement des sources, modélisation du modèle et préparation des requêtes.

**Visuel rapide :**

```text
SAP
↓
Extraction SQL
↓
Nettoyage / Transformation
↓
Modélisation
↓
Dashboard Power BI
```

📄 Fichier lié : [Bi.pbix](Bi.pbix) (modèle Power BI / suivi).

## 24. KPI / Dashboard

Tableaux de bord synthétiques pour suivre la performance de l’activité et faciliter la prise de décision.

- 📄 Fichier lié : [Bi_export_donnees.pdf](Bi_export_donnees.pdf)

## 25. Exemples de requêtes DAX / métriques KPI

### Exemple – Ventes

```dax
Ventes Totales = SUM ( 'Ventes'[Montant] )

Ventes par Culture = CALCULATE (
    [Ventes Totales],
    'Ventes'[Culture]
)
```

### Exemple – Interventions / dosage

```dax
Interventions Réalisées = COUNTROWS ( 'Interventions' )

Quantité de Bioprédateurs Appliquée = SUM ( 'Interventions'[Quantite] )

Interventions par Culture = CALCULATE (
    [Interventions Réalisées],
    'Interventions'[Culture]
)
```

### Exemple – KPI agrégés

```dax
Ventes / Intervention = DIVIDE ( [Ventes Totales], [Interventions Réalisées] )

Taux de Transformation = [Quantité de Bioprédateurs Appliquée] / [Interventions Réalisées]
```

---

**💡 Recommandations business**

## 26. Résultats

Synthèse des analyses menées à partir des indicateurs clés, pour mesurer la performance, identifier les écarts et orienter les décisions.

- 📄 Fichier lié : [Resultat.pdf](Resultat.pdf)

## 27. Perspectives et/ou proposition

Pistes d’amélioration et évolutions envisagées pour renforcer les analyses et soutenir les décisions futures.

- 📄 Fichier lié : [Recommandations.docx](Recommandations.docx)

---

**🔄 Retour d'expérience**

## 28. REX – Retour sur expérience

- Bilan du projet : réussites, difficultés rencontrées et enseignements à retenir pour les prochains projets.
- 📄 Fichier lié : [REX.docx](REX.docx) — Retour sur expérience.

## 29. Procédure de dépannage rapide

| Erreur / Symptôme | Cause probable | Action |
|---|---|---|
| Connexion impossible Power BI → SAP | URL, firewall, authentification | Vérifier URL, tester via `/IWFND/GW_CLIENT`, vérifier SSO |
| Timeout OData | Taille des requêtes / paramètres | Ajuster les paramètres de requêtes OData |
| Refresh impossible dans Power BI Service | Gateway / credentials | Configurer la passerelle et les identités |
| Données non actualisées | Refresh planifié non activé | Planifier le refresh |

## 30. Sources et références

- **SAP :** [help.sap.com – SAP Fiori Client](https://help.sap.com/doc/d55f83e12e4b40779158fbaf08fe0f14/1.11/fr-FR/index.html)
- **Power BI :** [learn.microsoft.com – Documentation Power BI](https://learn.microsoft.com/fr-fr/power-bi/)
- **BIOLINE :** [www.biolineagrosciences.com – Bioline AgroSciences](https://www.biolineagrosciences.com/fr/)

- **RGPD :** Conformité au Règlement Général sur la Protection des Données (UE) 2016/679 (RGPD) applicable aux données personnelles collectées pour les analyses biocontrôle (données SAP, données métier, données d’investigation). Règles générales retenues : licéité, loyauté et transparence ; minimisation des données ; limitation des finalités ; limitation de la conservation ; exactitude ; intégrité et confidentialité des données ; accountability. Droits des personnes concernées : accès, rectification, effacement, portabilité, opposition et limitation du traitement ; notification des violations de données et réparation des dommages. Source : EUR-Lex – Règlement (UE) 2016/679 et CNIL (Commission Nationale de l'Informatique et des Libertés). À suivre dans le cadre des traitements de données Power BI / SAP de BIOLINE.

---

*Fin du document.*
