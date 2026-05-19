from datetime import datetime

patient_name = input("Nhap ten benh nhan: ")

birth_year = int(input("Nhap nam sinh (VD: 2000): "))

sick_days = int(input("Nhap so ngay bi benh: "))

body_temperature = float(input("Nhap nhiet do co the (VD: 37.5): "))

medical_fee = float(input("Nhap chi phi kham: "))



current_year = datetime.now().year

if (
    patient_name.strip() == ""
    or birth_year < 1900
    or birth_year > current_year
    or sick_days < 0
    or body_temperature < 30
    or body_temperature > 45
    or medical_fee <= 0
):
    print("Dữ liệu không hợp lệ")
    exit()


patient_age = current_year - birth_year

extra_fee = medical_fee * 0.1

total_cost = medical_fee + extra_fee


if body_temperature > 38 and sick_days > 3:
    health_status = "Nguy hiểm"

elif body_temperature > 38:
    health_status = "ốt cao"

elif body_temperature > 37.5:
    health_status = "sốt nhẹ"

else:
    health_status = "bình thường"


if health_status == "Nguy hiểm":

    if patient_age > 60:
        priority_level = "Cấp cứu"

    else:
        priority_level = "Ưu tiên cao"

else:
    priority_level = "bình thường"


fee_level = "Cao" if total_cost > 500000 else "Thấp"


print(f"Tên bệnh nhân: {patient_name}\n"
      f"Tuổi: {patient_age}\n"
      f"ình trạng sức khỏe: {health_status}\n"
      f"Mức độ ưu tiên: {priority_level}\n"
      f"Phụ phí: {extra_fee}\n"
      f"Tổng chi phí: {total_cost}\n"
      f"Mức chi phí: {fee_level}")