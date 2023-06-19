# Google OSINT
Tabular quick Google search, very usefull in OSINT searches


## Description
This tool is designed to provide a simple interface for conducting open-source intelligence (OSINT) investigations. The tool leverages Google's Custom Search JSON API to search for multiple terms and return relevant results.

## Installation
Clone this repository to your local machine:
```
git clone https://github.com/yourusername/OSINT-Search-Engine-Scraper.git](https://github.com/CalebFIN/GoogleOSINT.git
```
Then navigate to the directory:
```
cd GoogleOSINT
```
Install the required packages:
```
pip install -r requirements.txt
```

## Usage
Before using this tool, add your Google Custom Search JSON API key and CSE ID to the `api.py` file:
```python
api_key="YOUR API KEY HERE"
cse_id="YOUR CSE ID HERE"
```
Run the main script:
```
python SEARCHMAIN.py
```
Enter search terms when prompted, separating multiple terms with commas:
```
Enter search terms, separated by commas-->term1, term2, term3
```
The script will return a formatted table of search results, displaying the title and link for each result.

## Contributing
If you would like to contribute to this project, please feel free to submit a pull request or open an issue.
