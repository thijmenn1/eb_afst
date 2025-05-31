import streamlit as st
import datetime
from models import Case

st.title("➕ Nieuwe Case Aanmaken")

if "medewerkers" not in st.session_state or not st.session_state.medewerkers:
    st.warning("Er zijn nog geen medewerkers geregistreerd. Ga naar 'Login' om een medewerker toe te voegen.")
    st.stop()

with st.form("case_form"):
    description = st.text_input("Beschrijving")
    gekozen_medewerker = st.selectbox(
        "Eigenaar (medewerker)",
        options=st.session_state.medewerkers,
        format_func=lambda m: f"{m['naam']} ({m['id']})"
    )
    owner = gekozen_medewerker["id"]

    status = st.selectbox("Status", ["open", "in behandeling", "afgehandeld"])
    customer_id = st.text_input("Klant ID")
    category = st.text_input("Categorie")
    priority = st.selectbox("Prioriteit", ["laag", "normaal", "hoog"])
    submitted = st.form_submit_button("Toevoegen")

    if submitted:
        now = datetime.datetime.now()
        date = now.strftime("%d-%m-%Y")
        time = now.strftime("%H:%M")
        case_id = f"case_{len(st.session_state.get('cases', [])) + 1:04d}"

        new_case = Case(case_id, description, owner, status, date, time, customer_id, category, priority)

        if "cases" not in st.session_state:
            st.session_state.cases = []
        st.session_state.cases.append(new_case)

        st.success(f"Case {case_id} toegevoegd.")