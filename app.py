import streamlit as st
from datetime import datetime

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Contract Analysis Bot", layout="centered")

st.title("📄 Contract Analysis Bot")
st.write("Upload a contract file (TXT only)")

# ---------------- FILE UPLOAD ----------------
uploaded_file = st.file_uploader(
    "Choose a contract file",
    type=["txt"],
    help="Upload a .txt contract file"
)

if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8")
    lower_text = text.lower()

    # ---------------- CONTRACT CONTENT ----------------
    st.subheader("Contract Content")
    st.text_area("Text", text, height=300)

    # ---------------- BASIC ANALYSIS ----------------
    st.subheader("Basic Analysis")
    st.write(f"• Total characters: {len(text)}")
    st.write(f"• Total words: {len(text.split())}")

    # ---------------- CLAUSE DETECTION ----------------
    st.subheader("Clause Detection")

    termination = "termination" in lower_text
    payment = "payment" in lower_text or "pay" in lower_text
    indemnity = "indemnity" in lower_text
    jurisdiction = "jurisdiction" in lower_text
    dispute = "arbitration" in lower_text or "dispute" in lower_text

    def show_clause(found, name):
        if found:
            st.warning(f"⚠️ {name} clause detected")
        else:
            st.success(f"✅ {name} clause not found")

    show_clause(termination, "Termination")
    show_clause(payment, "Payment")
    show_clause(indemnity, "Indemnity")
    show_clause(jurisdiction, "Jurisdiction")
    show_clause(dispute, "Dispute Resolution")

    # ---------------- OVERALL RISK ----------------
    st.subheader("Overall Contract Risk")

    risk_score = 0
    if termination:
        risk_score += 2
    if indemnity:
        risk_score += 2
    if dispute:
        risk_score += 1
    if jurisdiction:
        risk_score += 1

    if risk_score >= 4:
        overall_risk = "HIGH"
        st.error("HIGH")
    elif risk_score >= 2:
        overall_risk = "MEDIUM"
        st.warning("MEDIUM")
    else:
        overall_risk = "LOW"
        st.success("LOW")

    # ---------------- CONTRACT SUMMARY ----------------
    st.subheader("Contract Summary")

    summary_points = []

    if "lease" in lower_text:
        summary_points.append("• This agreement defines lease-related terms")
    elif "vendor" in lower_text:
        summary_points.append("• This agreement defines vendor supply obligations")
    elif "service" in lower_text:
        summary_points.append("• This agreement defines service obligations")
    else:
        summary_points.append("• This contract defines obligations between parties")

    if payment:
        summary_points.append("• Payments are time-bound")
    if termination:
        summary_points.append("• Termination rights are clearly stated")
    if indemnity:
        summary_points.append("• Legal protection clauses are included")

    for point in summary_points:
        st.write(point)

    # ---------------- AUDIT LOG ----------------
    st.subheader("Audit Log")
    st.write(f"Analyzed on: {datetime.now().strftime('%d %B %Y %H:%M')}")




#streamlit run app.py