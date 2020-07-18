import sys
import argparse
sys.path.append("instagram")
sys.path.append("instagram/models")
from instagramScraper import instagramScraper
from instagramUser import instagramUser

parser = argparse.ArgumentParser()
parser.add_argument('--input-file')
parser.add_argument('--output-file')
args = parser.parse_args()

inputFileContent = open(args.input_file, 'r') 
lines = inputFileContent.readlines() 

outputFileContent = open(args.output_file, 'w') 
outputFileContentString = "User Name" 
outputFileContentString += "\t" + "Biography" 
outputFileContentString += "\t" + "Business Category Name"  
outputFileContentString += "\t" + "Follow Count"  
outputFileContentString += "\t" + "Follower Count"

for i in range(12):
    outputFileContentString += "\t" + "Photo-" + str(i) + " Url" 
    outputFileContentString += "\t" + "Photo-" + str(i) + " Like" 
    outputFileContentString += "\t" + "Photo-" + str(i) + " Date (UTC)"

outputFileContentString += "\n"
outputFileContent.writelines(outputFileContentString)

scraper=instagramScraper()
for line in lines:
    username=line.replace("\r", "").replace("\n", "")
    userData=scraper.fetch(username)
    outputFileContentString = str(userData["username"]) + "\t" 
    outputFileContentString += str(userData["biography"].replace("\r", "").replace("\n", "")) 
    outputFileContentString += "\t" + str(userData["business_category_name"]) 
    outputFileContentString += "\t" + str(userData["follow_count"]) 
    outputFileContentString += "\t" + str(userData["follower_count"])

    for i in range(12):
        if len(userData["photos"])<=i: break
        outputFileContentString += "\t" + str(userData["photos"][i]["url"]) 
        outputFileContentString += "\t" + str(userData["photos"][i]["numberOfLike"]) 
        outputFileContentString += "\t" + str(userData["photos"][i]["takenAt"])

    outputFileContentString += "\n"
    outputFileContent.writelines(outputFileContentString)

outputFileContent.close() 