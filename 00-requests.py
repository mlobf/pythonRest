import requests


def main():
    """
    docstring
    """
    payload = {"base": "USD", "symbols": "GBP"}
    response = requests.get("https://api.exchangeratesapi.io/latest", params=payload)

    if response.status_code != 200:
        print("Status Code: ", response.status_code)
        raise Exception("There was a error!")

    print("Status Code: ", response.status_code)
    #print("-----------+++---------------")
    #print("Headers: ", response.headers["Content-Type"])
    #print("Content: ", response.text)
    print("-----------+++---------------")
    print("Now its time to return some Json file.....")
    data = response.json()
    print("-----------+++---------------")
    print(data)
    print("-----------+++---------------")


if __name__ == "__main__":
    main()