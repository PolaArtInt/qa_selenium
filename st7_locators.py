from selenium import webdriver

driver = webdriver.Chrome()

url = 'https://hyperskill.org/tracks'

driver.get(url)

# header:
header_title = ('xpath', '//div[contains(@class, "header-annual-banner")]')
header_text = ('xpath', '//div[contains(@class, "header-annual-banner")]//p')
header_price = ('xpath', '//b[@class="tw-font-bold"]')
header_btn = ('xpath', '//a[text()=" Buy now "]')
header_close_btn = ('xpath', '//button[@click-event-target="close"]')

# nav:
nav_main = ('xpath', '//nav[@id="header"]')
nav_signin_btn = ('xpath', '//button[text()=" Sign in "]')
nav_start_btn = ('xpath', '//button[text()="Start for free"]')
nav_icon = ('xpath', '(//*[contains(@data-component-name, "alt-logo-icon-hyperskill")])[1]')
nav_logo = ('xpath', '(//a[@class="nav-link"])[1]')
nav_dropdown = ('xpath', '//a[contains(@class, "dropdown")]')
nav_pricing = ('xpath', '(//a[@class="nav-link"])[2]')
nav_business = ('xpath', '(//a[@class="nav-link"])[3]')

# section main:
main_header = ('xpath', '//h1')
main_secondary_header = ('xpath', '//h2')
main_text = ('xpath', '//h2/following-sibling::p')
main_category_btns = ('xpath', '//div[contains(@class, "category")]/a')  # 19 btns list
main_category_btn = ('xpath', '(//div[contains(@class, "category")]/a)[1]')
main_category_btn_spans = ('xpath', '//span[@class="badge-count"]')  # 18 spans list
main_category_btn_span = ('xpath', '(//span[@class="badge-count"])[1]')

# card:
cards = ('xpath', '//div[@class="card-body"]')  # 69 cards list
card_badge = ('xpath', '(//div[@class="card-badges"])[1]')
card_title = ('xpath', '(//div[@class="card-body"]//h5)[1]')
card_rate_star = ('xpath', '(//*[@data-component-name="ph-star-fill"])[1]')
card_rate_num = ('xpath', '(//span[text()="Rating:"])[1]')
card_stats = ('xpath', '(//div[contains(@class, "track-statistics")])[1]')
card_stats_span = ('xpath', '((//div[contains(@class, "track-statistics")])[1]/span)[1]')
card_text = ('xpath', '(//span[contains(@class, "track-description")])[1]')
card_jet_logo = ('xpath', '(//img[@alt="JetBrains Academy"])[1]')
card_jet_desc = ('xpath', '(//*[contains(text(), " JetBrains Academy")])[1]')
card_stats_bottom = ('xpath', '(//div[contains(text(), " already learning")])[1]')

# footer:
footer_menu = ('xpath', '(//div[@class="category-col-links"])[2]')
footer_menu_link = ('xpath', '(//div[@data-component-name="TrackCategoryList"]//a)[1]')
footer_catalog_btn = ('xpath', '(//a[contains(text(), " Full catalog ")])[2]')
footer_nav = ('xpath', '(//)')
footer_nav_title_1 = ('xpath', '//footer//div[text()="Resources"]')
footer_nav_link_blog = ('xpath', '//footer//a[@click-event-target="blog"]')
footer_logo = ('xpath', '//a[@click-event-target="logo"]')

# social:
google_btn = ('xpath', '//a[@click-event-target="google-play"]')
app_store_btn =  ('xpath', '//a[@click-event-target="app-store"]')
fb_link = ('xpath', '//a[@click-event-target="Facebook"]')
insta_link = ('xpath', '//a[@click-event-target="Instagram"]')
youtube_link = ('xpath', '//a[@click-event-target="YouTube"]')
