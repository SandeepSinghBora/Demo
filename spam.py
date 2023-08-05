# coding: utf-8
spam=0.30
Nospam=0.70
cong_spam=0.75
cong_Nospam=0.35
spam_congrats=(cong_spam * spam)/(cong_spam * spam +(cong_Nospam * Nospam )) 
print("P(Spam|congrat) = ",spam_congrats)
