import openai
import run_google_search

def summary(question: str) -> str:
    link = run_google_search.search(question)
    info = run_google_search.get_more_details(link)

    openai.api_key = '<Add api key here>'
    response = openai.ChatCompletion.create(
         model='gpt-3.5-turbo',
        messages= [{"role": "user", "content": info}],
        )
    
    summary = response.choices[0].message["content"]
    print(summary)
    return summary

def main():
    #summary(input())
    summary('why is my poop black')

if __name__ == '__main__':
    main()

    
