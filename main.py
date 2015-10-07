import csv
import json
import requests

def request_analysis(text_to_analyze):
    payload = "text=" + str(text_to_analyze)
    response = requests.post("http://text-processing.com/api/sentiment/",
               data=payload)
    return response

def analyze_text(file):
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            print('Analyzing: ' + str(row))
            output = request_analysis(str(row))
            output = output.json()
            if 'pos' in output['label']:
                print('Analyzed as positive with a probability of ' +
                      str(output['probability']['pos']))
            elif 'neg' in output['label']:
                print('Analyzed as negative with a probability of ' +
                      str(output['probability']['neg']))
            else:
                print('Analyzed as neutral with a probability of ' +
                      str(output['probability']['neutral']))
            print()
        csvfile.close

def main():
    input_file = input("Enter a .csv file path for input: ")
    analyze_text(input_file)

main()
