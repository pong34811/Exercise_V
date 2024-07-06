from django.shortcuts import render

# Create your views here.

# def Linkfacebook (request):
#     return render(request, 'linkfacebook.html')

def Linkfacebook (request):
    # ดึงข้อมูลภาพและลิงก์ Facebook จากฐานข้อมูลหรือจากตัวแปร
    image_url = "https://scontent-bkk1-1.xx.fbcdn.net/v/t39.30808-6/357149828_826310685519327_4035963962083128051_n.jpg?_nc_cat=108&ccb=1-7&_nc_sid=6ee11a&_nc_eui2=AeE-P6dJemS5zNQM4coC-vRnZf9Kd_xIPA5l_0p3_Eg8DrQ0iH9v7bvmAidk5E-S6ePrUmSoMTwNaE-OW8QLxfSF&_nc_ohc=N39RBLz5ddMQ7kNvgEAzRgh&_nc_ht=scontent-bkk1-1.xx&oh=00_AYCzz80w7Uvk_vW9XiqXN1su4sdoM4xkBQFyAOtNEEWVSw&oe=668EA0D7"
    facebook_link = "https://www.facebook.com/profile.php?id=100044212092752"

    return render(request, 'Linkfacebook.html', {'image_url': image_url, 'facebook_link': facebook_link})