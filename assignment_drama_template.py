# ==========================
# assignment_drama_template.py (학생용 템플릿)
# 조건: 함수/조건문/반복문 금지. 변수 선언과 input(), print()만 사용.
# ==========================깃 테스트용 주석추가

drama1 = {
    "제목": "사랑의 불시착",
    "장르": "로맨스/코미디",
    "주제": "남북한 사랑 이야기와 가족의 의미",
    "방영기간": "2019-12-14 ~ 2020-02-16",
    "배우": ["현빈", "손예진", "서지혜", "김정현"],
    "명대사": "\"나는 당신이 행복하길 바라요. 그게 내가 바라는 전부예요.\""
}

drama2 = {
    "제목": "킹덤",
    "장르": "스릴러/사극/호러",
    "주제": "조선시대 좀비 창궐과 권력 투쟁",
    "방영기간": "2019-01-25 ~ 2020-03-13",
    "배우": ["주지훈", "배두나", "류승룡", "김상호"],
    "명대사": "\"임금이 되려거든, 백성을 구해야 한다.\""
}
new_title = input("새 드라마 제목: ")  

new_genre = input("새 드라마 장르: ")                            
new_theme = input("새 드라마 주제: ")                            
new_period = input("새 드라마 방영기간: ")                        
new_actors_input = input("새 드라마 배우: ")                     
new_quote_raw = input("새 드라마 대사: ")                      

new_actors = new_actors_input.split(",")
new_quote = f"\"{new_quote_raw}\""

drama3 = {
    "제목": new_title,
    "장르": new_genre,
    "주제": new_theme,
    "방영기간": new_period,
    "배우": new_actors,
    "명대사": new_quote
}


upd_title = input("수정(덮어쓰기)할 제목(대상: drama2): ")  
upd_genre = input("수정(덮어쓰기)할 장르(대상: drama2): ")                      
upd_theme = input("수정(덮어쓰기)할 주제(대상: drama2): ")                        
upd_period = input("수정(덮어쓰기)할 방영기간(대상: drama2): ")                   
upd_actors_input = input("수정(덮어쓰기)할 배우(대상: drama2): ")                  
upd_quote_raw = input("수정(덮어쓰기)할 대사(대상: drama2): ")                     

upd_actors = upd_actors_input.split(",")
upd_quote = f"\"{upd_quote_raw}\""
drama2["제목"] = upd_title
drama2["장르"] = upd_genre
drama2["주제"] = upd_theme
drama2["방영기간"] = upd_period
drama2["배우"] = upd_actors
drama2["명대사"] = upd_quote

print("\n[드라마 1]")
print(f"제목: {drama1['제목']}")
print(f"장르: {drama1['장르']}")
print(f"주제: {drama1['주제']}")
print(f"방영기간: {drama1['방영기간']}")
print(f"배우: {drama1['배우']}")
print(f"명대사: {drama1['명대사']}")

print("\n[드라마 2]  # 수정 후")
print(f"제목: {drama2['제목']}")
print(f"장르: {drama2['장르']}")
print(f"주제: {drama2['주제']}")
print(f"방영기간: {drama2['방영기간']}")
print(f"배우: {drama2['배우']}")
print(f"명대사: {drama2['명대사']}")

print("\n[드라마 3]  # 새로 추가")
print(f"제목: {drama3['제목']}")
print(f"장르: {drama3['장르']}")
print(f"주제: {drama3['주제']}")
print(f"방영기간: {drama3['방영기간']}")
print(f"배우: {drama3['배우']}")
print(f"명대사: {drama3['명대사']}")
