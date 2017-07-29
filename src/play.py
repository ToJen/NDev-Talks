from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time, random

driver = webdriver.Chrome('./assets/chromedriver')
driver.get('https://gabrielecirulli.github.io/2048/')

time.sleep(2)	# wait for page to load

gameElem = driver.find_element_by_class_name('grid-container')

directions = [Keys.UP, Keys.DOWN, Keys.RIGHT, Keys.LEFT]

ActionChains(driver).move_to_element_with_offset(gameElem, 0, 50).perform()

time.sleep(3)

# TODO: use some algorithm to decide which direction to move to
# def choose_next_move():


def print_current_tiles(curr_round):
	tiles = driver.find_elements_by_class_name('tile')
	for tile in tiles:
		print(curr_round, ": ", tile.text, end=" ")

def is_over(browser):
	try:
		game_over = browser.find_element_by_class_name('game-over')
		return game_over
	except:
		# print("not over yet")
		pass


game_ended = False #set flag if game has ended
i = 0
while not game_ended:
	game_ended = is_over(driver)
	
	if game_ended:
		print('game over boi!')
		i += 1
		game_ended = True if (i==2) else False
		time.sleep(3)
		restartElem = driver.find_element_by_link_text('Try again')
		restartElem.click()
		# print('restarting...')

	for direction in directions:
		choice = random.choice(direction)
		# print_current_tiles(i)
		ActionChains(driver).send_keys(choice).perform()
