import os, requests

todo_endpoint = os.environ.get('TODO_URL', "http://localhost:8081/todos/")
wikipedia_url = "https://en.wikipedia.org/wiki/Special:Random"

def get_wikipedia_article():
    try:
        response = requests.get(wikipedia_url, allow_redirects=False)
        response.raise_for_status()
        return response.headers["location"]
    except requests.exceptions.RequestException as e:
        print(f"Error while fetching {wikipedia_url}: {e}")
    return "Error occured while fetching Wikipedia article's URL"    

def create_todo(todo_text):
    data = {'todo_text': todo_text}
    response = requests.post(todo_endpoint, data=data)
    return response


def main():
    article_url = get_wikipedia_article()
    response = create_todo("Read {}".format(article_url))

    if response.status_code == 200:
        print("Todo created successful!")
    else:
        print("Error occured while creating todo")

if __name__=="__main__":
    main()

