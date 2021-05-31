from user_profile.models import Profile
import datetime

def profileCreate(profile_data,instance):
    name = profile_data.get('name')
    age = profile_data.get('age')
    email = profile_data.get('email')
    Profile.objects.create(name=name,age=age,email=email,user=instance)

def checkExpiredCertificate(certificates):
    for certificate in certificates:
        cert_date = certificate.date_expired
        today = datetime.date.today()
        if today > cert_date:
            certificate.status = 'dead'
            certificate.save()