import streamlit as st
import datetime
from models import Case

st.title("✏️ Case Bewerken")

if "selected_case_id" not in st.session_state:
    st.warning("Geen case geselecteerd. Ga terug naar de homepage en kies een case.")
    st.stop()

if "cases" not in st.session_state or not st.session_state.cases:
    st.info("Er zijn nog geen cases beschikbaar om te bewerken.")
    st.stop()

selected_case = None
for case in st.session_state.cases:
    if case.case_id == st.session_state.selected_case_id:
        selected_case = case
        break

if selected_case is None:
    st.error("Geselecteerde case niet gevonden.")
    st.stop()

st.write(f"**Status:** {selected_case.status}")
st.write(f"**Eigenaar:** {selected_case.owner}")
st.write(f"**Datum/tijd:** {selected_case.date} {selected_case.time}")
st.write(f"**Klant ID:** {selected_case.customer_id}")
st.write(f"**Categorie:** {selected_case.category}")
st.write(f"**Prioriteit:** {selected_case.priority}")
if selected_case.resolved_at:
    st.write(f"**Afgehandeld op:** {selected_case.resolved_at}")

new_status = st.selectbox(
    f"Wijzig status van {selected_case.case_id}",
    options=["open", "in behandeling", "afgehandeld"],
    index=["open", "in behandeling", "afgehandeld"].index(selected_case.status),
    key=f"status_{selected_case.case_id}"
)
if new_status != selected_case.status:
    selected_case.status = new_status
    if new_status == "afgehandeld":
        selected_case.resolved_at = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
    st.success(f"Status van {selected_case.case_id} bijgewerkt naar '{new_status}'.")

note_author = st.text_input("Auteur", key=f"author_{selected_case.case_id}")
note_text = st.text_area("Notitie", key=f"note_{selected_case.case_id}")
if st.button("Voeg notitie toe", key=f"btn_{selected_case.case_id}"):
    timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
    if not hasattr(selected_case, "notes") or selected_case.notes is None:
        selected_case.notes = []
    selected_case.notes.append({
        "timestamp": timestamp,
        "author": note_author,
        "text": note_text
    })
    st.success(f"Notitie toegevoegd aan {selected_case.case_id}")

if selected_case.notes:
    st.markdown("**Notities:**")
    for note in selected_case.notes:
        st.markdown(f"- [{note['timestamp']}] *{note['author']}*: {note['text']}")