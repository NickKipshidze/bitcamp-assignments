import main

def test_get_data():
    assert main.get_data("https://www.home.ge/komerciuli-fartebi/iyideba-komerciuli-fartebi/iyideba-universaluri-parti-dighomi-1-9-186148.html") == {'title': 'იყიდება სახლი დიღომი ', 'price': '800,000.00 $', 'preview': 'https://www.home.ge/files/12-2021/ad186148/1677510413167242841_large.jpg', 'location': 'თბილისი ', 'area': '475 მ² ', 'rooms': 10, 'floor': 1}