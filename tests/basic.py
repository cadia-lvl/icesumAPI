# -*- coding: utf-8 -*-
import requests


#source: https://www.ruv.is/frett/2020/10/30/domstolar-nyta-ekki-fjarfundarbunad-sem-skyldi
article = """
Ákærendafélag Íslands segir að dómstólar séu of illa búnir til að geta nýtt sér
bráðabirgðaheimild til málsmeðferða í gegnum fjarfundarbúnað. Umsýsla dómstóla
segir að tæknilausnir séu til staðar en að unnið sé að úrbótum.

Þetta kemur fram á forsíðu Fréttablaðsins í morgun. Í vor var sett í lög
bráðabirgðaákvæði þess efnis að heimilt sé að skýrslutaka og önnur málsmeðferð
fari fram í gegnum fjarfundarbúnað. Var það gert í sóttvarnarskyni vegna
faraldursins. Dómsmálaráðherra lagði nýverið fram frumvarp um framlengingu
þessarar heimildar sem nær út árið 2021 en hún féll úr gildi 1. október. 

Í umsögn Ákærendafélags Íslands kemur fram að dómstólar hafi ekki nýtt sér
þessa heimild eins og kostur er bestur í ljósi þess tækjabúnaður sé ekki
fullnægjandi. Þá sé allur gangur á því hvaða kröfur séu gerðar til þeirra sem
gefa skýrslu varðandi staðsetningu og einrúm skýrslugjafans. 

„Í sumum tilvikum hefur skýrslugjafi hreinlega staðið úti á götu í heimabæ
sínum en í öðrum tilvikum hafa dómarar verið strangir á því að skýrslugjafi sé á
tilteknum stað og í einrúmi við skýrslugjöfina. Það væri e.t.v. rétt að
lagaákvæðið eða greinargerðin gæfu einhverjar leiðbeiningar í þessum efnum.“
segir í umsögn félagsins.

Einnig kemur fram í umsögninni að heimildin sé af hinu góða þar sem málsmeðferð
hefði tafist verulega ef hennar nyti ekki við. 

„Sumir dómstólar hafa þó lagt sig fram við að bæta tækjabúnað sinn og er það
reynsla ákærenda að í þeim tilvikum þar sem þetta hefur verið framkvæmt hafi það
gefist vel og ef þessarar heimildar hefði ekki notið við væru þessi mál enn til
meðferðar fyrir dómstólum.

Ólöf Finnsdóttir, framkvæmdastjóri dómstólasýslunnar segir við Fréttablaðið að
tækjabúnaður sé til staðar hjá dómstólum til að nýta heimildina. Vandinn sé sá
að tryggja þurfi að allt sem fram fer sé tekið upp í hljóði og mynd. Aðeins
Héraðsdómur Reykjavíkur og Landsréttur séu komnir með slíkt heilstætt kerfi.
Unnið sé að því að koma því við hjá öðrum dómstólum landsins.Það verði gert á
næstu vikum og mánuðum. Þeir hafi þurft að reiða sig á bráðabirgðalausn.
Upptökukerfi í dómsal taki upp það sem fer fram á fjarfundinum.
"""

r = requests.post("http://0.0.0.0:8080/summarizer/impl", params={'article':article})
exp = 'Ákærendafélag Íslands segir að dómstólar séu of illa búnir til að geta nýtt sér bráðabirgðaheimild til málsmeðferða í gegnum fjarfundarbúnað. Umsýsla dómstóla segir að tæknilausnir séu til staðar en að unnið sé að úrbótum. Í vor var sett í lög bráðabirgðaákvæði þess efnis að heimilt sé að skýrslutaka og önnur málsmeðferð fari fram í gegnum fjarfundarbúnað. Í umsögn Ákærendafélags Íslands kemur fram að dómstólar hafi ekki nýtt sér þessa heimild eins og kostur er bestur í ljósi þess tækjabúnaður sé ekki fullnægjandi.'
print(r.text)
assert '{"response":{"type":"texts","content":'+exp+'}}'
