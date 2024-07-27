import requests
from urllib.parse import quote

class Verify:
    def __init__(self, ivr):
        self.ivr = ivr
        
    def test(self, user_name, pass_word) -> dict:
        client = requests.Session()
        self.client = client
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Referer': 'https://ais.usvisa-info.com/es-mx/niv'}
        page_home = self.client.get(url='https://ais.usvisa-info.com/es-mx/niv/users/sign_in', headers=headers)
        csrf = self.capture(page_home.text, 'name="csrf-token" content="', '"')
        if csrf == None: return {'status': 'ERROR CSRF'}
        headers = { 'X-CSRF-Token': csrf, 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Accept': '*/*;q=0.5, text/javascript, application/javascript, application/ecmascript, application/x-ecmascript', 'X-Requested-With': 'XMLHttpRequest', 'Origin': 'https://ais.usvisa-info.com', 'Referer': 'https://ais.usvisa-info.com/es-mx/niv/users/sign_in' }
        postdata = f'user%5Bemail%5D={quote(user_name)}&user%5Bpassword%5D={pass_word}&policy_confirmed=1&commit=Iniciar+sesi%C3%B3n'
        login_page = self.client.post(url='https://ais.usvisa-info.com/es-mx/niv/users/sign_in', data=postdata, headers=headers)
        if 'Correo electrónico o contraseña inválida' in login_page.text: return {'status': 'INCORRECT PASSWORD'}
        headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'Referer': login_page.url }
        account = self.client.get(url='https://ais.usvisa-info.com/es-mx/niv/account', headers=headers)
        if self.ivr == "0":
            if "Programe la cita" in self.capture(account.text, "<h4 class='status'>","</h4>"): url_continue =  self.capture(account.text, 'class="button primary small" href="', '"')
            else: return {'status': 'NOT READY'}
        else:
            url_continue = self.find_ivr(account.text, self.ivr)
            if url_continue == None: return {'status': 'NOT IVR'}
    
    def capture(self, data: str, start, end):
        try:
            star = data.index(start) + len(start)
            last = data.index(end, star)
            return data[star:last]

        except ValueError:
            return None
    
    def find_ivr(self, data: str, ivr):
        accounts = []
        while True:
            try:
                star = data.index("class='alert application card ready_to_schedule'>") + len("class='alert application card ready_to_schedule'>")
                last = data.index("</strong>\n</div>", star)
                if star == last : break
                accounts.append(data[star:last])
                data = data[:star] + data[last:]
            except ValueError:
                break
        for acot in accounts:
            if ivr in acot:
                return self.capture(acot, 'class="button primary small" href="', '"')
        return None

def VerifyAccount(attrs):
    if not attrs['type_acot'] == 'P' and not attrs['type_acot'] == 'F': return "TYPE_ACOT INVALID"
    if not attrs['status'] == 'A' and not attrs['status'] == 'D': return "STATUS INVALID"
    if all(mes in ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"] for mes in attrs['months'].split(',')) == False: return "MONTHS INVALID" 
    if not attrs['consul'] == '0' and all(consul in ["Ciudad", "Guadalajara", "Hermosillo", "Matamoros", "Merida", "Mexico", "Monterrey", "Nogales", "Nuevo", "Tijuana"] for consul in attrs['consul'].split(',')) == False: return "CONSUL INVALID" 
    if not attrs['cas'] == '0' and all(cas in ["Ciudad", "Guadalajara", "Hermosillo", "Matamoros", "Merida", "Mexico", "Monterrey", "Nogales", "Nuevo", "Tijuana"] for cas in attrs['cas'].split(',')) == False: return "CAS INVALID" 
    account = Verify(attrs['ivr'])
    resp = account.test(attrs['email'], attrs['password'])
    if resp == {'status': 'ERROR CSRF'}: return "ERROR CSRF"
    elif resp == {'status': 'INCORRECT PASSWORD'}: return "INCORRECT PASSWORD"
    elif resp == {'status': 'NOT IVR'}: return "NOT IVR"
    elif resp == {'status': 'NOT READY'}: return "NOT READY"
    return "READY"
 
   
    