# Journal des mises à jour – Procédure Power BI ↔ SAP / BIOLINE

**Fichier concerné :** `procedure-powerbi-sap.html`
**Date :** 2026-10-29
**Projet :** BIOLINE – Gestion de projet Data Analyst / BI

---

## Résumé des changements

---

## Ajouts

| Date | Section / Élément ajouté | Contenu ajouté |
|---|---|---|
| 2026-10-29 | Présentation de l’entreprise | Nouvelle section `#presentation-entreprise` insérée avant le Contexte : mission Bioline, produits (biostimulants, biocontrol, phéromones, pièges, pollinisation, outils digitaux), cultures et cibles, contact. |
| 2026-10-29 | Cahier des charges | Nouvelle section `#cahier-des-charges` insérée avant les Prérequis : Contexte, Objectifs, Sources de données, Livrables, Planning, Risques. |
| 2026-10-29 | Architecture | Nouvelle section `#architecture` : diagramme SAP → Extraction SQL → Python → Data Warehouse → Power BI ; puis variante SAP S/4 → SQL Server → Power BI. |
| 2026-10-29 | Analyse | Nouvelle section `#analyse` : EDA, questions (produits, région, saisonnalité), livrables (histogrammes, boxplots, heatmaps). |
| 2026-10-29 | Script / ETL | Nouvelle section `#script` : pipeline Extraction → Nettoyage → Transformation → Chargement ; outils (Python, Power Query, SSIS, Talent, Airflow, dbt). |
| 2026-10-29 | KPI / Dashboard | Nouvelle section `#kpi-dashboard` : pages typiques (Direction, Vente, Stock, Prévisions). |
| 2026-10-29 | Résultats | Nouvelle section `#resultats` : volet à alimenter ultérieurement. |
| 2026-10-29 | Perspectives | Nouvelle section `#perspectives` : volet à alimenter ultérieurement. |
| 2026-10-29 | Cartographie métier | Nouvelle section `#cartographie-metier` insérée avant le Contexte : schéma du processus métier (Demande / Besoin → … → Recommandations business). |
| 2026-10-29 | Schéma de l’étoile | Nouvelle section `#schema-etoile` : insertion du schéma, fichier `schema_etoile.loo`. |
| 2026-10-29 | Gouvernance des données | Nouvelle section `#gouvernance-donnees` : insérée juste avant l’Analyse (EDA). |

## Modifications

| Date | Section | Avant → Après | Détail |
|---|---|---|---|
| 2026-10-29 | Présentation de l’entreprise | Absent | Ajoutée en tête du document, avant le Contexte. |
| 2026-10-29 | Cahier des charges | Absent | Ajoutée avant les Prérequis. |
| 2026-10-29 | Architecture | Absent | Ajoutée avant les nouvelles sections d’analyse/script/KPI/résultats/perspectives. |
| 2026-10-29 | Analyse / Script / KPI / Résultats / Perspectives | Absent | Ajoutés comme sections vides/placeholders (fichiers à alimenter ultérieurement). |

## Suppressions

| Date | Élément supprimé | Section concernée | Remplacement |
|---|---|---|---|
| 2026-10-29 | Bloc « Outils de gestion de projet » (Microsoft Planner, Project, Excel, GanttProject, Trello, GitHub Projects, Azure DevOps) | Gantt (`#gantt`) | Supprimé. |
| 2026-10-29 | Bloc « États Kanban » (Backlog, To Do, In Progress, Testing, Done) | Gantt (`#gantt`) | Supprimé. |

## Bloc-notes (notes de version)

```text
2026-10-29 – Version courante du document HTML.

Contenu :
- Présentation de l’entreprise : mission, produits, cultures, contact.
- Contexte & Sources : SAP / Power BI / BIOLINE.
- Cahier des charges : Contexte, Objectifs, Sources, Livrables, Planning, Risques.
- Prérequis, Étapes, Modélisation, Dépannage, Bonnes pratiques, Checklist,
  Questionnaire, Exemples DAX / KPI, Modèle biologique.
- Gantt : diagramme SVG + lien Excel (outils/Kanban supprimés).
- Données : tableau réel T01–T25 extrait du planning Excel.
- Nouvelles parties : Architecture, Analyse, Script, KPI / Dashboard, Résultats, Perspectives.

Contenu supplémentaire (versions récentes) :
- Cartographie métier (schéma processus métier).
- Schéma de l’étoile (`schema_etoile.loo`).
- Gouvernance des données.
- Séparateurs visuels par phase (Présentation entreprise, Compréhension des données, Qualité des analyses, Visualisation, Recommandations business, Retour d'expérience).

État : version restaurée (rich) avec les données réelles, puis enrichie
des nouvelles parties demandées.
```

## Historique complet des versions

| Version | Date | Changements majeurs |
|---|---|---|
| 1.0 | 2026-10-29 | Création initiale (Contexte, Prérequis, Étapes, Modélisation, Dépannage, Bonnes pratiques, Sources). |
| 1.1 | 2026-10-29 | Ajout Checklist, Questionnaire SAP, Exemples DAX / KPI, Modèle biologique, Gantt, Données réelles. |
| 1.2 | 2026-10-29 | Restauration de la version riche avec données réelles. |
| 1.3 | 2026-10-29 | Restructuration en version riche (finale adoptée). |
| 1.4 | 2026-10-29 | Ajout Présentation de l’entreprise, Cahier des charges, Architecture, Analyse, Script, KPI / Dashboard, Résultats, Perspectives. |
| 1.5 | 2026-10-29 | Suppression des outils de gestion de projet et des États Kanban (Gantt). |
| 1.6 | 2026-10-29 | Ajout de la partie « Power BI – Modélisation et reporting » avant l’EDA (visuel SVG + lien `Bi.pbix`). Ajout des liens de navigation manquants. |
| 1.7 | 2026-10-29 | Ajout Dictionnaire des données, Dictionnaire des acronymes, Catalogue des KPI, liens Data Quality Report / Journal des décisions (EDA), partie REX. Mise à jour README.txt. |
| 1.8 | 2026-10-29 | Réorganisation des sections (Catalogue après KPI/Dashboard, Dictionnaire données après EDA, Dictionnaire acronymes après Architecture, Power BI après KPI/Dashboard, Exemples après Power BI), renumérotation 1-26, mode sombre éclairci. |
| 1.9 | 2026-10-29 | Réorganisation complète : Dépannage rapide en fin (avant Sources), Cartographie métier après Présentation, Gouvernance des données avant EDA, Power BI juste avant KPI / Dashboard, Catalogue des KPI avant Exemples DAX / KPI, Modèle de données biologique avant EDA, nouvelle partie Schéma de l’étoile (`schema_etoile.loo`), séparateurs visuels ajoutés, renumérotation 1-29, Markdown synchronisé. |
| 1.10 | 2026-10-29 | Ajustements contenu : Résultats, KPI/Dashboard, EDA, Script, Perspectives remplacés par des formulations opérationnelles ; aperçu 5 lignes ajouté ; lien + résumé Cahier des charges ; titre Gantt « Planning des tâches » ; bilan REX ; suppression Schéma/cartographie et mentions « (présent dans le même dossier). » ; séparateurs 🔍 et ✅ repositionnés (🔍 renforcé avant §13, ✅ avant §19). |

---

*Fin du journal des mises à jour.*
