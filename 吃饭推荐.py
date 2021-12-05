from pyknow import *
import graphviz
import pyknow.matchers
from random import choice

breakfast = ''
lunch = ''
snacks = ''
dinner = ''

class MyDietician(KnowledgeEngine):
    #def __init__(self, *args, **kwargs):
     #   super(self, args, kwargs)
        #self.breakfast = ''
        #self.lunch = ''
        #self.snacks = ''
        #self.dinner = ''

    @Rule(mass(calorie=P(lambda calorie:calorie>=1190)&P(lambda calorie:calorie<=1290),preference='Veg'))
    def calorie_a(self):
        global breakfast,lunch,snacks,dinner
        breakfast = 'Oatmeal dry+Milk+Apple'
        lunch = 'Brown Rice 1 cup (195 gm) + Mixed Vegetables 1/2 cup + Salad 1 bowl + Raita 1 small bowl'
        snacks = 'Popcorn+blacktea'
        dinner = '2 Rotis + Vegetable Soup 1 bowl + Salad 1 bowl'


    @Rule(mass(calorie=P(lambda calorie: calorie >= 1190) & P(lambda calorie: calorie <= 1290), preference='Non-veg'))
    def calorie_aa(self):
        global breakfast,lunch,snacks,dinner
        breakfast = 'Tea without Sugar + 2 Biscuits+Fruit'
        lunch = 'Cooked Rice/Plain(1 cup)+Dal+Curry(meat)+Pickle'
        snacks = 'Tuna(with light mayonnaise,celery and pickles) +Basic Protein Shake'
        dinner = '2 Roti + Lentils Dal 1/2 cup+ Raita 1 small bowl'


    @Rule(mass(calorie=P(lambda calorie: calorie >= 1291) & P(lambda calorie: calorie <= 1399), preference='Veg'))
    def calorie_b(self):
        global breakfast, lunch, snacks, dinner
        breakfast = 'Buttered Toast + Fruits + Tea / Coffee'
        lunch = 'Plain Rice + dal + veg curry + pickle'
        snacks = 'Porridge + Nuts(fried) + Waffers'
        dinner = 'Roasted veggies + Paratha / Nan'


    @Rule(mass(calorie=P(lambda calorie: calorie >= 1291) & P(lambda calorie: calorie <= 1399), preference='Non-veg'))
    def calorie_bb(self):
        global breakfast, lunch, snacks, dinner
        breakfast = 'Thick slice of one whole grain toast +Raspberry Jam +One whole egg +Green tea ( or coffee)+1 piece of fruit'
        lunch = 'Green vegetables (100g.)+cooked rice+papad+pickle+curry(meat)'
        snacks = 'Sandwich/hamburger+fruit juice'
        dinner = 'Medium grilled salmon+Half cup of brown rice+Lightly stir-fried vegetables+Cranberry(or any you prefer) sauce+A piece of fruit'

    @Rule(mass(calorie=P(lambda calorie: calorie >= 1400) & P(lambda calorie: calorie <= 1499), preference='Veg'))
    def calorie_c(self):
        global breakfast, lunch, snacks, dinner
        breakfast ='Biscuits + Skimmed milk with sugar+Fruits+Nuts'
        lunch='Vegetable brown rice pulav+Carrot raita+ Mix veg salad'
        snacks='Spaghetti with sauce+fresh juice'
        dinner='Curd+Chapati+Veg curry+sliced cucumber'

    @Rule(mass(calorie=P(lambda calorie: calorie >= 1400) & P(lambda calorie: calorie <= 1499), preference='Non-veg'))
    def calorie_cc(self):
        global breakfast, lunch, snacks, dinner
        breakfast = 'Oatmeal and Eggs+fruits'
        lunch = 'Chicken and Broccoli Over Pasta'
        snacks = 'Chinese noodles+tea/coffee(without sugar)'
        dinner = 'mixed greens+ cooked chicken breast+ medium red bell pepper, sliced+grated carrots'

    @Rule(mass(calorie=P(lambda calorie: calorie >= 1500) & P(lambda calorie: calorie <= 1599), preference='Veg'))
    def calorie_d(self):
        global breakfast, lunch, snacks, dinner
        breakfast = 'Shredded Wheat Cereal - 1 cup +Skimmed Milk(1½ cups)+Fruits'
        lunch = 'Brown Rice 1 cup (195 gm) + Mixed Vegetables 1/2 cup + Salad 1 bowl + Raita 1 small bowl'
        snacks = 'Natural peanut butter (1 tablespoon )+brown bread +Fruit smootie'
        dinner = 'Vegetable Salad/Soup + 2 small Chapatis with dal or vegetable curry + 1 cup (150ml) curd made from double toned milk.'

    @Rule(mass(calorie=P(lambda calorie: calorie >= 1500) & P(lambda calorie: calorie <= 1599), preference='Non-veg'))
    def calorie_dd(self):
        global breakfast, lunch, snacks, dinner
        breakfast = '2 Scrambled Eggs + 1 Slice Brown Bread+ Skimmed Milk 1 cup'
        lunch = 'Brown Rice+Grilled Chicken Breast+Green Beans+curd+papad'
        snacks = '1 cup fruit smoothie and 5 almonds + hamburger/sandwich'
        dinner = 'Spaghetti & meat, sauce etc..'

    @Rule(mass(calorie=P(lambda calorie: calorie >= 1600) & P(lambda calorie: calorie <= 1699), preference='Veg'))
    def calorie_e(self):
        global breakfast, lunch, snacks, dinner
        breakfast = 'Boiled egg and toast with fruit+1 hard boiled egg with 2 slices wholemeal toast topped with 2tsp low-fat spread. Plus 1 small glass of orange juice and 6 grapes.'
        lunch = 'Plain Rice+dal+veg curry+pickle'
        snacks = ' apple +½ cup cottage cheese +2 chocolate chip cookies+Protien shake'
        dinner = 'Three bean salad: 3 spring onions+5 cherry tomatoes+ 1 green pepper+3tbsp each of red kidney beans,chick peas and cannelini beans. Serve with salad and 1 wholemeal bread roll topped with 2tsp low-fat spread'

    @Rule(mass(calorie=P(lambda calorie: calorie >= 1600) & P(lambda calorie: calorie <= 1699), preference='Non-veg'))
    def calorie_ee(self):
        global breakfast, lunch, snacks, dinner
        breakfast = 'Boiled egg and toast with fruit+1 hard boiled egg with 2 slices wholemeal toast topped with 2tsp low-fat spread. Plus 1 small glass of orange juice and 6 grapes.'
        lunch = 'Plain Rice+dal+veg curry+pickle'
        snacks = ' apple +½ cup cottage cheese +2 chocolate chip cookies+Protien shake'
        dinner = 'Three bean salad: 3 spring onions+5 cherry tomatoes+ 1 green pepper+3tbsp each of red kidney beans,chick peas and cannelini beans.'

    @Rule(mass(calorie=P(lambda calorie: calorie >= 1700) & P(lambda calorie: calorie <= 1899), preference='Veg'))
    def calorie_f(self):
        global breakfast, lunch, snacks, dinner
        breakfast = 'One cup cooked oatmeal with two tablespoons of light cream and one teaspoon brown sugar; two light sausages; one grapefruit with two teaspoons white sugar.'
        lunch = 'Brown rice+dal/vegetable curry+pickle+papad'
        snacks = 'Tea/coffee+suzi ko halwa'
        dinner = 'Vegetable Salad/Soup + 2 small Chapatis with dal or vegetable curry + 1 cup (150ml) curd made from double toned milk.'


    @Rule(mass(calorie=P(lambda calorie: calorie >= 1700) & P(lambda calorie: calorie <= 1899), preference='Non-veg'))
    def calorie_ff(self):
        global breakfast, lunch, snacks, dinner
        breakfast = '2 slices of whole grain toast, 2 tablespoons of butter, 2 hardboiled eggs, 1/2 cup melon, 170 ml orange juice'
        lunch = '1 cup cooked brown rice, 85 grams baked or roasted chicken breast, salad made with lettuce, carrots, onions, tomatoes and olives'
        snacks = '1/2 cup of mixed nuts and dried fruits,1 cup low-fat yogurt, 1/2 cup fresh or frozen berries'
        dinner = '115 grams of roasted chicken breast, 140 grams of baked sweet potato topped with 1 teaspoon of butter, 1/2 cup steamed broccoli.'


    @Rule(mass(calorie=P(lambda calorie: calorie >= 1900) & P(lambda calorie: calorie <= 1999), preference='Veg'))
    def calorie_g(self):
        global breakfast, lunch, snacks, dinner
        breakfast = 'Oatmeal with brown sugar+ 1 cup of milk+fruits+ 1 whole wheat toast with 1 teaspoon of butter.'
        lunch = 'Plain rice+dal+curd+vegetable curry+salad'
        snacks = '1 cup coffee made with skim milk+ fat-free strained yogurt+1/4 cup oat honey granola to add to the yogurt'
        dinner = '1 whole wheat roti (6 inches diameter)+chana masala	+ alu gobhi+cucumber and tomato raita'

    @Rule(mass(calorie=P(lambda calorie: calorie >= 1900) & P(lambda calorie: calorie <= 1999), preference='Non-veg'))
    def calorie_gg(self):
        global breakfast, lunch, snacks, dinner
        breakfast = 'toasted whole grain / high fiber bread+1 egg white omelet with chopped spinach, red capsicum (bell pepper), onions & green chillies+1 cup coffee/tea made with skim milk..'
        lunch = 'vegetables+whole grains+1 cup of brown rice+grilled skinless chicken breast'
        snacks = 'Steak and salad+milkshake'
        dinner = 'Roti + Fish(50 gm) + Lentils Dal 1/2 cup+ Raita 1 small bowl'

    @Rule(mass(calorie=P(lambda calorie: calorie >= 2000) & P(lambda calorie: calorie <= 2099), preference='Veg'))
    def calorie_h(self):
        global breakfast, lunch, snacks, dinner
        breakfast = 'Oatmeal with Fruit & Nuts:oatmeal cooked + cup skim milk+medium apple, diced+ chopped walnuts'
        lunch = 'cup rice+dal tadka (masoor)+ palak paneer+curd'
        snacks = 'Apple(or any fruit)+10 walnut halves+cheese(cheddar)'
        dinner = 'wheat roti+ moong sprouts+  cabbage(any other veggies)+cucumber and tomato raita'


    @Rule(mass(calorie=P(lambda calorie: calorie >= 2000) & P(lambda calorie: calorie <= 2099), preference='Non-veg'))
    def calorie_hh(self):
        global breakfast, lunch, snacks, dinner
        breakfast = 'cooked oatmeal + almonds +  raisins + low-fat milk'
        lunch = 'tofu cooked with 1 teaspoon of oil +brown rice + steamed broccoli'
        snacks = '1 cup low fat yogurt + 1 apple(any fruit)+mixed nuts+1 cup of orange juice'
        dinner = '3 ounces of grilled chicken breast + spinach +whole grain bread(2 slices)'

    @Rule(mass(calorie=P(lambda calorie: calorie >= 2100) & P(lambda calorie: calorie <= 2199), preference='Veg'))
    def calorie_i(self):
        global breakfast, lunch, snacks, dinner
        breakfast = 'oats with slices of 1 medium banana and 6 to 7 walnut halves+1 cup coffee/tea made with skim milk'
        lunch = 'Plain Rice+dal+veg curry+pickle+papad+ghee'
        snacks = 'Fruit juice+sandwich/burger+fried nuts+wafers'
        dinner = 'Brown rice+ Potato, lentil and cauliflower curry+pickle+papad'


    @Rule(mass(calorie=P(lambda calorie: calorie >= 2200) & P(lambda calorie: calorie <= 2299), preference='Veg'))
    def calorie_j(self):
        global breakfast, lunch, snacks, dinner
        breakfast = 'Coffee/tea+cottage cheese+cream+bread slices+fruits'
        lunch = 'Brown Rice 1 cup (195 gm) + Mixed Vegetables 1/2 cup + Salad 1 bowl + Raita 1 small bowl+papad+pickle+dal'
        snacks = '2 chocolate chip cookies+Banana smoothie+nuts+fries'
        dinner = '2 Rotis + Vegetable Soup 1 bowl + Salad 1 bowl+curd'


    @Rule(mass(calorie=P(lambda calorie: calorie >= 2200) & P(lambda calorie: calorie <= 2299), preference='Non-veg'))
    def calorie_jj(self):
        global breakfast, lunch, snacks, dinner
        breakfast = '1 whole egg + 4 egg whites (scrambled)+ toasted whole grain Muffin+1 cup plain nonfat yogurt topped with:1 banana, sliced'
        lunch = '5 ounces  firm tofu+ 3 ounces  chicken breast+broccoli florets+fresh spinach leaves+  Season with soy sauce, garlic, pepper and ginger+½ cup  steamed brown rice+½ medium mango'
        snacks = '½ cup vanilla yogurt+1 cup baby carrots+fruit juice'
        dinner = '8 ounces grilled shrimp+brown rice+2 cups chopped mixed vegetables (tomatoes, peppers, carrots, cucumber, onion)+leafy greens'

    @Rule(mass(calorie=P(lambda calorie: calorie >= 2300) & P(lambda calorie: calorie <= 2399), preference='Veg'))
    def calorie_k(self):
        global breakfast, lunch, snacks, dinner
        breakfast = '4slices wholemeal toast topped with 1tbsp peanut butter+fruit.+coffee/tea'
        lunch = 'Plain Rice+dal+veg curry+pickle+kwati+salad'
        snacks = 'Veg Pizza+Milk Shake+fried nuts '
        dinner = 'Chinese noodles/fried rice+juice'


    @Rule(mass(calorie=P(lambda calorie: calorie >= 2300) & P(lambda calorie: calorie <= 2399), preference='Non-veg'))
    def calorie_kk(self):
        global breakfast, lunch, snacks, dinner
        breakfast = '4slices wholemeal toast topped with 1tbsp peanut butter+fruit.+coffee/tea'
        lunch = 'Chicken breast(white meat)+rice steamed+salad (tomato,onion)+ Roasted chickpeas+soup'
        snacks = 'Bread slice+jelly(any fruit flavor)+peanut butter+fruit juice'
        dinner = 'Coronation chicken with sweetcorn:1 grilled skinless chicken breast+3tbsp sweetcorn+2tbsp yogurt+1 tbsp reduced-calorie mayonnaise+1tsp curry powder (or to taste). Serve with 1 jacket potato and salad'

    @Rule(mass(calorie=P(lambda calorie: calorie >= 2400) & P(lambda calorie: calorie <= 2499), preference='Veg'))
    def calorie_l(self):
        global breakfast, lunch, snacks, dinner
        breakfast = 'cooked oatmeal+ mixed raisins and almonds+1 cup low-fat milk'
        lunch = ' 1 cup cooked brown rice+ 1.5 cups steamed broccoli+1 cup tofu or cottage cheese curry cooked with 1 tablespoon vegetable oil'
        snacks = '1 cup low-fat yogurt, 1 cup sliced apples+20 grams dry roasted peanuts'
        dinner = '2 whole grain bread slices+grilled mushroom/tofu+2 cups of leafy green vegetables'

    @Rule(mass(calorie=P(lambda calorie: calorie >= 2400) & P(lambda calorie: calorie <= 2499), preference='Non-veg'))
    def calorie_ll(self):
        global breakfast, lunch, snacks, dinner
        breakfast = '1.5 cups of Raisin bran Cereal + 1.5 cups of non-fat milk+1 tablespoon of peanut butter +fruits'
        lunch = ' 1 Skinless chicken breast + 1.5 cups of cooked brown rice'
        snacks = '1 banana (any fruit)+pizza/burger'
        dinner = '2 whole grain bread slices + 1 roasted chicken breast'

    @Rule(mass(calorie=P(lambda calorie: calorie >= 2500) & P(lambda calorie: calorie <= 2599), preference='Veg'))
    def calorie_m(self):
        global breakfast, lunch, snacks, dinner
        breakfast = 'Buttered toast(2)+protein shake'
        lunch = ' Jeera rice+spinach salad+veg curry+curd'
        snacks = 'Cheese slices+popcorn+brown butter with lemon+veg cutlet'
        dinner = 'Pan pasta + fried corn and onions'

    @Rule(mass(calorie=P(lambda calorie: calorie >= 2500) & P(lambda calorie: calorie <= 2599), preference='Non-veg'))
    def calorie_mm(self):
        global breakfast, lunch, snacks, dinner
        breakfast = '1 ½ cups of 1% fat cottage cheese+fruit cocktail+ coffee, no sugar'
        lunch = ' chicken breast + peaches(sliced) + cornstarch + ginger + chestnuts + rice + peas +olive oil'
        snacks = '2 slices of bread+4 teaspoons of jelly + 2 tablespoons of peanut(or any) butter'
        dinner = 'chicken breast+ steamed white rice+ garden salad with tomato and onion+ 1/2 cup mayonnaise+ cheese/dried fruits'

    @Rule(mass(calorie=P(lambda calorie: calorie >= 2600) & P(lambda calorie: calorie <= 2699), preference='Veg'))
    def calorie_n(self):
        global breakfast, lunch, snacks, dinner
        breakfast = 'cookies + milk shake + fruits'
        lunch = ' Black beans + sweet potato+ Plain roti + raita + palak paneer+green salad'
        snacks = 'Cheese slices+popcorn+brown butter with lemon+veg cutlet'
        dinner = 'Pan pasta + fried corn and onions'

    @Rule(mass(calorie=P(lambda calorie: calorie >= 2600) & P(lambda calorie: calorie <= 2699), preference='Non-veg'))
    def calorie_nn(self):
        global breakfast, lunch, snacks, dinner
        breakfast = 'Oatmeal with skim milk +almonds+fruits+coffee/tea'
        lunch = 'Brown rice+baked fish+cauliflower+lettuce salad'
        snacks = 'Fat free cookies+yogurt+wheat crackers'
        dinner = 'Baked chicken breast+mashed potatoes+steamed broccoli'

    @Rule(mass(calorie=P(lambda calorie: calorie >= 2700) & P(lambda calorie: calorie <= 2799), preference='Veg'))
    def calorie_o(self):
        global breakfast, lunch, snacks, dinner
        breakfast = 'Skimmed Milk with cornflakes + fruits + soaked almonds+milk shake '
        lunch = ' Vegetable stuffed paratha(2)+curd+sprout salad+pickle '
        snacks = ' veg spaghetti+veggie wrap+juice '
        dinner = 'Biryani+lassi+spinach '

    @Rule(mass(calorie=P(lambda calorie: calorie >= 2700) & P(lambda calorie: calorie <= 2799),preference='Non-veg'))
    def calorie_oo(self):
        global breakfast, lunch, snacks, dinner
        breakfast = '4 whole eggs, scrambled + 1 slice cheddar cheese + 2 slices whole-wheat toast +1/4 cup sliced avocado '
        lunch = ' chicken breast + chopped broccoli, steamed +curd+ long-grain brown rice+salad '
        snacks = ' natural peanut butter +apple +Greek yogurt+bread slices '
        dinner = 'chicken breast + white rice + bell pepper + Green onion + onion + mushrooms + 2 tbsp soy sauce + egg'

    @Rule(mass(calorie=P(lambda calorie: calorie >= 2800) & P(lambda calorie: calorie <= 2899),preference='Veg'))
    def calorie_p(self):
        global breakfast, lunch, snacks, dinner
        breakfast = 'cooked oatmeal with 1 cup low-fat milk+ mixed raisins and almonds+coconut milk protein shake'
        lunch = ' Fried rice+veg curry+salad '
        snacks = ' peanut butter and jelly sandwich: slices whole wheat bread + 2 Tbsp.peanut butter + 1 Tbsp.jelly or jam'
        dinner = 'Pan pasta + fried corn and onions '

    @Rule(mass(calorie=P(lambda calorie: calorie >= 2800) & P(lambda calorie: calorie <= 2899),preference='Non-veg'))
    def calorie_pp(self):
        global breakfast, lunch, snacks, dinner
        breakfast = 'reduced - fat waffle + reduced - fat pancakes + fruits + egg OR ¼ cup scrambled egg + 1 cup skim milk'
        lunch = 'Chicken breast(white meat)+rice steamed + salad(tomato, onion) + Roasted chickpeas + soup'
        snacks = 'peanut butter and jelly sandwich: 2 slices whole wheat bread + 2 Tbsp.peanut butter + 1 Tbsp.jelly or jam'
        dinner = 'barbecue chicken breast OR baked fish + baked potato OR mashed potatoes +whole wheat dinner roll OR 1 slice whole wheat bread + steamed broccoli +cooked carrots + frozen yogurt + skim milk '

    @Rule(mass(calorie=P(lambda calorie: calorie >= 2900) & P(lambda calorie: calorie <= 2999),preference='Veg'))
    def calorie_q(self):
        global breakfast, lunch, snacks, dinner
        breakfast = 'Corn flakes cereal + Skim milk + Wheat bread + creamy peanut butter + fruits'
        lunch = 'brown rice + steamed broccoli + tofu or cottage cheese curry cooked with vegetable oil '
        snacks = ' Creamy ramen noodles+green veggies+juice  '
        dinner = 'Vegetable Salad/Soup + 2 small Chapatis with dal or vegetable curry + 1 cup (150ml) curd made from double toned milk'

    @Rule(mass(calorie=P(lambda calorie: calorie >= 2900) & P(lambda calorie: calorie <= 2999),preference='Non-veg'))
    def calorie_qq(self):
        global breakfast, lunch, snacks, dinner
        breakfast = 'wheat bread + margarine & fruit spread + Fried egg + cheese + Sausage + fruits + Milk, skim'
        lunch = 'chicken breast + brown rice + pickles + papad'
        snacks = 'Creamy ramen noodles with fried egg '
        dinner = '2 Tomato-Cheddar Cheese Toasts+ 2 cups mixed greens+ carrot+ cucumber+1 hard-boiled egg+dry-roasted almonds+olive oil & balsamic vinegar '

    @Rule(mass(calorie=P(lambda calorie: calorie >= 3000) & P(lambda calorie: calorie <= 3099),preference='Veg'))
    def calorie_r(self):
        global breakfast, lunch, snacks, dinner
        breakfast = 'Skimmed Milk with cornflakes + fruits + soaked almonds+milk shake '
        lunch = '1 cup cooked brown rice, 85 grams baked or roasted chicken breast, salad made with lettuce, carrots, onions, tomatoes and olives '
        snacks = ' 3 cups Popcorn, microwave, natural flavor, mixed juice'
        dinner = 'Baked Potato + veggie chili +onion+ cheese+ Green lettuce, carrots, cucumbers, tomatoes, mushroom+ low fat cottage cheese '

    @Rule(mass(calorie=P(lambda calorie: calorie >= 3000) & P(lambda calorie: calorie <= 3099),preference='Non-veg'))
    def calorie_rr(self):
        global breakfast, lunch, snacks, dinner
        breakfast = 'Basic scrambled egg + protein shake + bread toast + fruits'
        lunch = 'Chicken breast(white meat) + rice steamed + salad(tomato, onion) + Roasted chickpeas + soup'
        snacks = '3 cups Popcorn, microwave, natural flavor, salt free mixed juice'
        dinner = 'of roasted chicken breast, 140 grams of baked sweet potato topped with 1 teaspoon of butter, 1/2 cup steamed broccoli'

    @Rule(mass(calorie=P(lambda calorie: calorie >= 3100) & P(lambda calorie: calorie <= 3199),preference='Veg'))
    def calorie_s(self):
        global breakfast, lunch, snacks, dinner
        breakfast = 'Buttered toast(2) + protein shake'
        lunch = 'Brown rice / white rice + lentils + curd + green vegetable + paneer'
        snacks = 'Chocolate cookies(2) + lemonade + fried nuts + wafers'
        dinner = 'Brown rice+ Potato, lentil and cauliflower curry+pickle+papad'

    @Rule(mass(calorie=P(lambda calorie: calorie >= 3100) & P(lambda calorie: calorie <= 3199),preference='Non-veg'))
    def calorie_ss(self):
        global breakfast, lunch, snacks, dinner
        breakfast = 'Buttered toast(2 pieces) + protein shake + omelette'
        lunch = 'chicken breast + white rice + bell pepper + Green onion + onion + mushrooms + 2 tbsp soy sauce + 1 egg'
        snacks = 'Chocolate cookies(2) + lemonade + fried nuts + wafers'
        dinner = 'Cheese pizza+ salad with lettuce, tomato, carrots, cucumber green pepper & radishes+ Vinegar & oil salad dressing +Carrot, raw + Apple Juice'

    @Rule(mass(calorie=P(lambda calorie: calorie >= 3200) & P(lambda calorie: calorie <= 3299),preference='Veg'))
    def calorie_t(self):
        global breakfast, lunch, snacks, dinner
        breakfast = 'Buttered toast + fruits + tea / coffee'
        lunch = 'Brown Rice 1 cup(195gm) + Mixed Vegetables 1 / 2 cup + Salad 1 bowl + Raita 1 small bowl + papad + pickle + dal'
        snacks = 'Iced - blended coffee & peanut butter protein shake + wafers'
        dinner = 'Porridge+fried potato+pickle'

    @Rule(mass(calorie=P(lambda calorie: calorie >= 3200) & P(lambda calorie: calorie <= 3299),preference='Non-veg'))
    def calorie_tt(self):
        global breakfast, lunch, snacks, dinner
        breakfast = 'Cheese egg white omlette + protein shake + fruits'
        lunch = 'Brown Rice 1 cup(195gm) + curry(meat) + Salad 1 bowl + Raita 1 small bowl + papad + pickle + dal'
        snacks = 'Iced - blended coffee & peanut butter protein shake + wafers'
        dinner = 'chicken breast+ white rice+ bell pepper +Green onion+ onion+ mushrooms+2 tbsp soy'
engine = MyDietician()
engine.reset()

ask_calorie = int(input("How much calories would you like to eat? 1190 - 3299: "))
ask_preference= input("What is your preference? Veg or Non-veg: ")

engine.declare(mass(calorie=ask_calorie, preference=ask_preference))

engine.run()

print("[*]Breakfast: " + breakfast)
print("[*]Lunch: " + lunch)
print("[*]Snacks: " + snacks)
print("[*]Dinner: " + dinner)

engine.facts
engine.matcher.show_network()