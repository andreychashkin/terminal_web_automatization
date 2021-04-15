import os

terminal_ip = "10.1.0.129"
# параметры вызова
protocol = ["H323", "SIP"]
speed = ["10240", "8192", "6144", "5120", "4608", "4096", "3584", "3072",
              "2560", "2048", "1536", "1024", "768", "512", "448", "384", "320", "256", "128", "64"]
resolution = ["4K 3840x2160", "FullHD 1920x1080", "HD 1280x720", "SVGA 800x600", "w576p 1024x576", "4CIF 704x576",
              "4SIF 704x480", "VGA 640x480", "w448p 768x448", "w288p 512x288", "CIF 352x288", "SIF 352x240",
              "QCIF 176x144", "QSIF 176x120"]
fps = ["1", "5", "10", "15", "24", "30", "60"]

# путь к файлу ролика
video = os.path.abspath("videos/test_video.mp4")

# данные для создания тестового контакта
test_number = "10.1.0.11"
test_name = 'test_contact'
test_protocol = ['auto', 'H323', 'SIP', 'SIP_TCP', 'SIP_TLS', 'LOCAL']