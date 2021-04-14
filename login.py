import uiautomator2 as u2
import cv2
import pytesseract
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s')
log = logging.getLogger('login.bot')
d = u2.connect('7b0c54dd')


def verification(vc_img):
    img = cv2.imread(vc_img, 0)
    _, th1 = cv2.threshold(img, 30, 255, cv2.THRESH_BINARY)
    vc_string = pytesseract.image_to_string(th1, lang='eng')

    return(vc_string)

def open_url(target_url):
    ######open Chrome then insert url in searchbar/url bar    
    d.app_start(package_name='com.android.chrome', activity='com.google.android.apps.chrome.Main')
    target_url = target_url    
    d(resourceId='com.android.chrome:id/url_bar').set_text(target_url)
    d.press('enter')
    d.implicitly_wait(10)

def get_fields():
    ####get fields
    uname_field = d.xpath('//*[@text="商业版管理系统"]/android.view.View[3]/android.view.View[1]')
    pw_field = d.xpath('//*[@text="商业版管理系统"]/android.view.View[3]/android.view.View[2]')
    vc_field = d.xpath('//*[@text="商业版管理系统"]/android.view.View[3]/android.view.View[3]/android.widget.EditText[1]') ##click verification string input area
    return(uname_field, pw_field,vc_field)

def get_vc():
    img= 'captcha.jpeg'
    vc = d.screenshot(img)
    result = verification(vc)
    return(result.strip())

def fill_up(uname, pw,vc_string):
    ####form filling
    uname_field, pw_field, vc_field = get_fields()
    uname_field.set_text(uname)
    pw_field.set_text(pw)
    vc_field.set_text(vc_string.strip())

def start(uname='admin', pw='admin123456', device_no='7b0c54dd', target_url='https://bot-w.uatcashieroffice.com/login'):
    d = u2.connect(device_no)
    open_url(target_url)
    if(d(textContains='请登录').exists(timeout=5)):
        if(d(textContains='验证码').exists(timeout=5)):
            vc_string = get_vc()
            fill_up(uname, pw, vc_string)

def login_loop():
    d = u2.connect('7b0c54dd')
    d.unlock()
    open_url('https://bot-w.uatcashieroffice.com/login')
    count=0
    while(d(textContains="请登录")):
        count +=1
        if(d(resourceId="captcha_img").exists(timeout=10)):
            start()
            d(textContains='登 录').click()
            if(d(textContains='登 录').wait_gone(timeout=3.0)):
                log.info("login success! Retries: " + str(count))