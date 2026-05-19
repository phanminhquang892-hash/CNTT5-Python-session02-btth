import random

patient_name = input("Nhập tên bệnh nhân: ")
gender = input("Nhập giới tính: ")
birth_year = input("Nhập năm sinh: ")
phone_number = input("Nhập số điện thoại: ")
email = input("Nhập email: ")
symptom = input("Nhập triệu chứng ban đầu: ")
examination_fee = input("Nhập chi phí khám: ")

random_number = random.randint(100,999)
patient_id = "BN" + str(birth_year) + str(random_number)

print(
    f"Mã BN      : {patient_id}\n"
    f"Tên        : {patient_name})\n"
    f"Giới tính  : {gender} \n"
    f"Năm sinh   : {int(birth_year)}\n"
    f"Điện thoại : {phone_number} \n"
    f"Email      : {email} \n"
    f"Triệu chứng: {symptom} \n"
    f"Chi phí    : {float(examination_fee)} VND )"
)
