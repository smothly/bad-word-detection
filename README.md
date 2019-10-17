# BadWordDetection
## 비속어 탐지 모델

---

# Outline
- 욕설 키워드 기반 크롤링(네이버 뉴스, 카페, 블로그, 디씨인사이드, 네이트 뉴스)
- 회의나 공식석상에서 나올법한 단어 위주로 학습(약 18000개 라벨링)
- 자모분리를 통한 fasttext word embedding vocab구성
- 정확도 약 85퍼
- 데이터가 커서 올라가지 않음

---

# Process
- 문장에서 정규식표현으로 욕설이 나오는 부분 추출
- 추출된 어절 중심으로 좌우 단어 trigram 반환 ex) (나는, 바보, 멍청이, 3) 3번째위치에 바보가 있고 좌우어절은 나는, 멍청이 이다
- trigram을 fasttext embedding model을 활용하여 vectorize
- vectorize된 데이터를 Random Forest or 1DCNN Model에 넣어 예측

---

# Test
-
