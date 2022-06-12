import re 
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select

app=QtWidgets.QApplication([])
tela=uic.loadUi("janela_principal.ui")


flag = 0
def configurar():
    password = tela.senha_acesso.text()
    while True:   
        if (len(password)<8): 
            flag = -1
            break
        elif not re.search("[a-z]", password): 
            flag = -1
            break
        elif not re.search("[A-Z]", password): 
            flag = -1
            break
        elif not re.search("[0-9]", password): 
            flag = -1
            break
        elif not re.search("[_@$]", password): 
            flag = -1
            break
        elif re.search("\s", password): 
            flag = -1
            break
        else: 
            flag = 0
            login_cliente = tela.text_login.text()
            pppoe_cliente = tela.text_pppoe.text()
            senha_cliente = tela.text_ssid2.text()
            nome_rede = tela.rede_wireless.text()
            modelo = tela.comboBox.currentText()
            senha_acesso = tela.senha_acesso.text()
            

            

            ################################# CODIGO QUE VAI NO APP #########################################



            #para executar o webdrive no diretorio r'./chromedriver.exe#
            navegador = webdriver.Chrome(executable_path=r'./chromedriver.exe')

            #para navegar ate o ip do roteador#
            navegador.get("http://192.168.1.1/")

            #para preencer o campo de texto username com o "multipro"#
            navegador.find_element_by_name("Frm_Username").send_keys("multipro")

            navegador.find_element_by_name("Frm_Password").send_keys("multipro" + Keys.RETURN)

            #tempo minimo nescessario para o nevegador processar as informações#
            time.sleep(0.5)

            #########
            navegador.find_element_by_id("Btn_Close").click()
            #########
            time.sleep(0.5)
            #para mandar um click no id#
            navegador.find_element_by_id("internet").click()
            time.sleep(0.5)
            navegador.find_element_by_id("internetConfig").click()
            time.sleep(0.5)
            navegador.find_element_by_id("addInstBar_Internet").click()

            #para preencer o campo de texto "nome "
            navegador.find_element_by_name("WANCName:1").send_keys("PPPoE-LCI")

            #para desativar a TR069 do roteador#
            navegador.find_element_by_id("Servlist_TR069:1").click()

            #para desmarcar a IPTV#
            navegador.find_element_by_id("Servlist_IPTV:1").click()
            time.sleep(0.5)
            #Para preencer a PPoE como username e password"
            navegador.find_element_by_name("UserName:1").send_keys(login_cliente)
            navegador.find_element_by_name("Password:1").send_keys(pppoe_cliente)

            # para alterar a ip version para IPv4/v6 #
            select = Select(navegador.find_element_by_name("IpMode:1"))
            select.select_by_visible_text("IPv4/v6")

            #para clicar em aplicar#
            navegador.find_element_by_id("Btn_apply_internet:1").click()

            #para clicar em securit#
            navegador.find_element_by_id("security").click()
            #dar um tempo para o navegador processar#
            time.sleep(0.5)



            ## CONFIGURAÇÕES DO ""SERVICE CONTROL - IPv4" ##

            #para clicar em "Controle de serviço local"
            navegador.find_element_by_id("localServiceCtrl").click()
            time.sleep(0.5)

            #para dar um enable na opção IPv4
            navegador.find_element_by_id("Enable1:serviceCtl:0").click()

            #Para preencer e mudar o nome para "AcessoLCI"

            navegador.find_element_by_name("Name:serviceCtl:0").send_keys("AcessoLCI")

            #Para ativar a opção Targer#                                                                                                                                                                                                                          ra marcar a opção Target#
            navegador.find_element_by_id("FilterTarget1:serviceCtl:0").click()

            #Para preencer o Ip ranger de 189.113.112.1 ate 189.113.113.254#
            navegador.find_element_by_name("sub_MinSrcIp0:0").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_id("sub_MinSrcIp0:0").send_keys("189")
            navegador.find_element_by_id("sub_MinSrcIp1:0").send_keys("113")
            navegador.find_element_by_id("sub_MinSrcIp2:0").send_keys("113")
            navegador.find_element_by_id("sub_MinSrcIp3:0").send_keys("1")

            navegador.find_element_by_name("sub_MinSrcIp3:0").send_keys(Keys.TAB)

            navegador.find_element_by_name("sub_MaxSrcIp0:0").send_keys("189")
            navegador.find_element_by_id("sub_MaxSrcIp1:0").send_keys("113")
            navegador.find_element_by_id("sub_MaxSrcIp2:0").send_keys("113")
            navegador.find_element_by_id("sub_MaxSrcIp3:0").send_keys("254")

            #Para ativar os service type "HTTP, TELNET, HTTPS, PING"
            navegador.find_element_by_id("Servise_HTTP:0").click()
            navegador.find_element_by_id("Servise_TELNET:0").click()
            navegador.find_element_by_id("Servise_HTTPS:0").click()
            navegador.find_element_by_id("Servise_PING:0").click()

            #Para dar um Apply#
            navegador.find_element_by_id("Btn_apply_serviceCtl:0").click()

            time.sleep(0.5)

            ## CONFIGURAÇÕES DE "REMOTE SERVICE PORT CONTROL - IPV4" ##

            #Clicar em Remote service port control #
            navegador.find_element_by_id("ServPortCfgBar").click()

            navegador.find_element_by_id("ServPort_0").click()
            navegador.find_element_by_name("ServPort_0").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_name("ServPort_0").send_keys(Keys.BACKSPACE)
            #Preencher o campo HTTP, FTP, TELNET, HTTPS #
            navegador.find_element_by_id("ServPort_0").send_keys("4555")
            navegador.find_element_by_id("ServPort_0").send_keys(Keys.TAB)

            navegador.find_element_by_name("ServPort_1").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_id("ServPort_1").send_keys("4588")

            navegador.find_element_by_id("ServPort_2").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_id("ServPort_2").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_id("ServPort_2").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_id("ServPort_2").send_keys("4566")

            #Dar um apply#
            navegador.find_element_by_id("Btn_apply_ServPortCfg").click()


            #clicar em rede local#
            navegador.find_element_by_id("localnet").click()
            time.sleep(0.5)
            #clicar em WLAN#
            navegador.find_element_by_id("wlanConfig").click()
            time.sleep(0.5)
            #clicar em Configuração WLAN SSID#
            navegador.find_element_by_id("WLANSSIDConfBar").click()
            #limpar#

            navegador.find_element_by_id("ESSID:0").click()
            navegador.find_element_by_name("ESSID:0").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_name("ESSID:0").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_name("ESSID:0").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_name("ESSID:0").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_name("ESSID:0").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_name("ESSID:0").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_name("ESSID:0").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_name("ESSID:0").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_name("ESSID:0").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_name("ESSID:0").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_name("ESSID:0").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_name("ESSID:0").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_name("ESSID:0").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_name("ESSID:0").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_name("ESSID:0").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_name("ESSID:0").send_keys(Keys.BACKSPACE)
            #para alterar o nome da rede 2.4 usando a variavel wifi_cliente1#
            navegador.find_element_by_name("ESSID:0").send_keys(nome_rede)
            #para alterar a senha da rede 2.4#
            navegador.find_element_by_id("Switch_KeyPassType:0").click()

            navegador.find_element_by_id("KeyPassphrase:0").click()
            navegador.find_element_by_name("KeyPassphrase:0").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_name("KeyPassphrase:0").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_name("KeyPassphrase:0").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_name("KeyPassphrase:0").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_name("KeyPassphrase:0").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_name("KeyPassphrase:0").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_name("KeyPassphrase:0").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_name("KeyPassphrase:0").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_name("KeyPassphrase:0").send_keys(senha_cliente)

            #configurações da rede 5GHz#
            navegador.find_element_by_id("instName_WLANSSIDConf:4").click()

            navegador.find_element_by_id("ESSID:4").click()
            navegador.find_element_by_name("ESSID:4").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_name("ESSID:4").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_name("ESSID:4").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_name("ESSID:4").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_name("ESSID:4").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_name("ESSID:4").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_name("ESSID:4").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_name("ESSID:4").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_name("ESSID:4").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_name("ESSID:4").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_name("ESSID:4").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_name("ESSID:4").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_name("ESSID:4").send_keys(Keys.BACKSPACE)

            #preenxer o nome da rede 5ghz#
            navegador.find_element_by_id("ESSID:4").send_keys(nome_rede)
            navegador.find_element_by_id("Switch_KeyPassType:4").click()
            navegador.find_element_by_id("KeyPassphrase:4").click()
            navegador.find_element_by_name("KeyPassphrase:4").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_name("KeyPassphrase:4").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_name("KeyPassphrase:4").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_name("KeyPassphrase:4").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_name("KeyPassphrase:4").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_name("KeyPassphrase:4").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_name("KeyPassphrase:4").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_name("KeyPassphrase:4").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_name("KeyPassphrase:4").send_keys(senha_cliente)

            #Para aplicar a configurações#
            navegador.find_element_by_id("Btn_apply_WLANSSIDConf:0").click()
            time.sleep(0.5)
            navegador.find_element_by_id("Btn_apply_WLANSSIDConf:4").click()
            time.sleep(0.5)

            #Ativar o UPnP#
            navegador.find_element_by_id("upnp").click()
            time.sleep(0.5)
            #clicar em ligado para ativar o UPnP#
            navegador.find_element_by_id("OBJ_UPNPCONFIG_ID.EnableUPnPIGD1:LocalUPnP").click()
            time.sleep(0.5)
            #clicar em aplicar#
            navegador.find_element_by_id("Btn_apply_LocalUPnP").click()

            #Altera senha de acesso pela internet#
            #clicar em management & Diagnosis#
            navegador.find_element_by_id("mgrAndDiag").click()
            time.sleep(0.5)
            #clicar em gerenciamento de conta#
            navegador.find_element_by_id("accountMgr").click()
            time.sleep(0.5)
            #preencer senha antiga#
            navegador.find_element_by_name("Password:0").send_keys("multipro")

            #para preencher e confirmar a nova senha de acesso ao roteador#
            navegador.find_element_by_name("NewPassword:0").send_keys(senha_acesso)
            navegador.find_element_by_name("NewConfirmPassword:0").send_keys(senha_acesso)
            #clicar em Aplicar#
            navegador.find_element_by_id("Btn_apply_AccountManag:0").click()
            time.sleep(0.5)

            #Configuração da interface LAN#

            #clicar na LAN#
            navegador.find_element_by_id("localnet").click()
            time.sleep(0.5)
            navegador.find_element_by_id("lanConfig").click()
            time.sleep(0.5)
            time.sleep(0.5)
            #clicar em servidor DHCP"
            navegador.find_element_by_id("DHCPBasicCfgBar").click()
            navegador.find_element_by_name("sub_IPAddr2:DHCPBasicCfg").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_name("sub_IPAddr2:DHCPBasicCfg").send_keys("0")
            navegador.find_element_by_name("sub_MinAddress3:DHCPBasicCfg").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_name("sub_MinAddress3:DHCPBasicCfg").send_keys("100")
            navegador.find_element_by_name("sub_MaxAddress3:DHCPBasicCfg").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_name("sub_MaxAddress3:DHCPBasicCfg").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_name("sub_MaxAddress3:DHCPBasicCfg").send_keys(Keys.BACKSPACE)
            navegador.find_element_by_name("sub_MaxAddress3:DHCPBasicCfg").send_keys("200")
            #para clicar em aplicar#
            navegador.find_element_by_id("Btn_apply_DHCPBasicCfg").click()


            ################################# CODIGO QUE VAI NO APP #########################################
            break
    
    if flag ==-1: 
        QMessageBox.critical(tela,"ERRO", 'A senha de Acesso para roteadores "ZTE" precisa ter pelo menos um caracter maiúsculo!')
        
tela.pushButton.clicked.connect(configurar)

tela.show()
app.exec()
