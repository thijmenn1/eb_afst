import streamlit as st
from models import Case
import random
import pandas as pd

def genereer_demo_cases():
    namen = ["Tim", "Sophie", "Jeroen", "Fatima", "Lars", "Emma"]
    categorieën = ["Technisch", "Administratief", "Service", "Facturatie"]
    prioriteiten = ["laag", "normaal", "hoog"]
    statussen = ["open", "in behandeling", "afgehandeld"]

    for i in range(1, 31):
        case_id = f"case_{i:04d}"
        description = f"Voorbeeldcase {i}"
        owner = f"med_{random.randint(100, 999)}"
        status = random.choice(statussen)
        date = f"{random.randint(1,28):02d}-0{random.randint(1,9)}-2024"
        time = f"{random.randint(8,17):02d}:{random.randint(0,59):02d}"
        customer_id = f"klant_{random.randint(1000,9999)}"
        category = random.choice(categorieën)
        priority = random.choice(prioriteiten)

        case = Case(case_id, description, owner, status, date, time, customer_id, category, priority)
        st.session_state.cases.append(case)

col1, col2, col3 = st.columns([6, 1, 2])

with col3:
    if os.path.exists("logo_kleur.png"):
        st.image("logo_kleur.png", width=300)
    else:
        st.warning("Logo kon niet worden geladen.")

toon_demo = st.checkbox("Toon demo-cases", value=True)

if "cases" not in st.session_state:
    st.session_state.cases = []

if toon_demo and not st.session_state.cases:
    genereer_demo_cases()

st.title("Cases – Homepagina")
st.subheader("Overzicht van alle cases")

if st.session_state.cases:
    case_data = [{
        "Case ID": c.case_id,
        "Beschrijving": c.description,
        "Status": c.status,
        "Prioriteit": c.priority,
        "Eigenaar": c.owner
    } for c in st.session_state.cases]

    df = pd.DataFrame(case_data)
    st.dataframe(df, use_container_width=True)

    geselecteerde_case_id = st.selectbox(
        "Selecteer een case om te bewerken:",
        [c.case_id for c in st.session_state.cases]
    )

    if st.button("✏️ Bewerk geselecteerde case"):
        st.session_state.selected_case_id = geselecteerde_case_id
        st.switch_page("pages/Bewerken.py")

# Nieuwe pagina voor het beheren van medewerkers
if st.button("Beheer medewerkers"):
    st.switch_page("pages/Login.py")
