import streamlit as st
import pandas as pd
import joblib

# Charger le modèle
#model_path = r"C:\Users\DELL\Desktop\streamlit\classifier.pkl"
model_path = "classifier.pkl"
model = joblib.load(model_path)

# Charger les encodeurs
#label_encoders_path = r"C:\Users\DELL\Desktop\streamlit\label_encoders2.pkl"
label_encoders_path = "label_encoders2.pkl"
label_encoders_path = joblib.load(label_encoders_path)

# Titre de l'application
st.title("Formulaire de Saisie des Données")

#Créer un formulaire pour les saisies utilisateur
st.header("Entrez les informations de l'utilisateur")

st.text_input("Entrer votre Nom :")

st.text_input("Entrer votre Prenom :")

# Champs de saisie pour les caractéristiques
country = st.text_input("Pays")
year = st.number_input("Année", min_value=2000, max_value=2100, value=2023)
uniqueid = st.text_input("ID Unique")
bank_account = st.selectbox("Compte Bancaire", ["Oui", "Non"])
location_type = st.selectbox("Type de Localisation", ["Rural", "Urbain"])
cellphone_access = st.selectbox("Accès au Téléphone Portable", ["Oui", "Non"])
household_size = st.number_input("Taille du ménage", min_value=1, value=1)
age_of_respondent = st.number_input("Âge du répondant", min_value=0, max_value=120, value=30)
gender_of_respondent = st.selectbox("Genre du répondant", ["Masculin", "Féminin"])
relationship_with_head = st.text_input("Relation avec le chef de ménage")
marital_status = st.selectbox("Statut marital", ["Célibataire", "Marié", "Divorcé", "Veuf"])
education_level = st.selectbox("Niveau d'éducation", ["Aucun", "École primaire", "École secondaire", "Tertiaire"])
job_type = st.text_input("Type de travail")

# Bouton de validation
if st.button("Soumettre"):
    st.success("Les données ont été soumises avec succès !")





