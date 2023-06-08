from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.theming import ThemeManager
from kivy.core.text import LabelBase
from kivymd.font_definitions import theme_font_styles

import webbrowser

screen_helper = """
ScreenManager:
    StartScreen:
    SearchScreen:
    GenreList:
    BestofList:

<StartScreen>:
    name: 'start'
    MDLabel:
        text: 'AMORE:'
        halign: 'center'
        pos_hint: {'center_x': 0.5, 'center_y': 0.75}
        font_style: "VT323-Regular"

    MDLabel:
        text: 'Automated Movie Recommender'
        halign: 'center'
        pos_hint: {'center_x': 0.5, 'center_y': 0.65}
        font_style: 'Caption'

    MDRoundFlatButton:
        text: 'Start searching'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint: (0.5, 0.1)
        theme_color_style: 'Green'
        text_color: (43/255, 50/255, 60/255, 1)
        on_press: root.manager.current = 'search'
        md_bg_color: app.theme_cls.primary_light


<SearchScreen>:
    name: 'search'
    MDRoundFlatButton:
        text: 'GENRE'
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
        theme_color_style: 'Custom'
        text_color: (43/255, 50/255, 60/255, 1)
        on_press: root.manager.current = 'genre_list'
        md_bg_color: app.theme_cls.primary_light

    MDRoundFlatButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        on_press: root.manager.current = 'start'

    MDLabel:
        text: 'SEARCH BY:'
        halign: 'center'
        pos_hint: {'center_x': 0.5, 'center_y': 0.9}
        font_style: "VT323-Regular"

    MDRoundFlatButton:
        text: 'TRENDING'
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        theme_color_style: 'Custom'
        text_color: (43/255, 50/255, 60/255, 1)
        on_press: app.trending_link()
        md_bg_color: app.theme_cls.primary_light

    MDRoundFlatButton:
        text: 'NEW RELEASES'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        theme_color_style: 'Custom'
        text_color: (43/255, 50/255, 60/255, 1)
        on_press: app.newreleases_link()
        md_bg_color: app.theme_cls.primary_light

    MDRoundFlatButton:
        text: 'BEST OF'
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        theme_color_style: 'Custom'
        text_color: (43/255, 50/255, 60/255, 1)
        on_press: root.manager.current = 'best_list'
        md_bg_color: app.theme_cls.primary_light

    MDRoundFlatButton:
        text: 'ALL-TIME FAVE'
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        theme_color_style: 'Custom'
        text_color: (43/255, 50/255, 60/255, 1)
        on_press: app.alltime_link()
        md_bg_color: app.theme_cls.primary_light


#Second Screen
<GenreList>:
    name: 'genre_list'
    MDLabel:
        text: 'GENRE'
        halign: 'center'
        pos_hint: {'center_x': 0.5, 'center_y': 0.8}
        font_style: "VT323-Regular"

    MDRoundFlatButton:
        text: 'ASIAN MOVIES'
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        theme_color_style: 'Custom'
        text_color: (43/255, 50/255, 60/255, 1)
        on_press: app.asian_link()
        md_bg_color: app.theme_cls.primary_light

    MDRoundFlatButton:
        text: 'HOLLYWOOD'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        theme_color_style: 'Custom'
        text_color: (43/255, 50/255, 60/255, 1)
        on_press: app.hollywood_link()
        md_bg_color: app.theme_cls.primary_light

    MDRoundFlatButton:
        text: 'ANIMATION MOVIE'
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        theme_color_style: 'Custom'
        text_color: (43/255, 50/255, 60/255, 1)
        on_press: app.animation_link()
        md_bg_color: app.theme_cls.primary_light

    MDRoundFlatButton:
        text: 'Start'
        pos_hint: {'center_x': 0.7, 'center_y': 0.2}
        on_press: root.manager.current = 'start'

    MDRoundFlatButton:
        text: 'Search By'
        pos_hint: {'center_x': 0.3, 'center_y': 0.2}
        on_press: root.manager.current = 'search'




<BestofList>:
    name: 'best_list'
    MDLabel:
        text: 'BEST OF:'
        halign: 'center'
        pos_hint: {'center_x': 0.5, 'center_y': 0.85}
        font_style: "VT323-Regular"

    MDRoundFlatButton:
        text: '2020'
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
        theme_color_style: 'Custom'
        text_color: (43/255, 50/255, 60/255, 1)
        on_press: app.twenty_link()
        md_bg_color: app.theme_cls.primary_light

    MDRoundFlatButton:
        text: '2019'
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        theme_color_style: 'Custom'
        text_color: (43/255, 50/255, 60/255, 1)
        on_press: app.nineteen_link()
        md_bg_color: app.theme_cls.primary_light

    MDRoundFlatButton:
        text: '2018'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        theme_color_style: 'Custom'
        text_color: (43/255, 50/255, 60/255, 1)
        on_press: app.eighteen_link()
        md_bg_color: app.theme_cls.primary_light
        

    MDRoundFlatButton:
        text: '2017'
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        theme_color_style: 'Custom'
        text_color: (43/255, 50/255, 60/255, 1)
        on_press: app.seventeen_link()
        md_bg_color: app.theme_cls.primary_light

    MDRoundFlatButton:
        text: '2016'
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        theme_color_style: 'Custom'
        text_color: (43/255, 50/255, 60/255, 1)
        on_press: app.sixteen_link()
        md_bg_color: app.theme_cls.primary_light

    MDRoundFlatButton:
        text: '2015'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        theme_color_style: 'Custom'
        text_color: (43/255, 50/255, 60/255, 1)
        on_press: app.fifteen_link()
        md_bg_color: app.theme_cls.primary_light

    MDRoundFlatButton:
        text: 'Start'
        pos_hint: {'center_x': 0.7, 'center_y': 0.1}
        on_press: root.manager.current = 'start'

    MDRoundFlatButton:
        text: 'Search By'
        pos_hint: {'center_x': 0.3, 'center_y': 0.1}
        on_press: root.manager.current = 'search'

"""


class StartScreen(Screen):
    pass


class SearchScreen(Screen):
    pass


class GenreList(Screen):
    pass


class BestofList(Screen):
    pass


# Create the screen manager
sm = ScreenManager()
sm.add_widget(StartScreen(name='start'))
sm.add_widget(SearchScreen(name='search'))
sm.add_widget(GenreList(name='genre_list'))
sm.add_widget(BestofList(name='best_list'))


class DemoApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Green"
        LabelBase.register(
            name="VT323-Regular",
            fn_regular="VT323-Regular.ttf")

        theme_font_styles.append('VT323-Regular')
        self.theme_cls.font_styles["VT323-Regular"] = [
            "VT323-Regular",
            75,
            False,
            0.15,
        ]
        return Builder.load_string(screen_helper)

    def alltimelink(self):
        return webbrowser.open(
            'https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwi0hv_HjcbtAhWXfXAKHfeUA5oQFjAKegQIARAC&url=https%3A%2F%2Fwww.marvel.com%2F&usg=AOvVaw0FKV41lqGjoAhHrFT1yg4x')

    def asian_link(self):
        # marvels pa rin ito palitan mo n Lang
        return webbrowser.open(
            'https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwi0hv_HjcbtAhWXfXAKHfeUA5oQFjAKegQIARAC&url=https%3A%2F%2Fwww.marvel.com%2F&usg=AOvVaw0FKV41lqGjoAhHrFT1yg4x')

    def hollywood_link(self):
        # marvels pa rin ito palitan mo n Lang
        return webbrowser.open(
            'https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwi0hv_HjcbtAhWXfXAKHfeUA5oQFjAKegQIARAC&url=https%3A%2F%2Fwww.marvel.com%2F&usg=AOvVaw0FKV41lqGjoAhHrFT1yg4x')

    def animation_link(self):
        return webbrowser.open(
            'https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwi0hv_HjcbtAhWXfXAKHfeUA5oQFjAKegQIARAC&url=https%3A%2F%2Fwww.marvel.com%2F&usg=AOvVaw0FKV41lqGjoAhHrFT1yg4x')

    def twenty_link(self):
        # marvels pa rin ito palitan mo n Lang
        return webbrowser.open(
            'https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwi0hv_HjcbtAhWXfXAKHfeUA5oQFjAKegQIARAC&url=https%3A%2F%2Fwww.marvel.com%2F&usg=AOvVaw0FKV41lqGjoAhHrFT1yg4x')

    def nineteen_link(self):
        # marvels pa rin ito palitan mo n Lang
        return webbrowser.open(
            'https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwi0hv_HjcbtAhWXfXAKHfeUA5oQFjAKegQIARAC&url=https%3A%2F%2Fwww.marvel.com%2F&usg=AOvVaw0FKV41lqGjoAhHrFT1yg4x')

    def eighteen_link(self):
        # marvels pa rin ito palitan mo n Lang
        return webbrowser.open(
            'https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwi0hv_HjcbtAhWXfXAKHfeUA5oQFjAKegQIARAC&url=https%3A%2F%2Fwww.marvel.com%2F&usg=AOvVaw0FKV41lqGjoAhHrFT1yg4x')

    def seventeen_link(self):
        # marvels pa rin ito palitan mo n Lang
        return webbrowser.open(
            'https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwi0hv_HjcbtAhWXfXAKHfeUA5oQFjAKegQIARAC&url=https%3A%2F%2Fwww.marvel.com%2F&usg=AOvVaw0FKV41lqGjoAhHrFT1yg4x')

    def sixteen_link(self):
        # marvels pa rin ito palitan mo n Lang
        return webbrowser.open(
            'https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwi0hv_HjcbtAhWXfXAKHfeUA5oQFjAKegQIARAC&url=https%3A%2F%2Fwww.marvel.com%2F&usg=AOvVaw0FKV41lqGjoAhHrFT1yg4x')

    def fifteen_link(self):
        # marvels pa rin ito palitan mo n Lang
        return webbrowser.open(
            'https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwi0hv_HjcbtAhWXfXAKHfeUA5oQFjAKegQIARAC&url=https%3A%2F%2Fwww.marvel.com%2F&usg=AOvVaw0FKV41lqGjoAhHrFT1yg4x')

    def trending_link(self):
        return webbrowser.open(
            'https://www.the-numbers.com/movies/trending')

    def newreleases_link(self):
        return webbrowser.open(
            'https://www.metacritic.com/browse/movies/release-date/theaters/date?view=detailed')

DemoApp().run()
