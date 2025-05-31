import streamlit as st
from models import Case

st.title("👤 Medewerker Login & Registratie")

# Initieer medewerkerlijst
if "medewerkers" not in st.session_state:
    st.session_state.medewerkers = []

if "logged_in_user" not in st.session_state:
    st.session_state.logged_in_user = None

# Functie om unieke medewerker-ID te maken
def genereer_medewerker_id(afdeling, naam):
    afk = afdeling[:2].upper()
    count = sum(1 for m in st.session_state.medewerkers if m['afdeling'] == afdeling) + 1
    return f"MW{afk}{str(count).zfill(3)}"

# FORM: medewerker registreren
st.subheader("Nieuwe medewerker registreren")
with st.form("registreer_form"):
    naam = st.text_input("Naam")
    afdeling = st.text_input("Afdeling")
    registreer = st.form_submit_button("Registreer")

    if registreer and naam and afdeling:
        medewerker_id = genereer_medewerker_id(afdeling, naam)
        st.session_state.medewerkers.append({
            "id": medewerker_id,
            "naam": naam,
            "afdeling": afdeling
        })
        st.success(f"Medewerker {naam} geregistreerd met ID: {medewerker_id}")

# FORM: inloggen als medewerker
st.subheader("Inloggen als medewerker")

if not st.session_state.medewerkers:
    st.info("Nog geen medewerkers beschikbaar. Registreer eerst iemand.")
else:
    gekozen = st.selectbox("Kies medewerker", options=st.session_state.medewerkers, format_func=lambda x: f"{x['naam']} ({x['id']})")
    if st.button("Inloggen"):
        st.session_state.logged_in_user = gekozen
        st.success(f"Ingelogd als: {gekozen['naam']} ({gekozen['id']})")