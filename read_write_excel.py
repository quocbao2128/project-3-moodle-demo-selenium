import pandas as pd


# Hàm hỗ trợ đọc dữ liệu từ file excel
# Tham số(parameter):
# file_path: tên file excel bao gồm cả phần đuôi mở rộng
# sheet_name: tên của trang(sheet) trong file excel
def read_from_excel(file_path, sheet_name):
    # Đọc dữ liệu từ file Excel
    input_data = pd.read_excel(file_path, sheet_name=sheet_name).fillna('')

    # Chuyển đổi thành list của tuples
    data = input_data.to_records(index=False).tolist()

    return data


# Hàm hỗ trợ ghi dữ liệu vào file excel
# Tham số(parameter):
# file_path: đường dẫn tới file excel
# sheet_name: tên trang(sheet) trong file excel
# col_index: chỉ số cột cần ghi dữ liệu vào
# row_index: chỉ số dòng cần ghi dữ liệu vào
# value: giá trị cần ghi vào
def write_to_excel(file_path, sheet_name, col_index, row_index, value):
    df2 = pd.DataFrame([value])

    with pd.ExcelWriter(file_path, engine='openpyxl', mode="a", if_sheet_exists="overlay") as writer:
        # Start at F2 write value in df2
        df2.to_excel(writer, sheet_name=sheet_name, index=False, header=False, startcol=col_index, startrow=row_index)

