import requests
import pandas as pd
import math
import streamlit as st

def apt_info(hscpNo, maemul_cnt):
    building_type = 'A1:B1:B2'
    if maemul_cnt == 0:    # 매물 총잔량이 없으면 함수 종료
        return
    page_cnt = math.ceil(maemul_cnt/20)       # 소수점 올림
    hdr = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    df_maemul_list = pd.DataFrame()
    error = False
    res = ''
    for page in range(1, page_cnt+1):
        URL = f'https://m.land.naver.com/complex/getComplexArticleList?hscpNo={hscpNo}&tradTpCd={building_type}&order=point_&showR0=N&page={page}'
        APIKEY = '897ae59b782a2342e2e34fa6dd6aad91'  # ip 우회   https://dashboard.scraperapi.com/
        ScraperAPI = f"http://api.scraperapi.com/?api_key={APIKEY}&url={URL}"  # ip 우회  https://dashboard.scraperapi.com/
        res = requests.get(ScraperAPI, headers=hdr)
        try:
            maemul_list = res.json()['result']['list']
            df_maemul_list = df_maemul_list._append(maemul_list)
        except:
            error = True
    if error:
        st.markdown(res, unsafe_allow_html=True)

    def convert_list_to_string(data):  # 리스트, 딕셔너리 형태를 문자열로 변환해 주는 함수
        return ', '.join(map(str, data))

    df_maemul_list['tagList'] = df_maemul_list['tagList'].apply(convert_list_to_string)  # 리스트,딕셔너리 해체 함수 적용
    df_maemul_list['cpLinkVO'] = df_maemul_list['cpLinkVO'].apply(convert_list_to_string)  # 리스트,딕셔너리 해체 함수 적용

    df_maemul_list = df_maemul_list.replace('', 'missing')  # 결측치 데이터 채우기
    # 영어로 된 컬럼명 한글로 수정
    df_maemul_list = df_maemul_list.rename(columns={'repImgUrl': '이미지주소', 'atclNo': '매물번호', 'vrfcTpCd': '등록인cd',
          'atclNm': '이름', 'bildNm': '동', 'tradTpCd': '내부구조cd', 'tradTpNm': '거래종류', 'rletTpNm': '부동산종류',
          'spc1': '공급', 'spc2': '전용', 'flrInfo': '층', 'atclFetrDesc': '홍보글', 'cfmYmd': '날짜',
          'prcInfo': '금액', 'sameAddrCnt': '광고등록건수', 'sameAddrHash': '매물주소 hash', 'sameAddrMaxPrc': '최고 호가',
          'sameAddrMinPrc': '최저 호가', 'tagList': '매물 특징', 'direction': '방향', 'directTradYn': '직거래',
          'rltrNm': '부동산', 'cpCnt': '매물등록 건수', 'tradCmplYn': '거래완료', 'rletTpCd': '부동산종류cd'                                             })

    df_maemul_list = df_maemul_list[
        ['이름', '동',  '거래종류', '부동산종류', '공급', '전용',  '층', '홍보글', '날짜',  '금액',
        '최고 호가', '최저 호가', '매물 특징', '방향', '직거래', '부동산', '매물등록 건수', ]
         ]

    return df_maemul_list

