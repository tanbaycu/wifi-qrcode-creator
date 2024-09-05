from wifi_qrcode_generator import wifi_qrcode
from PIL import Image

def get_authentication_type():
    auth_type = input("Nhập loại xác thực (WPA/WPA2): ").strip()
    if auth_type not in ['WPA', 'WPA2']:
        raise ValueError("Loại xác thực phải là WPA hoặc WPA2.")
    return auth_type

try:
    # mã hóa xác thực authen hidden là False
    ssid = input("Nhập tên WiFi (SSID): ")
    password = input("Nhập mật khẩu WiFi: ")
    hidden = input("WiFi có ẩn không? (True/False): ").strip().lower() == 'true'
    authentication_type = get_authentication_type()

    # tiến hành tạo
    qr_code = wifi_qrcode(
        ssid=ssid, 
        hidden=hidden,
        authentication_type=authentication_type, 
        password=password
    )

    # dạng ảnh
    qr_code_img = qr_code.make_image()

    # save ảnh
    file_name = "wifi_code_img.png"
    qr_code_img.save(file_name)

    # mở ảnh lên bằng PIL
    image = Image.open(file_name)
    image.show()

    print(f"QR code đã được lưu và mở thành công từ file {file_name}")

except ValueError as e:
    print(f"Lỗi: {e}")

except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")

