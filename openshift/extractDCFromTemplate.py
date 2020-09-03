import requests
import sys
import json

class ExtractDeployConfigs:
    def __init__(self):
        pass

    def process(self):
        data = sys.stdin.read()
        templateData = json.loads(data)
        newData = templateData.copy()
        newData['items'] = []
        cnt = 0
        for itemIndex in range(0, len(templateData["items"])):
            if templateData["items"][itemIndex]['kind'] == 'DeploymentConfig':
                newData['items'].append(templateData["items"][itemIndex])
        json.dump(newData, sys.stdout)

if __name__ == '__main__':
    dcExtractor = ExtractDeployConfigs()
    dcExtractor.process()

            

            
