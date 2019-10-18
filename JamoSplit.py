#!/usr/bin/env python
# coding: utf-8

# # 자모 스플릿 하는 코드

# In[54]:


CHOSUNGS = [u'ㄱ',u'ㄲ',u'ㄴ',u'ㄷ',u'ㄸ',u'ㄹ',u'ㅁ',u'ㅂ',u'ㅃ',u'ㅅ',u'ㅆ',u'ㅇ',u'ㅈ',u'ㅉ',u'ㅊ',u'ㅋ',u'ㅌ',u'ㅍ',u'ㅎ']
JOONGSUNGS = [u'ㅏ',u'ㅐ',u'ㅑ',u'ㅒ',u'ㅓ',u'ㅔ',u'ㅕ',u'ㅖ',u'ㅗ',u'ㅘ',u'ㅙ',u'ㅚ',u'ㅛ',u'ㅜ',u'ㅝ',u'ㅞ',u'ㅟ',u'ㅠ',u'ㅡ',u'ㅢ',u'ㅣ']
JONGSUNGS = [u'_',u'ㄱ',u'ㄲ',u'ㄳ',u'ㄴ',u'ㄵ',u'ㄶ',u'ㄷ',u'ㄹ',u'ㄺ',u'ㄻ',u'ㄼ',u'ㄽ',u'ㄾ',u'ㄿ',u'ㅀ',u'ㅁ',u'ㅂ',u'ㅄ',u'ㅅ',u'ㅆ',u'ㅇ',u'ㅈ',u'ㅊ',u'ㅋ',u'ㅌ',u'ㅍ',u'ㅎ']
TOTAL = CHOSUNGS + JOONGSUNGS + JONGSUNGS

# 자모분리
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


# 자모결합
def jamo_combine(word):

    result = ""
    index = 0
    
    while index < len(word):
    
        # 3개의 char를 보아 글자가 만들어지면 만들고 아니면 1개의 char만 추가한다.
        try:
            cho = CHOSUNGS.index(word[index]) * 21 * 28
            joong = JOONGSUNGS.index(word[index+1]) * 28
            jong = JONGSUNGS.index(word[index+2])

            result += chr(cho + joong + jong + 0xAC00) 
            index += 3

        except:
            result += word[index]
            index += 1
        
    return result