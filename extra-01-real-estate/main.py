from bs4 import BeautifulSoup
import requests, json

def output(data):
    for key in data:
        print(f"{key:>10} : {data[key]}")

def get_data(url):
    raw_html = requests.get(url).text

    soup = BeautifulSoup(raw_html, "html.parser")

    field_title = soup.find(id="df_field_title")
    field_price = soup.find(id="df_field_price")
    field_preview = soup.find("div", class_="preview")
    field_location = soup.find(id="df_field_mdebareoba")
    field_area = soup.find(id="df_field_square_feet")
    field_rooms = soup.find(id="df_field_rooms")
    field_floor = soup.find(id="df_field_floor")

    data = {
        "title": field_title.find(class_="value").text[1:],
        "price": field_price.span.text,
        "preview": field_preview.img.get_attribute_list("src")[0],
        "location": field_location.find(class_="value").text[1:],
        "area": field_area.find(class_="value").text[1:],
        "rooms": int(field_rooms.find(class_="value").text[1:]),
        "floor": int(field_floor.find(class_="value").text[1:])
    }

    return data

def main():
    data = get_data("https://www.home.ge/komerciuli-fartebi/iyideba-komerciuli-fartebi/iyideba-universaluri-parti-dighomi-1-9-186148.html")

    output(data) # Extra

    open("data.json", "w").write(json.dumps(data, indent=4))

if __name__ == "__main__":
    main()