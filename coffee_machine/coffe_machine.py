class CoffeeMachine:
    """
    Class attributes
    ----------------
    stages_of_coffee_brewing : multiline str
    no_type_coffee: dict
    espresso: dict
    latte: dict
    cappuccino: dict
    coffee_machine_res: dict
    coffee_type_list: dict
    current_state: list
    
    Attributes
    ----------
    **kwargs - The keyword arguments are used for coffee machine's resources 
             {"water" : int, "milk": int, "coffee_beans" : int, "coffee_money": int, "cup": int, "available_water": int,
            "available_milk": int, "available_coffee_beans": int,"disposable_cups": int, "money": int}

    """
    stages_of_coffee_brewing = '''Starting to make a coffee 
Grinding coffee beans 
Boiling water 
Mixing boiled water with crushed coffee beans 
Pouring coffee into the cup 
Pouring some milk into the cup 
Coffee is ready!'''
    no_type_coffee = {"water": 200, "milk": 50, "coffee_beans": 15}
    espresso = {"water": 200, "milk": 50, "coffee_beans": 15, "coffee_money": 4}
    latte = {"water": 350, "milk": 75, "coffee_beans": 20, "coffee_money": 7}
    cappuccino = {"water": 200, "milk": 100, "coffee_beans": 12, "coffee_money": 6}
    coffee_type_list = {"1": espresso, "2": latte, "3": cappuccino}
    coffee_machine_res = {"available_water": 400, "available_milk": 540, "available_coffee_beans": 120,
                          "disposable_cups": 9, "money": 550}
    current_state = {}

    def __init__(self, **kwargs):
        """
        Constructs all the necessary attributes for the coffee machine object.
        :param kwargs: The keyword arguments are used for coffee machine's resources
            {"water" : int, "milk": int, "coffee_beans" : int, "coffee_money": int, "cup": int, "available_water": int,
            "available_milk": int, "available_coffee_beans": int,"disposable_cups": int, "money": int}
        """
        self.water = kwargs.get("water", 0)
        self.milk = kwargs.get("milk", 0)
        self.coffee_beans = kwargs.get("coffee_beans", 0)
        self.coffee_money = kwargs.get("coffee_money", 0)
        self.cup = kwargs.get("cup", 0)
        self.available_water = kwargs.get("available_water", 0)
        self.available_milk = kwargs.get("available_milk", 0)
        self.available_coffee_beans = kwargs.get("available_coffee_beans", 0)
        self.disposable_cups = kwargs.get("disposable_cups", 0)
        self.money = kwargs.get("money", 0)

    def get_stage_of_coffee_brewing(self):
        """
        Prints stages_of_coffee_brewing
        :return: None
        """
        print(self.stages_of_coffee_brewing)

    def calculate_coffee_resources(self):
        """
        Calculates coffee resources when user input cup value
        CoffeeMachine(*args) should be defined
        :return: None
        """
        self.cup = int(input("Write how many cups of coffee you will need: "))
        print(f'''For {self.cup} cups of coffee you will need: 
        {self.cup * self.water} ml of water 
        {self.cup * self.milk} ml of milk 
        {self.cup * self.coffee_beans} g of coffee beans''')

    def calculate_coffee_availability(self):
        """
        Calculates and returns how many cups of coffee Coffee Machine can make
        Coffee Machine(**kwargs) should be defined
        :return: int
        """
        available_res_list = [self.available_water, self.available_milk, self.available_coffee_beans]
        cup_res_list = [self.water, self.milk, self.coffee_beans]
        cup_count_list = []
        for cr in range(len(cup_res_list)):
            if cup_res_list[cr] != 0:
                cup_count_list.append(available_res_list[cr] // cup_res_list[cr])
        return min(cup_count_list)

    def get_coffee_availability_text(self, stage=None):
        """
        Prints coffee availability message
        Coffee Machine(**kwargs) should be defined
        :param stage: int, 3 or None
        :return: srt (if stage !=3) "Yes" or "No"
        """
        if stage == 3:
            self.available_water = int(input("Write how many ml of water the coffee machine has: "))
            self.available_milk = int(input("Write how many ml of milk the coffee machine has: "))
            self.available_coffee_beans = int(input("Write how many grams of coffee beans the coffee machine has: "))
            self.cup = int(input("Write how many cups of coffee you will need: "))
            cup_count = self.calculate_coffee_availability()
            if cup_count == self.cup:
                print("Yes, I can make that amount of coffee")
            elif cup_count > self.cup:
                extra_coffee = cup_count - self.cup
                print(f"Yes, I can make that amount of coffee (and even {extra_coffee} more than that)")
            else:
                print(f"No, I can make only {cup_count} cups of coffee")
        else:
            cup_count = self.calculate_coffee_availability()
            if cup_count > 0:
                print("I have enough resources, making you a coffee!")
                return "Yes"
            else:
                if self.available_water - self.water < 0:
                    print("Sorry, not enough water!")
                elif self.available_milk - self.milk < 0:
                    print("Sorry, not enough milk!")
                elif self.available_coffee_beans - self.coffee_beans < 0:
                    print("Sorry, not enough coffee beans!!")
                return "No"

    def coffee_machine_has(self):
        """
        Prints current Coffee Machine resources
        :return: None
        """
        print(f'''The coffee machine has:
        {self.available_water} of water
        {self.available_milk} of milk
        {self.available_coffee_beans} of coffee beans
        {self.disposable_cups} of disposable cups
        {self.money} of money''')

    def set_coffee_type_values(self, coffee_type):
        """
        Set CoffeeMachine(*args) by coffee type
        :param coffee_type: str, "1" or "2" or "3"
        :return: None
        """
        self.water = self.coffee_type_list[coffee_type]["water"]
        self.milk = self.coffee_type_list[coffee_type]["milk"]
        self.coffee_beans = self.coffee_type_list[coffee_type]["coffee_beans"]
        self.coffee_money = self.coffee_type_list[coffee_type]["coffee_money"]

    def buy_coffee(self, coffee_type):
        """
        Sets coffee values by coffee type -> set_coffee_type_values(coffee_type)
        Prints regarding coffee availability message -> get_coffee_availability_text()
        Get str from get_coffee_availability_text(), if "Yes":
            Subtracts corresponding coffee from Coffee Machine resources
            Subtracts disposable cup from Coffee Machine
            Adds money in Coffee Machine resources
        :param coffee_type: str , "1" or "2" or "3"
        :return: None
        """
        self.set_coffee_type_values(coffee_type)
        ready = self.get_coffee_availability_text()
        if ready == "Yes":
            self.available_water -= self.water
            self.available_milk -= self.milk
            self.available_coffee_beans -= self.coffee_beans
            self.money += self.coffee_money
            self.disposable_cups -= 1

    def coffee_machine_action_for_stage_4_5(self, action, buy_text):
        """
        Asks user choose action (buy, fill, take, remaining, exit).
                buy: Asks user choose type of coffee and after use buy_coffee(coffee_type) method
                fill: Increases Coffee Machine resources (water, milk, coffee beans and disposable cups)
                 regarding user's input
                take: Subtracts Coffee Machine money and prints corresponding text
                remaining: Prints current Coffee Machine resources -> coffee_machine_has()
        :param buy_text: str, corresponding text for different tasks
        :return: None
        """
        if action == "buy":
            coffee_type = input(f"What do you want to buy? {buy_text}: ")
            if coffee_type == "back":
                return "back"
            else:
                self.buy_coffee(coffee_type)
        elif action == "fill":
            self.available_water += int(input("Write how many ml of water you want to add: "))
            self.available_milk += int(input("Write how many ml of milk you want to add: "))
            self.available_coffee_beans += int(input("Write how many grams of coffee beans you want to add: "))
            self.disposable_cups += int(input("Write how many disposable coffee cups you want to add: "))
        elif action == "take":
            print(f"I gave you {self.money}")
            self.money = 0
        elif action == "remaining":
            self.coffee_machine_has()
        elif action == "exit":
            return "exit"

    def save_input(self, user_input, key_name):
        """
        Saves user input in current_state = {"key_name": user_input}
        :param user_input:
        :param key_name:
        :return: None
        """
        self.current_state[key_name] = user_input
        print(f"Current state: {self.current_state}")

    def do_action(self, string_from_current):
        """
        Gets str from current_state and do corresponding things (buy, fill, take, remaining)
        :param string_from_current: str
        :return: None
        """
        if string_from_current == "buy":
            if self.current_state["buy_option"] in self.coffee_type_list.keys():
                self.buy_coffee(self.current_state["buy_option"])
        elif string_from_current == "fill":
            self.available_water += self.current_state["water"]
            self.available_milk += self.current_state["milk"]
            self.available_coffee_beans += self.current_state["coffee_beans"]
            self.disposable_cups += self.current_state["disposable_cups"]
        elif string_from_current == "take":
            print(f"I gave you {self.money}")
            self.money = 0
        elif string_from_current == "remaining":
            self.coffee_machine_has()


print("--------------------------------------------------STAGE 1")
coffee_stage1 = CoffeeMachine()
coffee_stage1.get_stage_of_coffee_brewing()

print("--------------------------------------------------STAGE 2")
coffee_stage2 = CoffeeMachine(**CoffeeMachine.no_type_coffee)
coffee_stage2.calculate_coffee_resources()

print("--------------------------------------------------STAGE 3")
coffee_stage3 = CoffeeMachine(**CoffeeMachine.no_type_coffee)
coffee_stage3.get_coffee_availability_text(3)

print("--------------------------------------------------STAGE 4")
coffee_stage4 = CoffeeMachine(**CoffeeMachine.coffee_machine_res)
coffee_stage4.coffee_machine_has()
buy_string = "1 - espresso, 2 - latte, 3 - cappuccino"
get_action = input("Write action (buy, fill, take): ")
coffee_stage4.coffee_machine_action_for_stage_4_5(get_action, buy_string)
coffee_stage4.coffee_machine_has()

print("--------------------------------------------------STAGE 5")
coffee_stage5 = CoffeeMachine(**CoffeeMachine.coffee_machine_res)
buy_string = "1 - espresso, 2 - latte, 3 - cappuccino, back"
while True:
    get_action = input("Write action (buy, fill, take, remaining, exit): ")
    action = coffee_stage5.coffee_machine_action_for_stage_4_5(get_action, buy_string)
    if action == "back":
        continue
    elif action == "exit":
        break

print("--------------------------------------------------STAGE 6")
coffee_stage6 = CoffeeMachine()

input_text = {"action": "Write action (buy, fill, take, remaining, exit): ",
              "buy options": "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back: ",
              "fill water": "Write how many ml of water you want to add: ",
              "fill milk": "Write how many ml of milk you want to add: ",
              "fill coffee beans": "Write how many grams of coffee beans you want to add: ",
              "fill disposable cups": "Write how many disposable coffee cups you want to add: "}

while True:
    coffee_stage6.current_state = {}
    coffee_stage6.save_input(input(input_text["action"]), "action")

    if coffee_stage6.current_state["action"] == "back":
        continue
    elif coffee_stage6.current_state["action"] == "exit":
        break
    elif coffee_stage6.current_state["action"] == "buy":
        coffee_stage6.save_input(input(input_text["buy options"]), "buy_option")
    elif coffee_stage6.current_state["action"] == "fill":
        coffee_stage6.save_input(int(input(input_text["fill water"])), "water")
        coffee_stage6.save_input(int(input(input_text["fill milk"])), "milk")
        coffee_stage6.save_input(int(input(input_text["fill coffee beans"])), "coffee_beans")
        coffee_stage6.save_input(int(input(input_text["fill disposable cups"])), "disposable_cups")

    coffee_stage6.do_action(coffee_stage6.current_state["action"])

print("--------------------------------------------------STAGE 7")
print("Checking docstrings")
print(CoffeeMachine.__doc__)
print("-----------------------------------")
help(CoffeeMachine)
