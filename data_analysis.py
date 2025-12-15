import pandas as pd
import matplotlib.pyplot as plt
import os

def show_statistics(filename="ledger.csv"):
    """Pandas와 Matplotlib을 활용한 데이터 분석 (Lecture 9)"""
    
    if not os.path.exists(filename):
        print("분석할 데이터 파일이 없습니다.")
        return

    try:
        df = pd.read_csv(filename)
        
        if df.empty:
            print("데이터가 비어있습니다.")
            return

        """자산 현황 요약 (수입/지출/잔액 계산)"""

        # '수입' 행만 뽑아서 Amount 합계 구하기
        total_income = df[df['Type'] == '수입']['Amount'].sum()
        
        # '지출' 행만 뽑아서 Amount 합계 구하기
        total_expense = df[df['Type'] == '지출']['Amount'].sum()
        
        # 잔액 계산
        current_balance = total_income - total_expense

        print("\n" + "="*30)
        print("[나의 자산 현황 요약]")
        print("="*30)
        # {:,}을 쓰면 천 단위 쉼표
        print(f"총 수입액 : {total_income:,}원")
        print(f"총 지출액 : {total_expense:,}원")
        print("-" * 30)
        print(f"현재 잔액 : {current_balance:,}원")
        print("="*30 + "\n")

        # 지출 데이터만 필터링 (불리안 인덱싱)
        expense_df = df[df['Type'] == '지출'] 

        if expense_df.empty:
            print("지출 내역이 없어 분석할 수 없습니다.")
            return

        # 카테고리별 지출 합계 계산 (Groupby)
        category_sum = expense_df.groupby('Category')['Amount'].sum()

        print("\n[카테고리별 지출 분석]")
        print(category_sum)

        # 시각화 (파이 차트, Lecture 9 Matplotlib)
        plt.figure(figsize=(8, 8)) # Figure 설정
        
        # 한글 폰트 설정 (Windows: Malgun Gothic, Mac: AppleGothic)
        plt.rcParams['font.family'] = 'Malgun Gothic' 
        
        plt.pie(category_sum, labels=category_sum.index, autopct='%1.1f%%', startangle=140)
        plt.title("나의 소비 패턴 분석")
        plt.show() # 그래프 출력

    except Exception as e:
        print(f"분석 중 오류가 발생했습니다: {e}")