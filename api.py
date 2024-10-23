from fastapi import FastAPI, Request, File, UploadFile, Response, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, RedirectResponse, StreamingResponse, JSONResponse


import pyjokes
from whois import whois
from random import randint
import json
from rembg import remove
from PIL import Image
import pyshorteners
from random import randint, choice
import string
import requests
import g4f
from datetime import datetime
import jdatetime
import pytz
from captcha.image import ImageCaptcha
from qrcode import QRCode, ERROR_CORRECT_L
from io import BytesIO
from gtts import gTTS
from deep_translator import GoogleTranslator
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

app = FastAPI()

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_experimental_option("useAutomationExtension", False)
driver = webdriver.Chrome(options=chrome_options)

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

### Update
# Instagram Downloader
# YouTube Downloader
# Instagram User Info
# Telegram User Info
# Yasdl
# Weather
# Myket Downloader
# Create Logo
# Google Search
# Soundcloud Downloader
# PPTP
# IP Information
# Farsroid
# Aparat Downloader
# Fall Hafez With Image
# Google Play Downloader

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {'request':request})

@app.get("/images")
async def get_images():
    images = [f for f in os.listdir("./static/picture/") if f.endswith(('.png', '.jpg', '.jpeg'))]

    image_links = [f"http://localhost:8000/static/picture/{image}" for image in images]
    return JSONResponse(content={"images": image_links})

@app.get("/joke")
def getJoke():
    joke = pyjokes.get_joke()
    return joke

@app.get("/fall")
def getFall():
    with open('./assets/faals.json') as f:
      data = json.load(f)
    fal = randint(0,494)
    return {"fall": data[2]["data"][fal]["Poem"], "tafsir": data[2]["data"][fal]["Interpretation"]}


@app.get("/wallpaper")
def getWall():
    return RedirectResponse(url="https://picsum.photos/1920/1080")

@app.get("/password")
def passGen():
    char = string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice(char) for x in range(randint(8,16)))
    
    return password

@app.get("/textRev/{text}")
def textReverser(text):
    text = text[::-1]

    return text

@app.get("/arz")
def getCurrency():
    response_btc = requests.get('https://api.nobitex.ir/v2/orderbook/BTCIRT')
    price_btc = response_btc.json()['lastTradePrice']
    BTC = int(price_btc)
    BTC1 = BTC // 10
    number = BTC1
    BTCIRT = format(number, ',')
    response_btcusdt = requests.get('https://api.nobitex.ir/v2/orderbook/BTCUSDT')
    price_btcusdt = response_btcusdt.json()['lastTradePrice']
    BTCUSDT1 = float(price_btcusdt)
    BTCUSDT = float(BTCUSDT1)
    numberusdt = BTCUSDT
    BTCUSDT = format(numberusdt, ',')

    ## Ethereum
    response_eth = requests.get('https://api.nobitex.ir/v2/orderbook/ETHIRT')
    price_eth = response_eth.json()['lastTradePrice']
    ETH = int(price_eth)
    ETH1 = ETH // 10
    numbereth = ETH1
    ETHIRT = format(numbereth, ',')
    response_ethusdt = requests.get('https://api.nobitex.ir/v2/orderbook/ETHUSDT')
    price_ethusdt = response_ethusdt.json()['lastTradePrice']
    ETHUSDT1 = float(price_ethusdt)
    ETHUSDT = float(ETHUSDT1)
    numbereth1 = ETHUSDT
    ETHUSDT = format(numbereth1, ',')

    ## XRP
    response_xrp = requests.get('https://api.nobitex.ir/v2/orderbook/XRPIRT')
    price_xrp = response_xrp.json()['lastTradePrice']
    XRP = int(price_xrp)
    XRP1 = ETH // 10
    numberxrp = XRP1
    XRPIRT = format(numberxrp, ',')
    response_xrpusdt = requests.get('https://api.nobitex.ir/v2/orderbook/XRPUSDT')
    price_xrpusdt = response_xrpusdt.json()['lastTradePrice']
    XRPUSDT1 = float(price_xrpusdt)
    XRPUSDT = float(XRPUSDT1)
    numberxrp1 = XRPUSDT
    XRPUSDT = format(numberxrp1, ',')

    ## Litecoin
    response_ltc = requests.get('https://api.nobitex.ir/v2/orderbook/LTCIRT')
    price_ltc = response_ltc.json()['lastTradePrice']
    LTC = int(price_ltc)
    LTC1 = LTC // 10
    numberltc = LTC1
    LTCIRT = format(numberltc, ',')
    response_ltcusdt = requests.get('https://api.nobitex.ir/v2/orderbook/LTCUSDT')
    price_ltcusdt = response_ltcusdt.json()['lastTradePrice']
    LTCUSDT1 = float(price_ltcusdt)
    LTCUSDT = float(LTCUSDT1)
    numberltc1 = LTCUSDT
    LTCUSDT = format(numberltc1, ',')

    ## EOS
    response_eos = requests.get('https://api.nobitex.ir/v2/orderbook/EOSIRT')
    price_eos = response_eos.json()['lastTradePrice']
    EOS = int(price_eos)
    EOS1 = EOS // 10
    numbereos = EOS1
    EOSIRT = format(numbereos, ',')
    response_eosusdt = requests.get('https://api.nobitex.ir/v2/orderbook/EOSUSDT')
    price_eosusdt = response_eosusdt.json()['lastTradePrice']
    EOSUSDT1 = float(price_eosusdt)
    EOSUSDT = float(EOSUSDT1)
    numbereos1 = EOSUSDT
    EOSUSDT = format(numbereos1, ',')

    ## BNB
    response_bnb = requests.get('https://api.nobitex.ir/v2/orderbook/BNBIRT')
    price_bnb = response_bnb.json()['lastTradePrice']
    BNB = int(price_bnb)
    BNB1 = BNB // 10
    numberbnb = BNB1
    BNBIRT = format(numberbnb, ',')
    response_bnbusdt = requests.get('https://api.nobitex.ir/v2/orderbook/BNBUSDT')
    price_bnbusdt = response_bnbusdt.json()['lastTradePrice']
    BNBUSDT1 = float(price_bnbusdt)
    BNBUSDT = float(BNBUSDT1)
    numberbnb1 = BNBUSDT
    BNBUSDT = format(numberbnb1, ',')

    ## BCH
    response_bch = requests.get('https://api.nobitex.ir/v2/orderbook/BCHIRT')
    price_bch = response_bch.json()['lastTradePrice']
    BCH = int(price_bch)
    BCH1 = BCH // 10
    numberbch = BCH1
    BCHIRT = format(numberbch, ',')
    response_bchusdt = requests.get('https://api.nobitex.ir/v2/orderbook/BCHUSDT')
    price_bchusdt = response_bchusdt.json()['lastTradePrice']
    BCHUSDT1 = float(price_bchusdt)
    BCHUSDT = float(BCHUSDT1)
    numberbch1 = BCHUSDT
    BCHUSDT = format(numberbch1, ',')

    ##DOGE
    response_doge = requests.get('https://api.nobitex.ir/v2/orderbook/DOGEIRT')
    price_doge = response_doge.json()['lastTradePrice']
    DOGE = int(price_doge)
    DOGE1 = DOGE // 10
    numberdoge = DOGE1
    DOGEIRT = format(numberdoge, ',')
    response_dogeusdt = requests.get('https://api.nobitex.ir/v2/orderbook/DOGEUSDT')
    price_dogeusdt = response_dogeusdt.json()['lastTradePrice']
    DOGEUSDT1 = float(price_dogeusdt)
    DOGEUSDT = float(DOGEUSDT1)
    numberdoge1 = DOGEUSDT
    DOGEUSDT = format(numberdoge1, ',')

    ## USDT
    response_usdt = requests.get('https://api.nobitex.ir/v2/orderbook/USDTIRT')
    price_usdt = response_usdt.json()['lastTradePrice']
    USDT = int(price_usdt)
    USDT1 = USDT // 10
    number = USDT1
    USDT = format(number, ',')

    ## TRON
    response_tron = requests.get('https://api.nobitex.ir/v2/orderbook/TRXIRT')
    price_tron = response_tron.json()['lastTradePrice']
    TRON = int(price_tron)
    TRON1 = TRON // 10
    number = TRON1
    TRXIRT = format(number, ',')
    response_trxusdt = requests.get('https://api.nobitex.ir/v2/orderbook/TRXUSDT')
    price_trxusdt = response_trxusdt.json()['lastTradePrice']
    TRXUSDT1 = float(price_trxusdt)
    TRXUSDT = float(TRXUSDT1)
    numbertrx1 = TRXUSDT
    TRXUSDT = format(numbertrx1, ',')

    return {"BITCOIN": {"USD":  BTCUSDT, "IRT": BTCIRT},"ETHEREUM": {"USD":  ETHUSDT, "IRT": ETHIRT},"XRP": {"USD":  XRPUSDT, "IRT": XRPIRT},"LITECOIN": {"USD":  LTCUSDT, "IRT": LTCIRT},"EOS": {"USD":  EOSUSDT, "IRT": EOSIRT},"BNB": {"USD":  BNBUSDT, "IRT": BNBIRT},"BCH": {"USD":  BCHUSDT, "IRT": BCHIRT},"DOGE": {"USD":  DOGEUSDT, "IRT": DOGEIRT},"TRON": {"USD":  TRXUSDT, "IRT": TRXIRT},"USDT": {"IRT":  USDT}}

@app.get("/shortURL/{link}")
def shorterURL(link):
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(link)

    return short_url

@app.get("/chatGPT/{question}")
def chatGPT(question):
    response = g4f.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{"role": "user", "content": question}],
        stream=True
    )

    return response

@app.get("/datetime")
def getDateTime():
    utc_now = datetime.now()
    
    ir_now = datetime.now(pytz.timezone('Asia/Tehran'))

    utc_date = utc_now.strftime("%Y/%m/%d")
    utc_time = utc_now.strftime("%H:%M:%S %p")
    
    ir_date = jdatetime.date.today().strftime("%Y/%m/%d")
    ir_time = ir_now.strftime("%H:%M:%S")

    return {"Date": {"Date": utc_date, "Time": utc_time},"Iran-Date": {"Date": ir_date, "Time": ir_time}}

@app.get("/captcha")
def getCaptcha():
    image = ImageCaptcha(width=280, height=90)
    char = string.ascii_letters + string.digits
    captcha_text = "".join(choice(char) for i in range(randint(4,6)))

    data = image.generate(captcha_text)
    image_bytes = data.getvalue()

    image.write(captcha_text, 'captcha.png')

    return Response(content=image_bytes, media_type="image/png")

@app.get("/qrcode/{link}")
def getqrcode(link: str):
    qr = QRCode(version=1, error_correction=ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    return Response(content=buffer.read(), media_type="image/png")

@app.get("/text2voice/{text}")
def textToSpeech(text: str):
    tts = gTTS(text=text, lang='en')
    audio_file = "output.mp3"
    tts.save(audio_file)
    
    return FileResponse(audio_file, media_type='audio/mpeg', filename="output.mp3")

@app.get("/translate/{text}")
def translator(text: str):
    translated = GoogleTranslator(source='auto', target='fa').translate(text)

    return translated

@app.get("/bmi")
def calculate_bmi(weight: float, height: float):
    bmi = weight / (height ** 2)

    return {"BMI": round(bmi, 2)}

@app.get("/pinterest")
def pinterestDownloader(url: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    images = soup.find_all('img')

    image_urls = [img['src'] for img in images if 'src' in img.attrs]

    return {"image_urls": image_urls[0]}

@app.get("/removeBG")
def removeBackground(image: str):

    response = requests.get(image)
    image_bytes = response.content
    output = remove(image_bytes)
    return StreamingResponse(BytesIO(output), media_type="image/png")

@app.get("/whois")
def getWhois(url: str):
    dm_info =  whois(url)

    return dm_info

@app.get("/screenshot")
def ssWebsite(url: str):
    driver.get(url)
    screenshot = driver.get_screenshot_as_png()
    driver.quit()
    buffer = BytesIO(screenshot)

    return StreamingResponse(buffer, media_type="image/png")
