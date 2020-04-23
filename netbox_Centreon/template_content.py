from extras.plugins import PluginTemplateExtension
from .models import CentreonObjectStatus
import requests


class SiteCentreonObjectStatus(PluginTemplateExtension):
    model = 'ipam.ipaddress'

    def getAllHosts(self):
        payload = {'username': 'gabriel','password': '5UtGqvY5'}
        response = requests.request("POST", "http://"+config.centreon_url+"/centreon/api/index.php?action=authenticate", data=payload)
        if response.status_code == 200:
            url = "http://"+config.centreon_url+"/centreon/api/index.php?action=action&object=centreon_clapi"

            payload = "{\r\n  \"action\": \"show\",\r\n  \"object\": \"host\"\r\n}"
            headers = {
                'Content-Type': 'application/json',
                'centreon-auth-token': response.json()["authToken"],
                'Content-Type': 'text/plain'
            }

            response = requests.request("POST", url, headers=headers, data=payload)

            return response.json()

        else:
            return ""

    def getHostsByName(self,name):
        payload = {'username': 'gabriel','password': '5UtGqvY5'}
        response = requests.request("POST", "http://"+config.centreon_url+"/centreon/api/index.php?action=authenticate", data=payload)
        if response.status_code == 200:
            url = "http://"+config.centreon_url+"/centreon/api/index.php?action=action&object=centreon_clapi"

            payload = "{\r\n  \"action\": \"show\",\r\n  \"object\": \"host\",\r\n  \"values\": \""+name+"\"\r\n}"
            headers = {
                'Content-Type': 'application/json',
                'centreon-auth-token': response.json()["authToken"],
                'Content-Type': 'text/plain'
            }

            response = requests.request("POST", url, headers=headers, data=payload)

            return response.json()

        else:
            return ""

    def updateStatus(self,object):
        return

    def buttons(self):
        print("test")
        self.getAllHosts()

    def right_page(self):
        c = CentreonObjectStatus()
        obj = str(self.context['object']).split("/")[0] if '/' in str(self.context['object']) else str(self.context['object'])
        for i in CentreonObjectStatus.objects.all():
            if obj == i.name:
                c=i
        return self.render('netbox_Centreon/status.html', extra_context={
            'c': c,
        })

template_extensions = [SiteCentreonObjectStatus]