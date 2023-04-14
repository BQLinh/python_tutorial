# mỗi 1 project cần 1 mỗi trường khác nhau vì chúng lưu trữ các thư viện với các version khác nhau

# ví dụ: project A sử dụng flask version 1.1, project B sử dụng version 3.3, nếu ko có môi trường riêng thì:
# - nếu chúng dùng 1 version thì code có thể không chạy( bị lỗi) 
# - nếu muốn chạy project A thì phải cài flask 1.1, rồi khi chạy project B thì ta phải xóa flask 1.1 đi và cài 3.3. 
# Nhưng thậm chí đôi khi chúng ta còn ko thể cài đc như vây. Vì các thư viện có liên đới với nhau

# cách tạo 1 môi trường:
# gõ câu: python3 -m venv env_name
# env_name là tên môi trường của mình, mình có thể để các tên khác ví dụ: linh_env => python3 -m venv linh_env
# thường thì tên môi trường mình sẽ để là env => cú pháp: python3 -m venv env
