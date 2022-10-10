#czy str zawiera conajmniej 1 duza litere

txt='7abraCADABRA'

#txt.issupper() # zawiera tylko duze

#1 tekst jest tylko skaldaajacy sie z liter
#2 nie zawiera tylko malych

#txt.issupper()
#txt.islower()

print(txt.isalpha() and not txt.islower())