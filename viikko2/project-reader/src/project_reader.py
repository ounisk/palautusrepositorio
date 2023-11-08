from urllib import request
from project import Project
import toml   

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)
        dict_content= toml.loads(content, _dict=dict)
        #print (dict_content['tool']['poetry']['name'])
        #print (dict_content['tool']['poetry']['description'])
        dependencies_list = []
        #print (dict_content['tool']['poetry']['dependencies'].keys())
        for item in (dict_content['tool']['poetry']['dependencies'].keys()):
            dependencies_list.append(item)
        #print(dependencies_list)
        dev_dependencies_list = []
        for item in (dict_content['tool']['poetry']['group']['dev']['dependencies'].keys()):
            dev_dependencies_list.append(item)   

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        name = dict_content['tool']['poetry']['name']
        description = dict_content['tool']['poetry']['description']
        license = dict_content['tool']['poetry']['license']
        authors = dict_content['tool']['poetry']['authors']
        #dependencies = (", ".join(dependencies_list)) # ei tarvitse
        #print(dependencies)
        #dev_dependencies = (", ".join(dev_dependencies_list)) #ei tarvitse
        #print(dev_dependencies)

        return Project(name, description, license, authors, dependencies_list, dev_dependencies_list)
 