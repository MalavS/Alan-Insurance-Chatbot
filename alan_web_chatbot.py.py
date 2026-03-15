import streamlit as st

st.set_page_config(
    page_title="Alan Insurance AI Advisor",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for beautiful dark theme
st.markdown("""
    <style>
    .main {background-color: #0f172a;}
    .stButton > button {border-radius: 12px; height: 60px; font-size: 16px; font-weight: bold;}
    .stMetric {background-color: #1e293b; padding: 20px; border-radius: 12px;}
    h1 {color: #60a5fa !important; font-size: 3rem !important;}
    .stAppViewContainer {background-color: #0f172a;}
    </style>
""", unsafe_allow_html=True)

st.title("🤖 Alan Insurance AI Advisor")
st.markdown("**Get your perfect Bear or Marmot plan in 3 clicks** 🚀")

# Sidebar with instructions
with st.sidebar:
    st.markdown("## 📋 Quick Guide")
    st.markdown("""
    **Individual:**
    • Employed → Marmot (comprehensive)
    • Self-employed → Bear (basic)
    
    **Business:**
    • 1-49 employees → Bear Group
    • 50-500 → Marmot Group (20% cheaper!)
    """)
    st.markdown("---")
    st.markdown("*Built by Malav Shah | Alan Internship Q3*")

# Main content
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("👤 **Individual**")
    if st.button("Employed - Full Coverage", use_container_width=True, type="primary"):
        st.session_state.plan = "Marmot"
        st.session_state.type = "individual"
        st.session_state.status = "employed"
        st.rerun()
    
    if st.button("Self-Employed - Basic", use_container_width=True):
        st.session_state.plan = "Bear"
        st.session_state.type = "individual" 
        st.session_state.status = "self-employed"
        st.rerun()

with col2:
    st.subheader("🏢 **Business**")
    employees = st.number_input("Employees (1-500):", 1, 500, 25, help="Enter your company size")
    
    col1b, col2b = st.columns(2)
    with col1b:
        if st.button("Get Group Plan", use_container_width=True):
            st.session_state.plan = "Bear" if employees <= 49 else "Marmot"
            st.session_state.type = "business"
            st.session_state.employees = employees
            st.rerun()
    
    with col2b:
        if st.button("Custom Quote", use_container_width=True, type="secondary"):
            st.session_state.show_custom = True
            st.rerun()

# Results section
if 'plan' in st.session_state:
    st.markdown("---")
    
    if st.session_state.type == "individual":
        with st.container():
            colr1, colr2 = st.columns([2, 1])
            with colr1:
                st.markdown(f"## 🎯 **Recommended: Alan {st.session_state.plan} Plan**")
                st.markdown(f"**Status:** {st.session_state.status.title()}")
                
                if st.session_state.plan == "Marmot":
                    st.success("""
                    ### ✅ **Comprehensive Coverage**
                    - Prescription drugs + paramedical (physio, massage)
                    - Dental (checkups, major procedures)
                    - Vision + prescription glasses  
                    - **Semi-private hospital rooms**
                    """)
                else:
                    st.success("""
                    ### ✅ **Essential Coverage**
                    - Prescription drugs
                    - Paramedical services
                    - Dental (checkups, cleanings)
                    - **Vision coverage**
                    """)
            
            with colr2:
                st.button("📅 Book Demo", use_container_width=True, type="primary")
                st.button("🔄 New Recommendation", on_click=lambda: st.cache_data.clear(), use_container_width=True)
    
    else:  # business
        st.markdown(f"## 🎯 **Recommended: Alan {st.session_state.plan} Group Plan**")
        st.markdown(f"**{st.session_state.employees} employees**")
        
        st.success(f"""
        ### 💰 **Group Benefits** 
        - **20% cheaper** than traditional brokers
        - Rx, dental, paramedical for all employees
        - Instant online enrollment (no paperwork!)
        - Perfect for Canadian tech startups & SMBs
        """)
        
        colb1, colb2 = st.columns(2)
        with colb1:
            st.button("📅 Group Demo", use_container_width=True, type="primary")
        with colb2:
            st.button("🔄 New Quote", on_click=lambda: st.cache_data.clear(), use_container_width=True)

# Footer
st.markdown("---")
st.markdown("*Pure Python/Streamlit • Production-ready • Built for Alan Canada Internship*")

if __name__ == "__main__":
    pass
