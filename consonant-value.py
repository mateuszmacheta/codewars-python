# 6 kyu Consonant value
# https://www.codewars.com/kata/59c633e7dcc4053512000073/train/python

import re


def solve(s):
    print(s)
    words = re.split(r'[aeiou]',s)
    return max([sum(ord(c)-96 for c in list(word)) for word in words])


test96 = 'raiuiouaymewywiaikioetiqheuimfbideieoyroeuifekiginaowaewwiezunaykhyaxkcdrsuaegovynoozyeeaozcaxscyqacobbqridaehcbuaneoeiaoupumaeafvhexadgeipcaiiwuilesqirounuuxiqejmoladcpeuofexqzagespkeayueimsoayefuaiuudwuiobqxzkoffteoiuaaheguexoeeanrxezihzkjaobjpanftevdooiooeaedhjagiykhaocauganluoaeaeabuasamxioseeibpjwkrkexoeemciooiuucoskejaqegkclzvueiahuucapssufizwwowidbaakumdcaasjieciauozlxuuhweoqcunajfiwrembixiejoqgkeippuoielaxezaeaglkeeuasaaeekigoiieovaveuacxiaifiaubleuieiiiouqnuiiyoiidpekuoiieimeuiieoaieooaufiyqaaeauiijogeazjnkuoeeowiqoaaeivouewakqueueouoeqnimghukobeeecfheopauropeuatqvereucexuamzahtulwooiaeoiiacoouaaopqleohouhwtuuaoneuadehooguivuidwmooijieeeaeatiaaeobqioaiacpioluiosejlavuidnzeieijayeaemyuvxoczuuajsaaoenxiooaoeeixeonivuauuodauqieclfmieeighuoavegbbaaqaaoooijyucejniahaaqnxtaaxoouaoiioixkpujealowupooxuoayabufkocadiaeuxyuoaomuolawiqxoozukceiaarnpubecieozduoqogooupooreaogolhwdneyaiuogijekscufnaoodiiukkuoajuuayioueohuuoiauzueaigyaujrwdieeioaaaacaluhaouujfpnyyuaoieiuuapfyoquqpueifkdinahieizoiaktimnoeueiauzgouhuizeuueaoueneqopraesux'

print(solve(test96))