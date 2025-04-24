import sys
import json
import argparse

class ExtractDeployConfigs:
    def __init__(self):
        self.objectTypesToInclude = None
        self.knownKinds = ['BuildConfig', 'ImageStreamTag', 'ImageStream', 'Deployment', 'Service', 'Route', 'Role', 'RoleBinding', 'ServiceAccount', 'Secret']

    def processArgs(self):
        parser = argparse.ArgumentParser(description='Filter the output from oc process by object type.')
        parser.add_argument('ocObjectType', metavar='Openshift object type', type=self.checkKind, nargs='+',
                    help='List of openshift object types to extract')
        
        args = parser.parse_args()
        self.objectTypesToInclude = args.ocObjectType

    def checkKind(self, kind):
        if kind not in self.knownKinds:
            raise argparse.ArgumentTypeError("%s is not a known openshift object type (kind)" % kind)
        return kind

    def process(self):
        data = sys.stdin.read()
        templateData = json.loads(data)
        newData = templateData.copy()
        newData['items'] = []
        for itemIndex in range(0, len(templateData["items"])):
            if templateData["items"][itemIndex]['kind'] in self.objectTypesToInclude:
                newData['items'].append(templateData["items"][itemIndex])
        json.dump(newData, sys.stdout)

if __name__ == '__main__':
    dcExtractor = ExtractDeployConfigs()
    dcExtractor.processArgs()
    dcExtractor.process()
