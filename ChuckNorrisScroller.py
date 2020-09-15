from Max7219Textscroller import MatrixTextscroller
import utime
from umqtt.simple import MQTTClient
import ubinascii
import machine
import micropython
import network

class e4kMQQT:
    def __init__(self, ssid, password, mqqt_server):
        self.__ssid = ssid
        self.__password = password
        self.__mqtt_server = mqqt_server
        #EXAMPLE IP ADDRESS
        #mqtt_server = '192.168.1.144'
        self.__client_id = ubinascii.hexlify(machine.unique_id())
        self.__topic_pub = b'lichtkrant/mqqt_connect'
        self.__topic_sub = b'lichtkrant/tape'
        self.scoller1 = MatrixTextscroller()
        self.__topic_connect_pub = 'lichtkrant/mqqt_connect'
        self.__lichtKrantTekst = '   MQQT default  '
        self.__client = None
        self.__debug = False

    def __sub_cb(self, topic, msg):
    #    if(topic == topic_sub): #and (msg == b'received'):
        print(self.client_id, '\n\tESP received', msg)

        print(self.client_id, '\tBericht ontvangen topic=',topic, '   msg=', msg)
        
        if(topic == self.__topic_sub):
            print(self.client_id, '\t topic ',topic, ' was bijgewerkt met nieuwe msg.')
            self.lichtKrantTekst = str(msg)
            self.scoller1.scrollText(textToScroll='  ' + self.lichtKrantTekst)
            
        elif(topic == 'lichtkrant/alive'):
            self.__client.publish('kattenvoer/receiveAlive', "client " + str(self.client_id) + " " + ' MQQT is beschikbaar')
        else:
            pass


    def connect_and_subscribe(self):
        strTxt1 = 'Verbind aan ' + self.__ssid
        print(strTxt1)
        self.scoller1.scrollText(textToScroll='    ' + strTxt1)
        station = network.WLAN(network.STA_IF)

        station.active(True)
        station.connect(self.__ssid, self.__password)

        while station.isconnected() == False:
          pass

        strTxt1 = 'WiFi Connection successful'
        print(strTxt1)
        self.scoller1.scrollText(textToScroll='    ' + strTxt1)
        print(station.ifconfig())
      
        self.__client = MQTTClient(self.client_id, self.__mqtt_server, user="admin", password="admin")
        self.__client.set_callback(self.__sub_cb)
        
        if not self.__client.connect(clean_session=False):
            print("New session being set up")
            
        strTxt1 = str(self.client_id) + '; connected aan ' + self.__topic_connect_pub + '.'
        self.__client.subscribe(self.topic_sub)    
        self.__client.publish(self.__topic_connect_pub, strTxt1)
        print(strTxt1)
        self.scoller1.scrollText(textToScroll='    ' + strTxt1)
        
        print('')

        strTxt1 = str(self.client_id) + ' connected to ' + str(self.__mqtt_server) + ' MQTT broker, subscribed to topic ' + str(self.topic_sub)
        print(strTxt1)
        self.scoller1.scrollText(textToScroll='    ' + strTxt1)

        return self.__client

    def restart_and_reconnect(self):
        print('Failed to connect to MQTT broker. Reconnecting...')
        time.sleep(10)
        machine.reset()

    def init(self):
        self.scoller1.debug = False
        self.scoller1.scrollspeed = 0.2
        self.scoller1.scrollText(textToScroll='    MQQT maxint_lichtkrant  ')
        
    @property
    def client(self):
        return self.__client
    
    @property
    def lichtKrantTekst(self):
        return self.__lichtKrantTekst

    @lichtKrantTekst.setter
    def lichtKrantTekst(self, value):
        self.__lichtKrantTekst = value


    @property
    def debug(self):
        return self.__debug

    @debug.setter
    def debug(self, value):
        self.__debug = value


    @property
    def topic_pub(self):
        return self.__topic_pub

    @topic_pub.setter
    def topic_pub(self, value):
        self.__topic_pub = value


    @property
    def topic_sub(self):
        return self.__topic_sub

    @topic_sub.setter
    def topic_sub(self, value):
        self.__topic_sub = value

    @property
    def client_id(self):
        return self.__client_id

    @client_id.setter
    def client_id(self, value):
        self.__client_id = value


def main():
    message_interval = (1000*60) * 5
    next_publishevent = None
    eersteStart = True
    isWaar1 = True
    client = None
    teller1 = 0

    mqqt1 = e4kMQQT(ssid='ssid', password='secret', mqqt_server='dietpi')    
    
    while (isWaar1):
        try:
            if (eersteStart):
                next_publishevent = utime.ticks_ms() + message_interval
                eersteStart = False

            if(client == None):
                client = mqqt1.connect_and_subscribe()

            if (utime.ticks_ms() > next_publishevent):
                mqqt1.client.publish(mqqt1.topic_pub, str(mqqt1.client_id) + ';' + str(next_publishevent))
                next_publishevent = utime.ticks_ms() + message_interval

            new_message = mqqt1.client.check_msg()
            mqqt1.scoller1.scrollText(textToScroll='  ' + mqqt1.lichtKrantTekst)
            
            teller1 += 1

            utime.sleep_ms(1)            
        except OSError as e:
            mqqt1.restart_and_reconnect()


print('App start')
main()

print('App eind')

