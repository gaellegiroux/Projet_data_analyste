# MODE OPÉRATOIRE – Création / Mise à jour de la page HTML « Procédure Power BI ↔ SAP »

**Document concerné :** `procedure-powerbi-sap.html` (version en ligne / HTML autonome)
**Fichiers liés :** `procedure-powerbi-sap.md`, `README.txt`, `Evolution.txt`, `PROCEDURE_UPDATE_LOG.md`, `source.txt`
**Société :** BIOLINE AgroSciences
**Date :** 2026-11-01

---

## 1. Objectifs du mode opératoire

Ce mode opératoire décrit, de façon **exhaustive et répétable**, l’ensemble des actions réalisées
pour créer, mettre à jour, faire évoluer et maintenir la page HTML de la procédure Power BI ↔ SAP.

Il doit permettre, à l’avenir :

1. de **reproduire** la création du fichier HTML ;
2. de **mettre à jour** le contenu sans rien casser ;
3. d’**ajouter** de nouvelles sections ;
4. de **renommer** des fichiers tout en restant cohérent (HTML, Markdown, liens) ;
5. de **changer le nom de la société** sans modifier l’ensemble du long de la page ;
6. de **modifier la charte graphique / le graphique** ;
7. de **créer un raccourci en haut de page** ;
8. de suivre les règles **RGPD** et les sources des données.

---

## 2. Arborescence et fichiers concernés

```text
bioline/
├── procedure-powerbi-sap.html   ← DOCUMENT PRINCIPAL (page web autonome)
├── procedure-powerbi-sap.md     ← VERSION MARKDOWN (synchronisée avec le HTML)
├── README.txt                    ← Présentation du dossier
├── Evolution.txt                 ← Journal des étapes (cahier des charges)
├── PROCEDURE_UPDATE_LOG.md      ← Journal des mises à jour
├── source.txt                    ← Source de référence (documentation SAP / Power BI / Bioline)
├── schema_etoile.loo             ← Schéma de l’étoile
├── *.docx / *.xlsx / *.pdf       ← Documents sources / livrables
└── save/                         ← Anciennes versions (exclues du dépôt)
```

---

## 3. Structure du fichier HTML `procedure-powerbi-sap.html` (création)

### 3.1. En-tête `<head>` – feuille de style

- Balises : `<!DOCTYPE html>`, `<html lang="fr">`, `<meta charset="UTF-8">`, `<meta name="viewport">`, `<title>…</title>`.
- CSS : variables racines dans `:root` :
  - `--bleu: #0f6cbd`, `--bleu-fonce: #0b4f8a`, `--vert: #107c41`, `--orange: #ca5010`,
    `--gris: #f5f5f5`, `--bg: #fafafa`, `--card: #ffffff`, `--texte: #1b1b1b`, `--muted: #555`, `--bordure: #e1dfdd`.
- Thème sombre : `body[data-theme="dark"]` avec variables remplaçantes
  (`--bg`, `--card`, `--texte`, `--muted`, `--bordure`, `--gris`, `--bleu: #5aa9ff`, `--bleu-fonce: #4a90e0`).

### 3.2. Header

```html
<header>
  <h1>📋 Procédure – Gestion de projet Data Analyst / BI (SAP + Power BI) – BIOLINE</h1>
  <p>Guide professionnel complet : cycle de vie de la donnée, de l’analyse SAP au dashboard Power BI.</p>
  <a href="#haut" class="top-shortcut">↑ Retour en haut</a>
</header>
```

### 3.3. Theme switch

```html
<div class="theme-switch">
  <button class="theme-btn" data-theme="light" type="button">Thème : Clair</button>
  <button class="theme-btn" data-theme="dark" type="button">Thème : Sombre</button>
</div>
```

### 3.4. Navigation (onglets / liens d’accès rapide)

```html
<nav>
  <a href="#presentation-entreprise">Présentation</a>
  …
  <a href="#sources">Sources</a>
</nav>
```

### 3.5. Contenu principal – sections

Chaque section suit ce modèle :

```html
<!-- ============ N. TITRE DE LA SECTION ============ -->
<section id="identifiant-unique">
  <h2>N. Titre de la section</h2>
  …
</section>
```

Règles :

- `N.` = numéro séquentiel (1 à 30 en version actuelle) ;
- `id` = identifiant unique kebab-case, doit correspondre l’ancre utilisée dans la `<nav>` ;
- Un séparateur visuel peut précéder certaines sections :
  - `🏢 Présentation entreprise` avant §1 ;
  - `🔍 Compréhension des données` avant §13 (classe `separator separator-strong`) ;
  - `✅ Qualité des analyses` avant §19 ;
  - `📊 Visualisation` avant §22 ;
  - `💡 Recommandations business` avant §27 ;
  - `🔄 Retour d’expérience` avant §28.

### 3.6. Footer, raccourci retour en haut, script JavaScript

```html
<button class="back-to-top" id="backToTop" type="button" aria-label="Retour en haut">↑</button>

<footer>
  <p>Procédure Power BI ↔ SAP – Société … – Source : documentation SAP, Power BI et site BIOLINE</p>
</footer>

<script>
  const NOM_SOCIETE = "Bioline AgroSciences";
  const NOM_SOCIETE_COURT = "BIOLINE";
  function majTextesSociete() { … }
  majTextesSociete();
  document.title = "… – " + NOM_SOCIETE_COURT;
  …
  const backToTopBtn = document.getElementById('backToTop');
  window.addEventListener('scroll', …);
  backToTopBtn.addEventListener('click', …);
</script>
```

### 3.7. Graphique / charte graphique

- **Gantt** : SVG dans la section `#gantt` (section 11), barres `rect` + `text`, sélecteur de thème implicite via variables CSS.
- **Visuel rapides** : SVG dans la section `#powerbi` (section 23).
- **Couleurs** : uniquement via les variables CSS (`--bleu`, `--bleu-fonce`, …) pour rester cohérent en clair/sombre.

---

## 4. Procédure de mise à jour du HTML

1. Ouvrir `procedure-powerbi-sap.html`.
2. Localiser la section concernée (`grep` / éditeur).
3. Modifier le contenu HTML (textes, tableaux, `<pre>`, liens).
4. **Hors thème sombre** : vérifier les couleurs via les variables CSS.
5. **En thème sombre** : vérifier via `body[data-theme="dark"]`.
6. Vérifier la cohérence des numéros de sections (voir §5).
7. Vérifier les ancres `<nav>` ↔ `id` des sections.
8. Vérifier les liens `<a href>` vers les fichiers présents dans le dossier.
9. Synchroniser la version Markdown (`procedure-powerbi-sap.md`) avec les changements.
10. Mettre à jour les logs (`Evolution.txt`, `PROCEDURE_UPDATE_LOG.md`).

---

## 5. Procédure pour ajouter une nouvelle section

1. Choisir le **numéro** suivant (ex. nouvelle section après §30 → §31).
2. Créer le bloc :

```html
  <!-- ============ N. TITRE ============ -->
  <section id="identifiant-unique">
    <h2>N. Titre de la section</h2>
    …
  </section>
```

3. Ajouter l’ancre dans la `<nav>` avec le bon libellé.
4. Ajouter le séparateur visuel si nécessaire (juste avant la section).
5. Renumer **aussi** les sections suivantes (HTML + Markdown + commentaires).
6. Mettre à jour les liens (voir §6) et les logs.

---

## 6. Impact des renommages de fichiers et mise à jour des liens

Quand un fichier est renommé (ex. `Planning_stage_data_analyse.xlsx` → `11_Planning_stage_data_analyse.xlsx`) :

1. Renommer le fichier physique.
2. Mettre à jour **tous** les liens dans le HTML :

```html
<p>📄 Fichier source lié : <a href="Planning_stage_data_analyse.xlsx">Planning_stage_data_analyse.xlsx</a></p>
```

→ remplacer par le nouveau nom (ex. `11_Planning_stage_data_analyse.xlsx`).

3. Mettre à jour les liens dans le Markdown (avec gestion des espaces : `Data%20Quality%20Report.xlsx`).
4. Vérifier les références dans les sections (Gantt, Données, Sources, etc.).
5. Commiter (`git add -A && git commit -m "…"`) et pousser ultérieurement.

---

## 7. Variable de nom de société

### 7.1. Principe

Pour ne **pas modifier toute la page** lorsqu’on change de société, on utilise :

- **Variables JS** (un seul endroit à modifier) :

```js
const NOM_SOCIETE = "Bioline AgroSciences";
const NOM_SOCIETE_COURT = "BIOLINE";
```

- **Attributs HTML** `data-nom-societe` et `data-nom-societe-court` posés sur les éléments concernés :

```html
<strong data-nom-societe>Bioline AgroSciences</strong>
<span data-nom-societe>Bioline AgroSciences</span>
<span data-nom-societe-court>BIOLINE</span>
```

- **Règle JS** appliquée au chargement :

```js
function majTextesSociete() {
  document.querySelectorAll('[data-nom-societe]').forEach(function (el) { el.textContent = NOM_SOCIETE; });
  document.querySelectorAll('[data-nom-societe-court]').forEach(function (el) { el.textContent = NOM_SOCIETE_COURT; });
}
majTextesSociete();
document.title = "Procédure – Gestion de projet Data Analyst / BI (SAP + Power BI) – " + NOM_SOCIETE_COURT;
```

### 7.2. Où la modifier

- **Nom complet** : variable `NOM_SOCIETE` (JS) + valeurs `data-nom-societe`.
- **Nom court** : variable `NOM_SOCIETE_COURT` (JS) + valeurs `data-nom-societe-court`.

### 7.3. Ajouter une nouvelle société / un nouveau nom

- Modifier `NOM_SOCIETE` et `NOM_SOCIETE_COURT`.
- Ajouter / remplacer les attributs `data-nom-societe` / `data-nom-societe-court` sur les nouveaux éléments.
- Aucun autre endroit à modifier : le JS se charge du remplacement.

---

## 8. Emplacement du graphique / de la charte graphique

- **Gantt** : section 11 (`#gantt`), balises SVG `<svg>`, `<rect>`, `<text>`, coordonnées.
- **Flux rapide Power BI** : section 23 (`#powerbi`), SVG flux SAP → … → Dashboard.
- **Couleurs / thème** : CSS custom properties (`--bleu`, `--bleu-fonce`, `--vert`, `--orange`, `--bg`, `--card`, `--texte`, `--muted`, `--bordure`, `--gris`) + `body[data-theme="dark"]`.

Pour modifier une couleur : modifier la variable dans `:root` ou `body[data-theme="dark"]` (une seule source de vérité).

---

## 9. Raccourci en haut de page

- Un lien/raccourci **« ↑ Retour en haut »** a été ajouté dans l’`<header>` :

```html
<a href="#haut" class="top-shortcut">↑ Retour en haut</a>
```

- L’ancre cible : `<main id="haut">`.
- CSS : `.top-shortcut { display: inline-block; margin-top: 12px; color: #fff; border: 1px solid rgba(255,255,255,0.55); padding: 6px 14px; border-radius: 16px; text-decoration: none; font-size: 0.9rem; }`.

- **Retour en haut** (bouton fixe) : bouton `<button class="back-to-top" id="backToTop">↑</button>` + JS :

```js
const backToTopBtn = document.getElementById('backToTop');
window.addEventListener('scroll', function () {
  backToTopBtn.style.display = (window.scrollY > 400) ? 'flex' : 'none';
});
backToTopBtn.addEventListener('click', function () { window.scrollTo({ top: 0, behavior: 'smooth' }); });
```

---

## 10. RGPD – paragraphe, règles générales, source et données à suivre

### 10.1. Paragraphe RGPD ajouté

- **Section :** 30. Sources et références (`#sources`) dans le HTML ; `## 30. Sources et références` dans le Markdown.
- Contenu : conformité au Règlement Général sur la Protection des Données (UE) 2016/679 (RGPD) applicable aux données
  personnelles collectées pour les analyses biocontrôle (données SAP, données métier, données d’investigation).
- **Règles générales retenues :** licéité, loyauté et transparence ; minimisation des données ; limitation des finalités ;
  limitation de la conservation ; exactitude ; intégrité et confidentialité des données ; accountability.
- **Droits des personnes concernées :** accès, rectification, effacement, portabilité, opposition et limitation du traitement ;
  notification des violations de données et réparation des dommages.

### 10.2. Source

- **EUR-Lex** – Règlement (UE) 2016/679.
- **CNIL** – Commission Nationale de l’Informatique et des Libertés.

### 10.3. Données à suivre

- Toute nouvelle collecte / traitement de données personnelles doit être réévaluée au regard du RGPD.
- Le paragraphe doit rester présent dans la section Sources.

---

## 11. Section « Tests de validation » (nouvelle section 20)

- Position : juste après l’Analyse exploratoire (EDA) (§19) et avant le Script / ETL (§21 après renumérotation).
- Contenu : « Tests de validation : vérifications menées pour s’assurer que les données et les résultats sont exacts,
  cohérents et conformes aux attentes avant leur mise en production. »
- Fichiers liés :
  - `20_1_Tests_Validation.docx` ;
  - `20_Tests_Validation.pdf`.
- Renumerisation appliquée : Script / ETL → §21, Catalogue des KPI → §22, Power BI → §23, KPI / Dashboard → §24,
  Exemples DAX / KPI → §25, Résultats → §26, Perspectives → §27, REX → §28, Dépannage → §29, Sources → §30.

---

## 12. Récapitulatif des actions réalisées (session en cours)

1. **Section 12 – Données réelles :** suppression du grand tableau (T01–T25) ; conservation de l’« Aperçu des 5 premières lignes ».
2. **Section 20 – Tests de validation :** ajout (nouvelle section après l’EDA).
3. **Renumerrotation** des sections 20 → 30 (cascade après insertion de la section 20).
4. **RGPD :** paragraphe ajouté en section Sources (Sources et références → §30).
5. **Cartographie métier (§2) :** ajout de la partie « 🔁 CIRCUIT » (Client → Commande → SAP → Livraison → Facturation → Reporting Power BI).
6. **Présentation (§1) :** contenu repris du fichier `1_1_presentation_entreprise.docx`.
7. **Contexte (§3), Cahier des charges (§4), Prérequis (§5), Procédure (§6), Modélisation (§7), Bonnes pratiques (§8),
   Checklist (§9), Questionnaire (§10) :** contenus synchronisés / vérifiés avec les fichiers sources DOCX.
8. **Bouton retour en haut :** ajout CSS, HTML, JS.
9. **Raccourci en haut de page :** ajout `<a href="#haut" class="top-shortcut">↑ Retour en haut</a>` dans l’header.
10. **Variable société :** ajout `NOM_SOCIETE`, `NOM_SOCIETE_COURT`, attributs `data-nom-societe`, `data-nom-societe-court`, `document.title`.

---

## 13. Commandes Git utilisées (en attendant le push GitHub)

```bash
git init -b main
git add -A
git rm -r --cached save        # exclure anciennes versions
git commit -m "Version 1.10 - HTML + Markdown + documents lies"
```

---

*Fin du mode opératoire.*
