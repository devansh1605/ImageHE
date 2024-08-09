from PIL import Image
import encdec_func as edec
import keygenerate as key
publickey, privatekey = key.generate_keys()

print(publickey.__repr__())

im = Image.open("101_4.jpg")
encrypt_image = edec.image_encryption(publickey,im)
edec.show_encrypted_image(encrypt_image)
inc_bright = edec.increase_brightness(publickey,encrypt_image,60)
im = edec.image_decryption(publickey,privatekey,inc_bright)
im.show()

