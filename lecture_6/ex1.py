# tạo 1 class SinhVien có các thuộc tính: ID, Name, Điểm TA, Điểm Toán, Điểm Văn
# và phương thức get_diem_tb() in ra điểm tb của hs theo ID, phương thức get_diem_cac_mon() => in ra điểm 3 môn

class SinhVien:
    def __init__(self, id, name, math_score, eng_score, philology_score):
        self.id = id
        self.name = name
        self.math_score = math_score
        self.eng_score = eng_score
        self.philology_score = philology_score

    def get_average_score(self):
        return (self.math_score + self.eng_score + self.philology_score) / 3

    def get_total_score(self):
        return self.math_score + self.eng_score + self.philology_score

    def get_all_scores(self):
        print(f'''
            Điểm Toán: {self.math_score} 
            Điểm Văn: {self.eng_score}
            Điểm TA: {self.philology_score}
        ''')

sv1 = SinhVien(1, 'linh', 8,8,8)
sv1.get_all_scores()