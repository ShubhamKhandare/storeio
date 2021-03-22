from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings

from seller.models import Seller


class SellerAccessTokenSerializer(TokenObtainPairSerializer):

    # Password was mandatory field so
    # https://stackoverflow.com/a/62851458/7840402
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].required = False

    def validate(self, attrs):
        # Initialize response json
        data = {}
        otp = None
        try:
            request = self.context["request"]
            otp = request.data.get('otp')
        except KeyError:
            pass

        mobile_number = attrs['mobile_number']

        # TODO check if OTP is correct
        # Currently OTP is just substring of mobile number
        if str(mobile_number).find(str(otp)) == -1:
            return {'status': 'failed', 'message': 'Please input correct OTP.'}
        else:
            seller_obj = None
            try:
                seller_obj = Seller.objects.get(mobile_number=mobile_number)
            except Seller.DoesNotExist:
                # Creating seller if does not exists
                # This logic could be added to sending OTP API but
                # Lets not create user unless he actually tries to login
                seller_obj = Seller.objects.create_user(mobile_number=mobile_number)
                # TODO handle seller creation failure cases

            self.user = seller_obj

            refresh = self.get_token(self.user)

            data['refresh'] = str(refresh)
            data['access'] = str(refresh.access_token)

            if api_settings.UPDATE_LAST_LOGIN:
                update_last_login(None, self.user)

            return data
