def zunda(kudamono) :
    print("ずんだは" + kudamono + "が好きです")

new_kudamono = input('食べ物を入力してください:')

if new_kudamono == "" :
    zunda_kudamono = "緑のもの"
    zunda(zunda_kudamono)

else :
    zunda(new_kudamono)
