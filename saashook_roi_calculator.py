import streamlit as st

# Page config
st.set_page_config(
    page_title="ROI Calculator | SaaSHook",
    page_icon="💰",
    layout="centered"
)

# Branding
st.title("SaaSHook ROI Calculator")
st.markdown(
    """
    **Find out if your ad spend is working — or burning cash.**

    This free ROI calculator shows how efficiently your SaaS marketing is turning spend into revenue.  
    Built for B2B founders, growth leads & performance marketers.

    _Powered by [SaaSHook](https://saashook.com) — We help SaaS brands 3x their pipeline with conversion-obsessed marketing._
    """
)

# Inputs
st.header("Enter Your Numbers")
ad_spend = st.number_input("Total Ad Spend ($)", min_value=0.0, step=10.0, format="%.2f")
revenue = st.number_input("Revenue Attributed to Campaign ($)", min_value=0.0, step=10.0, format="%.2f")

# Calculations
if ad_spend > 0:
    roi = ((revenue - ad_spend) / ad_spend) * 100
    roas = revenue / ad_spend
    profit = revenue - ad_spend

    st.markdown("---")
    st.subheader("Results")
    st.metric("ROI (%)", f"{roi:.2f}%", help="Return on Investment = Net Profit / Spend")
    st.metric("ROAS", f"{roas:.2f}", help="Return on Ad Spend = Revenue / Spend")
    st.metric("Net Profit", f"${profit:.2f}")
else:
    st.info("Enter your ad spend to calculate ROI.")

# CTA
st.markdown("---")
st.subheader("Not Happy With Your ROI?")
st.markdown(
    """
    **SaaSHook** builds conversion-optimized paid funnels that drive pipeline — not just clicks.

    → [Book a Free Growth Audit](https://saashook.com)  
    → Or explore our [LinkedIn + Paid Ads system](https://saashook.com)

    Let’s 3x your pipeline — the smart way.
    """
)