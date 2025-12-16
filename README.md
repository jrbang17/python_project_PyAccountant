# PyAccountant (Python 스마트 가계부)

## 1. 프로젝트 소개
**PyAccountant**는 파이썬 프로그래밍 수업에서 배운 내용을 이용하여 만든 스마트 가계부 프로그램이다. 
단순히 얼마를 쓰고 벌었는지뿐만 아니라 `Pandas`와 `Matplotlib`을 활용하여 사용자의 소비 패턴을 카테고리별로 분석하고 원그래프로 시각화해준다.

## 2. 선정 이유
가계부를 만들려고 하면 일일이 타이핑해서 카테고리별로 분류하는 게 불편하고 은행 앱에서도 한 달에 얼마나, 무엇에 돈을 사용하는지 한눈에 알기 어려워 이를 수업 시간에 배운 Python 코드를 통해 구현해보고 싶어서 이 주제를 선정하게 되었다. 

## 3. 주요 기능 및 적용된 강의 내용
* **객체 지향 프로그래밍 (Lecture 6):** `AccountBook` 클래스를 통해 데이터를 관리하고 기능을 모듈화했다.
* **파일 입출력 및 데이터 보존 (Lecture 8):** `csv` 모듈을 사용하여 데이터를 파일로 영구 저장하며, 프로그램 재실행 시에도 데이터가 유지된다.
* **자산 현황 요약 및 분석 (Lecture 9):** `Pandas`를 활용하여 **총 수입, 총 지출, 현재 잔액**을 즉시 계산하여 보여준다.
* **데이터 시각화 (Lecture 9):** `Matplotlib`을 사용하여 소비 카테고리별 지출 비율을 **원그래프**로 시각화한다.
* **Pythonic Code (Lecture 5):** `List Comprehension`, `enumerate` 등을 사용하여 효율적인 코드를 작성했다.

## 4. 파일 구조
```text
PyAccountant/
│
├── main.py              # 프로그램 실행 파일 (메인)
├── README.md            # 설명 파일
├── account_manager.py   # 가계부 클래스 (데이터 저장/로드/조회)
├── data_analysis.py     # 자산 현황 요약 및 소비 패턴 분석(그래프) 모듈
└── ledger.csv           # 데이터 저장용 CSV (자동 생성됨)
```

## 5. 실행 방법
1. 필요한 라이브러리 설치:
   ```bash
   pip install pandas matplotlib
   ```
2. 프로그램 실행:
   ```bash
   python main.py
   ```

## 6. 실행 결과
<img width="767" height="618" alt="image" src="https://github.com/user-attachments/assets/e263ed9a-f8eb-46f0-8a9c-ddd19da1a3bc" />
<img width="397" height="546" alt="image" src="https://github.com/user-attachments/assets/947ce075-eba3-4c54-8420-af3a238cab96" />
<img width="546" height="522" alt="image" src="https://github.com/user-attachments/assets/6b265224-c68e-499e-934c-7d4e2888ffef" />




