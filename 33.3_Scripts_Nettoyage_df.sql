-- 33.3 – Scripts SQL de nettoyage – Base / Schéma : df
-- Projet : BIOLINE – Power BI / SAP – Analyse de données
-- Objectif : nettoyage des donnees avant exploitation (doublons, formats, NULL)

-- ---------------------------------------------------------------
-- 33.3.1 – Utilisation de la base / du schema `df`
-- ---------------------------------------------------------------
USE [df];

-- ---------------------------------------------------------------
-- 33.3.2 – Suppression des doublons
-- (adaptez le schema / le nom de table selon le jeu de donnees)
-- ---------------------------------------------------------------
SELECT *
FROM (
    SELECT
        *,
        ROW_NUMBER() OVER (
            PARTITION BY [COLONNES_CLES]
            ORDER BY [COLONNES_CLES]
        ) AS rn
    FROM dbo.[NomTable]
) AS t
WHERE rn = 1;

-- ---------------------------------------------------------------
-- 33.3.3 – Gestion des valeurs manquantes (NULL)
-- ---------------------------------------------------------------
-- Option 1 : suppression des lignes avec cle manquante
SELECT *
INTO dbo.[NomTable]_nettoyee
FROM dbo.[NomTable]
WHERE [COLONNES_CLES] IS NOT NULL;

-- Option 2 : remplissage via UPDATE (mediane / moyenne / constante)
UPDATE dbo.[NomTable]
SET [COLONNE_NUMERIQUE] = (
    SELECT AVG([COLONNE_NUMERIQUE])
    FROM dbo.[NomTable] t2
    WHERE t2.[CLE] = t1.[CLE]
)
WHERE [COLONNE_NUMERIQUE] IS NULL;

-- ---------------------------------------------------------------
-- 33.3.4 – Nettoyage des formats (dates, chaines)
-- ---------------------------------------------------------------
UPDATE dbo.[NomTable]
SET [COLONNE_DATE] = CONVERT(date, [COLONNE_DATE], 120)
WHERE [COLONNE_DATE] IS NOT NULL;

UPDATE dbo.[NomTable]
SET [COLONNE_TEXTE] = TRIM([COLONNE_TEXTE]);

-- ---------------------------------------------------------------
-- Fin des scripts SQL de nettoyage (base : df)
-- ---------------------------------------------------------------
