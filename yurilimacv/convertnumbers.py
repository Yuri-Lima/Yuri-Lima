import re
from Locate import unit_EN


class Convert_numbers_english:
    
    def __init__(self, number_typed):
        self.number_typed = number_typed
        self._decimal = len(self.number_typed)
        self._check_zero = self.check_zeros()
        self.joins = list()
        self.joins_str = ""
        self.place = {
            'ones': 0, 'tens': 0, 'hundreds': 0, 'thousands': 0, 'ten_thousands': 0, 'hundred_thousands': 0,
            'millions': 0, 'ten_millions': 0, 'hundred_millions': 0, 'billions': 0, 'ten_billions': 0,
            'hundred_billions': 0, 'trillions': 0, 'ten_trillions': 0, 'hundred_trillions': 0,
            'quadrillions': 0, 'ten_quadrillions': 0, 'hundred_quadrillions': 0,'ends': 0}
        
        self.validates = {
            'flag_hundred_quadrillion': True,'flag_quadrillion': True,
            'flag_hundred_trillion': True, 'flag_ten_trillion': True,'flag_trillion': True,
            'flag_hundred_billion': True, 'flag_ten_billion': True, 'flag_billion': True,
            'flag_hundred_million': True, 'flag_ten_million': True, 'flag_million': True,
            'flag_hundred_thousand': True, 'flag_ten_thousand': True, 'flag_thousand': True,
            'flag_hundred': True, 'flag_decimal': True, 'flag_one': True}

    #Getter
    @property
    def number_typed(self): 
        return self._number_typed
    #Setter
    @number_typed.setter
    def number_typed(self, value):
        #Regular Expression
        value = ''.join(re.findall("\d+", value))#Return only numbers [0-9]
        value = re.search('[^0|\s]\d*', value)[0]#Regular Expression
        self._number_typed = value

    #***********************************************************************************
    #===================================================================================
    ########################        Start Main Functions       #########################
    #===================================================================================
    def start_convertion(self):
        self.change_validations()
    
    def change_validations(self):
        #three statment below are always true
        self.validates['flag_one'] = True
        self.validates['flag_decimal'] = True
        self.validates['flag_hundred'] = True
        #====================================================================================================
        # Thousands
        if self._decimal == 4:
            self.validates['flag_thousand'] = True
        # ====================================================================================================
        # Ten_thousands
        elif self._decimal == 5:
            self.validates['flag_ten_thousand'] = True
        # ====================================================================================================
        # hundreds_thousands
        elif self._decimal == 6:
            self.validates['flag_hundred_thousand'] = True
        # ====================================================================================================
        # Millions 
        elif self._decimal == 7:
            self.validates['flag_million'] = True
            self.validates['flag_hundred_thousand'] = True
        # ====================================================================================================
        # Ten_millions 
        elif self._decimal == 8:
            self.validates['flag_ten_million'] = True
            self.validates['flag_hundred_thousand'] = True
        # ====================================================================================================
        # Hundred_millions 
        elif self._decimal == 9:
            self.validates['flag_hundred_million'] = True
            self.validates['flag_hundred_thousand'] = True
        # ====================================================================================================
        # Billions 
        elif self._decimal == 10:
            self.validates['flag_billion'] = True
            self.validates['flag_hundred_million'] = True
            self.validates['flag_hundred_thousand'] = True
        # ====================================================================================================
        # Ten_billions 
        elif self._decimal == 11:
            self.validates['flag_ten_billion'] = True
            self.validates['flag_hundred_million'] = True
            self.validates['flag_hundred_thousand'] = True
        # ====================================================================================================
        # Hundred_billions 
        elif self._decimal == 12:
            self.validates['flag_hundred_billion'] = True
            self.validates['flag_hundred_million'] = True
            self.validates['flag_hundred_thousand'] = True
        # ====================================================================================================
        # Trillions 
        elif self._decimal == 13:
            self.validates['flag_trillion'] = True 
            self.validates['flag_hundred_billion'] = True
            self.validates['flag_ten_billion'] = True
            self.validates['flag_hundred_million'] = True
            self.validates['flag_hundred_thousand'] = True
        # ====================================================================================================
        # Ten_Trillions
        elif self._decimal == 14:
            self.validates['flag_ten_trillion'] = True
            self.validates['flag_hundred_billion'] = True
            self.validates['flag_hundred_million'] = True
            self.validates['flag_hundred_thousand'] = True
         # ====================================================================================================
        # Hundred_trillions 
        elif self._decimal == 15:
            self.validates['flag_hundred_trillion'] = True
            self.validates['flag_hundred_billion'] = True
            self.validates['flag_hundred_million'] = True
            self.validates['flag_hundred_thousand'] = True
        # ====================================================================================================
        # Quadrillions 
        elif self._decimal == 16:
            self.validates['flag_quadrillion'] = True
            self.validates['flag_hundred_trillion'] = True
            # self.validates['flag_ten_trillion'] = True
            self.validates['flag_hundred_billion'] = True
            self.validates['flag_ten_billion'] = True
            # self.validates['flag_billion'] = True
            self.validates['flag_hundred_million'] = True
            self.validates['flag_ten_million'] = True
            self.validates['flag_million'] = True
            self.validates['flag_hundred_thousand'] = True
        
        self.populate_decimal_place()

    def populate_decimal_place(self):#vai popular place e retornar
        index = None
        for index, k in enumerate(self.place.keys(), start=1):
            if index == self._decimal + 1:
                # print('index: {} number_typed: {}'.format(index, self._decimal))
                break
            else:
                self.place[k] = int(self.number_typed[-index])#ele vai alimentando PLACE de traz para frente place[k] <-- 6 <-- int(num[-index])
                # print('place k: {} place: {}'.format(self.place[k], self.place))
        #if place['trillions']== 0 else index - 0
        self.decimal_part_of_number()

    #Para saber se e maior ou menor que 20
    def decimal_part_of_number(self):
        self.tens_part = int(str(self.place['tens']) + str(self.place['ones']))
        self.tens_thousands_part = int(str(self.place['ten_thousands']) + str(self.place['thousands']))
        self.tens_millions_part = int(str(self.place['ten_millions']) + str(self.place['millions']))
        self.tens_billions_part = int(str(self.place['ten_billions']) + str(self.place['billions']))
        self.tens_trillions_part = int(str(self.place['ten_trillions']) + str(self.place['trillions']))
        self.tens_quadrillions_part = int(str(self.place['ten_quadrillions']) + str(self.place['quadrillions']))
        #index_tens (int): recevi the tens places to find the position into the dictionary place[]
        self.concatanation_number_in_word()
        #Go check the positions when the Tens Part is bigger than Twenty, you can see into the file Locate.py --> unit_EN
        #Starting from Ten_thousands

    def find_position_in_place(self, index_tens):
        self.index_tens = index_tens
        self._collection = str('{} {}'.format(unit_EN[(index_tens - (9 * (int((index_tens / 10)) - 2))) - (index_tens % 10)], 
                    unit_EN[index_tens % 10] if index_tens % 10 != 0 else ''))#Isso virou uma constante e faz as concatenacoes ['One Hundred', 'Twenty Three Thousand', ' Four Hundred', 'Fifty Six']
        return self._collection

    def check_zeros(self):
        #It means that the number after the first one are zeros Trillions #9.--> 000.000.000.000 <--
        inc = 0
        # print(f'TESTE: {self.number_typed[1::1]}')
        for enum, n in enumerate(self.number_typed[1::1], start=1):
            if n == '0':
                inc += 1
        self._check_zero = False if inc == enum else True
        return self._check_zero

    def concatanation_number_in_word(self):
        # ====================================================================================================
        #  Quadrillions #9.000.000.000.000.000
        if self.validates['flag_quadrillion'] and self.place['quadrillions'] != 0:
            self.joins.append((str(unit_EN[self.place['quadrillions']] + ' ' + 'Quadrillion')))#Teste de 9.000.000.000.000.000
            #I will block the next condition(block the flag_hundred_trillion)
            self.validates['flag_hundred_trillion'] = self._check_zero
        # ====================================================================================================
        #  Hundred_trillions #999.000.000.000.000
        if self.validates['flag_hundred_trillion'] and self.place['hundred_trillions'] != 0:
            if self.place['hundred_trillions'] != 0:
                self.joins.append((str(unit_EN[self.place['hundred_trillions']] + ' ' + 'Hundred')))

            if self.tens_trillions_part <= 20:
                self.joins.append((str(unit_EN[self.tens_trillions_part] + ' ' + 'Trillion')))
                self.validates['flag_ten_trillion'] = False
                self.validates['flag_trillion'] = False

            if self.tens_trillions_part >= 21:
                self.joins.append((self.find_position_in_place(self.tens_trillions_part) + ' ' + 'Trillion'))
                self.validates['flag_ten_trillion'] = False
                self.validates['flag_trillion'] = False
        # ====================================================================================================
        #  Ten_trillons #99.000.000.000.000
        if self.validates['flag_ten_trillion'] and self.place['ten_trillions'] != 0:
            if self.tens_trillions_part <= 20:
                self.joins.append((str(unit_EN[self.tens_trillions_part] + ' ' + 'Trillion')))
                self.validates['flag_trillion'] = False

            if self.tens_trillions_part >= 21:
                self.joins.append(self.find_position_in_place(self.tens_trillions_part) + ' ' + 'Trillion')
                self.validates['flag_trillion'] = False
        # ====================================================================================================
        #  Trillions #9.000.000.000.000
        if self.validates['flag_trillion'] and self.place['trillions'] != 0:
            self.joins.append((str(unit_EN[self.place['trillions']] + ' ' + 'Trillion')))#Teste de 9.000.000.000.000
            #I will block the next condition(block the flag_hundred_billion)
            self.validates['flag_hundred_billion'] = self._check_zero
        # ====================================================================================================
        #  Hundred_billions #999.999.999.999
        if self.validates['flag_hundred_billion'] and self.place['hundred_billions'] != 0:
            if self.place['hundred_billions'] != 0:
                self.joins.append((str(unit_EN[self.place['hundred_billions']] + ' ' + 'Hundred')))

            if self.tens_billions_part <= 20:
                self.joins.append((str(unit_EN[self.tens_billions_part] + ' ' + 'Billion')))
                self.validates['flag_ten_billion'] = False
                self.validates['flag_billion'] = False

            if self.tens_billions_part >= 21:
                self.joins.append((self.find_position_in_place(self.tens_billions_part) + ' ' + 'Billion'))
                self.validates['flag_ten_billion'] = False
                self.validates['flag_billion'] = False
        # ====================================================================================================
        #  Ten_billions #99.999.999.999
        if self.validates['flag_ten_billion'] and self.place['ten_billions'] != 0:
            if self.tens_billions_part <= 20:
                self.joins.append((str(unit_EN[self.tens_billions_part] + ' ' + 'Billion')))
                self.validates['flag_billion'] = False

            if self.tens_billions_part >= 21:
                self.joins.append(self.find_position_in_place(self.tens_billions_part) + ' ' + 'Billion')
                self.validates['flag_billion'] = False
        # ====================================================================================================
        #  Billions #9.999.999.999
        if self.validates['flag_billion'] and self.place['billions'] != 0:
            self.joins.append((str(unit_EN[self.place['billions']] + ' ' + 'Billion')))
            #I will block the next condition(block the flag_hundred_billion)
            self.validates['flag_hundred_million'] = self._check_zero
        # ====================================================================================================
        #  Hundred_millions #999.999.999
        if self.validates['flag_hundred_million'] and self.place['hundred_millions'] != 0:
            self.joins.append((str(unit_EN[self.place['hundred_millions']] + ' ' + 'Hundred')))

            if self.tens_millions_part <= 20:#9_'99'.999.999
                self.joins.append((str(unit_EN[self.tens_millions_part] + ' ' + 'Million')))
                self.validates['flag_ten_million'] = False
                self.validates['flag_million'] = False

            if self.tens_millions_part >= 21:#9_'99'.999.999
                self.joins.append((self.find_position_in_place(self.tens_millions_part) + ' ' + 'Million'))
                self.validates['flag_ten_million'] = False
                self.validates['flag_million'] = False
        # ====================================================================================================
        #  Ten_millions #99.999.999
        if self.validates['flag_ten_million'] and self.place['ten_millions'] != 0:
            if self.tens_millions_part <= 20:#9_'9.9'99.999
                self.joins.append((str(unit_EN[self.tens_millions_part] + ' ' + 'Million')))
                self.validates['flag_million'] = False

            if self.tens_millions_part >= 21:
                self.joins.append((self.find_position_in_place(self.tens_millions_part) + ' ' + 'Million'))
                self.validates['flag_million'] = False
        # ==================================================================================================== 
        #  Millions #9.999.999
        if self.validates['flag_million'] and self.place['millions'] != 0:
            self.joins.append((str(unit_EN[self.place['millions']] + ' ' + 'Million')))

            #It means that the number after the first one are zeros
            #I will block the next condition(block the flag_hundred_billion)
            self.validates['flag_hundred_thousand'] = self._check_zero
        # ====================================================================================================
        #  Hundreds_thousands #100.000
        if self.validates['flag_hundred_thousand'] and self.place['hundred_thousands'] != 0:

            self.joins.append((str(unit_EN[self.place['hundred_thousands']] + ' ' + 'Hundred')))

            if self.tens_thousands_part <= 20:
                self.joins.append((str(unit_EN[self.tens_thousands_part] + ' ' + 'Thousand')))
                self.validates['flag_ten_thousand'] = False
                self.validates['flag_thousand'] = False
    
            if self.tens_thousands_part >= 21:
                self.joins.append((self.find_position_in_place(self.tens_thousands_part) + ' ' + unit_EN[unit_EN.index('Thousand')]))
                self.validates['flag_ten_thousand'] = False
                self.validates['flag_thousand'] = False
        # ====================================================================================================
        #  Ten_thousands #99.999
        if self.validates['flag_ten_thousand'] and self.place['ten_thousands'] != 0:
            if self.tens_thousands_part <= 20:
                self.joins.append((str(unit_EN[self.tens_thousands_part] + ' ' + 'Thousand')))

            if self.tens_thousands_part >= 21:
                self.joins.append((self.find_position_in_place(self.tens_thousands_part) + ' ' + 'Thousand'))
            
            self.validates['flag_thousand'] = False
        # ====================================================================================================
        #  Thousands #9.999
        if self.validates['flag_thousand'] and self.place['thousands'] != 0:
            #isso e uma possibilidade de troca de idioma
            self.joins.append((str(unit_EN[self.place['thousands']] + ' ' + 'Thousand')))

            #It means that the number after the first one are zeros
            #I will block the next condition(block the flag_hundred)
            self.validates['flag_hundred'] = self._check_zero
            self.validates['flag_decimal'] = self._check_zero
        # ====================================================================================================
        #  Hundreds #999
        if self.validates['flag_hundred'] and self.place['hundreds'] != 0:
            self.joins.append((str(unit_EN[self.place['hundreds']] + ' ' + 'Hundred')))
        # ====================================================================================================
        #  Tens #99
        if ((self.validates['flag_decimal'] or self.validates['flag_one']) and (self.place['tens'] != 0 or self.place['ones'] != 0)):
            
            if self.tens_part <= 19:
                self.joins.append(str(unit_EN[self.tens_part]))
            elif self.tens_part >= 20:
                #Go check the positions when the Tens Part is bigger than Twenty, you can see into the file Locate.py --> unit_EN
                #Specifc for this condition that formula is diferent from function calles (find_position_in_place)
                self.joins.append(str('{} {}'.format(unit_EN[(self.tens_part - (9 * (self.place['tens'] - 2))) - self.place['ones']], unit_EN[self.place['ones']] if self.place['ones'] != 0 else '')))
    #===================================================================================
    ########################        End Main Functions       ###########################
    #===================================================================================

    #************************************************************************************
    #************************************************************************************

    #===================================================================================
    ########################        Start Extra Functions       ###########################
    #===================================================================================
    def how_many_decimal_places(self):
        return self._decimal
    
    def str_number_in_word(self):
        joins = ', '.join(self.joins) 
        return joins

    def list_number_in_word(self):
        return self.joins
    
    def even_or_odd(self):
        result = int(self.number_typed) % 2
        return 'Even' if result == 0 else 'Odd'
    
    def bool_check_zeros(self):
        return self._check_zero
    
    def place_decimal(self):
        return self.place

        

    #===================================================================================
    ########################        End Extra Functions       ###########################
    #===================================================================================
    #************************************************************************************

