# BadWordDetection
## 비속어 탐지 모델

> # Outline

- 욕설 키워드 기반 크롤링(네이버 뉴스, 카페, 블로그, 디씨인사이드, 네이트 뉴스)
- STT변환을 통해 나올 수 있는 단어(완전한 글자) 위주로 학습(약 14000개 라벨링)
- 자모분리를 통한 fasttext word embedding vocab구성
- RandomForest: accuracy: 약 86퍼, f1-score: 약85퍼
- 1DCNN: accuracy: 약 86퍼, f1-score: 약89퍼
- 학습 데이터가 커서 올라가지 않음

---

> # Process

- 문장에서 정규식표현으로 욕설이 나오는 부분 추출
- 추출된 어절 중심으로 좌우 단어 trigram 반환 ex) (나는, 바보, 멍청이, 3) 3번째위치에 바보가 있고 좌우어절은 나는, 멍청이 이다
- trigram을 fasttext embedding model을 활용하여 vectorize
- vectorize된 데이터를 Random Forest or 1DCNN Model에 넣어 예측
- EDA -> FastTextVocab -> TrigramVectorize -> 1DCNN or RandomForest -> Test
---

> # Test

- Pretrained 모델로 예측해보기
- Test.ipynb 실행

---

> # vocab 시각화

### vocab 2차원으로 임베딩 후 plot
![image](https://trello-attachments.s3.amazonaws.com/5d6cac86cbfe1b604908c66b/5da7f09503d7a77cb20ecdd2/3253a5efe850ba0f591326219ac3510f/word_embedding_2dim.png)

### 유사한 단어들 뽑아보기
![image](https://trello-attachments.s3.amazonaws.com/5d6cac86cbfe1b604908c66b/5da7f09503d7a77cb20ecdd2/247f9863ee368cb8a865dce8405c5f21/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7_2019-10-17_%EC%98%A4%ED%9B%84_1.42.00.png)

---

> # 모델 결과

### 1DCNN
![image](https://trello-attachments.s3.amazonaws.com/5d831fcfe983994f027abcdf/432x288/81114955f146e917e23261cba4ea83d4/1DCNN_reuslt.png)

### Random Forest
![image](https://trello-attachments.s3.amazonaws.com/5d831fcfe983994f027abcdf/428x172/3be62876f0ae2aefcd430c1e2b810a9f/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2019-10-17_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_2.07.58.png)
