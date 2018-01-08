import os
import pyqrcode
import cairosvg
import kivy
from kivy.graphics.svg import Svg
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.button import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from web3 import Web3, HTTPProvider, IPCProvider
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.graphics.svg import Svg
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
import time
web3 = Web3(HTTPProvider('http://localhost:8545'))
block = web3.eth.getBlock('latest')
print('')
print('██████╗ ██╗██╗  ██╗███████╗ ██████╗██╗  ██╗ █████╗ ██╗███╗   ██╗   ██╗ ██████╗ ')
print('██╔══██╗██║██║ ██╔╝██╔════╝██╔════╝██║  ██║██╔══██╗██║████╗  ██║   ██║██╔═══██╗')
print('██████╔╝██║█████╔╝ █████╗  ██║     ███████║███████║██║██╔██╗ ██║   ██║██║   ██║')
print('██╔══██╗██║██╔═██╗ ██╔══╝  ██║     ██╔══██║██╔══██║██║██║╚██╗██║   ██║██║   ██║')
print('██████╔╝██║██║  ██╗███████╗╚██████╗██║  ██║██║  ██║██║██║ ╚████║██╗██║╚██████╔╝')
print('╚═════╝ ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚═╝╚═╝ ╚═════╝ ')
print('')
print('###############################################################################')
print('')
print('Current Block Number:')
print(block.number)
print('')
print('###############################################################################')
print('')
print('List of Current Accounts:')
acts = web3.eth.accounts
for a in acts:
    print(a)
print('')
print('###############################################################################')
print('')
print('Current Personal Accounts:')
pacts = web3.personal.listAccounts
for b in pacts:
    print(b)
print('')
print('Creating New Personal Account:')
npact = web3.personal.newAccount('bikechain.io')
print(npact)
print('')
print('Passphrase: bikechain.io')
print('')
print('Current Personal Accounts:')
pacts = web3.personal.listAccounts
for b in pacts:
    print(b)
print('')
web3.miner.start(2)
time.sleep(10)
web3.miner.stop()
web3.eth.getBalance(npact)
print('run kivy android app')
npactstr = str(npact)
print(npactstr)
loadqr = pyqrcode.create(npact)
loadqr.svg('./images/bikechain-address.svg', background='white', scale=8)
cairosvg.svg2png(url='images/bikechain-address.svg', write_to='images/bikechain-address.png')
os.remove('images/bikechain-address.svg')
Builder.load_string("""
<MenuScreen>:
    BoxLayout:
        orientation: "vertical"

        Image:
            source: './images/chainlink.png'
        Label:
            text: '[b]Bikechain.io[/b]'
            markup: True
            height: 30
            size_hint: (1, None)
        Button:
            text: 'Import ETH Address'
            on_press: root.manager.current = 'importscreen'
            height: 30
            size_hint: (1, None)
        Button:
            text: 'Register Bicycle'
            on_press: root.manager.current = 'registerscreen'
            height: 30
            size_hint: (1, None)
        Button:
            text: 'Report Bicycle'
            on_press: root.manager.current = 'reportscreen'
            height: 30
            size_hint: (1, None)
        Button:
            text: 'Recover Bicycle'
            on_press: root.manager.current = 'recoverscreen'
            height: 30
            size_hint: (1, None)
        Button:
            text: 'Search Bikechain.io'
            on_press: root.manager.current = 'searchscreen'
            height: 30
            size_hint: (1, None)
        Button:
            text: 'Quit'
            on_press: app.stop()
            height: 30
            size_hint: (1, None)

<ImportScreen>:
    BoxLayout:
        orientation: "vertical"
        Image:
            source: './images/chainlink.png'
        Image:
            source: './images/bikechain-address.png'
        Label:
            text: str(root.DisplayEthAddr())
            markup: True
            height: 30
            size_hint: (1, None) 
        Label:
            text: '[b]Import Ethereum Address[/b]'
            markup: True
            height: 30
            size_hint: (1, None)
        TextInput:
            id: txt_importkey
            text: 'Ethereum Private Key'
            on_text: print(args)
            multiline: False
            height: 30
            size_hint: (1, None)
        TextInput:
            id: txt_pswd
            text: 'Ethereum Password'
            on_text: print(args)
            multiline: False
            height: 30
            size_hint: (1, None)
        Button:
            text: 'Import Wallet Key'
            height: 30
            on_press: root.ImportEthAddr()
            size_hint: (1, None)
        Button:
            text: 'Create New Address'
            height: 30
            size_hint: (1, None)
        Button:
            text: 'Export and Backup'
            height: 30
            size_hint: (1, None)
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
            height: 30
            size_hint: (1, None)

<RegisterScreen>:
    BoxLayout:
        orientation: "vertical"
        Image:
            source: './images/chainlink.png'
        Label:
            text: '[b]Serial Number:[/b]'
            markup: True
            height: 30
            size_hint: (1, None)
        Label:
            text: "[b]Eth Address: [/b]" + str(root.DisplayEthAddr())
            markup: True
            height: 30
            size_hint: (1, None) 
        Label:
            text: '[b]Register Bicycle to Bikechain.io[/b]'
            markup: True
            height: 30
            size_hint: (1, None)
        TextInput:
            id: txt_serialnumber
            text: 'Bicycle Serial Number'
            on_text: print("serial number " + str(args))
            multiline: False
            height: 30
            size_hint: (1, None)
        Spinner:
            text: 'Enter Bike Manufacturer'
            values: ('A-bike', 'Abici', 'Adler', 'AIST', 'ALAN', 'Alcyon', 'Alldays & Onions', 'American Bicycle Company', 'American Eagle', 'American Machine and Foundry', 'American Star Bicycle', 'Aprilia', 'Argon 18', 'Ariel', 'Atala', 'Author', 'Avanti', 'Baltik vairas', 'Bacchetta', 'Barnes Cycle Company', 'Batavus', 'Battaglin', 'Berlin & Racycle Manufacturing Company', 'BH', 'Bianchi', 'Bickerton', 'Bike Friday', 'Bilenky', 'Biomega', 'Birdy', 'BMC', 'Boardman Bikes', 'Bohemian Bicycles', 'Bontrager', 'Bootie', 'Bottecchia', 'Bradbury', 'Brasil & Movimento', 'Brennabor', 'Bridgestone', 'British Eagle', 'Brodie Bicycles', 'Brompton Bicycle', 'Brunswick', 'BSA', 'Burley Design', 'Calcott Brothers', 'Calfee Design', 'Caloi', 'Campion Cycle Company', 'Cannondale', 'Canyon bicycles', 'Catrike', 'CCM', 'Centurion', 'Cervélo', 'Chater-Lea', 'Chicago Bicycle Company', 'CHUMBA', 'Cilo', 'Cinelli', 'Clark-Kent', 'Claud Butler', 'Clément', 'Co-Motion Cycles', 'Coker', 'Colnago', 'Columbia Bicycles', 'Corima', 'Cortina Cycles', 'Coventry-Eagle', 'Cruzbike', 'Cube', 'Currys', 'Cycle Force Group', 'Cycles Devinci', 'Cycleuropa Group', 'Cyfac', 'Dahon', 'Dawes Cycles', 'Defiance Cycle Company', 'Demorest', 'Den Beste Sykkel', 'Derby Cycle', 'De Rosa', 'Cycles Devinci', 'Di Blasi Industriale', 'Diamant', 'Diamant', 'Diamondback Bicycles', 'Dolan Bikes', 'Dorel Industries', 'Dunelt', 'Dynacraft', 'Esmaltina', 'Eagle', 'Bicycle Manufacturing Company', 'Eddy Merckx Cycles', 'Electra Bicycle Company', 'Ellis Briggs', 'Ellsworth Handcrafted Bicycles', 'Emilio Bozzi', 'Enigma Titanium', 'Ērenpreiss Bicycles', 'Excelsior', 'Falcon Cycles', 'Fat City Cycles', 'Felt', 'Fleetwing -USA', 'Flying Pigeon', 'Flying Scot', 'Focus Bikes', 'Cycles Follis', 'Folmer & Schwing','Fondriest', 'Fram', 'Freddie Grubb', 'Fuji Bikes', 'Fyxation', 'GaryFisher', 'Gazelle', 'Gendron Bicycles', 'Genesis', 'Gepida', 'GiantManufacturing', 'Gimson', 'Gitane', 'Gladiator Cycle Company', 'Gnome et Rhône', 'Gocycle', 'Gormully & Jeffery', 'Gräf & Stift', 'GT Bicycles', 'Guerciotti','Gustavs Ērenpreis Bicycle Factory', 'Gunnar', 'Harley-Davidson', 'HaroBikes', 'Harry Quinn', 'Hase bikes', 'Heinkel', 'Helkama', 'Henley Bicycle Works', 'Hercules', 'Hercules', 'Hero Cycles Ltd', 'René Herse', 'Hetchins', 'Hillman', 'Hoffman BMX Bikes', 'Hoffmann', 'Holdsworth', 'Huffy', 'Humber', 'Hurtu', 'Husqvarna', 'Ibis', 'Ideal Bikes', 'Indian', 'IFA', 'Independent Fabrication', 'Iride', 'Iron Horse Bicycles', 'Islabikes', 'Italvega', 'Itera', 'Ivel Cycle Works', 'Iver Johnson', 'Iverson', 'Jan Janssen', 'JMC Bicycles', 'Jamis Bicycles', 'Kalkhoff', 'Kangaroo', 'Karbon Kinetics Limited', 'K2 Sports', 'Kent', 'Kestrel USA', 'Kettler', 'KHS', 'Kia', 'Kinesis Industry', 'Klein', 'Koga Miyata', 'Kogswell Cycles', 'Kona', 'Kronan', 'Kross', 'KTM', 'Kuota', 'Kuwahara', 'Laurin & Klement', 'Lapierre', 'LeMond', 'Alexander Leutner & Co.', 'Lightning Cycle Dynamics', 'itespeed', 'Look', 'Louison Bobet', 'Lotus', 'Magna', 'Malvern Star', 'Marin Bikes', 'Masi Bicycles', 'Matchless', 'Matra', 'Melon Bicycles', 'Mercian Cycles', 'Merida Bikes', 'Merlin', 'Merckx', 'Miele bicycles', 'Milwaukee Bicycle Co.', 'Minerva', 'Miyata', 'Mochet', 'Monark', 'Mondia', 'Mongoose', 'Montague', 'Moots Cycles', 'Moser Cicli', 'Motobécane', 'Moulton', 'Mountain Equipment Co-op', 'Murray', 'Muddy Fox', 'Nagasawa', 'National', 'Neil Pryde', 'Neobike', 'NEXT', 'Nishiki and Europe', 'Norco', 'Norman Cycles', 'Novara', 'NSU', 'Nymanbolagen', 'Olive Wheel Company', 'Olmo', 'Opel', 'Orange Mountain Bikes', 'Orbea', 'Órbita', 'Orient Bikes', 'Overman Wheel Company', 'Pacific Cycle', 'Pacific Cycles', 'Panasonic', 'Pashley Cycles', 'Pedersen bicycle', 'Pegas', 'Peugeot', 'Phillips Cycles', 'Phoenix', 'Pierce Cycle Company', 'Pinarello', 'Planet X Bikes', 'Pocket Bicycles', 'Pogliaghi', 'Polygon Bikes', 'Pope Manufacturing Company', 'Premier', 'Procycle Group', 'Prophete', 'Puch', 'Quadrant Cycle Company', 'Quality Bicycle Products', 'Quintana Roo', 'R+E Cycles', 'Radio Flyer', 'Rabasa Cycles', 'Raleigh', 'Rambler', 'Rans Designs', 'Razor', 'Redline bicycles', 'Rhoades Car', 'Ridgeback', 'Ridley', 'Riese und Müller', 'RIH', 'Riley Cycle Company', 'Rivendell Bicycle Works', 'Roadmaster', 'Roberts Cycles', 'Robin Hood', 'Rocky Mountain Bicycles', 'ROSE Bikes', 'Ross', 'Rover Company', 'Rowbike', 'Rudge-Whitworth', 'Salcano', 'Samchuly', 'Santa Cruz Bikes', 'Santana Cycles', 'Saracen Cycles', 'Maskinfabriks-aktiebolaget Scania', 'Schwinn Bicycle Company', 'SCOTT Sports', 'Serotta', 'Seven Cycles', 'Shelby Cycle Company', 'Shimano', 'Simpel', 'Simson', 'Sinclair Research', 'Singer', 'Softride', 'Sohrab', 'Solé Bicycle Co.', 'Solex', 'Solifer', 'SOMA Fabrications', 'Somec', 'Spalding', 'Sparta B.V.', 'Specialized', 'Speedwell bicycles', 'Star Cycle Company', 'Stearns', 'Stelber Cycle Corp', 'Stella', 'Sterling Bicycle Co.', 'Steyr', 'Strida', 'Sun Cycle & Fittings Co.', 'Sunbeam', 'Surly Bikes', 'Suzuki', 'Swift Folder', 'Swing Bike', 'Syracuse Cycle Company', 'Tern', 'Terrot', 'Thomas', 'Thorn Cycles', 'Time', 'TI Cycles of India', 'Titus', 'Tommaso bikes', 'Torker', 'Trek Bicycle Corporation', 'Trinx', 'Triumph Cycle', 'Triumph', 'Tube Investments', 'Tunturi', 'Turner Suspension Bicycles', 'Univega', 'Uppadine Cycles', 'Urago', 'Van Dessel Sports', 'Velocite Bikes', 'Velomotors', 'VéloSoleX', 'Velo Vie', 'Victoria', 'Villiger', 'Villy Customs', 'Vindec', 'Vitus', 'Volae', 'Volagi', 'Wanderer', 'Waterford Precision Cycles', 'Western Flyer', 'Westfield Manufacturing', 'Whippet', 'Wilderness Trail Bikes', 'Wilier Triestina', 'Witcomb Cycles', 'Wittson Custom Ti Cycles', 'Worden Bicycles', 'Worksman Cycles', 'Wright Cycle Company', 'Whyte', 'Xootr', 'Yamaguchi Bicycles', 'Yamaha', 'Yeti Cycles', 'Zigo', 'Zündapp')
            sync_height: True
            size_hint_y: None
            height: 30
            size_hint: (1, None)
        Button:
            text: 'Register Bicycle'
            on_press: root.RegisterBike()
            height: 30
            size_hint: (1, None)
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
            height: 30
            size_hint: (1, None)
            

<ReportScreen>:
    BoxLayout:
        orientation: "vertical"
        Image:
            source: './images/chainlink.png'
        Image:
            source: './images/bikechain-address.png'
        Label:
            text: str(root.DisplayEthAddr())
            markup: True
            height: 30
            size_hint: (1, None) 
        Label:
            text: '[b]Report Stolen Bike to Bikechain.io[/b]'
            markup: True
            height: 30
            size_hint: (1, None)
        TextInput:
            id: txt_stolentag
            text: 'Enter Identifaction tag shortlinks to pictures or googlemaps link to the location of the stolen bike'
            on_text: print("serial number " + str(args))
            multiline: False
            height: 30
            size_hint: (1, None)

        Button:
            text: 'Report Bicycle as Stolen'
            height: 30
            size_hint: (1, None)

        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
            height: 30
            size_hint: (1, None)

<RecoverScreen>:
    BoxLayout:
        orientation: "vertical"
        Image:
            source: 'chainlink.png'
        Label:
            text: '[b]Recover Bike Via Bikechain.io[/b]'
            markup: True
            height: 30
            size_hint: (1, None)
        Button:
            text: 'Burn Theft Token'
            height: 30
            size_hint: (1, None)
        Button:
            text: 'My recover  button'
            height: 30
            size_hint: (1, None)
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
            height: 30
            size_hint: (1, None)

<SearchScreen>:
    BoxLayout:
        orientation: "vertical"
        Label:
            text: '[b]Bikechain.io[/b]'
            markup: True
            height: 30
            size_hint: (1, None)
        Button:
            text: 'My settings button'
            height: 30
            size_hint: (1, None)
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
            height: 30
            size_hint: (1, None)
""")
# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
#####################################################################################
# Screen declarations and functions
#####################################################################################
## Menu Screen
class MenuScreen(Screen):
    pass
#####################################################################################
## Import Ethereum Address Screen
class ImportScreen(Screen):
    def DisplayEthAddr(self):
        return npact
#### IMPORT ETHEREUM ADDRESS
    def ImportEthAddr(self):
        print("Import Ethereum Address "+npact)
    def CreateEthAddr(self):
        print("Create Ethereum Address "+npact)
    def ExportEthAddr(self):
        print("Export Ethereum Address "+npact)
    pass
#####################################################################################
## Register Bike Screen
class RegisterScreen(Screen):
    def DisplayEthAddr(self):      
        return npact
    def DisplaySerial(self):
        print(args)
#### REGISTER BICYCLE ON BLOCKCHAIN
    def RegisterBike(self):
        print("Register Bicycle")
    pass
#####################################################################################
#### Report Bike Screen
class ReportScreen(Screen):
## REPORT BICYCLE ON BLOCKCHAIN    
    def DisplayEthAddr(self):
        return npact   
## REPORT BICYCLE ON BLOCKCHAIN
    def ReportBike(self):
        print("Report Stolen Bicycle - run ethereum contract call")
    pass
#####################################################################################
####  Recover Bike Screen
class RecoverScreen(Screen):
    def DisplayEthAddr(self):
        return npact
    def RecoverBike(self):
        print("Recover Bicycle")
    pass
#####################################################################################
####  Search Bikechain Screen
class SearchScreen(Screen):
    def DisplayEthAddr(self):
        return npact
    def SearchBikechain(self):
        print("Search Bicycle Serial number")
    pass
#####################################################################################
# Managing Screens on the Application
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ImportScreen(name='importscreen'))
sm.add_widget(RegisterScreen(name='registerscreen'))
sm.add_widget(ReportScreen(name='reportscreen'))
sm.add_widget(RecoverScreen(name='recoverscreen'))
sm.add_widget(SearchScreen(name='searchscreen'))

class TestApp(App):
    def build(self):
        return sm
if __name__ == '__main__':
    TestApp().run()

