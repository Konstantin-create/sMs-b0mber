from StructPacket import Service
from config import services
import random, time
from colorama import Fore

class Distribution_Service():
    def __init__(self):
        self.number_attack = Service()
        self.services = services()
        

    def phone(self, phone):
        self.number_attack.number(phone)


    def random_service(self, proxies):
        try:
            self.request_service(random.choice(self.services), proxies)
        except Exception:
            pass

    def request_service(self, service, proxies):
        print(f'[+] {service}')
        try:
            if service == 'aistaxi':
                self.number_attack.aistaxi(proxies)

            elif service == 'autheasypayua':
                self.number_attack.autheasypayua(proxies)

            elif service == 'apteka_one':
                self.number_attack.apteka_one(proxies)

            elif service == 'ionua':
                self.number_attack.ionua(proxies)

            elif service == 'sloncreditua':
                self.number_attack.sloncreditua(proxies)

            elif service == 'backzecreditcomua':
                self.number_attack.backzecreditcomua(proxies)

            elif service == 'ontaxicomua':
                self.number_attack.ontaxicomua(proxies)

            elif service == 'ukloncomua_two':
                self.number_attack.ukloncomua_two(proxies)

            elif service == 'partner_uklo_two':
                self.number_attack.partner_uklo_two(proxies)

            elif service == 'alloua':
                self.number_attack.alloua(proxies)

            elif service == 'n17459yclientscom':
                self.number_attack.n17459yclientscom(proxies)

            elif service == 'passporttwitchtv_two':
                self.number_attack.passporttwitchtv_two(proxies)

            elif service == 'apiiconjob_co_two':
                self.number_attack.apiiconjob_co_two(proxies)

            elif service == 'ggbetru':
                self.number_attack.ggbetru(proxies)

            elif service == 'durexrubackendprod':
                self.number_attack.durexrubackendprod(proxies)

            elif service == 'wwwdnsshopru_two':
                self.number_attack.wwwdnsshopru_two(proxies)

            elif service == 'almatyinstashopkz':
                self.number_attack.almatyinstashopkz(proxies)

            elif service == 'gdz_ruwork':
                self.number_attack.gdz_ruwork(proxies)

            elif service == 'smotrimru':
                self.number_attack.smotrimru(proxies)

            elif service == 'wwwriglaru':
                self.number_attack.wwwriglaru(proxies)

            elif service == 'loymaxivoinru':
                self.number_attack.loymaxivoinru(proxies)

            elif service == 'amurfarmaru':
                self.number_attack.amurfarmaru(proxies)

            elif service == 'kulinaristamarket':
                self.number_attack.kulinaristamarket(proxies)

            elif service == 'aptekamagnitu':
                self.number_attack.aptekamagnitu(proxies)

            elif service == 'autodozvon':
                self.number_attack.autodozvon(proxies)

            elif service == 'htvplatform24tv':
                self.number_attack.htvplatform24tv(proxies)

            elif service == 'apilike_videocom':
                self.number_attack.apilike_videocom(proxies)

            elif service == 'mydrom_ru':
                self.number_attack.mydrom_ru(proxies)

            elif service == 'harabaru':
                self.number_attack.harabaru(proxies)

            elif service == 'zaimbistrodengi':
                self.number_attack.zaimbistrodengi(proxies)

            elif service == 'passrutuberu':
                self.number_attack.passrutuberu(proxies)

            elif service == 'mobileapiqiwicom':
                self.number_attack.mobileapiqiwicom(proxies)

            elif service == 'medicina360ru':
                self.number_attack.medicina360ru(proxies)

            elif service == 'apieldoradoua_two':
                self.number_attack.apieldoradoua_two(proxies)

            elif service == 'wwwutairru':
                self.number_attack.wwwutairru(proxies)

            elif service == 'x80aaiccccwa6aik':
                self.number_attack.x80aaiccccwa6aik(proxies)

            elif service == 'disk_apimegafonru':
                self.number_attack.disk_apimegafonru(proxies)

            elif service == 'bigd_host':
                self.number_attack.bigd_host(proxies)

            elif service == 'sushiwokru':
                self.number_attack.sushiwokru(proxies)

            elif service == 'bettery_ru':
                self.number_attack.bettery_ru(proxies)

            elif service == 'pass_media':
                self.number_attack.pass_media(proxies)

            elif service == 'eshko':
                self.number_attack.eshko(proxies)

            elif service == 'dtrparts':
                self.number_attack.dtrparts(proxies)

            elif service == 'smsint2':
                self.number_attack.smsint2(proxies)

            elif service == 'turbosms':
                self.number_attack.turbosms(proxies)

            elif service == 'www360':
                self.number_attack.www360(proxies)

            elif service == 'delivio':
                self.number_attack.delivio(proxies)

            elif service == 'carte':
                self.number_attack.carte(proxies)

            elif service == 'farmakopeika':
                self.number_attack.farmakopeika(proxies)

            elif service == 'farmacia24':
                self.number_attack.farmacia24(proxies)

            elif service == 'wowworks2':
                self.number_attack.wowworks2(proxies)

            elif service == 'alfalife':
                self.number_attack.alfalife(proxies)

            elif service == 'alpari':
                self.number_attack.alpari(proxies)

            elif service == 'beeline_kz':
                self.number_attack.beeline_kz(proxies)

            elif service == 'gnevskii':
                self.number_attack.gnevskii(proxies)

            elif service == 'esk_ural':
                self.number_attack.esk_ural(proxies)

            elif service == 'findclone':
                self.number_attack.findclone(proxies)

            elif service == 'pikru':
                self.number_attack.pikru(proxies)

            elif service == 'edame':
                self.number_attack.edame(proxies)

            elif service == 'vladimirvilkinetru':
                self.number_attack.vladimirvilkinetru(proxies)

            elif service == 'remontnik':
                self.number_attack.remontnik(proxies)

            elif service == 'macdonal':
                self.number_attack.macdonal(proxies)

            elif service == 'api_prime':
                self.number_attack.api_prime(proxies)

            elif service == 'apteka':
                self.number_attack.apteka(proxies)

            elif service == 'artonline':
                self.number_attack.artonline(proxies)

            elif service == 'avtobzvon':
                self.number_attack.avtobzvon(proxies)

            elif service == 'bamperby':
                self.number_attack.bamperby(proxies)

            elif service == 'bartokyo':
                self.number_attack.bartokyo(proxies)

            elif service == 'beltelecom':
                self.number_attack.beltelecom(proxies)

            elif service == 'benzuber':
                self.number_attack.benzuber(proxies)

            elif service == 'bluefin':
                self.number_attack.bluefin(proxies)

            elif service == 'boosty':
                self.number_attack.boosty(proxies)

            elif service == 'buzzolls':
                self.number_attack.buzzolls(proxies)

            elif service == 'cabinet_wi_fi':
                self.number_attack.cabinet_wi_fi(proxies)

            elif service == 'callmyphone':
                self.number_attack.callmyphone(proxies)

            elif service == 'carsmile':
                self.number_attack.carsmile(proxies)

            elif service == 'cian':
                self.number_attack.cian(proxies)

            elif service == 'cinema5':
                self.number_attack.cinema5(proxies)

            elif service == 'citilink':
                self.number_attack.citilink(proxies)

            elif service == 'citrus':
                self.number_attack.citrus(proxies)

            elif service == 'city24':
                self.number_attack.city24(proxies)

            elif service == 'cleversite':
                self.number_attack.cleversite(proxies)

            elif service == 'cloudmailru':
                self.number_attack.cloudmailru(proxies)

            elif service == 'comfy_ua':
                self.number_attack.comfy_ua(proxies)

            elif service == 'creditter':
                self.number_attack.creditter(proxies)

            elif service == 'delitime':
                self.number_attack.delitime(proxies)

            elif service == 'derevenskoe':
                self.number_attack.derevenskoe(proxies)

            elif service == 'dgtl':
                self.number_attack.dgtl(proxies)

            elif service == 'dianet':
                self.number_attack.dianet(proxies)

            elif service == 'dns_shop':
                self.number_attack.dns_shop(proxies)

            elif service == 'e_vse':
                self.number_attack.e_vse(proxies)

            elif service == 'easypay':
                self.number_attack.easypay(proxies)

            elif service == 'uteka':
                self.number_attack.uteka(proxies)

            elif service == 'chibbis':
                self.number_attack.chibbis(proxies)

            elif service == 'syzran':
                self.number_attack.syzran(proxies)

            elif service == 'edostav':
                self.number_attack.edostav(proxies)

            elif service == 'eldorado':
                self.number_attack.eldorado(proxies)

            elif service == 'etm':
                self.number_attack.etm(proxies)

            elif service == 'farpost':
                self.number_attack.farpost(proxies)

            elif service == 'finam':
                self.number_attack.finam(proxies)

            elif service == 'fixprice':
                self.number_attack.fixprice(proxies)

            elif service == 'flipkart':
                self.number_attack.flipkart(proxies)

            elif service == 'foodband':
                self.number_attack.foodband(proxies)

            elif service == 'foxtrot':
                self.number_attack.foxtrot(proxies)

            elif service == 'friendsclub':
                self.number_attack.friendsclub(proxies)

            elif service == 'gazprom':
                self.number_attack.gazprom(proxies)

            elif service == 'getmancar':
                self.number_attack.getmancar(proxies)

            elif service == 'ginzadelivery':
                self.number_attack.ginzadelivery(proxies)

            elif service == 'grabtaxi':
                self.number_attack.grabtaxi(proxies)

            elif service == 'grinica':
                self.number_attack.grinica(proxies)

            elif service == 'groshi':
                self.number_attack.groshi(proxies)

            elif service == 'gurutaxi':
                self.number_attack.gurutaxi(proxies)

            elif service == 'hatimaki':
                self.number_attack.hatimaki(proxies)

            elif service == 'helsi':
                self.number_attack.helsi(proxies)

            elif service == 'hmara':
                self.number_attack.hmara(proxies)

            elif service == 'icq':
                self.number_attack.icq(proxies)

            elif service == 'icqcom':
                self.number_attack.icqcom(proxies)

            elif service == 'id_ykt':
                self.number_attack.id_ykt(proxies)

            elif service == 'ievaphone':
                self.number_attack.ievaphone(proxies)

            elif service == 'imgur':
                self.number_attack.imgur(proxies)

            elif service == 'indriver':
                self.number_attack.indriver(proxies)

            elif service == 'ingos':
                self.number_attack.ingos(proxies)

            elif service == 'invitro':
                self.number_attack.invitro(proxies)

            elif service == 'iqlab':
                self.number_attack.iqlab(proxies)

            elif service == 'ivi':
                self.number_attack.ivi(proxies)

            elif service == 'iwant':
                self.number_attack.iwant(proxies)

            elif service == 'izi':
                self.number_attack.izi(proxies)

            elif service == 'kant':
                self.number_attack.kant(proxies)

            elif service == 'karusel':
                self.number_attack.karusel(proxies)

            elif service == 'kaspi':
                self.number_attack.kaspi(proxies)

            elif service == 'kasta':
                self.number_attack.kasta(proxies)

            elif service == 'kfc':
                self.number_attack.kfc(proxies)

            elif service == 'kilovkusa':
                self.number_attack.kilovkusa(proxies)

            elif service == 'kinolab':
                self.number_attack.kinolab(proxies)

            elif service == 'koronapay':
                self.number_attack.koronapay(proxies)

            elif service == 'krista':
                self.number_attack.krista(proxies)

            elif service == 'kvivstart':
                self.number_attack.kvivstart(proxies)

            elif service == 'lenta':
                self.number_attack.lenta(proxies)

            elif service == 'levin':
                self.number_attack.levin(proxies)

            elif service == 'limetaxi':
                self.number_attack.limetaxi(proxies)

            elif service == 'loany':
                self.number_attack.loany(proxies)

            elif service == 'logistic':
                self.number_attack.logistic(proxies)

            elif service == 'makarolls':
                self.number_attack.makarolls(proxies)

            elif service == 'makimaki':
                self.number_attack.makimaki(proxies)

            elif service == 'menuau':
                self.number_attack.menuau(proxies)

            elif service == 'menzacafe':
                self.number_attack.menzacafe(proxies)

            elif service == 'mistercash':
                self.number_attack.mistercash(proxies)

            elif service == 'mngogomenu':
                self.number_attack.mngogomenu(proxies)

            elif service == 'mobileplanet':
                self.number_attack.mobileplanet(proxies)

            elif service == 'modulbank':
                self.number_attack.modulbank(proxies)

            elif service == 'molbulak':
                self.number_attack.molbulak(proxies)

            elif service == 'moneymanu':
                self.number_attack.moneymanu(proxies)

            elif service == 'monobank':
                self.number_attack.monobank(proxies)

            elif service == 'moscow':
                self.number_attack.moscow(proxies)

            elif service == 'mospizza':
                self.number_attack.mospizza(proxies)

            elif service == 'moyo':
                self.number_attack.moyo(proxies)

            elif service == 'mtstv':
                self.number_attack.mtstv(proxies)

            elif service == 'multiplex':
                self.number_attack.multiplex(proxies)

            elif service == 'mygames':
                self.number_attack.mygames(proxies)

            elif service == 'nb99':
                self.number_attack.nb99(proxies)

            elif service == 'niyama':
                self.number_attack.niyama(proxies)

            elif service == 'nl':
                self.number_attack.nl(proxies)

            elif service == 'nncard':
                self.number_attack.nncard(proxies)

            elif service == 'notecash':
                self.number_attack.notecash(proxies)

            elif service == 'nova':
                self.number_attack.nova(proxies)

            elif service == 'oauth_av':
                self.number_attack.oauth_av(proxies)

            elif service == 'ok':
                self.number_attack.ok(proxies)

            elif service == 'okean':
                self.number_attack.okean(proxies)

            elif service == 'oldi':
                self.number_attack.oldi(proxies)

            elif service == 'ollis':
                self.number_attack.ollis(proxies)

            elif service == 'online_sbis':
                self.number_attack.online_sbis(proxies)

            elif service == 'onlineua':
                self.number_attack.onlineua(proxies)

            elif service == 'oyorooms':
                self.number_attack.oyorooms(proxies)

            elif service == 'ozon':
                self.number_attack.ozon(proxies)

            elif service == 'panda99':
                self.number_attack.panda99(proxies)

            elif service == 'panpizza':
                self.number_attack.panpizza(proxies)

            elif service == 'pirogin':
                self.number_attack.pirogin(proxies)

            elif service == 'pizza46':
                self.number_attack.pizza46(proxies)

            elif service == 'pizza_33':
                self.number_attack.pizza_33(proxies)

            elif service == 'pizzakaz':
                self.number_attack.pizzakaz(proxies)

            elif service == 'pizzasinizza':
                self.number_attack.pizzasinizza(proxies)

            elif service == 'planetak':
                self.number_attack.planetak(proxies)

            elif service == 'plink_tech':
                self.number_attack.plink_tech(proxies)

            elif service == 'pliskov':
                self.number_attack.pliskov(proxies)

            elif service == 'pomodoro':
                self.number_attack.pomodoro(proxies)

            elif service == 'privatebank':
                self.number_attack.privatebank(proxies)

            elif service == 'prosushi':
                self.number_attack.prosushi(proxies)

            elif service == 'protovar':
                self.number_attack.protovar(proxies)

            elif service == 'qbbox':
                self.number_attack.qbbox(proxies)

            elif service == 'qiwi':
                self.number_attack.qiwi(proxies)

            elif service == 'qlean':
                self.number_attack.qlean(proxies)

            elif service == 'raiffeisen':
                self.number_attack.raiffeisen(proxies)

            elif service == 'rbt':
                self.number_attack.rbt(proxies)

            elif service == 'rendesvouz':
                self.number_attack.rendesvouz(proxies)

            elif service == 'richfamely':
                self.number_attack.richfamely(proxies)

            elif service == 'rieltor':
                self.number_attack.rieltor(proxies)

            elif service == 'rutaxi':
                self.number_attack.rutaxi(proxies)

            elif service == 'rutaxi_ru':
                self.number_attack.rutaxi_ru(proxies)

            elif service == 'rutube':
                self.number_attack.rutube(proxies)

            elif service == 'samaraetagi':
                self.number_attack.samaraetagi(proxies)

            elif service == 'sayoris':
                self.number_attack.sayoris(proxies)

            elif service == 'sedi':
                self.number_attack.sedi(proxies)

            elif service == 'shafa':
                self.number_attack.shafa(proxies)

            elif service == 'shopandshow':
                self.number_attack.shopandshow(proxies)

            elif service == 'signalis':
                self.number_attack.signalis(proxies)

            elif service == 'sipnet':
                self.number_attack.sipnet(proxies)

            elif service == 'smartomato':
                self.number_attack.smartomato(proxies)

            elif service == 'smartspace':
                self.number_attack.smartspace(proxies)

            elif service == 'sms4':
                self.number_attack.sms4(proxies)

            elif service == 'smsint':
                self.number_attack.smsint(proxies)

            elif service == 'sovest':
                self.number_attack.sovest(proxies)

            elif service == 'sportmasterua':
                self.number_attack.sportmasterua(proxies)

            elif service == 'sravni':
                self.number_attack.sravni(proxies)

            elif service == 'startpizza':
                self.number_attack.startpizza(proxies)

            elif service == 'studio':
                self.number_attack.studio(proxies)

            elif service == 'suandi':
                self.number_attack.suandi(proxies)

            elif service == 'sumaster':
                self.number_attack.sumaster(proxies)

            elif service == 'sunlignt':
                self.number_attack.sunlignt(proxies)

            elif service == 'sushifuji':
                self.number_attack.sushifuji(proxies)

            elif service == 'sushigour':
                self.number_attack.sushigour(proxies)

            elif service == 'sushiprof':
                self.number_attack.sushiprof(proxies)

            elif service == 'sushiroll':
                self.number_attack.sushiroll(proxies)

            elif service == 'sushivesla':
                self.number_attack.sushivesla(proxies)

            elif service == 'tabasko':
                self.number_attack.tabasko(proxies)

            elif service == 'tabris':
                self.number_attack.tabris(proxies)

            elif service == 'tanuki':
                self.number_attack.tanuki(proxies)

            elif service == 'tarantionofamely':
                self.number_attack.tarantionofamely(proxies)

            elif service == 'taxi310':
                self.number_attack.taxi310(proxies)

            elif service == 'taziritm':
                self.number_attack.taziritm(proxies)

            elif service == 'tehnosvit':
                self.number_attack.tehnosvit(proxies)

            elif service == 'tele2':
                self.number_attack.tele2(proxies)

            elif service == 'telegram':
                self.number_attack.telegram(proxies)

            elif service == 'thehive':
                self.number_attack.thehive(proxies)

            elif service == 'tiktok':
                self.number_attack.tiktok(proxies)

            elif service == 'tinder':
                self.number_attack.tinder(proxies)

            elif service == 'tinkoff':
                self.number_attack.tinkoff(proxies)

            elif service == 'topladeba':
                self.number_attack.topladeba(proxies)

            elif service == 'topshop':
                self.number_attack.topshop(proxies)

            elif service == 'tvoaapteka':
                self.number_attack.tvoaapteka(proxies)

            elif service == 'twitch':
                self.number_attack.twitch(proxies)

            elif service == 'ubepmsmorg':
                self.number_attack.ubepmsmorg(proxies)

            elif service == 'ubki':
                self.number_attack.ubki(proxies)

            elif service == 'uklon':
                self.number_attack.uklon(proxies)

            elif service == 'ulabka':
                self.number_attack.ulabka(proxies)

            elif service == 'uralsib':
                self.number_attack.uralsib(proxies)

            elif service == 'utrair':
                self.number_attack.utrair(proxies)

            elif service == 'vezitaxi':
                self.number_attack.vezitaxi(proxies)

            elif service == 'viza':
                self.number_attack.viza(proxies)

            elif service == 'vks':
                self.number_attack.vks(proxies)

            elif service == 'vodafone':
                self.number_attack.vodafone(proxies)

            elif service == 'webbank':
                self.number_attack.webbank(proxies)

            elif service == 'wifimetro':
                self.number_attack.wifimetro(proxies)

            elif service == 'work':
                self.number_attack.work(proxies)

            elif service == 'wowworks':
                self.number_attack.wowworks(proxies)

            elif service == 'yandexeda':
                self.number_attack.yandexeda(proxies)

            elif service == 'yapochink':
                self.number_attack.yapochink(proxies)

            elif service == 'youla':
                self.number_attack.youla(proxies)

            elif service == 'zaminka':
                self.number_attack.zaminka(proxies)

            elif service == 'zoopt':
                self.number_attack.zoopt(proxies)


            # МОИ РАЗРАБОТКИ

            elif service == 'petrovich':
                self.number_attack.petrovich(proxies)

            elif service == 'wink':
                self.number_attack.wink(proxies)

            elif service == 'sravni':
                self.number_attack.sravni(proxies)

            elif service == 'citymobil':
                self.number_attack.citymobil(proxies)

            elif service == 'maxi':
                self.number_attack.maxi(proxies)

            elif service == 'angels':
                self.number_attack.angels(proxies)

            elif service == 'pronkers':
                self.number_attack.pronkers(proxies)

            elif service == 'ftrade':
                self.number_attack.ftrade(proxies)

            elif service == 'sushiwok':
                self.number_attack.sushiwok(proxies)
                
            elif service == 'truck':
                self.number_attack.truck(proxies)

            elif service == 'broniboy':
                self.number_attack.broniboy(proxies)

            elif service == 'sokolov':
                self.number_attack.sokolov(proxies)

            elif service == 'savetime':
                self.number_attack.savetime(proxies)


            elif service == 'goldapple':
                self.number_attack.goldapple(proxies)

            elif service == 'uvelirocha':
                self.number_attack.uvelirocha(proxies)

            elif service == 'kristall':
                self.number_attack.kristall(proxies)

            elif service == 'goldrussia':
                self.number_attack.goldrussia(proxies)

            elif service == 'sephora':
                self.number_attack.sephora(proxies)

            elif service == 'bankiru':
                self.number_attack.bankiru(proxies)

            elif service == 'auchan':
                self.number_attack.auchan(proxies)

            elif service == 'mainpoint':
                self.number_attack.mainpoint(proxies)

            elif service == 'cupis':
                self.number_attack.cupis(proxies)

            elif service == 'bapteka':
                self.number_attack.bapteka(proxies)

            elif service == 'cmd':
                self.number_attack.cmd(proxies)     
            
            elif service == 'proapteka':
                self.number_attack.proapteka(proxies)           


        except Exception:
            pass
