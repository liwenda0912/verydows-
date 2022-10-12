import time
import unittest
import warnings
from selenium import webdriver
from 软件测试脚本.自动化项目.public.Login import Login
from selenium.webdriver.common.by import By


class buyThing(unittest.TestCase):
    def setUp(self) -> None:
        warnings.simplefilter('ignore', ResourceWarning)
        self.driver = webdriver.Chrome(executable_path="chromedriver")
        self.driver.maximize_window()
        Login().open1(self.driver)

    def test_select_buy(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/ul/li/a').click()  # 点击首页
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[2]/ul/li[1]').click()  # 点击第一个商品
        self.driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[13]/a[1]').click()  # 点击加入购物车
        self.driver.find_element(By.XPATH, '//*[@id="tocart-dialog"]/div/a[1]').click()  # 点击结算支付
        d = self.driver.find_element(By.XPATH, '//*[@id="cart"]/div[1]/table/tbody/tr[2]/td[2]/div/a').text  # 获取商品名称文本
        time.sleep(2)
        self.driver.find_element(By.XPATH, ' //*[@id="checkout-btn"]').click()  # 点击去结算
        self.driver.find_element(By.XPATH, ' //*[@id="consignee-list"]/li[2]/label/input').click()  # 选择发货地址
        self.driver.find_element(By.XPATH, '//*[@id="shipping_list"]/li[2]/label/input').click()  # 点击运送方式
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//*[@id="vdspopconfirm"]/div/button[1]').click()  # 点击确认
        m = self.driver.find_element(By.XPATH, '//*[@id="payment_list"]/li[2]/label').text  # 获取付款方式文本
        self.driver.find_element(By.XPATH, '//*[@id="payment_list"]/li[2]/label/input').click()  # 点击付款方式
        self.driver.find_element(By.XPATH, '//*[@id="order-form"]/div/a').click()  # 点击确认并提交订单
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/a').click()  # 点击立即付款
        win = self.driver.window_handles
        self.driver.switch_to.window(win[1])
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div/ul/li[1]/a').click()  # 查看订单
        time.sleep(2)
        # data = self.driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div/div/div[2]/div[1]/dl[3]').text
        data1 = self.driver.find_element(By.XPATH,
                                         '/html/body/div[4]/div[1]/div[2]/div/div/div[2]/div[1]/dl[4]/dd').text
        print(data1)
        data2 = self.driver.find_element(By.XPATH,
                                         '/html/body/div[4]/div[1]/div[2]/div/div/div[3]/table/tbody/tr[2]/td[2]/div/a').text
        self.assertEqual(d, data2)
        self.assertEqual(m, data1)

    def debug(self) -> None:
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
