$ Доброго времени суток user_name!
Это реализация аренды домов с помощью технологии блокчейн 

[+] Для начала работы перейдите в ДИРЕКТОРИЮ    ~/Contract

    1 Откройте PowerShell в этой директории испульзуя Shift + ПКМ
    2 Вставьте две команды приведённые ниже: 
                                            $  python.exe .\compile.py
                                            $  python.exe .\deploy.py
                                            
    3 Перейдите в ДИРЕКТОРИЮ ~/Network 
    4 Отроем PowerShell и впишем следующие две команды: 
    
                                            $  geth --datadir node1 init .\genesis.json 
                                            $  geth --datadir node2 init .\genesis.json 
                                            
      в файле config.json изменить IP-адрес на свой 
      свой Ip ты можешь узнать в командной строке командой $ ipconfig      
                    
                    
            "node1": {
                "ip": "192.168.43.111",
                             ^
                    сюда вставляй свой IP
                    
                    
    5 Перейдём в Каталог ~/bnode откроем PowerShell и впишем:
    
                                            $  python.exe .\start.py
    
    6 Вернитесь в Предыдущую Дерикторию и в папках node1 и node2 через PowerShell запустим 
    
                                            $  python.exe .\start.py
                                            
    7 Запускаем в Каталоге Contract майнер командой 
    
                                            $ python.exe .\miner.py
                                            выбираем 'yes'
                                            
    
    
    [+] Контракт запущен и готов к работе!
    
