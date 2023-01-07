# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 19:30:19 2020

@author: Lily
"""



def dInit():
    archive = {}
    with open (r"Definitions/archive.txt", "r") as data:
        fileContent  = data.read().split("\n")
        for line in fileContent:
            file, keyword = line.split(": ")
            if keyword in archive.keys():
                archive[keyword.upper()].append(file)
            else:
                archive[keyword.upper()] = [file]
    return archive

archive = dInit()

def searchFunc(userInput):
    userInput = userInput.upper()
    if userInput in archive.keys():
        output = archive[userInput]
        return output
    else:
        return []


    # with open (r"Definitions/archive.txt", "r") as data:
    #     fileContent  = data.read().split("\n")
    #     for line in fileContent:
    #         # file, _, keyword = re.compile('(: )').split(line)
    #         file, keyword = line.split(": ")
    #         if userInput.upper() in keyword.upper():
    #             if file in output:
    #                 continue
    #             url = file.replace(' ', '%20')
    #             output = output + '<br>' + "<a href=/file.view?document={}>{}</a>".format(url, file) + '\n'
    #             anymatch = True
    #         else:
    #             continue

    # if not anymatch:
    #     return '<h2> Term was not found in any scanned file </h2></p>'
