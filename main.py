from account_manager import AccountBook
from data_analysis import show_statistics
import sys

def main():
    my_book = AccountBook() # 인스턴스 생성

    while True:
        print("\n" + "="*30)
        print("PyAccountant 스마트 가계부")
        print("="*30)
        print("1. 내역 추가하기")
        print("2. 전체 내역 보기")
        print("3. 자산 현황 요약 및 소비 패턴 분석(그래프)")
        print("4. 종료")
        
        choice = input("메뉴를 선택하세요: ")

        if choice == '1':
            date = input("날짜(YYYY-MM-DD): ")
            category = input("카테고리(식비/교통/쇼핑 등): ")
            desc = input("내용: ")
            amount = input("금액: ")
            t_type = input("타입(수입/지출): ")
            my_book.add_transaction(date, category, desc, amount, t_type) # 메서드 호출
            
        elif choice == '2':
            my_book.show_all_history()
            
        elif choice == '3':
            print("데이터 분석을 시작합니다...")
            show_statistics()
            
        elif choice == '4':
            print("프로그램을 종료합니다.")
            sys.exit()
            
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")

if __name__ == "__main__": # 모듈 직접 실행 확인
    main()