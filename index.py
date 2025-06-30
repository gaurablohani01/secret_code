import random

alpha = ['a','b','c','d','e','f','g','h','i','j','k']

ch=int(input('1. Encoder\n2. Decoder\n'))
match(ch):
    case 1:

        word = input("Emter the word: ")
        word_split=word.split()
    
        list_en = []
        for i in word_split:
            if len(i)>=3:
                copy=i[1:]+i[0]
                for i in range(0,3):
                    random_ch= random.choice(alpha)
                    copy= copy+random_ch
                    random_ch= random.choice(alpha)
                    copy= random_ch+copy
                list_en.append(copy)
                    
            else:
                copy1 = i[::-1]
                list_en.append(copy1)

            
        print(' '.join(list_en))

    case 2:

        decoder= input("Enter the decoder word: ")
        decoder_split = decoder.split()
        list_dec=[]
        for i in decoder_split:
            if(len(i)>=3):
                copy_dec= i[3:-3]
                copy_dec = copy_dec[-1]+copy_dec[0:-1]
                list_dec.append(copy_dec)


            else:
                copy=i[::-1]
                list_dec.append(copy)


        print(' '.join(list_dec))