# How to Use
# 1. Import Lib
# 2. Open dir || you can add .convert("RGB") example
# 3. Save to dir


from PIL import Image
im = Image.open(
    r"C:\Users\ArX\Desktop\MSIB-BisaAi-Ai_Hacker_Image-Processing\Convert_Image_Format\Bahan\orange.webp")
im.save(r'C:\Users\ArX\Desktop\MSIB-BisaAi-Ai_Hacker_Image-Processing\Convert_Image_Format\Hasil\orange.png', format='png')
im.show()
