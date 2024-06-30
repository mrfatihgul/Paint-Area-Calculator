import math

def paint_calc(height, width, cover):
  sonuc = (height*width)/cover
  sonucyuv = math.ceil(sonuc)
  print(f"You'll need {sonucyuv} cans of paint.")

test_h = int(input())
test_w = int(input())
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
