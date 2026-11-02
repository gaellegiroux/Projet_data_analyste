# 33.2 – Scripts Python de nettoyage – DataFrame `df`
# Projet : BIOLINE – Power BI / SAP – Analyse de données
# Objectif : collecte, nettoyage et transformation du DataFrame `df`

import pandas as pd


# ------------------------------------------------------------------
# 33.2.1 – Visualisation du DataFrame `df`
# ------------------------------------------------------------------
def visualiser_df(df):
    """Affiche les informations de `df` : types, stats, valeurs manquantes, aperçu."""
    print("=== INFORMATIONS DU DATAFRAME df ===")
    print(df.info())
    print("\n=== 5 PREMIERES LIGNES ===")
    print(df.head())
    print("\n=== STATISTIQUES DESCRIPTIVES ===")
    print(df.describe())
    print("\n=== VALEURS MANQUANTES PAR COLONNE ===")
    print(df.isnull().sum())
    print("\n=== NOMBRE DE DOUBLONS ===")
    print("Doublons detectes :", df.duplicated().sum())
    return df


# ------------------------------------------------------------------
# 33.2.2 – Traitement des doublons
# ------------------------------------------------------------------
def traiter_doublons(df, colonnes=None):
    """Supprime les doublons du DataFrame `df` (sur les colonnes definies ou toutes)."""
    if colonnes is None:
        colonnes = df.columns
    df_nettoy = df.drop_duplicates(subset=colonnes).reset_index(drop=True)
    print(f"Suppression des doublons sur {colonnes} : {len(df) - len(df_nettoy)} doublons retire(s).")
    return df_nettoy


# ------------------------------------------------------------------
# 33.2.3 – Nettoyage des formats / types
# ------------------------------------------------------------------
def nettoyer_types(df):
    """Normalise les types : dates en datetime, nombres en numerique, chaines propres."""
    df_clean = df.copy()

    for col in df_clean.columns:
        if col.endswith("_date") or col.endswith("_jour") or col.endswith("_dt"):
            df_clean[col] = pd.to_datetime(df_clean[col], errors="coerce")

    for col in df_clean.select_dtypes(include=["object"]).columns:
        df_clean[col] = df_clean[col].astype(str).str.strip()

    for col in df_clean.select_dtypes(include=["object", "int64", "float64"]).columns:
        df_clean[col] = pd.to_numeric(df_clean[col], errors="coerce")

    return df_clean


# ------------------------------------------------------------------
# 33.2.4 – Gestion des valeurs manquantes
# ------------------------------------------------------------------
def nettoyer_valeurs_manquantes(df, colonne, strategie="interpolation"):
    """Gestion des valeurs manquantes : suppression ou remplissage."""
    df_clean = df.copy()
    if colonne not in df_clean.columns:
        return df_clean
    if strategie == "suppression":
        df_clean = df_clean.dropna(subset=[colonne])
    elif strategie == "moyenne":
        df_clean[colonne] = df_clean[colonne].fillna(df_clean[colonne].mean())
    elif strategie == "mediane":
        df_clean[colonne] = df_clean[colonne].fillna(df_clean[colonne].median())
    elif strategie == "mode":
        df_clean[colonne] = df_clean[colonne].fillna(df_clean[colonne].mode()[0])
    return df_clean


# ------------------------------------------------------------------
# 33.2.5 – Nettoyage complet
# ------------------------------------------------------------------
def nettoyage_complet(df):
    """Pipeline complet : visualisation -> doublons -> types -> valeurs manquantes -> retour df."""
    df = visualiser_df(df)
    df = traiter_doublons(df)
    df = nettoyer_types(df)
    return df
