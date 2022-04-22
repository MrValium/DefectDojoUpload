import argparse
from datetime import datetime
import json
import os
import requests

def upload_results(host, user, api_key, scanner, result_file, engagement_id, verify=False): # set verify to False if ssl cert is self-signed
    API_URL = "http://"+host+"/api/v2"
    IMPORT_SCAN_URL = API_URL+ "/import-scan/"
    AUTH_TOKEN = "Token " + api_key

    headers = dict()
    json = dict()
    files = dict()

    # Prepare headers
    # headers = {'Authorization': 'ApiKey dojo:3e24a3ee5af0305af20a5e6224052de3ed2f6859'}
    headers['Authorization'] = AUTH_TOKEN
    print(headers)

    # Prepare JSON data to send to API
    # json= {
    #   "minimum_severity": "Low",
    #   "scan_date": datetime.now().strftime("%Y-%m-%d"),
    #   "verified": False,
    #   "tags": "",
    #   "active": False,
    #   "engagement": "/api/v1/engagements/2/",
    #   "lead":"/api/v1/users/1/",
    #   "scan_type": "Bandit Scan"
    # }
    #json['minimum_severity'] = "Low"
    json['scan_date'] = datetime.now().strftime("%Y-%m-%d")
    #json['verified'] = False
    #json['tags'] = ""
    #json['active'] = False
    json['test_title']='ENGAGEMENT1vv'
    json['engagement_name'] = "ENGAGEMENT1"#"/api/v2/engagements/"+ engagement_id + "/"
    #json['lead'] =""
    json['product_name']='Prodotto1'
    json['scan_type'] = scanner
    print(json)

    # Prepare file data to send to API
    files['file'] = open(result_file)

    # Make a request to API
    response = requests.post(IMPORT_SCAN_URL, headers=headers, files=files, data=json, verify=verify)
    # print r.request.body
    # print r.request.headers
    # print r.status_code
    # print r.text
    print (response)
    print ("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    return response.status_code


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='CI/CD integration for DefectDojo')
    parser.add_argument('--host', help="DefectDojo Hostname", required=True)
    parser.add_argument('--api_key', help="API Key", required=True)
    parser.add_argument('--username', help="Username of Defect dojo user", required=True)
    parser.add_argument('--engagement_id', help="Engagement ID (optional)", required=True)
    parser.add_argument('--result_file', help="Scanner file", required=True)
    parser.add_argument('--scanner', help="Type of scanner", required=True)
    parser.add_argument('--product_id', help="DefectDojo Product ID", required=False)
    parser.add_argument('--build_id', help="Reference to external build id", required=False)

    # Parse out arguments
    args = vars(parser.parse_args())
    host = args["host"]
    api_key = args["api_key"]
    user = args["username"]
    product_id = args["product_id"]
    result_file = args["result_file"]
    scanner = args["scanner"]
    engagement_id = args["engagement_id"]
    build_id = args["build_id"]

    # upload_results(self, host, user, api_key, scanner, result_file, engagement_id, verify=False): # set verify to False if ssl cert is self-signed
    result = upload_results(host, user, api_key, scanner, result_file, engagement_id)

    if result == 201 :
         print("Successfully uploaded the results to Defect Dojo")
    else:
         print("Something went wrong, please debug " + str(result))
         
         
         
         
         
         
         
         
         
         
         
         
def upload_scan(self, engagement_id, scan_type, file, active, verified, close_old_findings, skip_duplicates, scan_date, tags=None, build=None, version=None, branch_tag=None, commit_hash=None, minimum_severity="Info", auto_group_by=None):
        """Uploads and processes a scan file.
        :param application_id: Application identifier.
        :param file_path: Path to the scan file to be uploaded.
        """
        if build is None:
            build = ''

        with open(file, 'rb') as f:
             filedata = f.read()

        self.logger.debug("filedata:")
        self.logger.debug(filedata)

        data = {
            'file': filedata,
            'engagement': ('', engagement_id),
            'scan_type': ('', scan_type),
            'active': ('', active),
            'verified': ('', verified),
            'close_old_findings': ('', close_old_findings),
            'skip_duplicates': ('', skip_duplicates),
            'scan_date': ('', scan_date),
            'tags': ('', tags),
            'build_id': ('', build),
            'version': ('', version),
            'branch_tag': ('', branch_tag),
            'commit_hash': ('', commit_hash),
            'minimum_severity': ('', minimum_severity),
            # 'push_to_jira': ('', True)
        }

        if auto_group_by:
            data['auto_group_by'] = (auto_group_by, '')

        """
        TODO: implement these parameters:
          lead
          test_type
          scan_date
        """

        return self._request(
            'POST', 'import-scan/',
            files=data
        )

