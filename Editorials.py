from lib.Titles_With_Links import *
from lib.Dict_To_PDF import *


# Extracting Editorials
def extract_editorials():
    driver_path = "C:\webdrivers\chromedriver"
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)

    title_to_story = {}

    for i in title_to_link:
        title_to_story[i] = ""

        driver.get("https://www.hindustantimes.com" + title_to_link[i])
        content = driver.page_source
        soup = BeautifulSoup(content, "html.parser")

        # Short Description of the Story
        p = soup.find("h2", attrs={"class": "sortDec"})
        title_to_story[i] += p.text + " "

        # Detailed Story
        div = soup.find("div", attrs={"class": "detail"})
        for paras in div.find_all("p"):
            title_to_story[i] += paras.text

    driver.quit()
    return title_to_story


if __name__ == "__main__":
    while True:
        options = input(
            "Enter Your Option: \n 1. All the Editorials in a Single PDF \n 2. All the Editorials in Different PDF'S \n 3. Exit \n Enter Your Option Here: "
        )

        if options == "3":
            break
        match options:
            case "1":
                Titles_With_Links()
                dict_to_sing_pdf(extract_editorials())
            case "2":
                Titles_With_Links()
                dict_to_mul_pdf(extract_editorials())
            case _:
                print("Please choose from the following options")
