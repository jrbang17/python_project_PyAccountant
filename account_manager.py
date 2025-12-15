import csv
import os

class AccountBook:
    """(Lecture 6 객체 지향형 프로그래밍)"""
    
    def __init__(self, filename="ledger.csv"):
        self.filename = filename
        self.columns = ["Date", "Category", "Description", "Amount", "Type"] # 날짜, 카테고리, 설명, 금액, 수입/지출
        self._initialize_file()

    def _initialize_file(self):
        """(Lecture 8 파일 입출력)"""
        if not os.path.exists(self.filename):
            with open(self.filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(self.columns)

    def add_transaction(self, date, category, desc, amount, t_type):
        """거래 내역 추가 메서드"""
        try:
            amount = int(amount) # 예외 처리 가능성 확인
        except ValueError:
            print("금액은 숫자로 입력해야 합니다.")
            return

        with open(self.filename, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([date, category, desc, amount, t_type])
        print("저장이 완료되었습니다.")

    def show_all_history(self):
        """(Lecture 5 리스트 컴프리헨션 활용)"""
        try:
            with open(self.filename, mode='r', encoding='utf-8') as file:
                reader = csv.reader(file)
                data = [row for row in reader]
                
                if len(data) <= 1:
                    print("기록된 내역이 없습니다.")
                    return

                for idx, row in enumerate(data): # Lecture 5 enumerate
                    if idx == 0: continue # 헤더 건너뛰기
                    print(f"[{idx}] 날짜: {row[0]} | 분류: {row[1]} | 내용: {row[2]} | 금액: {row[3]}원 | 타입: {row[4]}")
        except FileNotFoundError:
            print("파일이 존재하지 않습니다.")