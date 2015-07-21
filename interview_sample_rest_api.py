import requests, json
import unittest

#s = requests.Session()

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.s = requests.Session()
        headers = {'Content-Type': 'application/json'}
        login = {'username': '-----', 'password': '-----'}
        json_login = json.dumps(login)
        r = self.s.post("http://localhost:8080/AppCenter/services/rest/login",
            data=json_login, headers=headers)
    def test_import_cloudAccount(self):
         files = {'ca': open('/Users/nata/Downloads/CloudAccount-nata5cloud.xml')}
         r = self.s.post("http://localhost:8080/AppCenter/services/rest/cloudaccount/import",
             files = files)
         self.assertEqual(r.status_code, 200)
    def test_set_limits(self):
         r = self.s.post('http://localhost:8080/AppCenter/services/rest/cloudaccount/capacity?cloudAccount=OpenStack%20Cloud%20Account&cloudLocation=RegionOne&resource=Virtual%20Server&capacity=7')
         self.assertEqual(r.status_code, 200)
    def test_discover_all(self):
        r = self.s.get('http://localhost:8080/AppCenter/services/rest/cloudaccount/nata%20export%20cloud/discoverAll')
        self.assertEqual(r.status_code, 200)
    def test_export_profiles(self):
        data = {"Name":"OS Profile", "Criteria": {"ProfileID":"UBUNTU"}}
        headers = {'Content-Type': 'application/json'}
        r = self.s.post('http://localhost:8080/AppCenter/services/rest/standards/fetch',
        data=json.dumps(data), headers=headers)
        with open('ubuntu.json', 'w') as outfile:
            json.dump(r.json(), outfile)
        outfile.close()
        self.assertEqual(r.status_code, 200)
    def test_import_profiles(self):
        headers = {'Content-Type': 'application/json'}
        with open('ubuntu.json') as data_file:
            data = json.load(data_file)
        #print data
        r = self.s.post("http://localhost:8080/AppCenter/services/rest/standards?name=OS+Profile", json=data, headers=headers)
        self.assertEqual(r.status_code, 200)
    def test_create_organization(self):
        r = self.s.post('http://localhost:8080/AppCenter/services/rest/org/create?name=ProdNata&displayName=Production%20Group&description=Group%20Housing%20Production%20Stakeholders')
        self.assertEqual(r.status_code, 200)
    def test_subscribe_blueprint(self):
        headers = {'Content-Type': 'application/json'}
        r = self.s.post('http://localhost:8080/AppCenter/services/rest/org/subscribe?sourceOrg=Cloud%20Service%20Provider&targetOrg=Dev&entityName=Prov2&entityType=Blueprints',
        headers=headers)
        self.assertEqual(r.status_code, 200)
    def test_Applications(self):
        headers = {'Content-Type': 'application/json'}
        r = self.s.post('http://localhost:8080/AppCenter/services/rest/org/subscribe?sourceOrg=Cloud%20Service%20Provider&targetOrg=Dev&entityName=Prov3&entityType=Applications',
        headers = headers)
        self.assertEqual(r.status_code, 200)
    def test_resource_model(self):
        headers = {'Content-Type': 'application/json'}
        r = self.s.post("http://localhost:8080/AppCenter/services/rest/org/subscribe?sourceOrg=Cloud%20Service%20Provider&targetOrg=Dev&entityName=Virtual%20Server&entityType=Resource%20Model&resourceId=77073",
        headers = headers)
        self.assertEqual(r.status_code, 200)
    def test_subscribe_CA_capacity(self):
        headers = {'Content-Type': 'application/json'}
        data = {"cloudAccountName": "OpenStack Cloud Account","cloudLocationName":"RegionOne", "capacity": "3","resourceName":"Virtual Server"}
        r = self.s.post('http://localhost:8080/AppCenter/services/rest/org/subscribe?sourceOrg=Cloud%20Service%20Provider&targetOrg=Dev&entityName=OpenStack%20Cloud%20Account&entityType=CloudAccounts',
        data=json.dumps(data), headers = headers)
        self.assertEqual(r.status_code, 200)
    def test_Unsubscribe_blueprint(self):
        headers = {'Content-Type': 'application/json'}
        r = self.s.post('http://localhost:8080/AppCenter/services/rest/org/unsubscribe?sourceOrg=Cloud%20Service%20Provider&targetOrg=Dev&entityName=Prov2&entityType=Blueprints',
        headers = headers)
        self.assertEqual(r.status_code, 200)
    def test_permissions_on_objects(self):
        headers = {'Content-Type': 'application/json'}
        data = {"accessPermission":"true","managePermission":"false"}
        r = self.s.post('http://localhost:8080/AppCenter/services/rest/permission/assign?entity=Blueprints&instanceName=RMTest&isGroup=true&accessorName=PermGroup',
        data=json.dumps(data), headers = headers)
        self.assertEqual(r.status_code, 200)
    def test_Permission_on_Resource_Instances(self):
        headers = {'Content-Type': 'application/json'}
        data = {"accessPermission":"true","managePermission":"false"}
        r = self.s.post('http://localhost:8080/AppCenter/services/rest/permission/assign?entity=Resource+Model&instanceName=Virtual+Server&resourceLookUp=RegionOne%2F0ed7c6a4-ad34-4e40-9abb-6af70e3f6e59&isGroup=true&accessorName=PermGroup',
        data=json.dumps(data), headers = headers)
        self.assertEqual(r.status_code, 200)
    def test_Setup_Quota(self):
        headers = {'Content-Type': 'application/json'}
        data = {"maxLimit": 5,"perUserLimit":3}
        r = self.s.post('http://localhost:8080/AppCenter/services/rest/quota/assign?cloudAccount=OpenStack%20Cloud%20Account&cloudLocation=RegionOne&group=Global%20Admin%20Group&quota=VM_Count',
        data=json.dumps(data), headers = headers)
        self.assertEqual(r.status_code, 200)
    def test_import_policy(self):
        files = {'policy': open('/Users/nata/Downloads/Policy-DefaultApprovalPolicy.xml')}
        r = self.s.post('http://localhost:8080/AppCenter/services/rest/policy/import?override=false',
            files = files)
        self.assertEqual(r.status_code, 200)
    def test_publish_policy(self):
        r = self.s.post('http://localhost:8080/AppCenter/services/rest/policy/Default%20Approval%20Policy%20Nata/publish')
        self.assertEqual(r.status_code, 200)




if __name__ == '__main__':
    unittest.main()
