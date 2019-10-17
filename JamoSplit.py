#!/usr/bin/env python
# coding: utf-8

# # 자모 스플릿 하는 코드

# In[54]:


CHOSUNGS = [u'ㄱ',u'ㄲ',u'ㄴ',u'ㄷ',u'ㄸ',u'ㄹ',u'ㅁ',u'ㅂ',u'ㅃ',u'ㅅ',u'ㅆ',u'ㅇ',u'ㅈ',u'ㅉ',u'ㅊ',u'ㅋ',u'ㅌ',u'ㅍ',u'ㅎ']
JOONGSUNGS = [u'ㅏ',u'ㅐ',u'ㅑ',u'ㅒ',u'ㅓ',u'ㅔ',u'ㅕ',u'ㅖ',u'ㅗ',u'ㅘ',u'ㅙ',u'ㅚ',u'ㅛ',u'ㅜ',u'ㅝ',u'ㅞ',u'ㅟ',u'ㅠ',u'ㅡ',u'ㅢ',u'ㅣ']
JONGSUNGS = [u'_',u'ㄱ',u'ㄲ',u'ㄳ',u'ㄴ',u'ㄵ',u'ㄶ',u'ㄷ',u'ㄹ',u'ㄺ',u'ㄻ',u'ㄼ',u'ㄽ',u'ㄾ',u'ㄿ',u'ㅀ',u'ㅁ',u'ㅂ',u'ㅄ',u'ㅅ',u'ㅆ',u'ㅇ',u'ㅈ',u'ㅊ',u'ㅋ',u'ㅌ',u'ㅍ',u'ㅎ']
TOTAL = CHOSUNGS + JOONGSUNGS + JONGSUNGS

def jamo_split(word, end_char="_"):
    
    result = []
    
    for char in word:
        
        character_code = ord(char)
        
        if 0xD7A3 < character_code or character_code < 0xAC00:
            result.append(char)
            continue

        chosung_index = int((((character_code - 0xAC00) / 28) / 21) % 19)
        joongsung_index = int(((character_code - 0xAC00) / 28) % 21)
        jongsung_index = int((character_code - 0xAC00) % 28)
        
        chosung = CHOSUNGS[chosung_index]
        joongsung = JOONGSUNGS[joongsung_index]
        jongsung = JONGSUNGS[jongsung_index]
        
        # 종성 범위 밖에 있는 것들은 end_char로 메꿔준다.
        if jongsung_index == 0:
            jongsung = end_char
        
        result.append(chosung)
        result.append(joongsung)
        result.append(jongsung)

    return "".join(result)


# # 자모 합치는 코드

# In[56]:


def jamo_combine(word):
    result = ""

    # 완전한 글자를 만들기 위한 초성/중성/종성 의 카운트
    char3_count = 0
    
    for index, char in enumerate(word):
        # char가 한글이 아닌경우는 그냥 추가한다.
        if char not in TOTAL:
            result += char
            print(char)
            continue
            
        # 한글이면 초성 중성 종성에 있는 걸 해당하고 어디에 해당하는지 찾는다
        else:
            if char3_count <= 1:
                try:
                    # 초성의 인덱스를 저장
                    cho = CHOSUNGS.index(char) * 21 * 28
                    # 마지막에 초성이 나올경우
                    if index == len(word) - 1:
                        result += char
                    # 초성이 처음나올경우
                    elif char3_count == 0:
                        temp_chosung = char
                        char3_count = 1
                    else:
                        # 기존에 있던 초성을 더해준다.
                        result += temp_chosung
                        temp_chosung = char
                        char3_count = 1
                        continue

                # 중성일경우
                except:
                    try:
                        # 중성의 인덱스를 저장
                        joong = JOONGSUNGS.index(char) * 28
                        
                        # 중성이 마지막에 나올경우 
                        if index == len(word) - 1:
                            if char3_count == 1:
                                result += temp_chosung
                                result += char
                            else:
                                result += char
                        # 중성이 처음 나올경우
                        elif char3_count == 1:
                            char3_count = 2
                        # 기존에 있던 초성과 중성을 더해서 결과에 더해준다
                        # 그리고 나머지 중성도 더해준다.
                        else:
                            result += chr(cho + joong + 0xAC00)
                            result += char
                            # 다시 초성으로 가기 위함
                            char3_count = 1
                            continue
                    except:
                        pass
            else:
                jong = JONGSUNGS.index(char)
                result += chr(cho + joong + jong + 0xAC00) 
                char3_count = 0

    return result