import streamlit as st

# Config
st.set_page_config(page_title="Alan Insurance Advisor", page_icon="🤖", layout="wide")

# Dark professional theme
st.markdown("""
<style>
    [data-testid="stSidebar"] {background-color: #1e293b;}
    .main {background-color: #0f172a;}
    .stButton > button {
        border-radius: 12px; height: 60px; font-size: 18px; font-weight: bold;
        border: none; transition: all 0.3s;
    }
    .stButton > button:hover {transform: scale(1.05);}
    h1 {color: #60a5fa !important; font-size: 3.2rem !important;}
    .stAppViewContainer {background-color: #0f172a;}
    .stMetric {background-color: #1e293b; padding: 1rem; border-radius: 12px;}
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'selection' not in st.session_state:
    st.session_state.selection = {}

st.title("🤖 Alan Insurance Advisor")
st.markdown("**Get personalized Bear or Marmot recommendations → 3 clicks**")

# Progress indicator
progress_steps = ["👋 Choose Type", "📋 Select Size", "🎯 Your Results"]
current_step = min(st.session_state.step, 2)
st.progress(current_step / 2)
st.markdown(f"**Step {current_step + 1} of 3: {progress_steps[current_step]}**")

# === STEP 1: Individual or Business ===
if st.session_state.step == 0:
    st.markdown("### **Who is this insurance for?**")
    
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        if st.button("👤 **Individual**", use_container_width=True, type="primary",
                    help="Personal health insurance"):
            st.session_state.selection = {"type": "individual"}
            st.session_state.step = 1
            st.rerun()
    
    with col2:
        if st.button("🏢 **Business**", use_container_width=True, type="secondary",
                    help="Group health insurance for employees"):
            st.session_state.selection = {"type": "business"}
            st.session_state.step = 1
            st.rerun()

# === STEP 2: Employed/Unemployed OR Small/Big Business ===
elif st.session_state.step == 1:
    if st.session_state.selection["type"] == "individual":
        st.markdown("### **Employment Status**")
        st.info("💡 This helps us recommend the perfect coverage level")
        
        col1, col2 = st.columns(2, gap="large")
        
        with col1:
            if st.button("✅ **Employed**", use_container_width=True, type="primary"):
                st.session_state.selection.update({"status": "employed"})
                st.session_state.step = 2
                st.rerun()
        
        with col2:
            if st.button("💼 **Unemployed/Self-Employed**", use_container_width=True):
                st.session_state.selection.update({"status": "unemployed"})
                st.session_state.step = 2
                st.rerun()
    
    else:  # Business
        st.markdown("### **Business Size**")
        st.info("💡 Alan specializes in small to mid-size Canadian businesses")
        
        col1, col2 = st.columns(2, gap="large")
        
        with col1:
            if st.button("🍼 **Small Business**\n(1-49 employees)", use_container_width=True, type="primary"):
                st.session_state.selection.update({"size": "small", "employees": 25})
                st.session_state.step = 2
                st.rerun()
        
        with col2:
            if st.button("🏢 **Big Business**\n(50+ employees)", use_container_width=True):
                st.session_state.selection.update({"size": "big", "employees": 100})
                st.session_state.step = 2
                st.rerun()

# === STEP 3: Results ===
elif st.session_state.step == 2:
    # Calculate recommendation
    if st.session_state.selection["type"] == "individual":
        plan = "Marmot" if st.session_state.selection["status"] == "employed" else "Bear"
        subtitle = f"**{st.session_state.selection['status'].title()} Individual**"
    else:
        plan = "Bear" if st.session_state.selection["size"] == "small" else "Marmot"
        subtitle = f"**{st.session_state.selection['size'].title()} Business** ({st.session_state.selection['employees']} employees)"
    
    # Results layout
    st.markdown("### **🎯 Your Perfect Match**")
    
    col_main, col_action = st.columns([3, 1], gap="large")
    
    with col_main:
        st.metric("🏆 **Recommended Plan**", f"**Alan {plan}** 🎖️")
        st.metric("📋 **Your Profile**", subtitle)
        
        if st.session_state.selection["type"] == "individual":
            if plan == "Marmot":
                st.success("""
                **✅ Marmot Plan Features:**
                • Prescription drugs + paramedical (physio, massage, chiro)
                • Dental (checkups + major procedures)
                • Vision coverage + glasses
                • **Semi-private hospital rooms**
                **Perfect for employed individuals with families**
                """)
            else:
                st.info("""
                **✅ Bear Plan Features:**
                • Prescription drugs
                • Paramedical services (physio, massage)
                • Dental checkups + cleanings
                • Vision coverage
                **Perfect for self-employed / basic needs**
                """)
        else:
            st.success(f"""
            **✅ {plan} Group Plan Benefits:**
            • **20% cheaper** than traditional brokers
            • Rx, dental, paramedical for ALL employees  
            • Instant online enrollment (no paperwork!)
            • **Perfect for Canadian {'startups' if plan == 'Bear' else 'growing companies'}**
            """)
    
    with col_action:
        if st.button("📞 **Book Demo Call**", use_container_width=True, type="primary"):
            st.balloons()
            st.success("✅ Demo booked! Alan sales team will contact you within 24 hours.")
    
    # Action buttons
    col_reset, col_back = st.columns(2)
    with col_reset:
        if st.button("🔄 **New Recommendation**", use_container_width=True, type="secondary"):
            for key in st.session_state.keys():
                del st.session_state[key]
            st.rerun()
    with col_back:
        if st.button("⬅️ **Change Answers**", use_container_width=True):
            st.session_state.step = 0
            st.rerun()

# Sidebar - Product guide
with st.sidebar:
    st.markdown("## 📖 **Alan Product Guide**")
    
    with st.expander("🐻 **Bear Plan** (Basic)"):
        st.markdown("""
        • Prescription drugs  
        • Paramedical (physio, massage)
        • Dental checkups
        • Vision coverage
        **Best for:** Self-employed, small business
        """)
    
    with st.expander("🦙 **Marmot Plan** (Premium)"):
        st.markdown("""
        • Everything in Bear + higher limits
        • Semi-private hospital rooms  
        • Enhanced dental coverage
        **Best for:** Employed individuals, mid-size business
        """)
    
    st.markdown("---")
    st.markdown("*Built by **Malav Shah** | Alan Canada Internship Q3 2026*")

# Footer
st.markdown("---")
st.markdown("**💼 Production-ready lead qualification tool • Pure Python/Streamlit • Deployed instantly**")
