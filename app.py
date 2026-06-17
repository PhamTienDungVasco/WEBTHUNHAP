import streamlit as st
import base64

def chen_hinh_nen(ten_file):
    with open(ten_file, "rb") as f:
        du_lieu = f.read()
    chuoi_ma_hoa = base64.b64encode(du_lieu).decode()
    
    css_hinh_nen = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{chuoi_ma_hoa}");
        background-size: cover;
    }}
    [data-testid="stVerticalBlock"] > div:has(div.stNumberInput) {{
        background-color: rgba(255, 255, 255, 0.8);
        padding: 20px;
        border-radius: 10px;
    }}
    h1 {{
        color: black;
    }}
    </style>
    """
    st.markdown(css_hinh_nen, unsafe_allow_html=True)

chen_hinh_nen('background.jpg')

st.title("Ứng dụng tính thuế thu nhập cá nhân")

thu_nhap = st.number_input(
    "Nhập tổng thu nhập hàng tháng (triệu đồng)",
    min_value=0.0,
    value=20.0
)

nguoi_phu_thuoc = st.number_input(
    "Nhập số người phụ thuộc",
    min_value=0,
    value=1,
    step=1
)

if st.button("Tính toán"):
    giam_tru_ban_than = 11.0
    giam_tru_phu_thuoc = 4.4
    
    tong_giam_tru = giam_tru_ban_than + (nguoi_phu_thuoc * giam_tru_phu_thuoc)
    thu_nhap_tinh_thue = thu_nhap - tong_giam_tru
    
    if thu_nhap_tinh_thue <= 0:
        thu_nhap_tinh_thue = 0
        thue_phai_nop = 0
    else:
        if thu_nhap_tinh_thue <= 5:
            thue_phai_nop = thu_nhap_tinh_thue * 0.05
        elif thu_nhap_tinh_thue <= 10:
            thue_phai_nop = thu_nhap_tinh_thue * 0.10 - 0.25
        elif thu_nhap_tinh_thue <= 18:
            thue_phai_nop = thu_nhap_tinh_thue * 0.15 - 0.75
        elif thu_nhap_tinh_thue <= 32:
            thue_phai_nop = thu_nhap_tinh_thue * 0.20 - 1.65
        elif thu_nhap_tinh_thue <= 52:
            thue_phai_nop = thu_nhap_tinh_thue * 0.25 - 3.25
        elif thu_nhap_tinh_thue <= 80:
            thue_phai_nop = thu_nhap_tinh_thue * 0.30 - 5.85
        else:
            thue_phai_nop = thu_nhap_tinh_thue * 0.35 - 9.85

    st.success("Kết quả tính toán")
    st.write(f" Tổng các khoản giảm trừ: **{tong_giam_tru:,.2f} triệu đồng**")
    st.write(f" Thu nhập tính thuế: **{thu_nhap_tinh_thue:,.2f} triệu đồng**")
    st.write(f" Số thuế TNCN phải nộp: **{thue_phai_nop:,.2f} triệu đồng**")