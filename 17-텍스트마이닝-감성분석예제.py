import sentiment_module

test_sentence = "응애 나 애기 거련"
score = sentiment_module.sentiment_predict(test_sentence)
if score >= 0.5:
    print(f"{score * 100: .2f}% 확률로 긍정입니다.")
else:
    print(f"{100 - score * 100: .2f}% 확률로 부정입니다.")
print(score)