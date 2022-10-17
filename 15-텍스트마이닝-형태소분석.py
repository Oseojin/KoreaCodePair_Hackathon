from konlpy.tag import Okt

okt = Okt()
#result = okt.pos("딤거련은 최강이다.")
result = okt.nouns("딤거련은 최강이다.")
print(result)