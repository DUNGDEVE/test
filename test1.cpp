#include <iostream>
#include <string>
#include <vector>

using namespace std;

// Khai báo lớp SinhVien
class SinhVien {
public:
    string ten;
    int maSV;
    int tuoi;

    // Phương thức nhập thông tin sinh viên từ bàn phím
    void nhapThongTin() {
        cout << "Nhập tên: ";
        cin.ignore();
        getline(cin, ten);

        cout << "Nhập mã sinh viên: ";
        cin >> maSV;

        cout << "Nhập tuổi: ";
        cin >> tuoi;
    }

    // Phương thức hiển thị thông tin sinh viên
    void hienThiThongTin() const{
        cout << "Tên: " << ten << endl;
        cout << "Mã sinh viên: " << maSV << endl;
        cout << "Tuổi: " << tuoi << endl;
    }
};

int main() {
    // Tạo một vector để lưu trữ danh sách sinh viên
    vector<SinhVien> danhSachSinhVien;

    int soLuongSinhVien;
    cout << "Nhập số lượng sinh viên: ";
    cin >> soLuongSinhVien;

    // Nhập thông tin cho từng sinh viên
    for (int i = 0; i < soLuongSinhVien; i++) {
        SinhVien sinhVien;
        cout << "Nhập thông tin cho sinh viên " << i + 1 << ":" << endl;
        sinhVien.nhapThongTin();
        danhSachSinhVien.push_back(sinhVien);
    }

    // Hiển thị danh sách sinh viên
    cout << "Danh sách sinh viên:" << endl;
    for (const SinhVien& sv : danhSachSinhVien) {
        sv.hienThiThongTin();
        cout << "---------------------" << endl;
    }

    return 0;
}
