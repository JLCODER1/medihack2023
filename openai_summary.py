import openai
import run_google_search

def summary(question: str) -> str:
    #calls google search function
    link = run_google_search.search(question)
    #gets info from website
    info = run_google_search.get_more_details(link)

    openai.api_key = '<Add api key here>'
    response = openai.ChatCompletion.create(
         model='gpt-3.5-turbo',
        messages= [{"role": "user", "content": info}],
        )
    #previous code gives prompt to ai
    
    #gets a summary/answer from ai
    summary = response.choices[0].message["content"]
    print(summary)
    return summary

def main():
    #prompt for ai
    summary(input())
    #summary('why is my poop black')

if __name__ == '__main__':
    main()

    
