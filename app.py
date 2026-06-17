import streamlit as st
import time
st.title("App tính thuế thu nhập cá nhân _ đề tài 7_Võ Thị Bảo Như ")
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
    with st.spinner("Đang xử lý dữ liệu... Vui lòng chờ!"):
        time.sleep(1.5) 
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

st.image("anh.jpg")