from screening import Skype

if __name__ =='__main__':
    email = 'qwer@qwe.ru'
    skype_masker = Skype(mask_char="x")
    print(skype_masker.mask("skype:ale..___.x.max"))
    print(skype_masker.mask('<a href="skype:alasdadas222331dsada.sdasdex.masdasdasdax?call">skype</a>'))