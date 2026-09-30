import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import joblib
from sklearn.datasets import load_iris

# ==================== SET PAGE CONFIG ====================
st.set_page_config(
    page_title="Iris Flower Classifier - Pink Edition",
    page_icon="🌸",
    layout="wide"
)

# แอบใส่ CSS เปลี่ยนสีปุ่มให้เป็นสีชมพูหวานๆ 🎀
st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #FF69B4 !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
    }
    div.stButton > button:first-child:hover {
        background-color: #FF1493 !important;
    }
    </style>
""", unsafe_allow_html=True)

# โหลดข้อมูล Iris Dataset เพื่อเอาค่าเฉลี่ยมาเปรียบเทียบ
iris = load_iris()
feature_names = ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width']
species_names = iris.target_names

# คำนวณค่าเฉลี่ยของ Dataset แต่ละ Feature
df_iris = pd.DataFrame(iris.data, columns=feature_names)
dataset_averages = df_iris.mean().values

# โหลดโมเดลที่เทรนไว้ (หากไม่มีไฟล์โมเดล ให้สร้างโมเดลตัวอย่างชั่วคราว)
@st.cache_resource
def load_model():
    try:
        model = joblib.load('iris_model.pkl')
    except Exception:
        from sklearn.ensemble import RandomForestClassifier
        model = RandomForestClassifier(random_state=42)
        model.fit(iris.data, iris.target)
    return model

model = load_model()

# ==================== SIDEBAR ====================
with st.sidebar:
    st.markdown("### 🎀 Input Features")
    st.caption("Adjust the sliders to input flower measurements:")
    
    sepal_length = st.slider("📏 Sepal Length (cm)", min_value=4.0, max_value=8.0, value=7.10, step=0.01)
    sepal_width = st.slider("📏 Sepal Width (cm)", min_value=2.0, max_value=4.5, value=3.40, step=0.01)
    petal_length = st.slider("📏 Petal Length (cm)", min_value=1.0, max_value=7.0, value=3.80, step=0.01)
    petal_width = st.slider("📏 Petal Width (cm)", min_value=0.1, max_value=2.5, value=1.30, step=0.01)
    
    st.markdown("<br>", unsafe_allow_html=True)
    predict_btn = st.button("🌸 Predict Species", use_container_width=True)

# ==================== MAIN CONTENT ====================
st.title("🌸 Iris Flower Classifier")
st.write("Predict the species of Iris flowers using Machine Learning (Pink Theme ✨)")

st.markdown("---")

# คำนวณการทำนาย
input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
prediction = model.predict(input_data)[0]
probabilities = model.predict_proba(input_data)[0]

predicted_species = species_names[prediction].capitalize()
confidence = probabilities[prediction] * 100

col1, col2 = st.columns([1.1, 1])

# ----------------- COLUMN 1: INPUT VISUALIZATION -----------------
with col1:
    st.subheader("📈 Input Visualization")
    st.caption("Your Input vs Dataset Average")
    
    fig_bar = go.Figure()
    
    # แท่งแสดงค่า Input ของผู้ใช้ (สีชมพูเข้ม)
    fig_bar.add_trace(go.Bar(
        x=feature_names,
        y=[sepal_length, sepal_width, petal_length, petal_width],
        name='Your Input',
        marker_color='#FF1493', # Deep Pink
        text=[f"{sepal_length:.1f}", f"{sepal_width:.1f}", f"{petal_length:.1f}", f"{petal_width:.1f}"],
        textposition='auto'
    ))
    
    # แท่งแสดงค่าเฉลี่ยของ Dataset (สีชมพูอ่อน)
    fig_bar.add_trace(go.Bar(
        x=feature_names,
        y=dataset_averages,
        name='Dataset Average',
        marker_color='#FFB6C1', # Light Pink
        text=[f"{v:.2f}" for v in dataset_averages],
        textposition='auto'
    ))
    
    fig_bar.update_layout(
        barmode='group',
        height=380,
        margin=dict(l=20, r=20, t=20, b=40),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        xaxis_title="Features",
        yaxis_title="Value (cm)",
        plot_bgcolor='rgba(0,0,0,0)' # พื้นหลังกราฟโปร่งใส
    )
    st.plotly_chart(fig_bar, use_container_width=True)

# ----------------- COLUMN 2: PREDICTION RESULT -----------------
with col2:
    st.subheader("🎯 Prediction Result")
    
    # การ์ดแสดงผลคำนาย เปลี่ยนเกรเดียนท์เป็นโทนสีชมพู
    st.markdown(
        f"""
        <div style="
            background: linear-gradient(135deg, #FF7EB3, #FF758C);
            color: white;
            padding: 30px;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0px 4px 15px rgba(255,105,180,0.3);
            margin-bottom: 25px;
        ">
            <h3 style="margin: 0; font-size: 20px; font-weight: 500; opacity: 0.9;">Predicted Species</h3>
            <h1 style="margin: 15px 0; font-size: 42px; font-weight: 700;">{predicted_species}</h1>
            <p style="margin: 0; font-size: 16px; opacity: 0.9;">Confidence: {confidence:.1f}%</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("##### Probability Distribution")
    
    # กราฟแท่ง Probabilities
    fig_prob = go.Figure()
    
    # ปรับสีให้เข้ากับธีม (ชนิดที่ทายถูก = ชมพูเข้มสว่างๆ, ชนิดอื่น = ชมพูหม่น/เทา)
    colors = ['#F8BBD0' if i != prediction else '#FF007F' for i in range(3)]
    
    fig_prob.add_trace(go.Bar(
        x=[s.lower() for s in species_names],
        y=probabilities * 100,
        marker_color=colors,
        text=[f"{p*100:.1f}%" for p in probabilities],
        textposition='outside'
    ))
    
    fig_prob.update_layout(
        height=220,
        margin=dict(l=20, r=20, t=10, b=40),
        yaxis=dict(title="Probability (%)", range=[0, 115]),
        xaxis_title="Species",
        plot_bgcolor='rgba(0,0,0,0)'
    )
    st.plotly_chart(fig_prob, use_container_width=True)