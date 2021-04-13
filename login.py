import uiautomator2 as u2
import verification_code as verify

def open_url(device_no, target_url):
    ######open Chrome then insert url in searchbar/url bar
    d = u2.connect(device_no)
    target_url = target_url
    d.app_start(package_name='com.android.chrome', activity='com.google.android.apps.chrome.Main')
    d(resourceId='com.android.chrome:id/url_bar').set_text(target_url)
    d.press('enter')

def get_fields(d):
    ####get fields
    uname_field = d.xpath('//*[@text="商业版管理系统"]/android.view.View[3]/android.view.View[1]')
    pw_field = d.xpath('//*[@text="商业版管理系统"]/android.view.View[3]/android.view.View[2]')
    vc_field = d(textContains='验证码').down(className='android.widget.EditText') ##click verification string input area

def get_vc(d):
    img= 'captcha.jpeg'
    vc = d.screenshot(img)
    verifcation_string = verify.verification(vc)
    return(verification_string)

def fill_up(d,uname, pw,vc_string):
    ####form filling
    uname_field.set_text(uname)
    pw_field.set_text(pw)
    vc_field.set_text(vc_string)

def start(uname='admin', pw='admin123456', device_no='7b0c54dd', target_url='https://bot-w.uatcashieroffice.com/login'):
    d = u2.connect(device_no)
    open_url(device_no, target_url)
    while(d(textContains='请登录').exists()):
        get_fields(d)
        vc_string = get_vc(d)
        fill_up(d,uname, pw, vc_string)
        submit_btn = d(textContains='登 录').click()