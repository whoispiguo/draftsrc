from PIL import Image
import pytesseract
import pyautogui
import time
import webbrowser
pytesseract.pytesseract.tesseract_cmd =r"C:\Program Files\Tesseract-OCR\tesseract.exe"

time.sleep(3)

screenshot = pyautogui.screenshot(region=(1300, 110, 420, 1000))
screenshot.save("pick_1.png")

image = Image.open('pick_1.png')
champs = pytesseract.image_to_string(image, lang='eng')

screenshot_allies = pyautogui.screenshot(region=(100, 110, 450, 800))
screenshot_allies.save("allies_1.png")

image_allies = Image.open('allies_1.png')
ally1 = pytesseract.image_to_string(image_allies, lang='eng')

champion_ids = {
    "AATROX": "266",
    "AHRI": "103",
    "AKALI": "84",
    "AKSHAN": "166",
    "ALISTAR": "12",
    "AMUMU": "32",
    "ANIVIA": "34",
    "ANNIE": "1",
    "APHELIOS": "523",
    "ASHE": "22",
    "AURELION SOL": "136",
    "AZIR": "268",
    "BARD": "432",
    "BLITZCRANK": "53",
    "BRAND": "63",
    "BRAUM": "201",
    "CAITLYN": "51",
    "CAMILLE": "164",
    "CASSIOPEIA": "69",
    "CHO'GATH": "31",
    "CORKI": "42",
    "DARIUS": "122",
    "DIANA": "131",
    "DRAVEN": "119",
    "DR. MUNDO": "36",
    "EKKO": "245",
    "ELISE": "60",
    "EVELYNN": "28",
    "EZREAL": "81",
    "FIDDLESTICKS": "9",
    "FIORA": "114",
    "FIZZ": "105",
    "GALIO": "3",
    "GANGPLANK": "41",
    "GAREN": "86",
    "GNAR": "150",
    "GRAGAS": "79",
    "GRAVES": "104",
    "GWEN": "887",
    "HECARIM": "120",
    "HEIMERDINGER": "74",
    "ILLAOI": "420",
    "IRELIA": "39",
    "IVERN": "427",
    "JANNA": "40",
    "JARVAN IV": "59",
    "JAX": "24",
    "JAYCE": "126",
    "JHIN": "202",
    "JINX": "222",
    "KAI'SA": "145",
    "KALISTA": "429",
    "KARMA": "43",
    "KARTHUS": "30",
    "KASSADIN": "38",
    "KATARINA": "55",
    "KAYLE": "10",
    "KAYN": "141",
    "KENNEN": "85",
    "KHA'ZIX": "121",
    "KINDRED": "203",
    "KLED": "240",
    "KOG'MAW": "96",
    "LEBLANC": "7",
    "LEE SIN": "64",
    "LEONA": "89",
    "LILLIA": "876",
    "LISSANDRA": "127",
    "LUCIAN": "236",
    "LULU": "117",
    "LUX": "99",
    "MALPHITE": "54",
    "MALZAHAR": "90",
    "MAOKAI": "57",
    "MASTER YI": "11",
    "MISS FORTUNE": "21",
    "WUKONG": "62",
    "MORDEKAISER": "82",
    "MORGANA": "25",
    "NAMI": "267",
    "NASUS": "75",
    "NAUTILUS": "111",
    "NEEKO": "518",
    "NIDALEE": "76",
    "NOCTURNE": "56",
    "NUNU & WILLUMP": "20",
    "OLAF": "2",
    "ORIANNA": "61",
    "ORNN": "516",
    "PANTHEON": "80",
    "POPPY": "78",
    "PYKE": "555",
    "QIYANA": "246",
    "QUINN": "133",
    "RAKAN": "497",
    "RAMMUS": "33",
    "REK'SAI": "421",
    "RELL": "526",
    "RENATA GLASC": "888",
    "RENEKTON": "58",
    "RENGAR": "107",
    "RIVEN": "92",
    "RUMBLE": "68",
    "RYZE": "13",
    "SAMIRA": "360",
    "SEJUANI": "113",
    "SENNA": "235",
    "SERAPHINE": "147",
    "SETT": "875",
    "SHACO": "35",
    "SHEN": "98",
    "SHYVANA": "102",
    "SINGED": "27",
    "SION": "14",
    "SIVIR": "15",
    "SKARNER": "72",
    "SONA": "37",
    "SORAKA": "16",
    "SWAIN": "50",
    "SYLAS": "517",
    "SYNDRA": "134",
    "TAHM KENCH": "223",
    "TALIYAH": "163",
    "TALON": "91",
    "TARIC": "44",
    "TEEMO": "17",
    "THRESH": "412",
    "TRISTANA": "18",
    "TRUNDLE": "48",
    "TRYNDAMERE": "23",
    "TWISTED FATE": "4",
    "TWITCH": "29",
    "UDYR": "77",
    "URGOT": "6",
    "VARUS": "110",
    "VAYNE": "67",
    "VEIGAR": "45",
    "VEL'KOZ": "161",
    "VEX": "711",
    "VI": "254",
    "VIEGO": "234",
    "VIKTOR": "112",
    "VLADIMIR": "8",
    "VOLIBEAR": "106",
    "WARWICK": "19",
    "XAYAH": "498",
    "XERATH": "101",
    "XIN ZHAO": "5",
    "YASUO": "157",
    "YONE": "777",
    "YORICK": "83",
    "YUUMI": "350",
    "ZAC": "154",
    "ZED": "238",
    "ZERI": "221",
    "ZIGGS": "115",
    "ZILEAN": "26",
    "ZOE": "142",
    "ZYRA": "143"
}

picks = []
for champ, id in champion_ids.items():
    if champ in champs:
        picks.append(id)

pick_1 = ",".join(picks)

allies_list = []
for champ1, id in champion_ids.items():
    if champ1 in ally1 and id not in picks: 
        allies_list.append(id)

allies_1 = ",".join(allies_list)

time.sleep(1)

def generate_url(pick_1):
    url = f"https://www.metasrc.com/lol/counter-picker?allies={allies_1}&enemies={pick_1}"
    webbrowser.open(url)

generate_url(pick_1)
