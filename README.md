Displays Chuck Norris quotes on max7219 LED matrix panel using MQQT

<img src='https://github.com/pappavis/micropython-ChuckNorris-scroller-mqqt/blob/master/ChuckNorrisScroller_demo1.jpg?raw=true' width='20%' height='20%'><br/>

Voorbeeld: <h4>Chuck Norris' Christmas tree is actually a 20 foot Tesla coil. It is also necessary to power his electric beard trimmer.</h4>
<img src='https://media3.giphy.com/media/3hvmlYNsOTFWE/giphy.gif' alt='Chuck norris goedkeuring'>

# Installatie en benodigheden
Om deze te kunnen gebruiken

## Benodigheden
- ESP8266 of ESP32 met <a href='http://Micropython.org'>Micropython</a> geflasht bijvb Wemos D1 Mini   €2,50.
- Een MAX7219 <a href='https://nl.aliexpress.com/item/32618155357.html?spm=a2g0s.9042311.0.0.27424c4dJuFSZU'>LED Matrix</a> paneel  €2,80.
- Mijn <a href='https://github.com/pappavis/micropython-max7219MatrixTextscroller-lib'>micropython-max7219MatrixTextscroller-lib</a> bibliotheek.

## Installatiestappen
1. Installeer een Linux distributie zoals Ubuntu, of dietpi op Raspberry Pi
2. Installeer NodeRed.
3. Deploy de <a href='ChuckNorrisScroller_nodered.json'>ChuckNorrisScroller_nodered.json</a> Nodered flow.
4. Bijwerken jouw wifi gegevens.
```python
mqqt1 = e4kMQQT(ssid='mySSID', password='mypwd', mqqt_server='dietpi')
```

5. Installeer max7219MatrixTextscroller bibliotheek op jouw device bijvb met <a href='https://pypi.org/project/mpfshell/'>mpfshell</a>.
6. Installeer MQQT libs op jouw Micropython apparaat
```bash
MicroPython v1.11-8-g48dcbbe60 on 2019-05-29; ESP module with ESP8266

Type "help()" for more information. [backend=GenericMicroPython]
>>> import upip
>>> upip.install("micropython-umqtt.robust")
Installing to: /lib/

Warning: micropython.org SSL certificate is not validated

Installing micropython-umqtt.robust 1.0.1 from https://micropython.org/pi/umqtt.robust/umqtt.robust-1.0.1.tar.gz

>>> 
```

5. Uploaden naar jouw device en.. lachen :)<br>

# Node red flow
Deze <a href='https://github.com/pappavis/micropython-ChuckNorris-scroller-mqqt/blob/master/ChuckNorrisScroller_nodered.json'>flow</a> moet je deployen op jouw Node Red server.<br/>
<img src='https://github.com/pappavis/micropython-ChuckNorris-scroller-mqqt/blob/master/ChuckNorrisFlow_nodered.jpg?raw=true' width='80%' height='80%'><br/>

# Credits
20200825 door Michiel Erasmus.
