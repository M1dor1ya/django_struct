from rest_framework.views import APIView
from utils.return_deco import return_deco
import json
# Create your views here.


class DevInfo(APIView):

    @return_deco
    def get(self, request):
        """
        URL传参  http://127.0.0.1:8000/rest/network/dev/?name=ens3
        """
        print(request.user)
        if request.GET['name'] == 'all':
            return 0, 'this is all dev info'
        else:
            return 0, 'this is %s info' % request.GET['name']

    @return_deco
    def post(self, request):
        data = json.loads(request.body.decode())
        print(data)
        return 0, ''